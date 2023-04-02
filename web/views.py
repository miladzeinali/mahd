from django.shortcuts import render, redirect
from .models import Userprofile
from django.contrib import messages
from .SmsHandler import SmsHandler
from django.views.decorators.csrf import csrf_exempt

sms = SmsHandler()


def home(request):
    return render(request, 'index.html')


@csrf_exempt
def SignUp(request):
    return render(request,'register.html')

def Payment(request):
    return redirect('zarinpal:request')

def Webpaycontrol(request):
        try:
            nin = request.session['r']['nin']
            user = Userprofile.objects.get(nin=nin)
            user.pay = True
            user.save()
            return render(request,'succsess.html')
        except:
            messages.success(request, 'erorr in webpaycontrol', 'erorr')
            return render(request, 'addmission.html')

