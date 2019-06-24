from django.db import models

# Create your models here.
#用户信息
class User(models.Model):
    '''用户'''
    name = models.CharField(max_length=64,unique=True,primary_key=True)
    password = models.CharField(max_length=64)
    gender = (('mail','男'),('femail','女'),)
    sex = models.CharField(max_length=32, choices=gender, default='女')
    birth = models.DateField()

    email = models.EmailField(unique=True)
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return self.name

#皮肤分析历史
class UserSkin(models.Model):
    name =  models.CharField(max_length=64)
    time = models.DateTimeField()
    totalScore = models.IntegerField()
    youngScore = models.IntegerField()
    healthScore = models.IntegerField()
    oilScore = models.IntegerField()
    softScore = models.IntegerField()

    class Meta:
        unique_together = ("name","time")

#五官特征分析结果
class UserFace(models.Model):
    name = models.CharField(max_length=64)
    faceShape = models.CharField(max_length=16)
    lipShape = models.CharField(max_length=16)
    chinShape = models.CharField(max_length=16)
    eyeShape = models.CharField(max_length=16)
    browShape = models.CharField(max_length=16)
    noseShape = models.CharField(max_length=16)
    forehead = models.CharField(max_length=16)

#肤质测试记录
class SkinRecord(models.Model):
    name = models.CharField(max_length=64,primary_key=True)
    time = models.DateTimeField()
    image = models.BinaryField()
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
class FaceRecord(models.Model):
    name = models.CharField(max_length=64)
    time = models.DateTimeField()
    image = models.BinaryField()
    faceShape = models.CharField(max_length=16)
    lipShape = models.CharField(max_length=16)
    chinShape = models.CharField(max_length=16)
    eyeShape = models.CharField(max_length=16)
    browShape = models.CharField(max_length=16)
    noseShape = models.CharField(max_length=16)
    forehead = models.CharField(max_length=16)

#形象设计指南
class FaceRecomend(models.Model):
    type = models.CharField(max_length=16)
    comment = models.CharField(max_length=64)
    suggest = models.CharField(max_length=512)

