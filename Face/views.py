from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from json import JSONDecoder
import base64
import os
from . import models
import json

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
    if not request.session.get('is_login',None):
        #如果没有登录 也就不需要注销
        return redirect('index')
    #否则清除session
    request.session.flush()
    return redirect('index')
    
#检测
def detect(request):
    return render(request,'Face/takephoto.html')
    
#显示结果   
def result(request):
    #所用参数赋值
    type = 504205
    url = 'https://api.yimei.ai/v1/api/face/analysis/' + str(type)
    client_id = "f0dbe1dac09c2ae9";
    client_secret = "de7015dc94e87829b1552a639e6c9c13";
    a = client_id + ':' + client_secret
    #保存图片到本地
    cur_dir = os.path.dirname(__file__)#获取当前目录
    file_path = os.path.join(cur_dir,'../static/p.jpg')
    img = request.POST['pic']
    imagedata = decode_base64(img[len("data:image/jpg;base64,"):])
    file = open(file_path,'wb')
    file.write(imagedata)
    file.close()
    
    bodys = {"detect_types": type}
    #输入图片的URL
    bodys['image'] = "101.132.177.244:8080/static/p.jpg"
    headers = {'Authorization': 'Basic ' + str(base64.b64encode(a.encode("utf-8")), "utf-8"),
               "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8', "Host": "api.yimei.ai",
               "Accept": "application/json"}
    #发送请求
    response = requests.post(url, data=bodys, headers=headers)
    #对返回内容进行解码
    req_con = response.content.decode('utf-8')
    data = JSONDecoder().decode(req_con)
    #对返回结果进行判断


    #测试数据
    '''data={'code': 0,
'error_detect_types': 0,
'filename': 'prd-api1/2019/0628/abc16a09674213c00c608ef83d19d4d9-5699102.jpg',
'detect_types': '504205',
'age': {'result': 19},
'detect_type': 131072,
'color': {'result': 'baixi'},
'blackhead': {'filename': 'prd-apiout1/2019/0628/18499943987706adb45e6787dd1d868d-5698935.jpg', 'count': 3, 'score': 97},
'skin_type': {'filename': 'prd-apiout1/2019/0628/6317f1b7ca992a70a7c5d0cadf22c6c4-5699103.jpg', 'result': '0.765',
               'class': [{'result': 0.261, 'class': 'left_cheek'},
                         {'result': 1, 'class': 'right_cheek'},
                         {'result': 1, 'class': 'forehead'},
                         {'result': 0.233, 'class': 'chin'}],
               'oily': '1.000000', 'dry': '0.000000', 'mixed': '0.000000', 'score': 45},
'moisture': {'filename': 'prd-apiout1/2019/0628/1b9956b9f34663703437a7ca19215360-5698936.jpg', 'result': '0.484', 'score': '89',
              'class': [{'result': 0.405, 'class': 'left_cheek'},
                        {'result': 0.643, 'class': 'right_cheek'},
                        {'result': 0.503, 'class': 'forehead'},
                        {'result': 0.312, 'class': 'chin'}]},
'roughness': {'filename': 'prd-apiout1/2019/0628/10e78d1f5b4e2178dd544603979c745b-5698937.jpg', 'score': 80},
'appearance': {'score': 86},
'pore': {'filename': 'prd-apiout1/2019/0628/4a260193e23b95bcc4eb46a9f949702d-5699030.jpg', 'count': 79, 'score': 96},
'wrinkle': {'filename': 'prd-apiout1/2019/0628/ae5fc0af9f39fbb38e4170fdf8aba522-5699031.jpg', 'count': 2, 'score': 95,
              'class': [{'count': 0, 'class': 'forehead'},
                        {'count': 2, 'class': 'eyecorner'},
                        {'count': 0, 'class': 'nasolabial'},
                        {'count': 0, 'class': 'crowfeet'},
                         {'count': 0, 'class': 'glabella'}]},
'dark_circle': {'filename': 'prd-api1/2019/0628/abc16a09674213c00c608ef83d19d4d9-5699102.jpg', 'result': 0},
'pockmark': {'filename': 'prd-apiout1/2019/0628/83162ff1be216e8e2983da43cc63b2fb-5699105.jpg', 'count': 2, 'score': 96},
'face_box': {'x0': 68, 'y0': 69, 'x1': 385, 'y1': 537},
'id': '2df348a2289d5dd0b292d7d421fb7450'}'''


    #根据返回数据存储数据库

    #Table1 皮肤分析历史
    new_skin = models.UserSkin.objects.create()
    new_skin.uid = request.session['user_id']
    #年轻度
    age_ = data['age']['result']
    if age_>=0 and age_<=25:
        y = 100
    elif age_>=26 and age_<=35:
        y = 90
    elif age_>=36 and age_<=46:
        y = 80
    elif age_>=46 and age_<=56:
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
