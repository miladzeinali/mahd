from django.shortcuts import render, redirect
from .models import Userprofile
from django.contrib import messages
from .SmsHandler import SmsHandler
from django.views.decorators.csrf import csrf_exempt
from kavenegar import *


def home(request):
    return render(request, 'index.html')


@csrf_exempt
def SignUp(request):
    if request.method == 'POST' and request.POST['name']:
        nin = request.POST['nin']
        try:
            Userprofile.objects.get(nin=nin)
            messages.error(request, {'کد ملی تکراری است.'})
            return render(request, 'admission.html')
        except:
            pass
        name = request.POST['name']
        father = request.POST['father_name']
        birthday = request.POST['birthday']
        birth_place = request.POST['birthdayplace']
        create_card_place = request.POST['createcardplace']
        sericard = request.POST['sericard']
        serialcard = request.POST['serialcard']
        fatherseri = request.POST['fatherseri']
        fatherserial = request.POST['fatherserial']
        motherseri = request.POST['motherseri']
        motherserial = request.POST['motherserial']
        home_phone = request.POST['homephone']
        home_code = request.POST['homecode']
        address = request.POST['address']
        city = request.POST['city']
        province = request.POST['province']
        hand = request.POST['hand']
        talagh = request.POST['talagh']
        bimeh = request.POST['bimeh']
        shahid = request.POST['shahid']
        farhangi = request.POST['farhangi']
        children = request.POST['children']
        child = request.POST['child']
        father_name_lastname = request.POST['fathername']
        father_father_name = request.POST['fatherfathername']
        father_nin = request.POST['fathernin']
        father_education = request.POST['fathereducation']
        father_phone = request.POST['fatherphone']
        father_work = request.POST['fatherwork']
        father_birth = request.POST['fatherbirth']
        mother_name = request.POST['mothername']
        mother_father_name = request.POST['motherfathername']
        mother_nin = request.POST['mothernin']
        mother_education = request.POST['mothereducation']
        mother_phone = request.POST['motherphone']
        mother_work = request.POST['motherwork']
        mother_birth = request.POST['motherbirth']
        telegram_phone = request.POST['telegramphone']
        eplace = request.POST['eplace']
        try:
            Userprofile.objects.get(nin=nin)
            messages.error(request, {'کد ملی تکراری است.'})
            return render(request, 'admission.html')
        except:
            Userprofile.objects.create(name=name, father=father, birthday=birthday
                                       , birth_place=birth_place, nin=nin, create_card_place=create_card_place,
                                       Sericard=sericard, Serialcard=serialcard, Fatherseri=fatherseri,
                                       Fatherserial=fatherserial, Motherseri=motherseri, Motherserial=motherserial,
                                       Hand=hand, Talagh=talagh, Bimeh=bimeh, Shahid=shahid, Farhangi=farhangi,
                                       Children=children, Child=child, home_phone=home_phone, home_code=home_code,
                                       address=address, city=city, province=province,
                                       father_name_lastname=father_name_lastname, father_father_name=father_father_name,
                                       father_nin=father_nin, father_education=father_education,
                                       father_phone=father_phone, father_work=father_work, father_birth=father_birth,
                                       mother_name=mother_name, mother_father_name=mother_father_name,
                                       mother_nin=mother_nin, mother_education=mother_education,
                                       mother_phone=mother_phone, mother_work=mother_work, mother_birth=mother_birth,
                                       telegram_phone=telegram_phone, e_place=eplace)
            r = {
                'status': 'success',
                'total_price_to_pay': '100000',
                'nin': nin,
                'father_phone':father_phone
            }
            resp = []
            resp.insert(0, r)
            request.session['r'] = r
            return render(request, 'payment.html')
    else:
        pass
    return render(request, 'admission.html')

def Payment(request):
    return redirect('zarinpal:request')

def Webpaycontrol(request):
        try:
            nin = request.session['r']['nin']
            # father_phone = request.session['r']['father_phone']
            user = Userprofile.objects.get(nin=nin)
            user.pay = True
            user.save()
            # messages.success(request, {'اطلاعات شما با موفقیت ثبت شد .'})
            # api = KavenegarAPI('7335726878564E2F506C4A3857457773624F70634C466A7A586F456D345A78544F7845446B3263635832773D') 
            # params = { 'sender' : '100047778', 'receptor': f'{father_phone}', 'message' :' ثبت نام شما با موفقیت انجام شد !' } 
            # response = api.sms_send( params) 
            return render(request,'success.html')
        except:
            print('milad')

def UserDelete(request):
    try:
        nin = request.session['r']['nin']
        user = Userprofile.objects.get(nin=nin)
        user.delete()
        # return render(request, 'index.html')
    except:
        print('error in user delete!')
        # return render(request, 'index.html')
        
def Userprofiles(request):
    try:
        userprofiles = Userprofile.objects.all().order_by('-id')
        return render(request, 'userprofile.html', {'userprofiles': userprofiles})
    except:
        return render(request, 'index.html')


def UserDetail(request, id):
    try:
        userprofile = Userprofile.objects.get(id=id)
        return render(request, 'userdetail.html', {'userprofile': userprofile})
    except:
        return render(request, 'index.html')

def Userconfirm(request,id):
    try:
        userprofile = Userprofile.objects.get(id=id)
        if userprofile.pay:
            userprofile.pay = False
        else:
            userprofile.pay = True
        userprofile.save()
        return redirect('web:userprofile')
    except:
        messages.error(request,'در فرایند تغییرات اشکالی پیش امده است!','error')
        return redirect('web:userprofile')

