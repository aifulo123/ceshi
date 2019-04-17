# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_application', '0005_host_other'),
    ]

    operations = [
        migrations.CreateModel(
            name='HostData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('when_created', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4', null=True)),
                ('ip', models.CharField(max_length=128, verbose_name='ip')),
                ('biz_id', models.CharField(default=b'', max_length=128, verbose_name='\u4e1a\u52a1id')),
                ('yun_id', models.CharField(default=b'', max_length=128, verbose_name='\u4e91id')),
                ('memory', models.CharField(max_length=128, verbose_name='\u5185\u5b58')),
                ('cpu', models.CharField(max_length=128, verbose_name='cpu')),
                ('disk', models.CharField(max_length=128, verbose_name='\u78c1\u76d8')),
            ],
        ),
        migrations.AlterField(
            model_name='host',
            name='biz',
            field=models.CharField(max_length=128, verbose_name='\u4e1a\u52a1'),
        ),
        migrations.AlterField(
            model_name='host',
            name='biz_id',
            field=models.CharField(default=b'', max_length=128, verbose_name='\u4e1a\u52a1id'),
        ),
        migrations.AlterField(
            model_name='host',
            name='ip',
            field=models.CharField(max_length=128, verbose_name='ip'),
        ),
        migrations.AlterField(
            model_name='host',
            name='name',
            field=models.CharField(max_length=128, verbose_name='\u4e3b\u673a\u540d\u79f0'),
        ),
        migrations.AlterField(
            model_name='host',
            name='other',
            field=models.TextField(default=b'\xe5\x85\xb6\xe4\xbb\x96', verbose_name=''),
        ),
        migrations.AlterField(
            model_name='host',
            name='system',
            field=models.CharField(max_length=128, verbose_name='\u7cfb\u7edf'),
        ),
        migrations.AlterField(
            model_name='host',
            name='yun',
            field=models.CharField(max_length=128, verbose_name='\u4e91\u533a\u57df'),
        ),
        migrations.AlterField(
            model_name='host',
            name='yun_id',
            field=models.CharField(default=b'', max_length=128, verbose_name='\u4e91id'),
        ),
    ]
