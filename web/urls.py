from django.urls import path
from .views import SignUp

app_name = 'web'
urlpatterns = [
    path('signup/',SignUp,name='signup')
]