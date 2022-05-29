from django.contrib import messages
from django.shortcuts import render, redirect

from kids.models import Kids
from patient.models import register, mydata
from .models import Child, Injection, Single1, Child1, Multi1, hospital_record, colera_record, hos_dose
from .models import Hospital
from .models import Multi
from .models import Single
import random
import string
from datetime import datetime


def home(request):
    return render(request, 'index.html')


def regi(request):
    if request.method == "POST":
        # a = request.POST.get('regno')
        b = request.POST.get('pass')
        c = request.POST.get('nam')
        d = request.POST.get('email')
        e = request.POST.get('add')

        rn = (random.randint(1000, 10000))
        let = string.ascii_uppercase
        ltc = (''.join(random.choice(let) for i in range(3)))
        rne = str(ltc) + str(rn)

        Hospital.objects.create(RegisterNumber=rne, Password=b, Name=c, Email=d, Address=e)
        messages.success(request,
                         "This is your Register Number : " + rne)

        return redirect('login')

    return render(request, 'reg.html')


# def regis(request):
#
#
#     return render(request, 'userreg.html')


def log(request):
    if request.method == "POST":
        f = request.POST.get("username")
        p = request.POST.get("password")
        if Hospital.objects.filter(RegisterNumber=f, Password=p).exists():
            print("hiiiiiiii")
            return redirect('view')


        else:
            messages.info(request, 'User Is Not Exists')
            return redirect('login')

    return render(request, 'login.html')


def view1(request):
    print("hhhhhhhhhhhhhhhhhhhhhhhh")
    # if request.method == "POST":
    #     a = request.POST.get('name')
    #     b = request.POST.get('vno')
    #     c = request.POST.get('time')
    #     d = request.POST.get('gap')
    #
    #     Vaccine.objects.create(Name=a, VaccineNumber=b, Time=c, PreviousDose=d)

    # return redirect('login')
    return render(request, 'view.html')


def Admin_log(request):
    if request.method == "POST":
        f = request.POST.get("username")
        p = request.POST.get("password")
        a = "admin"
        b = "password"
        if f == a and p == b:
            print(a, b)
            return redirect('admin_view')


        else:
            messages.info(request, 'User Is Not Exists')
            return redirect('Admin_login')

    return render(request, 'Admin_login.html')


def admin_view(request):
    a = Hospital.objects.all()
    b = hospital_record.objects.all()
    c = Multi.objects.all()
    d = Child.objects.all()
    e = colera_record.objects.all()

    return render(request, 'Admin_view.html', {'prd': a, 'rrr': b, 'ddd': c, 'ccc': d, 'bbb': e})


def delete(request, product_Id):
    a = Hospital.objects.get(Id=product_Id)
    a.delete()
    return redirect('admin_view')


def cat1(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('vno')
        c = request.POST.get('details')
        d = request.POST.get('duration')
        e = request.POST.get('available')

        Single.objects.create(Name=a, VaccineNumber=b, Details=c, Duration=d, Number_of_vaccine=e)
    return render(request, 'cat1.html')


#
def cat2(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('vno')
        c = request.POST.get('details')
        d = request.POST.get('duration')
        e = request.POST.get('available')

        Multi.objects.create(Name=a, VaccineNumber=b, Details=c, Duration=d, Number_of_vaccine=e)
    return render(request, 'cat2.html')


#
#
def cat3(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('vno')
        c = request.POST.get('details')
        d = request.POST.get('duration')
        e = request.POST.get('available')

        Child.objects.create(Name=a, VaccineNumber=b, Details=c, Duration=d, Number_of_vaccine=e)
    return render(request, 'cat3.html')


def viee(request):
    # request.session['user_id'] = id
    return render(request, 'hospitaledit.html', )


def edi(request):
    if request.method == "POST":
        v = request.POST.get('regno')
        vax_name = request.POST.get('vax_name')
        w = request.POST.get('dosesss')

        now = datetime.now()

        print(vax_name)

        # dd/mm/YY H:M:S
        dt_string = now.strftime("%H:%M:%S")
        print("date and time =", dt_string)

        child = Kids.objects.filter(RegisterNumber=v)
        for i in child:

            if hos_dose.objects.filter(Registernumber=v, adult_child=0).exists():

                hos_dose.objects.filter(Registernumber=v, adult_child=0).update(vaccine_dose=w, date=dt_string,
                                                                                vaccinename=vax_name)
                vax = Child.objects.filter(Name=vax_name)
                for l in vax:
                    Child.objects.filter(Name=vax_name).update(Number_of_vaccine=str(int(l.Number_of_vaccine) - 1))

            else:

                hos_dose.objects.create(Registernumber=v, adult_child=0, vaccine_dose=w, date=dt_string,
                                        vaccinename=vax_name)
                vax = Child.objects.filter(Name=vax_name)
                for l in vax:
                    Child.objects.filter(Name=vax_name).update(Number_of_vaccine=str(int(l.Number_of_vaccine) - 1))

    return render(request, 'hospitaledit.html', )


def adult_edi(request):
    if request.method == "POST":
        v = request.POST.get('regno')
        w = request.POST.get('dosesss')

        now = datetime.now()

        print("now =", now)

        # dd/mm/YY H:M:S
        dt_string = now.strftime("%H:%M:%S")
        print("date and time =", dt_string)

        add = register.objects.filter(RegisterNumber=v)
        for i in add:
            if hos_dose.objects.filter(Registernumber=v, adult_child=1).exists():
                sk = Multi1.objects.filter(Patient_Id=i.Id)
                for ll in sk:
                    hos_dose.objects.filter(Registernumber=v, adult_child=1).update(vaccine_dose=w, date=ll.Date,
                                                                                    vaccinename=ll.Name)
            else:
                sk = Multi1.objects.filter(Patient_Id=i.Id)
                for ll in sk:
                    hos_dose.objects.create(Registernumber=v, adult_child=1, vaccine_dose=w, date=ll.Date,
                                            vaccinename=ll.Name)

    return render(request, 'hospitaledit.html', )


def editvie(request, id, d):
    request.session['uu'] = id
    request.session['uv'] = d
    kl = mydata.objects.filter(User_Id=id)
    for i in kl:
        print(i.File)

    return render(request, 'editview.html', {'prd': kl})


def btn(request):
    if request.method == 'POST':
        sec = request.session['uu']
        set = request.session['uv']
        u = request.POST.get('dose')

        if int(set) == 0:
            ll = Kids.objects.filter(Id=int(sec))
            for i in ll:

                if Injection.objects.filter(RegisterNumber=i.RegisterNumber, Patient_Id=i.Id).exists():

                    Injection.objects.filter(RegisterNumber=i.RegisterNumber, Patient_Id=i.Id).update(Vaccine_Dose=u)
                else:

                    Injection.objects.create(RegisterNumber=i.RegisterNumber, Patient_Id=i.Id, Vaccine_Dose=u,
                                             Name=i.Name, Child_or_adult=0)
        else:

            ll = register.objects.filter(Id=int(sec))
            for i in ll:

                if Injection.objects.filter(RegisterNumber=i.RegisterNumber, Patient_Id=i.Id).exists():

                    Injection.objects.filter(RegisterNumber=i.RegisterNumber, Patient_Id=i.Id).update(Vaccine_Dose=u)
                else:

                    Injection.objects.create(RegisterNumber=i.RegisterNumber, Patient_Id=i.Id, Vaccine_Dose=u,
                                             Name=i.Name, Child_or_adult=1)

    return render(request, 'editview.html', )


def shed(request):
    loggg = request.session['user_id']
    print(loggg)
    kk = Single1.objects.filter(Patient_Id=loggg)
    dd = register.objects.filter(Id=loggg)
    for i in kk:
        print(i.Name, i.Dosage, i.Date, i.vacc_type, i.Time)
    jj = Multi1.objects.filter(Patient_Id=loggg)
    kd = hospital_record.objects.filter(Patient_Id=loggg)
    for b in kd:
        print(b.Object)
    nn = Child1.objects.filter(Patient_Id=loggg)

    return render(request, "shedules.html", {'rrl': kk, 'rrd': jj, 'rrp': nn, 'llr': dd, 'lili': kd})


def stock(request):
    a = Multi.objects.all()
    b = Child.objects.all()
    # a = Multi.objects.get(Id=product_Id)
    # print(a)

    return render(request, "stock_update.html", {'prd': a, 'rrd': b})


def stockupdate(request, product_Id):
    if request.method == "POST":
        s = request.POST.get('tetunus')
        print(s, "ooooooooooooooooooooooooooooo")
        o = request.POST.get('childstock')

        print(o)

        k = Multi.objects.filter(Id=product_Id).update(Number_of_vaccine=s)
        b = Child.objects.filter(Id=product_Id).update(Number_of_vaccine=o)

    return render(request, "stock_update.html")
