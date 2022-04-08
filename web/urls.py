from django.urls import path
from .views import SignUp, Userprofiles,home,UserDetail

app_name = 'web'
urlpatterns = [
    path('signup/',SignUp,name='signup'),
    path('',home,name='home'),
    path('userprofiles/',Userprofiles,name='userprofile'),
    path('userdetail/<int:id>/',UserDetail,name='detail'),
]
