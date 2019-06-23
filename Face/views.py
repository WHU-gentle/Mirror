from django.shortcuts import render,redirect
from django.http import HttpResponse
import requests
from json import JSONDecoder
import base64
import os
from . import models

# Create your views here.
#主页
def index(request):    
    return render(request,'Face/home.html')
#登录&注册
def login(request):

    if request.session.get('is_login',None):
        user = models.User.objects.get(name=request.session['user_name'])
        data = {"name": user.name, "sex": user.sex, "height": user.height, "weight": user.weight, "age": 19}
        return render(request,'Face/info.html',data)

    #在没有session的条件下登录时创建session
    if request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        if username and password:#用户名和密码都不为空
            username = username.strip()
            #后期用于进行密码格式相关验证
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:#验证密码
                    request.session['is_login']=True
                    request.session['user_name']=user.name #将用户名作为session标记
                    data={"name":username,"sex":user.sex,"height":user.height,"weight":user.weight,"age":19}
                    return render(request,'Face/info.html',data)
            except:
                return render(request,'Face/info.html')

    return render(request,'Face/login.html')

#注册
def register(request):
    if request.method=="POST":
        new_user = models.User.objects.create()
        new_user.name = request.POST.get('name_r')
        if request.POST.get('psd_r')==request.POST.get('affirm_psd'):
            #密码一致
            new_user.password = request.POST.get('psd_r')
        else:
            #返回密码不一致信息
        new_user.sex = request.POST.get('sex_r')

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
    '''url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    key = "qM0Y_YHyYH4Xjajsa41ypxOUlnzEI-cg"
    secret = "L-lnwmoVCXzuL0ShEYhFB9TlVQ6hyIWZ"
    img = request.POST['pic']
    attr = "skinstatus"
    
    #保存图片到本地
    imagedata = decode_base64(img[len("data:image/jpg;base64,"):])
    with open('p.jpg','wb') as file:
        file.write(imagedata)

    data={"api_key":key,"api_secret":secret,"image_base64":img,"return_attributes":attr}
    #发送数据
    response = requests.post(url,data=data)
    #对返回内容进行解码
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    #对返回结果进行判断
    if len(req_dict['faces'])!=0:
        content = req_dict['faces'][0]['attributes']['skinstatus'] 
        return render(request,'Face/result.html',content)
    else:
        return render(request,'Face/error.html')'''
    
    #测试数据
    data={'code': 0,
'error_detect_types': 0,
'filename': 'prd-api1/2019/0427/ddfbb4fcb4ebad1cd7e408dc92b11fe5-2113336.jpg',
'detect_types': '504205',
'age': {'result': 31},
 'detect_type': 131072,
  'blackhead': {'filename': 'prd-apiout1/2019/0427/d88f41e87bf6fdb9e02a7e6012b1eb52-2113337.jpg',
                 'count': 12,
                 'score': 88},
  'color': {'result': 'ziran'},
  'roughness': {'filename': 'prd-apiout1/2019/0427/c915ad19e7b96613efca346c5a9d9096-2113338.jpg',
                'score': 96},
  'moisture': {'filename': 'prd-apiout1/2019/0427/eee90c2c3ed3059799396ab6c29cf87b-2113198.jpg',
                'result': '0.348',
                'score': '86',
                 'class': [{'result': 0.331, 'class': 'left_cheek'},
                             {'result': 0.36, 'class': 'right_cheek'},
                             {'result': 0.397, 'class': 'forehead'},
                             {'result': 0.287, 'class': 'chin'}]},
  'skin_type': {'filename': 'prd-apiout1/2019/0427/8389afca8e7c18ae901d3b3a6e587edf-2113241.jpg',
                'result': '0.831',
                'class': [{'result': 0.882, 'class': 'left_cheek'},
                            {'result': 0.509, 'class': 'right_cheek'},
                            {'result': 1, 'class': 'forehead'},
                             {'result': 0.801, 'class': 'chin'}],
                'oily': '1.000000', 'dry': '0.000000', 'mixed': '0.000000', 'score': 40},
   'appearance': {'score': 83},
   'pore': {'filename': 'prd-apiout1/2019/0427/c21cbff09c91c6e72a4f9ed1ee4a05dd-2113339.jpg', 'count': 403, 'score': 79},
   'wrinkle': {'filename': 'prd-apiout1/2019/0427/24719d4725c9d16a2fdb88d29945f695-2113199.jpg', 'count': 6, 'score': 82,
                'class': [{'count': 1, 'class': 'forehead'},
                            {'count': 2, 'class': 'eyecorner'},
                            {'count': 2, 'class': 'nasolabial'},
                            {'count': 1, 'class': 'crowfeet'},
                             {'count': 0, 'class': 'glabella'}]},
   'dark_circle': {'filename': 'prd-api1/2019/0427/ddfbb4fcb4ebad1cd7e408dc92b11fe5-2113336.jpg', 'result': 0},
   'pockmark': {'filename': 'prd-apiout1/2019/0427/1f6f84374fed35d7a80113ff4b8d2505-2113201.jpg', 'count': 2, 'score': 96},
   'id': 'a616e7364557b6f9975f2aca1b7b996c'}

    return render(request,'Face/scan.html',data)


#填补base64码的空白
def decode_base64(strg): 
    lens = len(strg)
    lenx = lens - (lens % 4 if lens % 4 else 4)
    r = base64.b64decode(strg[:lenx])
    return r
