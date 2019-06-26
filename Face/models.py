from django.db import models
import django.utils.timezone as timezone

# Create your models here.
#用户信息

class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10,unique=True)
    password = models.CharField(max_length=20)
    sex = (('mail','男'),('femail','女'),)
    gender = models.CharField(max_length=2, choices=sex, default='女')
    birth = models.DateField(default=timezone.now().date)

    def __str__(self):
        return self.name

#皮肤分析历史
class UserSkin(models.Model):
    uid = models.IntegerField(primary_key=True)
    stime = models.DateTimeField(default=timezone.now)
    totalScore = models.IntegerField(default=100)
    youngScore = models.IntegerField(default=100)
    healthScore = models.IntegerField(default=100)
    oilScore = models.IntegerField(default=100)
    softScore = models.IntegerField(default=100)

    def __str__(self):
        filename = self.uid+self.stime
        return filename

    class Meta:
        unique_together = ("stime", "uid")

#五官特征分析结果
class UserFace(models.Model):
    uid = models.ForeignKey(User)
    ftime = models.DateTimeField(default=timezone.now)
    faceShape = models.CharField(max_length=16)
    lipShape = models.CharField(max_length=16)
    chinShape = models.CharField(max_length=16)
    eyeShape = models.CharField(max_length=16)
    browShape = models.CharField(max_length=16)
    noseShape = models.CharField(max_length=16)
    forehead = models.CharField(max_length=16)

#肤质测试记录
class SkinRecord(models.Model):
    uid = models.ForeignKey(User)
    time = models.DateTimeField(default= timezone.now)
    age = models.IntegerField()
    wrinkleCount = models.IntegerField()
    wrinkleScore = models.IntegerField()
    wrinkleGlabellaCount = models.IntegerField()
    wrinkleCrowfeetCount = models.IntegerField()
    wrinkleNasolabialCount = models.IntegerField()
    wrinkleEyecornerCount = models.IntegerField()
    wrinkleForeheadCount = models.IntegerField()
    pockmarkCount = models.IntegerField()
    pockmarkScore = models.IntegerField()
    blackheadCount = models.IntegerField()
    blackheadScore = models.IntegerField()
    darkCircleResult = models.FloatField()
    colorResult = models.CharField(max_length=16)
    skinTypeOily = models.CharField(max_length=16)
    skinTypeDry = models.CharField(max_length=16)
    skinTypeMixed = models.CharField(max_length=16)
    foreheadOilResult = models.FloatField()
    foreheadChinResult = models.FloatField()
    foreheadLeftCheekResult = models.FloatField()
    foreheadRightCheekResult = models.FloatField()
    moistureResult = models.CharField(max_length=32)
    moistureScore = models.IntegerField()
    roughnessScore = models.IntegerField()
    poreCount = models.IntegerField()
    poreScore = models.IntegerField()

#五官特征测试记录
class ImageRecord(models.Model):
    uid = models.ForeignKey(User,primary_key=True)
    time = models.DateTimeField(default=timezone.now)
    image = models.BinaryField()