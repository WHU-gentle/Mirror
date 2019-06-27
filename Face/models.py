from django.db import models
import django.utils.timezone as timezone

# Create your models here.
#用户信息

class UserInfo(models.Model):
    uid = models.CharField(max_length=11,unique=True, primary_key=True)
    name = models.CharField(max_length=10)
    passwd = models.CharField(max_length=20)
    gender = models.CharField(max_length=2, default='女')
    birthday = models.DateField(default=timezone.now().date)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'UserInfo'

#皮肤分析历史
class UserSkin(models.Model):
    uid = models.CharField(max_length=11,primary_key=True)
    stime = models.DateTimeField(default=timezone.now)
    totalScore = models.IntegerField(default=100)
    youngScore = models.IntegerField(default=100)
    healthScore = models.IntegerField(default=100)
    oilScore = models.IntegerField(default=100)
    softScore = models.IntegerField(default=100)

    def __str__(self):
        filename = self.uid+str(self.stime)
        return filename

    class Meta:
        db_table = 'UserSkin'

#五官特征分析结果
class UserFace(models.Model):
    uid = models.CharField(max_length=11)
    ftime = models.DateTimeField(default=timezone.now)
    faceShape = models.CharField(max_length=16)
    lipShape = models.CharField(max_length=16)
    chinShape = models.CharField(max_length=16)
    eyeShape = models.CharField(max_length=16)
    browShape = models.CharField(max_length=16)
    noseShape = models.CharField(max_length=16)
    forehead = models.CharField(max_length=16)

    class Meta:
        db_table = 'UserFace'

#肤质测试记录
class SkinRecord(models.Model):
    uid = models.CharField(max_length=11)
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

    class Meta:
        db_table = 'SkinRecord'

#五官特征测试记录
class ImageRecord(models.Model):
    uid = models.CharField(max_length=11)
    time = models.DateTimeField(default=timezone.now)
    image = models.BinaryField()

    class Meta:
        db_table = 'ImageRecord'