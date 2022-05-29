import os
import random
import string
from datetime import date, time
from datetime import datetime, timedelta
import mimetypes
import os.path
from wsgiref.util import FileWrapper

from django.contrib import messages
from django.core.mail import send_mail
from django.http import StreamingHttpResponse
import threading
import time

from django.shortcuts import render, redirect

# Create your views here.
from django.utils.datetime_safe import strftime

from hospital.models import Hospital, Single, Multi, Child, Child1, Injection, hos_dose

# Create your views here.
from kids.models import Kids, aknow, messagesre
from patient.models import mydata, post1
from vaxin import settings
from datetime import datetime


def login(request):
    if request.method == "POST":
        f = request.POST.get("username")
        p = request.POST.get("password")
        if Kids.objects.filter(RegisterNumber=f, Password=p).exists():
            h = Kids.objects.filter(RegisterNumber=f, Password=p)
            for i in h:
                request.session['user_id'] = i.Id
            print("hiiiiiiii")
            return redirect('kidsbase')


        else:
            messages.info(request, 'User Is Not Exists')
            return redirect('kidslogin')

    return render(request, "kidslogin.html", )
    #     else:
    #         messages.info(request, 'User Is Not Exists')
    #         return redirect('login')
    # return render(request, 'transcription/userlogin.html')


def regi(request):
    if request.method == "POST":
        # a = request.POST.get('regno')
        b = request.POST.get('pass')
        c = request.POST.get('nam')
        d = request.POST.get('email')
        e = request.POST.get('add')
        f = request.POST.get('age')
        g = request.POST.get('dob')
        h = request.POST.get('phone')
        i = request.POST.get('addha')

        rn = (random.randint(1000, 10000))
        let = string.ascii_uppercase
        ltc = (''.join(random.choice(let) for i in range(3)))
        rne = str(ltc) + str(rn)

        Kids.objects.create(RegisterNumber=rne, Password=b, Name=c, Email=d, Address=e, Age=f, Dob=g, Phone=h, Aadhar=i)
        messages.success(request,
                         "This is your Register Number : " + rne)

        return redirect('kidslogin')

    return render(request, 'kidsreg.html')


def Base(request):
    c = Child.objects.all()

    # try:
    #     loggg = request.session['s']
    #     if loggg is not None:
    #
    #
    #         return redirect("base")
    # except:
    #     messages.info(request, 'Please Login')
    #     return redirect('login')
    # for i in a:
    #     print(i.Name)
    #     print(i.Voice, "------------------------------")
    return render(request, 'kidsBase.html', {'ssd': c})


def addhss(request):
    loggg = request.session['user_id']
    if loggg is not None:
        if request.method == "POST" and request.FILES['image']:
            i = request.FILES['image']
            b = request.POST.get("sub")

            if mydata.objects.filter(User_Id=loggg).exists():
                mydata.objects.filter(User_Id=loggg).update(File=i, Vaccinated=b)

            else:

                mydata.objects.create(File=i, Vaccinated=b, User_Id=loggg, )
            o = Hospital.objects.filter(Id=1)
            for i in o:
                subject = 'confirmation message'
                massage = 'http://127.0.0.1:8000/hospital/editview/' + str(loggg) + "/" + str(0) + "/"
                email_from = settings.EMAIL_HOST_USER
                to = [i.Email]
                send_mail(subject, massage, email_from, to)

            # return redirect('views')

    return render(request, 'kidsubmit.html')


# def booki(request, product_Id):
#     print(product_Id)
#     try:
#         loggg = request.session['user_id']
#         if loggg is not None:
#             a = Kids.objects.get(Id=product_Id)
#
#             return render(request, 'kidbook.html', {'prd': a})
#
#
#     except:
#         messages.info(request, 'Please Login')
#         return redirect('login')
def load_book(request):
    gg = Child.objects.all()

    loggg = request.session['user_id']

    v = Injection.objects.filter(Id=loggg)

    # l = None
    # for i in v:
    #     l = i.Vaccine_Dose
    #     print(l)
    # b = {'dose': range(l), 'prd': gg}
    # print(gg)

    return render(request, 'kidbook.html', {'prd': gg})


def bookin(request):
    if request.method == "POST":
        s = request.POST.get('vacc')
        t = request.POST.get('datee')
        q = request.POST.get('nam')
        print(q, 'sssssssssssssssssssss')
        u = request.POST.get('type')
        print(u, 'pppppppppppppp')
        w = request.POST.get('tim')
        v = "Child Vaccine"
        print(v, 'oooooooooooooooooooooooooo')

        loggg = request.session['user_id']
        print(loggg, "ppppppppppppp")

        date_format = "%d-%m-%Y"
        # c = datetime.strptime(t, date_format)
        # l = Child.objects.get(Id=product_Id)
        if u == v:
            print("tttttttttttttttttttttttttttt")
            a = Child.objects.filter(Name=q)
            vax_d = None
            for i in a:
                vax_d = int(i.Number_of_vaccine)
            if vax_d == 0:
                messages.success(request,
                                 "Vaccine out of Stock : ")
            else:

                pr = Child1.objects.create(Dosage=s, Date=t, Name=q, vacc_type=u, Time=w, Patient_Id=loggg)
                kj = Kids.objects.filter(Id=loggg)

                a = Child.objects.filter(Name=q)
                for i in a:
                    dose = int(i.Number_of_vaccine) - 1
                    Child.objects.filter(Name=q).update(Number_of_vaccine=str(dose))

                for i in kj:
                    subject = 'confirmation message'
                    massage = 'Your Booking Was Confirmed'
                    email_from = settings.EMAIL_HOST_USER
                    to = [i.Email]
                    send_mail(subject, massage, email_from, to)

    dd = Child.objects.all()

    # y = users.objects.get(Id=pr.Id)
    return render(request, 'kidbook.html', {'prd': dd})


# a = Child.objects.get(Id=product_Id)
#
# return render(request, 'kidbook.html', {'prd': a})


def boooooo(request):
    global aaa
    loggg = request.session['user_id']
    print(loggg, '*****************************************************')
    q = Kids.objects.filter(Id=loggg)
    print(q)

    for i in q:
        n = i.Id
        print(n, "//////////////")
        m = i.RegisterNumber
        print(m)
        if hos_dose.objects.filter(Registernumber=m).exists():
            if n == loggg:

                # Python program to create
                # a pdf file

                from fpdf import FPDF

                # save FPDF() class into a
                # variable pdf
                pdf = FPDF()

                # Add a page
                pdf.add_page()

                # set style and size of font
                # that you want in the pdf
                pdf.set_font("Arial", size=15)
                loggg = request.session['user_id']
                print(type(loggg))

                ff = hos_dose.objects.filter(Registernumber=m)
                xx = Kids.objects.filter(Id=str(loggg))
                aaa = None
                for i in xx:
                    aaa = i.Aadhar

                for i in ff:
                    ff = i.vaccinename
                    ddj = i.date
                    ddc = i.vaccine_dose

                    ddf = loggg
                    print(ff)
                    print("bbbbbbbbbbbbbbbbbbbbbbbbbbb")
                    print(ff)
                    # create a cell
                    pdf.cell(200, 10, txt="Provisional Certificate for Vaccination",
                             ln=1, align='C')
                    pdf.cell(200, 10, txt="Patient Id :" + str(ddf),
                             ln=2, align='C')
                    pdf.cell(200, 10, txt="Name :" + ff,
                             ln=3, align='C')
                    pdf.cell(200, 10, txt="Aadhar Number :" + aaa,
                             ln=4, align='C')
                    print(aaa, "0000000000000000000000000000000")
                    # add another cell
                    pdf.cell(200, 10, txt="time :" + str(ddj),
                             ln=5, align='C')
                    pdf.cell(200, 10, txt="No Of Doses :" + str(ddc),
                             ln=6, align='C')

                    # save the pdf with name .pdf
                    nm = pdf.output("GFG.pdf")
                    print(type(nm))

                    # sss = post1.objects.create(File=nm)

    return render(request, 'kidcertificate.html')


def download(request):
    loggg = request.session['user_id']
    print(loggg, '*****************************************************')
    q = Kids.objects.filter(Id=loggg)
    for i in q:
        n = i.Id
        print(n, "//////////////")
        m = i.RegisterNumber
        if hos_dose.objects.filter(Registernumber=m).exists():
            if n == loggg:
                filename = str('GFG.pdf')
                filepath = "C:/Users/C J/Desktop/vaxin/" + filename
                thefile = filepath
                filename = os.path.basename(thefile)
                chuck_size = 8192
                response = StreamingHttpResponse(FileWrapper(open(thefile, "rb"), chuck_size),
                                                 content_type=mimetypes.guess_type(thefile)[0])
                response['Content-Length'] = os.path.getsize(thefile)
                response['Content-Disposition'] = "Attachment;filename=%s" % filename
                return response


def aknowl(request, id):
    # loggg = request.session['user_id']
    # w = Child1.objects.all()
    # for i in w:
    #     print(i)
    #
    # aknow.objects.create(Id=loggg, )

    return render(request, 'aknowledgement_con.html')


def automsg():
    f = Kids.objects.all()
    now = datetime.now()


    # dd/mm/YY H:M:S
    dt_string = now.strftime("%H:%M:%S")
    while True:
        for i in f:

            if messagesre.objects.filter(Kid_Id=i.Id, value=0, vax_name="Hepatitis").exists():
                print("Your Next Dose is Hepatitis Re-Scheduled ")
                if messagesre.objects.filter(Kid_Id=i.Id, value=0, vax_name="Hepatitis",vaxin_reminder_count=9).exists():
                    a=messagesre.objects.get(Kid_Id=i.Id, value=0, vax_name="Hepatitis")
                    a.delete()
                    print("4 time reminder send so delete the user")
                else:
                    vax = Child.objects.filter(Name='Hepatitis')
                    for s in vax:
                        if s.Number_of_vaccine == 0:
                            pass
                        else:
                            k = messagesre.objects.filter(Kid_Id=i.Id, value=0, vax_name="Hepatitis")
                            for j in k:
                                tim = str(j.first_vax_date)
                                tim = tim.split(":")
                                tt = None
                                if len(str(int(tim[1]) + 1)) == 1:
                                    tt = "0" + str(int(tim[1]) + 2)
                                else:
                                    tt = str(int(tim[1]) + 2)
                                tim = str(tim[0]) + ":" + tt + ":" + str(tim[2])
                                print(str(dt_string), tim,"message time")
                                if str(dt_string) == tim:
                                    print("send secont mail")
                                    subject = 'Reminder message'
                                    massage = 'Your Next Dose is Hepatitis Re-Scheduled ' + str(
                                        'http://127.0.0.1:8000/kids/kidsapprove/') + str(i.Id) + "/" + "Hepatitis"
                                    email_from = settings.EMAIL_HOST_USER
                                    to = [i.Email]
                                    print("Your Next Dose is Hepatitis Re-Scheduled maile send")

                                    xx = send_mail(subject, massage, email_from, to)
                                    messagesre.objects.filter(Kid_Id=i.Id).update(first_vax_date=str(dt_string))
                                    a=messagesre.objects.filter(Kid_Id=i.Id)
                                    for p in a:
                                        messagesre.objects.filter(Kid_Id=i.Id).update(vaxin_reminder_count=str(int(p.vaxin_reminder_count)+1))
            elif messagesre.objects.filter(Kid_Id=i.Id, value=1, vax_name="Hepatitis").exists():
                print("Your Next Dose is bcg Scheduled  ")
                if messagesre.objects.filter(Kid_Id=i.Id, value=1, vax_name="Hepatitis",vaxin_reminder_count=9).exists():
                    a=messagesre.objects.get(Kid_Id=i.Id, value=1, vax_name="Hepatitis")
                    a.delete()
                    print("4 time reminder send so delete the user")
                else:
                    vax = Child.objects.filter(Name='bcg')
                    for s in vax:
                        if s.Number_of_vaccine == 0:
                            pass
                        else:
                            print("3 3condition child ")
                            if hos_dose.objects.filter(Registernumber=i.RegisterNumber, vaccinename="Hepatitis").exists():
                                a = hos_dose.objects.filter(Registernumber=i.RegisterNumber, vaccinename="Hepatitis")
                                for k in a:
                                    tim = str(k.date)
                                    tim = tim.split(":")
                                    tt = None
                                    if len(str(int(tim[1]) + 1)) == 1:
                                        tt = "0" + str(int(tim[1]) + 2)
                                    else:
                                        tt = str(int(tim[1]) + 2)
                                    tim = str(tim[0]) + ":" + tt + ":" + str(tim[2])
                                    print(str(dt_string), tim,"message time")
                                    if str(dt_string) == tim:
                                        subject = 'Reminder message'
                                        massage = 'Your Next Dose is bcg Scheduled ' + str(
                                            'http://127.0.0.1:8000/kids/kidsapprove/') + str(i.Id) + "/" + "bcg"
                                        email_from = settings.EMAIL_HOST_USER
                                        to = [i.Email]
                                        print("success")
                                        xx = send_mail(subject, massage, email_from, to)
                                        hos_dose.objects.filter(Registernumber=i.RegisterNumber,
                                                                vaccinename="Hepatitis").update(date=str(dt_string))
                                        a = messagesre.objects.filter(Kid_Id=i.Id)
                                        for p in a:
                                            messagesre.objects.filter(Kid_Id=i.Id).update(
                                                vaxin_reminder_count=str(int(p.vaxin_reminder_count) + 1))


            elif messagesre.objects.filter(Kid_Id=i.Id, value=2, vax_name="bcg").exists():
                print("Your Next Dose is ipv Scheduled ")
                if messagesre.objects.filter(Kid_Id=i.Id, value=2, vax_name="bcg",vaxin_reminder_count=9).exists():
                    a=messagesre.objects.get(Kid_Id=i.Id, value=2, vax_name="bcg")
                    a.delete()
                    print("4 time reminder send so delete the user")
                else:
                    vax = Child.objects.filter(Name='ipv')
                    for s in vax:
                        if s.Number_of_vaccine == 0:
                            pass
                        else:
                            if hos_dose.objects.filter(Registernumber=i.RegisterNumber, vaccinename="bcg").exists():
                                print("4 exist")
                                a = hos_dose.objects.filter(Registernumber=i.RegisterNumber, vaccinename="bcg")
                                for k in a:
                                    tim = str(k.date)
                                    tim = tim.split(":")
                                    tt = None
                                    if len(str(int(tim[1]) + 1)) == 1:
                                        tt = "0" + str(int(tim[1]) + 2)
                                    else:
                                        tt = str(int(tim[1]) + 2)
                                    tim = str(tim[0]) + ":" + tt + ":" + str(tim[2])
                                    print(str(dt_string), tim,"message time")
                                    if str(dt_string) == tim:
                                        subject = 'Reminder message'
                                        massage = 'Your Next Dose is ipv Scheduled ' + str(
                                            'http://127.0.0.1:8000/kids/kidsapprove/') + str(i.Id) + "/" + "ipv"
                                        email_from = settings.EMAIL_HOST_USER
                                        to = [i.Email]
                                        print("success")

                                        xx = send_mail(subject, massage, email_from, to)
                                        hos_dose.objects.filter(Registernumber=i.RegisterNumber,
                                                                vaccinename="bcg").update(date=str(dt_string))
                                        a = messagesre.objects.filter(Kid_Id=i.Id)
                                        for p in a:
                                            messagesre.objects.filter(Kid_Id=i.Id).update(
                                                vaxin_reminder_count=str(int(p.vaxin_reminder_count) + 1))

            elif messagesre.objects.filter(Kid_Id=i.Id, value=3, vax_name="ipv").exists():
                print("your ............... vaccine is complited ")
                pass

            else:
                print("Your Next Dose is Hepatitis Scheduled")
                vax = Child.objects.filter(Name='Hepatitis')
                for s in vax:
                    if s.Number_of_vaccine == 0:
                        pass
                    else:
                        if messagesre.objects.filter(Kid_Id=i.Id).exists():
                            messagesre.objects.filter(Kid_Id=i.Id).update(value=0, vax_name="Hepatitis",
                                                                          first_vax_date=str(dt_string),vaxin_reminder_count=1)
                        else:
                            messagesre.objects.create(Kid_Id=i.Id, value=0, vax_name="Hepatitis",
                                                      first_vax_date=str(dt_string),vaxin_reminder_count=1)

                        subject = 'Reminder message'
                        massage = 'Your Next Dose is Hepatitis Scheduled ' + str(
                            'http://127.0.0.1:8000/kids/kidsapprove/') + str(i.Id) + "/" + "Hepatitis"
                        email_from = settings.EMAIL_HOST_USER
                        to = [i.Email]
                        print("Your Next Dose is Hepatitis Scheduled mail send")

                        xx = send_mail(subject, massage, email_from, to)

        break


#
# from vaxin.nee_time import BackgroundTasks


# automsg()
def approve_kid(request, id, vax_name):
    subject = 'Reminder message'
    massage = 'Reminder viewed by user ' + str(id)
    email_from = settings.EMAIL_HOST_USER
    to = ['jeemonsjsj@gmail.com']
    send_mail(subject, massage, email_from, to)
    print("2222222222222222222222222222222222222222222222222")

    if vax_name == "Hepatitis":
        if messagesre.objects.filter(Kid_Id=id).exists():
            messagesre.objects.filter(Kid_Id=id).update(value=1, vax_name=vax_name,vaxin_reminder_count=1)
        else:
            messagesre.objects.create(Kid_Id=id, value=1, vax_name=vax_name,vaxin_reminder_count=1)
    elif vax_name == "bcg":
        if messagesre.objects.filter(Kid_Id=id).exists():
            messagesre.objects.filter(Kid_Id=id).update(value=2, vax_name=vax_name,vaxin_reminder_count=1)
        else:
            messagesre.objects.create(Kid_Id=id, value=2, vax_name=vax_name,vaxin_reminder_count=1)
    elif vax_name == "ipv":
        if messagesre.objects.filter(Kid_Id=id).exists():
            messagesre.objects.filter(Kid_Id=id).update(value=3, vax_name=vax_name,vaxin_reminder_count=1)
        else:
            messagesre.objects.create(Kid_Id=id, value=3, vax_name=vax_name,vaxin_reminder_count=1)

    return render(request, 'aknowledgement_con.html')
