# -*- coding: utf-8 -*-
"""
celery 任务示例

本地启动celery命令: python  manage.py  celery  worker  --settings=settings
周期性任务还需要启动celery调度命令：python  manage.py  celerybeat --settings=settings
"""
import datetime
import json
from home_application.models import *
import requests
from celery import task
from celery.schedules import crontab
from celery.task import periodic_task
from django.http import JsonResponse

from common.log import logger
from home_application.esb_helper import cc_search_biz, cc_search_set, run_fast_execute_script, cc_search_host, \
    get_job_instance_log, get_host_ip_list, cc_get_job_detail, run_execute_job, cc_fast_push_file


@task()
def async_task(x, y):
    """
    定义一个 celery 异步任务
    """
    logger.error(u"celery 定时任务执行成功，执行结果：{:0>2}:{:0>2}".format(x, y))
    return x + y


def execute_task():
    """
    执行 celery 异步任务

    调用celery任务方法:
        task.delay(arg1, arg2, kwarg1='x', kwarg2='y')
        task.apply_async(args=[arg1, arg2], kwargs={'kwarg1': 'x', 'kwarg2': 'y'})
        delay(): 简便方法，类似调用普通函数
        apply_async(): 设置celery的额外执行选项时必须使用该方法，如定时（eta）等
                      详见 ：http://celery.readthedocs.org/en/latest/userguide/calling.html
    """
    now = datetime.datetime.now()
    logger.error(u"celery 定时任务启动，将在60s后执行，当前时间：{}".format(now))
    # 调用定时任务
    async_task.apply_async(args=[now.hour, now.minute], eta=now + datetime.timedelta(seconds=60))


@periodic_task(run_every=crontab(minute='*/5', hour='*', day_of_week="*"))
def get_time():
    """
    celery 周期任务示例

    run_every=crontab(minute='*/5', hour='*', day_of_week="*")：每 5 分钟执行一次任务
    periodic_task：程序运行时自动触发周期任务
    """
    execute_task()
    get_fuzai()
    get_host_pro_data()
    now = datetime.datetime.now()
    logger.error(u"celery 周期任务调用成功，当前时间：{}".format(now))

@task
def get_fuzai():
    try:
        data_list = host.objects.filter()
        for item in data_list:
            ip = item.ip
            biz_id = int(item.biz_id)
            yun_id = int(item.yun_id)
            ip_list = [{
                "ip":ip,
                "bk_cloud_id":yun_id
            }]
            strip = """
            #!/bin/bash
            cat /proc/loadavg
            """
            result = run_fast_execute_script(biz_id,strip,ip_list)
            logs = 0
            if result["result"]:
                job_id = int(result["data"])
                log = get_job_instance_log(biz_id,job_id)[0]
                if log["is_success"]:
                    logs = log["log_content"].split(" ")[1]
            fuzai = FuZai()
            fuzai.ip = ip
            fuzai.value = logs
            fuzai.save()
    except Exception, e:
        logger.error(e)



@task
def get_host_pro_data():
    try:
        host_data = host.objects.filter()
        script = """#!/bin/bash

        MEMORY=$(free -m | awk 'NR==2{printf "%.2f%%", $3*100/$2 }')
        DISK=$(df -h | awk '$NF=="/"{printf "%s", $5}')
        CPU=$(top -bn1 | grep load | awk '{printf "%.2f%%", $(NF-2)}')
        DATE=$(date "+%Y-%m-%d %H:%M:%S")
        echo -e "$DATE|$MEMORY|$DISK|$CPU"
        """
        for item in host_data:
            biz_id = int(item.biz_id)
            ip = item.ip
            yun_id = int(item.yun_id)
            ip_list = [
                {
                "ip":ip,
                "bk_cloud_id":yun_id
                }
            ]
            proper = {}
            result = run_fast_execute_script(biz_id,script,ip_list)
            if result["result"]:
                job_id = int(result["data"])
                log = get_job_instance_log(biz_id,job_id)[0]
                if log["is_success"]:
                    logs = log["log_content"]
                    proper = format_data(logs)
                    prop = HostData()
                    prop.ip = ip
                    prop.biz_id = biz_id
                    prop.yun_id = yun_id
                    prop.memory = proper["memory"]
                    prop.cpu = proper["cpu"]
                    prop.disk = proper["disk"]
                    prop.save()
        logger.error("添加host性能")
    except Exception,e:
        logger.error("获取主机性能失败"+e)

def format_data(result):
    data = {"cpu_load":0,"memory_load":0,"disk_load":0}
    if result:
        res_list = result.split('|')
        data["memory"] = res_list[1].strip('%')
        data["disk"] = res_list[2].strip('%')
        data["cpu"] = res_list[3].strip('%\n')
    return data