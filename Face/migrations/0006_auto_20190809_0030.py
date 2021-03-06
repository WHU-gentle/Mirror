# Generated by Django 2.1.7 on 2019-08-08 16:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Face', '0005_imagerecord_skinrecord_userface_userinfo_userskin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerecord',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 16, 30, 17, 883140, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='skinrecord',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 16, 30, 17, 882343, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userface',
            name='ftime',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 16, 30, 17, 881872, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uid',
            field=models.CharField(max_length=11, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userskin',
            name='stime',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 8, 16, 30, 17, 881470, tzinfo=utc)),
        ),
    ]
