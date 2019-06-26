from django.urls import path

from . import views

urlpatterns = [
	path('',views.index,name='index'),
	path('result/',views.result,name='result'),
	path('login/',views.login,name='login'),
	path('register/',views.register,name='register'),
	path('detect/',views.detect,name='detect'),
	path('history/',views.history,name='history'),
	path('logout/',views.logout,name='logout'),
]
