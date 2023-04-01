from django.urls import re_path as url
from . import views
app_name='zarinpal'
urlpatterns = [
    url(r'^request/$', views.send_request, name='request'),
    url(r'^verify/$', views.verify, name='verify'),
]
