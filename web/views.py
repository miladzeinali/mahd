from django.shortcuts import render,redirect
from .models import Userprofile
from django.contrib import messages
def home(request):
    return render(request,'index.html')

def SignUp(request):
    if request.method == 'POST':
        name = request.POST['name']
        father = request.POST['father_name']
        birthday = request.POST['birthday']
        birth_place = request.POST['birthdayplace']
        nin = request.POST['nin']
        create_card_place = request.POST['createcardplace']
        serial_card = request.POST['serialcard']
        home_phone = request.POST['homephone']
        home_code = request.POST['homecode']
        address = request.POST['address']
        city = request.POST['city']
        province = request.POST['province']
        father_name_lastname = request.POST['fathername']
        father_father_name = request.POST['fatherfathername']
        father_nin = request.POST['fathernin']
        father_serial_card = request.POST['fatherserial']
        father_education = request.POST['fathereducation']
        father_phone = request.POST['fatherphone']
        father_work = request.POST['fatherwork']
        father_birth = request.POST['fatherbirth']
        mother_name = request.POST['mothername']
        mother_father_name = request.POST['motherfathername']
        mother_nin = request.POST['mothernin']
        mother_serial_card = request.POST['notherserial']
        mother_education = request.POST['mothereducation']
        mother_phone = request.POST['motherphone']
        mother_work = request.POST['motherwork']
        mother_birth = request.POST['motherbirth']
        telegram_phone = request.POST['telegramphone']
        Userprofile.objects.create(name=name,father=father,birthday=birthday,birth_place=birth_place,nin=nin,
                                   create_card_place=create_card_place,serial_card=serial_card,home_phone=home_phone,home_code=home_code,
                                   address=address,city=city,province=province,father_name_lastname=father_name_lastname,father_father_name=father_father_name,
                                   father_nin=father_nin,father_serial_card=father_serial_card,father_education=father_education,father_phone=father_phone,
                                   father_work=father_work,father_birth=father_birth,mother_name=mother_name,mother_father_name=mother_father_name,mother_nin=mother_nin,
                                   mother_serial_card=mother_serial_card,mother_education=mother_education,mother_phone=mother_phone,mother_work=mother_work,
                                   mother_birth=mother_birth,telegram_phone=telegram_phone)
        messages.success(request,{'اطلاعات شما با موفقیت ثبت شد .'})
        return render(request,'success.html')

    else:
        pass
    return render(request,'admission.html')
