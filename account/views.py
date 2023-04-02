from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
import re
from django.contrib import messages
from account.models import *
from random import randint
import requests
from django.views.decorators.csrf import csrf_exempt
import datetime
from web.models import Userprofile 
import requests

def home(request):
    return render(request, 'index.html')

def Usersms(request):
    if request.method == 'POST':
        form = request.POST
        if form['mobile']:
            rule = re.compile(r'(^0)[\d]{10}$')
            if not rule.search(form['mobile']):
                messages.error(request,'شماره موبایل معتبر نیست!','error')
                return render(request,'register.html')
            mobile = form['mobile']
            try:
                Userprofile.objects.filter(father_phone=mobile).last()
                try:
                    ValidOqbject = ValidationCode.objects.get(mobile=mobile)
                except:
                    code = randint(100000,999999)
                    ValidOqbject = ValidationCode.objects.create(mobile=mobile,validation_code=code)
            except:
                code = randint(100000,999999)
                ValidOqbject = ValidationCode.objects.create(mobile=mobile,validation_code=code)        
            code = ValidOqbject.validation_code
            # send sms to user
            params = (('receptor', f'{mobile}'), ('token', f'{code}'), ('template', 'codebafghmahd'))
            requests.post('https://api.kavenegar.com/v1/7335726878564E2F506C4A3857457773624F70634C466A7A586F456D345A78544F7845446B3263635832773D/verify/lookup.json',
                                  params = params)
            r = {
                            'mobile': mobile,
                        }
            resp = []
            resp.insert(0, r)
            request.session['r'] = r
            return render(request,'userverify.html')
        else:
            return redirect('account:register')
    else:
        return render(request,'register.html')

def UserVerify(request):
        try:
            mobile = request.session['r']['mobile']
            code = request.POST['code']
            if mobile:
                try:
                    ValidationCode.objects.get(mobile=mobile,validation_code=code)
                    r = requests.get('https://api.keybit.ir/time/')
                    resp = r.json()
                    year = resp['date']['year']['number']['en']
                    try:
                        user = User.objects.get(username=mobile)
                        profile = Userprofile.objects.filter(father_phone=mobile)
                        v = len(profile)
                        print(profile)
                        print(v)
                        if v != 0:
                            oldyear = profile.last().yearadded
                            if oldyear != year:
                                Userprofile.objects.create(father_phone=mobile,yearadded=year,user=user)
                    except:
                        user = User.objects.create_user(username=mobile,password=code)
                        try:
                            profile = Userprofile.objects.filter(father_phone=mobile).last()
                            userold = profile.user
                            if user != userold:
                                profile.user = user
                                profile.save()
                            Userprofile.objects.create(father_phone=mobile,user=user,yearadded=year) 
                        except:
                            Userprofile.objects.create(father_phone=mobile,yearadded=year,user=user)
                    if user:
                        login(request,user)
                        return redirect('account:dashbord')
                    else:
                        messages.error(request,'رمز را به صورت صحیح وارد نمایید!','error')
                        return render(request,'register.html')
                except:
                        messages.error(request,'رمز را به صورت صحیح وارد نمایید!','error')
                        return render(request,'register.html')
            else:
                messages.error(request,'مشکلی در فرآیند ثبت نام پیش آمده است!','error')
                return redirect('account:home')
        except:
            messages.error(request, 'مشکلی در فرآیند ثبت نام پیش آمده است!', 'error')
            return redirect('account:home')

@csrf_exempt
def Info(request):
    if request.method == 'POST' and request.POST['name']:
        name = request.POST['name']
        last_name = request.POST['last_name']
        father = request.POST['father']
        birthday = request.POST['birthday']
        birth_place = request.POST['birthdayplace']
        nin = request.POST['nin']
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
        # father_name_lastname = request.POST['fathername']
        father_father_name = request.POST['fatherfathername']
        father_nin = request.POST['fathernin']
        father_education = request.POST['fathereducation']
        # father_phone = request.POST['fatherphone']
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
        if name:
                user = request.user
                userProfile = Userprofile.objects.filter(user=user).last()
                userProfile.name = name
                userProfile.last_name = last_name
                userProfile.father = father
                userProfile.birth_place = birth_place
                userProfile.birthday = birthday
                userProfile.create_card_place = create_card_place
                userProfile.Sericard = sericard
                userProfile.Serialcard = serialcard
                userProfile.Fatherseri = fatherseri
                userProfile.Fatherserial = fatherserial
                userProfile.Motherseri = motherseri
                userProfile.Motherserial = motherserial
                userProfile.nin = nin
                userProfile.home_phone = home_phone
                userProfile.home_code = home_code
                userProfile.city = city
                userProfile.province = province
                userProfile.address = address
                userProfile.father_father_name = father_father_name
                userProfile.father_nin = father_nin
                userProfile.father_education = father_education
                userProfile.father_work = father_work
                userProfile.father_birth = father_birth
                userProfile.mother_name = mother_name
                userProfile.mother_father_name = mother_name
                userProfile.mother_father_name = mother_father_name
                userProfile.mother_nin = mother_nin
                userProfile.mother_education = mother_education
                userProfile.mother_phone = mother_phone
                userProfile.mother_work = mother_work
                userProfile.mother_birth = mother_birth
                userProfile.telegram_phone = telegram_phone
                userProfile.e_place = eplace
                userProfile.Hand = hand
                userProfile.Talagh = talagh
                userProfile.Shahid = shahid
                userProfile.Bimeh = bimeh
                userProfile.Farhangi = farhangi
                userProfile.Children = children
                userProfile.Child = child
                userProfile.save()
                mobile = userProfile.father_phone
                # send sms to user
                params = (('receptor', f'{mobile}'), ('token', f'{name}'), ('template', 'Info'))
                requests.post(
                    'https://api.kavenegar.com/v1/7335726878564E2F506C4A3857457773624F70634C466A7A586F456D345A78544F7845446B3263635832773D/verify/lookup.json',
                    params=params)
                messages.success(request,'اطلاعات شما با موفقیت ثبت شد!','success')
                return redirect('account:dashbord')
        else:
                messages.error(request,'اطلاعات به صورت صحیح وارد نشده است !','error')
                return redirect('account:dashbord')
    else:
        return render(request,'dashbord.html')

def Payment(request):
    return redirect('zarinpal:request')

def Webpaycontrol(request):
        try:
            user = request.user
            r = requests.get('https://api.keybit.ir/time/')
            resp = r.json()
            year = resp['date']['year']['number']['en']
            userProfile = Userprofile.objects.get(user=user,yearadded=year)
            userProfile.pay = True
            userProfile.save()
            messages.success(request, 'پرداخت شما با موفقیت ثبت شد .','success')
            return redirect('account:dashbord')
        except:
            messages.success(request, 'erorr in webpaycontrol', 'erorr')
            return redirect('account:dashbord')

def Dashbord(request):
    try:
        user =request.user
        if user.is_authenticated:
            userProfile = Userprofile.objects.filter(user=user.id).last()
            return render(request,'dashbord.html',{'profile':userProfile})
        else:
            messages.error(request, 'برای دسترسی ابتدا وارد شوید!', 'error')
            return redirect('account:home')
    except:
        messages.error(request,'اشکال در ارتباط با داشبورد','error')
        return render(request,'dashbord.html')
        return redirect('account:home')

def Yearcategory(request):
    years = Year.objects.all()
    return render(request,'yearcategory.html',{'years':years})

def Userprofiles(request,year):
    try:
        userprofiles = Userprofile.objects.filter(yearadded=year).order_by('-id')
        return render(request, 'userprofile.html', {'userprofiles': userprofiles})
    except:
        return render(request, 'index.html')

def UserDetail(request, id):
    try:
        userprofile = Userprofile.objects.get(id=id)
        return render(request, 'userdetail.html', {'userprofile': userprofile})
    except:
        return render(request, 'index.html')
    return redirect('account:home')

# def UserLogin(request):
#     if request.method == "POST":
#         try:
#             mobile = request.POST['mobile']
#             password = request.POST['password']
#             try:
#                 profile = Userprofile.objects.get(father_phone=mobile)
#                 user = profile.user
#                 userLogin = authenticate(request,username = mobile,password = password)
#                 if userLogin is not None:
#                     login(request,user)
#                     user.last_login = datetime.datetime.now()
#                     user.save()
#                     if profile.name:
#                         messages.success(request,f' عزیز شما با موفقیت وارد شدید!{profile.name}','success')
#                     else:
#                         messages.success(request,'شما با موفقیت وارد شدید!','success')
#                     return redirect('account:dashbord')
#                 else:
#                     messages.error(request,'لطفا رمز را به صورت صحیح وارد کنید!','error')
#                     return render(request,'login.html')
#             except:
#                 messages.error(request,'نوآموزی با این شماره موبایل ثبت نام نشده است!','error')
#                 return render(request,'login.html')
#         except:
#             messages.error(request,'لطفا مقادیر را به صورت صحیح وارد نمایید!','error')
#             return render(request,'login.html')
#     else:
#         return render(request,'login.html')

def UserLogout(request):
    logout(request)
    messages.success(request, "شما با موفقیت خارج شدید!", 'success')
    return redirect('account:home')

def about(request):
   return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def searchbar(request):
    print(request.POST)
    search = request.POST['search']
    print(search)
    if search:
        userprofiles = Userprofile.objects.filter(name__contains=search)
    return render(request, 'userprofile.html', {'userprofiles' : userprofiles})













