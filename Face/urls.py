from django.urls import path

from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('Face/result/',views.result,name='result'),
	path('login/',views.login,name='login'),
    #path('info/',views.login,name='login'),
]
