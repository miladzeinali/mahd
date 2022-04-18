from django.urls import path
from .views import SignUp,home

app_name = 'web'
urlpatterns = [
    path('signup/',SignUp,name='signup'),
    path('',home,name='home'),
]
