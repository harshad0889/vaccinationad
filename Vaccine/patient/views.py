import os
import random
import string
from django.contrib import messages
from django.core.mail import send_mail
import mimetypes
from wsgiref.util import FileWrapper
from django.http import StreamingHttpResponse

from django.shortcuts import render, redirect

# Create your views here.
from hospital.models import Hospital, Single, Multi, Child, Single1, Multi1, Injection, hospital_record, colera_record, \
    hos_dose, questiana_record, questianb_record
from patient.models import register, mydata
from vaxin import settings
from fpdf import FPDF


def home(request):
    print("hiiio")
    return render(request, 'index.html')


def log(request):
    if request.method == "POST":
        f = request.POST.get("username")
        p = request.POST.get("password")
        if register.objects.filter(RegisterNumber=f, Password=p).exists():
            h = register.objects.filter(RegisterNumber=f, Password=p)
            for i in h:
                request.session['user_id'] = i.Id
            print("hiiiiiiii")
            return redirect('base')


        else:
            messages.info(request, 'User Is Not Exists')
            return redirect('userlogin')

    return render(request, "userlogin.html", )
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
        i = request.POST.get('addh')

        rn = (random.randint(1000, 10000))
        let = string.ascii_uppercase
        ltc = (''.join(random.choice(let) for i in range(3)))
        rne = str(ltc) + str(rn)

        register.objects.create(RegisterNumber=rne, Password=b, Name=c, Email=d, Address=e, Age=f, Dob=g, Phone=h,
                                Aadhar=i)
        messages.success(request,
                         "This is your Register Number : " + rne)

        return redirect('userlogin')

    return render(request, 'userreg.html')


def Base(request):
    b = Multi.objects.all()
    print(b)
    # s = b[0], b[1]
    # print(s)
    # for i in b:

    return render(request, 'Base.html', {'rrd': b})


def addh(request):
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
                massage = 'http://127.0.0.1:8000/hospital/editview/' + str(loggg) + "/" + str(1) + "/"
                email_from = settings.EMAIL_HOST_USER
                to = [i.Email]
                send_mail(subject, massage, email_from, to)

            # return redirect('views')

    return render(request, 'submit.html')


def booo(request):
    bb = Multi.objects.all()
    loggg = request.session.get('user_id')
    v = Injection.objects.filter(Id=loggg)

    l = None
    for i in v:
        l = i.Vaccine_Dose
        print(l)
    # b = {'dose': range(l)}

    return render(request, 'patbook.html', {'prd': bb})


# def bookings(request):
#     if request.method == "POST":
#         s = request.POST.get('vaccs')
#         t = request.POST.get('datees')
#         q = request.POST.get('name')
#         p = request.POST.get('typee')
#         r = request.POST.get('ti')
#
#         v = "Single Dose"
#
#         print(type(t))
#
#         loggg = request.session['user_id']
#         print(loggg, "ppppppppppppp")
#
#         date_format = "%Y-%m-%d"
#         # c = datetime.strptime(t, date_format)
#         # l = Child.objects.get(Id=product_Id)
#         if p == v:
#             pr = Single1.objects.create(Dosage=s, Date=t, Name=q, Patient_Id=loggg, vacc_type=p, Time=r)
#
#     # y = users.objects.get(Id=pr.Id)
#     return render(request, 'patbook.html')


def bttn(request):
    print("rrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    if request.method == "POST":
        s = request.POST.get('do')
        request.session['dosee'] = s
        print(s, "gggggggggggggggggggggggggggggg")

        t = request.POST.get('da')
        request.session['date'] = t

        q = request.POST.get('namee')
        request.session['name'] = q

        l = request.POST.get('typeee')
        request.session['type'] = l
        loggg = request.session['user_id']

        r = request.POST.get('ti')
        request.session['time'] = r

        v = "General Vaccine"
        request.session['tyty'] = v

        if q == 'Tetanus':
            return redirect("tetquest")
        if q == "Chicken pox":
            return redirect("loada")
        if q == "Typhoid":
            return redirect("loadb")

        else:
            return redirect("loadcol")

    return render(request, "patbook.html")


def patcertificate(request):
    global aaa, ddg
    loggg = request.session['user_id']
    print(loggg, '*****************************************************')
    a = register.objects.filter(Id=loggg)
    for i in a:
        b = hos_dose.objects.filter(Registernumber=i.RegisterNumber)
        if hos_dose.objects.filter(Registernumber=i.RegisterNumber).exists():
            for k in b:
                # variable pdf
                pdf = FPDF()

                # Add a page
                pdf.add_page()

                # set style and size of font
                # that you want in the pdf
                pdf.set_font("Arial", size=15)

                pdf.cell(200, 10, txt="Provisional Certificate for Vaccination",
                         ln=1, align='C')
                pdf.cell(200, 10, txt="Register Number :" + str(i.RegisterNumber),
                         ln=2, align='C')
                pdf.cell(200, 10, txt="No Of Doses :" + str(k.vaccine_dose),
                         ln=3, align='C')

                pdf.cell(200, 10, txt="Aadhar Number :" + i.Aadhar,
                         ln=4, align='C')

                pdf.cell(200, 10, txt="Patient Id :" + str(loggg),
                         ln=5, align='C')
                pdf.cell(200, 10, txt="Name :" + k.vaccinename,
                         ln=6, align='C')

                # add another cell
                pdf.cell(200, 10, txt="Date :" + k.date,
                         ln=7, align='C')

                # save the pdf with name .pdf
                pdf.output("GFG.pdf")
        else:
            messages.success(request, "User Is Not Vaccinated ")

    # q = Multi1.objects.filter(Patient_Id=loggg)
    # print(q)
    # m = None
    # a = register.objects.filter(Id=loggg)
    # for k in a:
    #     m = k.RegisterNumber
    # for i in q:
    #     n = i.Patient_Id
    #     print(n, "//////////////")
    #     if Multi1.objects.filter(Patient_Id=n).exists():
    #         if n == loggg:
    #
    #             if request.method == "POST":
    #                 s = request.POST.get('typs')
    #                 v = "General Vaccine"
    #                 if s == v:
    #
    #                     # Python program to create
    #                     # a pdf file
    #
    #                     # save FPDF() class into a
    #                     # variable pdf
    #                     pdf = FPDF()
    #
    #                     # Add a page
    #                     pdf.add_page()
    #
    #                     # set style and size of font
    #                     # that you want in the pdf
    #                     pdf.set_font("Arial", size=15)
    #                     loggg = request.session['user_id']
    #                     print(type(loggg), "=============================================")
    #
    #                     ff = Multi1.objects.filter(Patient_Id=str(loggg),adult_child=1)
    #                     print(ff, 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeee')
    #                     x = Injection.objects.filter(Patient_Id=str(loggg))
    #                     xx = register.objects.filter(Id=str(loggg))
    #                     for i in xx:
    #                         aaa = i.Aadhar
    #                         ddg = i.RegisterNumber
    #                         print(ddg, "----------------------")
    #
    #
    #                     for i in x:
    #
    #                         ddc = i.Vaccine_Dose
    #                         print(ddc)
    #                         pdf.cell(200, 10, txt="Provisional Certificate for Vaccination",
    #                                  ln=1, align='C')
    #                         pdf.cell(200, 10, txt="Register Number :" + str(ddg),
    #                                  ln=2, align='C')
    #                         pdf.cell(200, 10, txt="No Of Doses :" + str(ddc),
    #                                  ln=3, align='C')
    #                     for i in ff:
    #                         ffg = i.Name
    #                         print(ffg, "===============")
    #                         ddj = i.Date
    #                         ddl = i.Time
    #                         ddd = i.vacc_type
    #                         ddf = i.Patient_Id
    #                         # create a cell
    #                         pdf.cell(200, 10, txt="Aadhar Number :" + aaa,
    #                                  ln=4, align='C')
    #                         print(aaa, "0000000000000000000000000000000")
    #
    #                         pdf.cell(200, 10, txt="Patient Id :" + ddf,
    #                                  ln=5, align='C')
    #                         print(ffg, "===============")
    #                         pdf.cell(200, 10, txt="Name :" + ffg,
    #                                  ln=6, align='C')
    #
    #                         # add another cell
    #                         pdf.cell(200, 10, txt="Date :" + ddj,
    #                                  ln=7, align='C')
    #                         pdf.cell(200, 10, txt="Time :" + ddl,
    #                                  ln=8, align='C')
    #
    #                         pdf.cell(200, 10, txt="Vaccination Type :" + ddd,
    #                                  ln=9, align='C')
    #                         # save the pdf with name .pdf
    #                         pdf.output("GFG.pdf")
    #         else:
    #             messages.success(request, "User Is Not Vaccinated ")
    return render(request, 'patcertificate.html')


def downloads(request):
    loggg = request.session['user_id']

    print(loggg, '*****************************************************aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    q = Multi1.objects.filter(Patient_Id=loggg)
    m = None
    a = register.objects.filter(Id=loggg)
    for k in a:
        m = k.RegisterNumber
    for i in q:
        n = i.Patient_Id
        print(n, "//////////////")

        print(m, "//////////////")

        if hos_dose.objects.filter(Registernumber=m).exists():
            a = hos_dose.objects.filter(Registernumber=m)
            print("111111111111111111")
            for k in a:

                b = Multi1.objects.filter(Patient_Id=i.Patient_Id)
                for s in b:
                    if k.vaccinename == s.Name:
                        print("222222222222222222")
                        print(k.vaccine_dose, s.Dosage)
                        if int(k.vaccine_dose) == int(s.Dosage):
                            print("3333333333333333333333333", n, loggg)
                            if int(n) == int(loggg):
                                print("44444444444444444")
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
                        else:
                            print("hiiiiiiiiiiiiiiiiii")
                            return redirect("patcertificate")
                    else:
                        print("hiiiiiiiiiiiiiiiiii")
                        return redirect("patcertificate")
        else:
            print("hiiiiiiiiiiiiiiiiii")
            return redirect("patcertificate")

    return redirect("patcertificate")


def load_tet(request):
    return render(request, "qform.html")


def lad_col(request):
    return render(request, "coleraqestion.html")


def qanda(request):
    print("=============================================")
    if request.method == "POST":
        r = request.POST.get('pin')
        d = request.POST.get('cln')
        c = request.POST.get('tet')
        e = request.POST.get('dir')
        f = request.POST.get('rea')
        g = request.POST.get('allur')
        loggg = request.session['user_id']

        hospital_record.objects.create(Object=r, Cleaned_obj_not=d, Tetenus=c, Caused_obj_Clean_not=e, Reaction=f,
                                       Alurgies=g, Patient_Id=loggg)
        loggg = request.session['user_id']
        dos = request.session.get('dosee')
        print(dos)
        dat = request.session['date']
        nam = request.session['name']
        print(nam, "session   ==========")
        typ = request.session['type']
        tim = request.session['time']
        gv = request.session['tyty']
        if typ == gv:
            print("---------------")
            a = Multi.objects.filter(Name=nam)
            print("---------------2222")

            print(a)
            b = 1
            for i in a:
                if b == 1:
                    if int(i.Number_of_vaccine) == 0:
                        messages.success(request,
                                         "Vaccine out of Stock : ")

                    else:
                        if Multi1.objects.filter(Patient_Id=loggg).exists():
                            pc = Multi1.objects.filter(Patient_Id=loggg).update(Dosage=dos, Date=dat, Name=nam,
                                                                                Patient_Id=loggg, vacc_type=typ,
                                                                                Time=tim)
                        else:
                            Multi1.objects.create(Dosage=dos, Date=dat, Name=nam, Patient_Id=loggg, vacc_type=typ,
                                                  Time=tim)
                        kj = register.objects.filter(Id=loggg)

                        a = Multi.objects.filter(Name=nam)
                        for i in a:
                            dose = int(i.Number_of_vaccine) - 1
                            Multi.objects.filter(Name=nam).update(Number_of_vaccine=str(dose))

                        for i in kj:
                            subject = 'confirmation message'
                            massage = 'Your Booking Was Confirmed'
                            email_from = settings.EMAIL_HOST_USER
                            to = [i.Email]
                            send_mail(subject, massage, email_from, to)
                b = b + 1
    return redirect("tetquest")


def colara(request):
    print("===================================================fffffffffffffffffff")
    if request.method == "POST":
        r = request.POST.get('q1')
        d = request.POST.get('q2')
        c = request.POST.get('q3')
        # e = request.POST.get('dir')
        # f = request.POST.get('rea')
        # g = request.POST.get('allur')
        loggg = request.session['user_id']

        colera_record.objects.create(Object=r, Cleaned_obj_not=d, Tetenus=c, Patient_Id=loggg)
    loggg = request.session['user_id']
    dos = request.session.get('dosee')
    print(dos)
    dat = request.session['date']
    nam = request.session['name']
    print(nam)
    typ = request.session['type']
    tim = request.session['time']
    gv = request.session['tyty']
    if typ == gv:
        print(nam)
        a = Multi.objects.filter(Name=nam)
        for i in a:
            if int(i.Number_of_vaccine) == 0:
                messages.success(request,
                                 "Vaccine out of Stock : ")

            else:
                if Multi1.objects.filter(Patient_Id=loggg).exists():
                    pc = Multi1.objects.filter(Patient_Id=loggg).update(Dosage=dos, Date=dat, Name=nam,
                                                                        Patient_Id=loggg, vacc_type=typ, Time=tim)
                else:
                    Multi1.objects.create(Dosage=dos, Date=dat, Name=nam, Patient_Id=loggg, vacc_type=typ,
                                          Time=tim)
                kj = register.objects.filter(Id=loggg)

                a = Multi.objects.filter(Name=nam)
                for i in a:
                    dose = int(i.Number_of_vaccine) - 1
                    Multi.objects.filter(Name=nam).update(Number_of_vaccine=str(dose))

                for i in kj:
                    subject = 'confirmation message'
                    massage = 'Your Booking Was Confirmed'
                    email_from = settings.EMAIL_HOST_USER
                    to = [i.Email]
                    send_mail(subject, massage, email_from, to)
    return redirect("loadcol")


def load_a(request):
    return render(request, "q1form.html")


def lad_b(request):
    return render(request, "q2form.html")


def questiana(request):
    print("===================================================fffffffffffffffffff")
    if request.method == "POST":
        r = request.POST.get('q11')
        d = request.POST.get('q12')
        c = request.POST.get('q13')
        e = request.POST.get('q14')
        f = request.POST.get('q15')
        g = request.POST.get('q16')
        j = request.POST.get('q17')
        l = request.POST.get('q18')
        w = request.POST.get('q19')
        loggg = request.session['user_id']

        questiana_record.objects.create(q1=r, q2=d, q3=c, q4=e, q5=f, q6=g, q7=j, q8=l, q9=w, Patient_Id=loggg)
        loggg = request.session['user_id']
        dos = request.session.get('dosee')
        print(dos)
        dat = request.session['date']
        nam = request.session['name']
        print(nam)
        typ = request.session['type']
        tim = request.session['time']
        gv = request.session['tyty']
        if typ == gv:
            print(nam)
            a = Multi.objects.filter(Name=nam)
            print("??????????????????????", a)
            for i in a:
                if int(i.Number_of_vaccine) == 0:
                    messages.success(request,
                                     "Vaccine out of Stock : ")

                else:
                    if Multi1.objects.filter(Patient_Id=loggg).exists():
                        pc = Multi1.objects.filter(Patient_Id=loggg).update(Dosage=dos, Date=dat, Name=nam,
                                                                            Patient_Id=loggg, vacc_type=typ, Time=tim)
                    else:
                        Multi1.objects.create(Dosage=dos, Date=dat, Name=nam, Patient_Id=loggg, vacc_type=typ,
                                              Time=tim)
                    kj = register.objects.filter(Id=loggg)

                    a = Multi.objects.filter(Name=nam)
                    for i in a:
                        dose = int(i.Number_of_vaccine) - 1
                        Multi.objects.filter(Name=nam).update(Number_of_vaccine=str(dose))

                    for i in kj:
                        subject = 'confirmation message'
                        massage = 'Your Booking Was Confirmed'
                        email_from = settings.EMAIL_HOST_USER
                        to = [i.Email]
                        send_mail(subject, massage, email_from, to)
                        print("Successfull")
    return redirect("loada")


def questianb(request):
    print("===================================================fffffffffffffffffff")
    if request.method == "POST":
        r = request.POST.get('q1')
        d = request.POST.get('q2')
        c = request.POST.get('q3')
        e = request.POST.get('q4')
        f = request.POST.get('q5')
        g = request.POST.get('q6')
        loggg = request.session['user_id']

        questianb_record.objects.create(q1=r, q2=d, q3=c, q4=e, q5=f, q6=g, Patient_Id=loggg)
        loggg = request.session['user_id']
        dos = request.session.get('dosee')
        print(dos)
        dat = request.session['date']
        nam = request.session['name']
        print(nam)
        typ = request.session['type']
        tim = request.session['time']
        gv = request.session['tyty']
        if typ == gv:
            print(nam)
            a = Multi.objects.filter(Name=nam)
            for i in a:
                if int(i.Number_of_vaccine) == 0:
                    messages.success(request,
                                     "Vaccine out of Stock : ")

                else:
                    if Multi1.objects.filter(Patient_Id=loggg).exists():
                        pc = Multi1.objects.filter(Patient_Id=loggg).update(Dosage=dos, Date=dat, Name=nam,
                                                                            Patient_Id=loggg, vacc_type=typ, Time=tim)
                    else:
                        Multi1.objects.create(Dosage=dos, Date=dat, Name=nam, Patient_Id=loggg, vacc_type=typ,
                                              Time=tim)
                    kj = register.objects.filter(Id=loggg)

                    a = Multi.objects.filter(Name=nam)
                    for i in a:
                        dose = int(i.Number_of_vaccine) - 1
                        Multi.objects.filter(Name=nam).update(Number_of_vaccine=str(dose))

                    for i in kj:
                        subject = 'confirmation message'
                        massage = 'Your Booking Was Confirmed'
                        email_from = settings.EMAIL_HOST_USER
                        to = [i.Email]
                        send_mail(subject, massage, email_from, to)
    return redirect("loadb")
