# Generated by Django 2.1.7 on 2019-06-25 15:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Face', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaceRecomend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=16)),
                ('comment', models.CharField(max_length=64)),
                ('suggest', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='FaceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('time', models.DateTimeField()),
                ('image', models.BinaryField()),
                ('faceShape', models.CharField(max_length=16)),
                ('lipShape', models.CharField(max_length=16)),
                ('chinShape', models.CharField(max_length=16)),
                ('eyeShape', models.CharField(max_length=16)),
                ('browShape', models.CharField(max_length=16)),
                ('noseShape', models.CharField(max_length=16)),
                ('forehead', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='SkinRecord',
            fields=[
                ('name', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('time', models.DateTimeField()),
                ('image', models.BinaryField()),
                ('age', models.IntegerField()),
                ('wrinkleCount', models.IntegerField()),
                ('wrinkleScore', models.IntegerField()),
                ('wrinkleGlabellaCount', models.IntegerField()),
                ('wrinkleCrowfeetCount', models.IntegerField()),
                ('wrinkleNasolabialCount', models.IntegerField()),
                ('wrinkleEyecornerCount', models.IntegerField()),
                ('wrinkleForeheadCount', models.IntegerField()),
                ('pockmarkCount', models.IntegerField()),
                ('pockmarkScore', models.IntegerField()),
                ('blackheadCount', models.IntegerField()),
                ('blackheadScore', models.IntegerField()),
                ('darkCircleResult', models.FloatField()),
                ('colorResult', models.CharField(max_length=16)),
                ('skinTypeOily', models.CharField(max_length=16)),
                ('skinTypeDry', models.CharField(max_length=16)),
                ('skinTypeMixed', models.CharField(max_length=16)),
                ('foreheadOilResult', models.FloatField()),
                ('foreheadChinResult', models.FloatField()),
                ('foreheadLeftCheekResult', models.FloatField()),
                ('foreheadRightCheekResult', models.FloatField()),
                ('moistureResult', models.CharField(max_length=32)),
                ('moistureScore', models.IntegerField()),
                ('roughnessScore', models.IntegerField()),
                ('poreCount', models.IntegerField()),
                ('poreScore', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserFace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('faceShape', models.CharField(max_length=16)),
                ('lipShape', models.CharField(max_length=16)),
                ('chinShape', models.CharField(max_length=16)),
                ('eyeShape', models.CharField(max_length=16)),
                ('browShape', models.CharField(max_length=16)),
                ('noseShape', models.CharField(max_length=16)),
                ('forehead', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='UserSkin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('totalScore', models.IntegerField()),
                ('youngScore', models.IntegerField()),
                ('healthScore', models.IntegerField()),
                ('oilScore', models.IntegerField()),
                ('softScore', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='user',
            name='height',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='weight',
        ),
        migrations.AddField(
            model_name='user',
            name='birth',
            field=models.DateField(default=datetime.datetime(2019, 6, 25, 15, 18, 36, 716963, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='name',
            field=models.CharField(max_length=64, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterUniqueTogether(
            name='userskin',
            unique_together={('name', 'time')},
        ),
    ]
