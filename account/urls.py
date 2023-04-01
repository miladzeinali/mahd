from django.urls import path
from .views import Userregister,UserForgetPass,\
    UserDetail,Userprofiles,UserVerify,home,Webpaycontrol,Payment,Dashbord,UserLogout,Info,about,contact,Usersms

app_name = 'account'
urlpatterns = [
    path('', home, name='home'),

    path('register/',Usersms,name='login'),
    path('verify/',UserVerify,name='userverify'),

    path('webpaycontrol/',Webpaycontrol,name='webpaycontrol'),
    path('payment/',Payment,name='payment'),
    path('dashbord/',Dashbord,name='dashbord'),
    path('Info/',Info,name='info'),

    path('logout/',UserLogout,name='logout'),
    # path('login/',UserLogin,name='login'),

    path('userprofiles/', Userprofiles, name='userprofiles'),
    path('userdetail/<int:id>/', UserDetail, name='detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
]
