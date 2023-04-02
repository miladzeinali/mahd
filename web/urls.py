from django.urls import path
from .views import home,SignUp

app_name = 'web'
urlpatterns = [
    path('signup/',SignUp,name='signup'),
    path('',home,name='home'),
]
