import requests, base64
from requests_toolbelt.multipart.encoder import MultipartEncoder
import pickle
from . import models
import json
import time

# 将图片上传到api请求解析
def upload2api(file_path):
    # 所用参数赋值
    type_num = 504205
    url = 'https://api.yimei.ai/v1/api/face/analysis/' + str(type_num)
    client_id = "f0dbe1dac09c2ae9"
    client_secret = "de7015dc94e87829b1552a639e6c9c13"
    a = client_id + ':' + client_secret

    # 打开图片 自动生成可用于上传的数据
    f = {"image": (file_path, open(file_path, 'rb'), "image/jpg"), "detect_types": str(type)}
    img = MultipartEncoder(f)
    # 请求头
    headers = {"Authorization": 'Basic ' + str(base64.b64encode(a.encode("utf-8")), "utf-8"),
               "Content-Type": img.content_type,
               "Host": "api.yimei.ai",
               "Accept": "application/json"}
    # 发送请求
    response = requests.post(url, data=img, headers=headers)
    return response


# 保存图片到本地
def imgSave(data_uri, file_path='detect.jpg'):
    img = data_uri[len('data:image/jpeg;base64;'):]
    imagedata = base64.b64decode(img)
    with open(file_path, 'wb') as fp:
        fp.write(imagedata)


# 保存api返回的数据，测试用
def saveData(data, name='tempData'):
    with open(str(name) + '.pke', 'wb') as fp:
        pickle.dump(data, fp)


# 读取测试文件
def readData(name='tempData'):
    with open(str(name) + '.pke', 'rb') as fp:
        data = pickle.load(fp)
    return data


# 解析api返回的数据,补充成完整的数据
def solveData(data):
    if data['code'] != 0:
        return 0

    # 年龄
    age = data['age']['result']
    if 0 <= age <= 25:
        y = 100
    elif 26 <= age <= 35:
        y = 90
    elif 36 <= age <= 46:
        y = 80
    elif 46 <= age <= 56:
        y = 70
    else:
        y = 60
    youngScore = int(y * 0.5 + data['wrinkle']['score'] * 0.5)

    # 黑眼圈
    darkCir = float(data['dark_circle']['result'])

    # 健康度
    if 0 <= darkCir <= 25:
        d = 100
    elif 26 <= darkCir <= 35:
        d = 90
    elif 36 <= darkCir <= 46:
        d = 80
    elif 46 <= darkCir <= 56:
        d = 70
    else:
        d = 60
    health = data['pockmark']['score'] * (1 / 3) + data['blackhead']['score'] * (1 / 3) + d * (1 / 3)
    if data['color']['result'] == 'anchen':
        health = health - 10
    healthScore = int(health)

    # 油干性
    oil = int(data['moisture']['score']) * 0.5 + data['skin_type']['score'] * 0.5
    oilScore = int(oil)

    # 细腻度
    softScore = int(data['roughness']['score'] * 0.5 + data['pore']['score'] * 0.5)

    # 总分
    totalScore = int((healthScore + oilScore + youngScore + softScore) / 4)

    timestamp = str("%.1f"% time.time())[2:]
    new_skin = models.UserSkin.objects.create(uid=timestamp)
    new_skin.healthScore = healthScore
    new_skin.youngScore = youngScore
    new_skin.totalScore = totalScore
    new_skin.oilScore = oilScore
    new_skin.softScore = softScore
    data['Userskin'] = new_skin

    # 建议文本
    with open('suggestion.json') as fp:
        suggest = json.load(fp)
    for key, value in suggest.items():
        data[key] = value

    # 播报文本生成
    text = '你的皮肤状态'
    if totalScore >= 85:
        text += '很好'
    elif 60 < totalScore < 85:
        text += '较好'
    else:
        text += '较差'
    text += ','
    if 80 <= oilScore <= 100:
        text += '油干性适中,'
    if data['color']['result'] == 'toubai' or data['color']['result'] == 'baixi':
        text += '肤色白皙,'
    if softScore > 80:
        text += '肤质细腻,'

    but = False
    if 60 <= d < 80:
        text += '但是,你有中度的黑眼圈问题,平时可以多按摩眼睛周围,缓解眼睛的压力,促进眼部周围的血液循环.'
        but = True

    if 60 <= data['pockmark']['score'] < 80:
        if not but:
            text += '但是'
            but = True
        text += '你的痘痘比较严重,注意饮食清淡,多吃水果蔬菜,需要配合使用调理角质代谢,疏通毛孔的护肤品.'
    elif data['pockmark']['score'] < 60:
        text += '你的痘痘太严重了,需要去三甲医院看皮肤科医生,在医生指导下进行系统调理.'

    if data['blackhead']['score'] < 80:
        if not but:
            text += '但是'
            but = True
        text += '你的黑头数量较多,平时需要注意T区的清洁,配合使用温和的调理角质、疏通毛孔的护肤品.'

    # 护肤品推荐
    pockS = data['pockmark']['score']
    if 80 <= oilScore <= 100:
        if 60 <= pockS <= 90:
            jiemian_ = '推荐使用较温和的氨基酸型洁面产品，日常清洁千万不可以忽视哦~'
        elif pockS < 60:
            jiemian_ = '推荐使用清洁力较强的SLS/SLES类或皂基类洁面产品，搭配去角质的啫喱或者活性泥，但不要过度清洁哦~'
    elif oilScore < 80:
        jiemian_ = '推荐使用较温和的氨基酸洁面慕斯或APG类洁面产品，对较干的皮肤很友好哦~'
    data['jiemian'] = jiemian_

    if 90 <= oilScore <= 100:
        if 60 <= pockS <= 90:
            hufushui_ = '推荐使用温和补水型的护肤水。'
            jinghua_ = '推荐使用含有维生素C和视黄酮成分的精华，可促进 代谢，美白抗衰老'
            ruye_ = '推荐使用温和的保湿型乳液进行日常的基础护理，先用护肤水再用乳液效果更好哦~'
            mianmo_ = '推荐使用温和保湿型面膜，一周两到三次即可'
            fangshai_ = '推荐使用温和乳状的防晒霜，日常防晒千万不可以忽视哦~'
        elif pockS < 60:
            hufushui_ = '推荐使用含有水杨酸和乳酸的护肤水，能起到温和去角质的作用，含有芦荟成分的护肤水能够缓解皮肤炎症。'
            jinghua_ = '推荐使用含有水杨酸等抗炎成分的精华，对缓解痘痘很有效，同时搭配具有活性修复因子的精华来祛除痘印，修复受损皮肤屏障。'
            ruye_ = '推荐使用清爽型具有舒缓抗炎作用的乳液，先用护肤水再用乳液效果更好哦~'
            mianmo_ = '推荐使用含有舒缓消炎成分的面膜，对缓解痘痘肌很有帮助哦~'
            fangshai_ = '推荐使用水剂型、无油配方、渗透力较强的防晒霜，如果痘痘有严重的发言或者皮肤破损时，必须暂停使用，出门时只能采取物理防晒。'
    elif oilScore < 90:
        hufushui_ = '推荐使用温和的保湿型护肤水，皮肤干燥或不适时可以使用保湿喷雾迅速缓解哦~'
        jinghua_ = '推荐使用滋润保湿和抗氧化的精华进行日常护理。'
        ruye_ = '推荐使用亲和力好的滋润保湿型面霜或乳液，先护肤水再乳液最后面霜的效果更好哦~'
        mianmo_ = '推荐使用滋润补水型面膜，皮肤需要适时补补水啦~'
        fangshai_ = '推荐使用霜类的防晒用品，选择具有滋润、补水功效的，能增强肌肤免疫力的防晒霜。'
    data['hufushui'] = hufushui_
    data['jinghua'] = jinghua_
    data['ruye'] = ruye_
    data['mianmo'] = mianmo_
    data['fangshai'] = fangshai_

    if 80 <= d <= 100:
        yanshuang_ = '推荐使用富含有VA衍生物、酸类成分、胜肽酸、酵素等成分的保湿型眼霜，可以改善眼周的皮肤状态、精致肌肤。'
    elif 60 <= d < 80:
        yanshuang_ = '推荐使用含有美白和有机酸成分的眼霜，改善色素沉淀、提亮肤色。'
    else:
        yanshuang_ = '推荐使用含有咖啡因、美白和有机酸成分的眼霜，改善微循环、加强代谢。'

    data['yanshuang'] = yanshuang_
    return data, text
