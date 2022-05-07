from django.urls import path
from .views import SignUp, Userprofiles,home,UserDetail,Webpaycontrol,Payment

app_name = 'web'
urlpatterns = [
    path('signup/',SignUp,name='signup'),
    path('',home,name='home'),
    path('userprofiles/',Userprofiles,name='userprofile'),
    path('userdetail/<int:id>/',UserDetail,name='detail'),
    path('webpaycontrol/',Webpaycontrol,name='webpaycontrol'),
    path('payment/',Payment,name='payment'),
]
