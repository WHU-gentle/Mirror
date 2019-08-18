## 环境配置指南 
强烈推荐在linux中配置，除非你特别爱折腾windows
1. 安装 conda
2. 从环境文件中恢复：
`conda env create -n New_Mirror -f environment.yml`
3. 切换到新环境
`conda activate New_Mirror`

## 本地调试运行
`python3 manage.py runserver 0.0.0.0:8080`

## https 运行
`python manage.py runserver_plus 0.0.0.0:8080 --cert-file /path/to/cert.crt`

## 访问、管理 
浏览器访问 http://127.0.0.1:8080/Face/  
测试用户名 test001 密码 test001    
管理界面 http://127.0.0.1:8080/admin/  
管理用户名 admin 密码 mirror

## runserver可能出现的错误：
1 `no mudole named 'django-extensions' ` 
Solution：pip install django-extensions 
检查：命令行输入python,在>>>输入 `import django-extenions` 若没有报错则成功

2 在实时视频界面，出现有关webcam的报错
可能是因为你用的ubuntu虚拟机，虚拟机没有分配到摄像头。
Solution：安装虚拟机的“增强功能”。搜教程建议用google而不是百度

## 拍照结果的说明
为了省钱，我把拍照调用API的代码注释掉了，这样每次拍照都不用花钱，显示的结果是我测试的时候的结果。传到服务器时记得取消注释。

## 招教程，请google,比百度找出来的教程少很多坑！！！

## 晨晨要做的事情：
Face/templates/Face/base.html      line 37
Face/templates/Face/home.html      line 66
Face/templates/Face/takephoto.html line 16

## 小武要做的事情：
添加声音控制拍照的功能（建议按照我QQ发给你的链接的教程来）
若有余力，再添加语音播报肤质分析结果的段落

## 你俩分开写，写好了到学校见面了一起合并，省得出错。
## 注意代码的质量，要逻辑清晰、美观
