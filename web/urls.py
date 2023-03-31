from django.urls import path
from .views import SignUp, Userprofiles,home,UserDetail,Webpaycontrol,Payment,Userconfirm

app_name = 'web'
urlpatterns = [
    path('signup/',SignUp,name='signup'),
    path('',home,name='home'),
    path('userprofiles/',Userprofiles,name='userprofile'),
    path('userdetail/<int:id>/',UserDetail,name='detail'),
    path('userconfirm/<int:id>/',Userconfirm,name='confirmpay'),
    path('webpaycontrol/',Webpaycontrol,name='webpaycontrol'),
    path('payment/',Payment,name='payment'),
]
