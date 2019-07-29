from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests, base64
from json import JSONDecoder
import os
from . import models
import json
from requests_toolbelt.multipart.encoder import MultipartEncoder

# Create your views here.
#主页
def index(request):    
    return render(request,'Face/home.html')
#登录
def login(request):

    if request.session.get('is_login',None):
        user = models.UserInfo.objects.get(uid=request.session['user_id'])
        return render(request,'Face/info.html',{'UserInfo': user})

    #在没有session的条件下登录时创建session
    if request.method == "POST":
        userID = request.POST.get('id')
        password = request.POST.get('pwd')
        if userID and password:#用户名和密码都不为空
            userID = userID.strip()
            try:
                user = models.UserInfo.objects.get(uid=userID)
                # 验证密码
                if user.passwd == password:
                    request.session['is_login']=True
                    # 将用户名作为session标记
                    request.session['user_id']=user.uid
                    return render(request,'Face/info.html', {'UserInfo': user})
            except:
                return render(request,'Face/login.html')
    return render(request,'Face/login.html')

#注册
def register(request):
    if request.method=="POST":
        new_user = models.UserInfo.objects.create()
        new_user.name = request.POST.get('name_r')
        new_user.uid = request.POST.get('id_r')
        if request.POST.get('psd_r')==request.POST.get('affirm_psd'):
            #密码一致
            new_user.passwd = request.POST.get('psd_r')
            new_user.gender = request.POST.get('sex_r')
            new_user.birthday = request.POST.get('birthday_r')
            new_user.save()
    return render(request,'Face/login.html')

#注销
def logout(request):
    if not request.session.get('is_login', None):
        #如果没有登录 也就不需要注销
        return redirect('index')
    #否则清除session
    request.session.flush()
    return redirect('index')
    
#检测
def detect(request):
    if not request.session.get('is_login', None):
        return render(request, 'Face/error.html', {"message":"请先进行登录"})
    else:
        return render(request, 'Face/takephoto.html')
    
#显示结果   
def result(request):
    #保存图片到本地
    cur_dir = os.path.dirname(__file__)#获取当前目录
    file_path = os.path.join(cur_dir,'../static/p.jpg')
    img = request.POST['pic']
    imagedata = decode_base64(img[len("data:image/jpg;base64,"):])
    file = open(file_path,'wb')
    file.write(imagedata)
    file.close()

    # 所用参数赋值
    type = 504205
    url = 'https://api.yimei.ai/v1/api/face/analysis/' + str(type)
    client_id = "f0dbe1dac09c2ae9"
    client_secret = "de7015dc94e87829b1552a639e6c9c13"
    a = client_id + ':' + client_secret
    # 打开图片 自动生成可用于上传的数据
    f = {"image": (file_path, open(file_path, 'rb'), "image/jpg"), "detect_types": str(type)}
    img = MultipartEncoder(f)
    #请求头
    headers = {"Authorization": 'Basic ' + str(base64.b64encode(a.encode("utf-8")), "utf-8"),
               "Content-Type": img.content_type,
               "Host": "api.yimei.ai",
               "Accept": "application/json"}
    #发送请求
    response = requests.post(url, data=img, headers=headers)
    # 解码
    req_con = response.content.decode('utf-8')
    data = JSONDecoder().decode(req_con)

    #出错处理
    if data['code'] != 0:
        return render(request, 'Face/error.html', {"message": data['msg']})

    #根据返回数据存储数据库
    #Table1 皮肤分析历史
    new_skin = models.UserSkin.objects.create()
    new_skin.uid = request.session['user_id']
    #年轻度
    age_ = data['age']['result']
    if age_ >= 0 and age_ <= 25:
        y = 100
    elif age_ >= 26 and age_ <= 35:
        y = 90
    elif age_ >= 36 and age_ <= 46:
        y = 80
    elif age_ >= 46 and age_ <= 56:
        y = 70
    else:
        y=60
    new_skin.youngScore = int(y*0.5+data['wrinkle']['score']*0.5)
    #健康度
    darkCir = data['dark_circle']['result']
    if darkCir>=0 and darkCir<=25:
        d=100
    elif darkCir>=26 and darkCir<=35:
        d=90
    elif darkCir>=36 and darkCir<=46:
        d=80
    elif darkCir>=46 and darkCir<=56:
        d=70
    else:
        d=60
    health = data['pockmark']['score']*(1/3)+data['blackhead']['score']*(1/3)+d*(1/3)
    if data['color']['result']=='anchen':
        health = health-10
    new_skin.healthScore = int(health)
    #油干性
    oil = int(data['moisture']['score'])*0.5+data['skin_type']['score']*0.5
    new_skin.oilScore = int(oil)
    #细腻度
    new_skin.softScore = int(data['roughness']['score']*0.5+data['pore']['score']*0.5)
    #总分
    new_skin.totalScore = int((new_skin.healthScore+new_skin.oilScore+new_skin.youngScore+new_skin.softScore)/4)
    new_skin.save()
    data['Userskin']=new_skin

    cur_dir = os.path.dirname(__file__)  # 获取当前目录
    sugg_path = os.path.join(cur_dir, './static/suggestion.json')
    with open(sugg_path) as f:
        suggest = json.load(f)
    for key, value in suggest.items():
        data[key] = value
    return render(request,'Face/scan.html', data)

#显示历史记录
def history(request):



    data1 = ['2.21', '2.22', '2.23', '2.24', '2.25', '22.26', '2.27', '2.28', '2.29', '2.30', '3.1', '3.1', '3.2',
             '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '3.10', '3.11', '3.12', '3.13', '3.14', '3.15', '3.16',
             '3.17', '3.18', '3.19', '3.20']
    data2 = [10, 10, 10, 10, 10, 48, 49, 100, 64, 63, 26, 25, 86, 84, 39, 85, 94, 35, 75, 52, 76, 86, 46, 37, 57, 35,
             75, 65, 34, 77]

    return render(request,'Face/history.html',{'var1':json.dumps(data1),'var2':json.dumps(data2)})



#填补base64码的空白
def decode_base64(strg): 
    lens = len(strg)
    lenx = lens - (lens % 4 if lens % 4 else 4)
    r = base64.b64decode(strg[:lenx])
    return r
