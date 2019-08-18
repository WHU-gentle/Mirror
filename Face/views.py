from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests, base64
from .utils import *
from . import models
from json import JSONDecoder
import json

# 显示检测结果
def result(request):
    # 保存图片到本地
    data_uri = request.POST['mydata']
    imgSave(data_uri)

    ########################################
    #  从本地读取上次api数据，测试用，不测试时最好注释掉

    data = readData()
    ########################################
    #todo 上传到api ,调用api 时应取消注释
    '''
    req_con = upload2api('detect.jpg').content.decode('utf-8')
    
    print("*******************************************")
    print(req_con)
    print("*******************************************")
    
    data = JSONDecoder().decode(req_con)
    saveData(data)  #保存解析文件，节约 debug 经费
    '''
    ########################################
    data, text = solveData(data)

    data["speak_text"] = json.dumps(text)
    #####################################

    # 出错处理
    if data['code'] != 0:
        return render(request, 'Face/error.html', {"message": data['msg']})

    return render(request, 'Face/scan.html', data)


# 显示历史记录
def history(request):
    # 检查登录
    if not request.session.get('is_login', None):
        return render(request, 'Face/error.html', {"message": "请先进行登录"})
    else:
        pass

    data1 = ['2.21', '2.22', '2.23', '2.24', '2.25', '22.26', '2.27', '2.28', '2.29', '2.30', '3.1', '3.1', '3.2',
             '3.3', '3.4', '3.5', '3.6', '3.7', '3.8', '3.9', '3.10', '3.11', '3.12', '3.13', '3.14', '3.15', '3.16',
             '3.17', '3.18', '3.19', '3.20']
    data2 = [10, 10, 10, 10, 10, 48, 49, 100, 64, 63, 26, 25, 86, 84, 39, 85, 94, 35, 75, 52, 76, 86, 46, 37, 57, 35,
             75, 65, 34, 77]

    return render(request, 'Face/history.html', {'var1': json.dumps(data1), 'var2': json.dumps(data2)})


# 主页
def index(request):
    # 检查登录
    if not request.session.get('is_login', None):
        return render(request, 'Face/error.html', {"message": "请先进行登录"})
    else:
        return render(request, 'Face/home.html')


# 拍照检测
def detect(request):
    return render(request, 'Face/takephoto.html')


# 登录
def login(request):
    if request.session.get('is_login', None):
        user = models.UserInfo.objects.get(uid=request.session['user_id'])
        now = time.strftime("%Y-%m-%d", time.localtime())
        age = int(now.split('-')[0]) - int(str(user.birthday).split('-')[0])
        try:
            record = models.UserSkin.objects.get(uid=user.uid)
            score = record.totalScore
        except:
            score = None
        return render(request, 'Face/info.html', {'UserInfo': user, 'age': age, 'score': score})

    # 在没有session的条件下登录时创建session
    if request.method == "POST":
        userID = request.POST.get('id')
        password = request.POST.get('pwd')
        if userID and password:  # 用户名和密码都不为空
            userID = userID.strip()
            try:
                user = models.UserInfo.objects.get(uid=userID)
                # 验证密码
                if user.passwd == password:
                    request.session['is_login'] = True
                    # 将用户ID(手机号)作为session标记
                    request.session['user_id'] = user.uid
                    now = time.strftime("%Y-%m-%d", time.localtime())
                    age = int(now.split('-')[0]) - int(str(user.birthday).split('-')[0])
                    try:
                        record = models.UserSkin.objects.get(uid=user.uid)
                        score = record.totalScore
                    except:
                        score = None
                    return render(request, 'Face/info.html', {'UserInfo': user, 'age': age, 'score': score})
            except:
                return render(request, 'Face/error.html', {"message": "此账户不存在"})
    return render(request, 'Face/login.html')


# 注册
def register(request):
    if request.method == "POST":
        name = request.POST.get('name_r')
        uid = request.POST.get('id_r')
        if request.POST.get('psd_r') == request.POST.get('affirm_psd'):
            # 密码一致
            passwd = request.POST.get('psd_r')
            gender = request.POST.get('sex_r')
            birthday = request.POST.get('birthday_r')
            new_user = models.UserInfo.objects.create(uid=uid, name=name,
                                                      passwd=passwd, gender=gender, birthday=birthday)
            new_user.save()
    return render(request, 'Face/login.html')



# 注销
def logout(request):
    if not request.session.get('is_login', None):
        # 如果没有登录 也就不需要注销
        return redirect('Face:index')
    # 否则清除session
    request.session.flush()
    return redirect('Face:login')


# 检测
def detect(request):
    if not request.session.get('is_login', None):
        return render(request, 'Face/error.html', {"message": "请先进行登录"})
    else:
        return render(request, 'Face/takephoto.html')
