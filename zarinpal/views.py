# -*- coding: utf-8 -*-
# Github.com/Rasooll
from django.http import HttpResponse
from django.shortcuts import redirect
from zeep import Client
from django.contrib import messages
from web.views import Webpaycontrol,UserDelete

MERCHANT = 'bdae3de6-ef15-49e6-903b-34cc18e656cb'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
# amount = 100  # Toman / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'email@example.com'  # Optional
mobile = '09123456789'  # Optional
CallbackURL = 'http://bafghmahd.ir/zarinpal/verify/' # Important: need to edit for realy server.



def send_request(request):
    amount=request.session['r']['total_price_to_pay']
    result = client.service.PaymentRequest(MERCHANT, amount, description, email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return HttpResponse('Error code: ' + str(result.Status))

def verify(request):
    amount=request.session['r']['total_price_to_pay']
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            Webpaycontrol(request)
            return redirect('web:home')
        elif result.Status==101:
            Webpaycontrol(request)
            return redirect('web:home')
        else:
            UserDelete(request)
            return redirect('web:home')
    else:
        UserDelete(request)
        return redirect('web:home')

