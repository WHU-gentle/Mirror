from django.shortcuts import render
from django.http import HttpResponse
import requests
from json import JSONDecoder

# Create your views here.
def index(request):    
    return render(request,'Face/home.html')
    
def result(request):

    url = "https://api-cn.faceplusplus.com/facepp/v3/detect"
    key = "qM0Y_YHyYH4Xjajsa41ypxOUlnzEI-cg"
    secret = "L-lnwmoVCXzuL0ShEYhFB9TlVQ6hyIWZ"
    img = request.POST['pic']
    attr = "skinstatus"

    data={"api_key":key,"api_secret":secret,"image_base64":img,"return_attributes":attr}
    
    response = requests.post(url,data=data)
    
    req_con = response.content.decode('utf-8')
    req_dict = JSONDecoder().decode(req_con)
    
    content = req_dict['faces'][0]['attributes']['skinstatus']

    return render(request,'Face/result.html',content)
