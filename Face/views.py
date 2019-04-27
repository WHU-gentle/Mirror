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
    if request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('pwd')
        if username and password:#用户名和密码都不为空
            username = username.strip()
            try:
                user = models.User.objects.get(name=username)
                if user.password == password:
                    data={"name":username,"sex":user.sex,"height":user.height,"weight":user.weight,"age":19}
                    return render(request,'Face/info.html',data)
            except:
                return render(request,'Face/info.html')

    return render(request,'Face/login.html')

#注册
#def register(request):

    
def result(request):

    #所用参数赋值
    url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
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
        return render(request,'Face/error.html')


#填补base64码的空白
def decode_base64(strg): 
    lens = len(strg)
    lenx = lens - (lens % 4 if lens % 4 else 4)
    r = base64.b64decode(strg[:lenx])
    return r
