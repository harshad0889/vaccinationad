from patient import views
from django.urls import path, include

urlpatterns = [
    path('', views.home, name='home'),
    path('patient/reg/', views.regi, name='userreg'),

    path('patient/login/', views.log, name='userlogin'),
    path('login/', views.log, name='login'),

    path('reg/', views.regi, name='reg'),

    path('base/', views.Base, name='base'),
    path('request/', views.addh, name='request'),
    path('book/', views.booo, name='book'),

    # path('singlebookings/', views.bookings, name='singlebookings'),
    path('multibookings/', views.bttn, name='multibookings'),
    path('patcertificate/', views.patcertificate, name='patcertificate'),
    path('patientdownload/', views.downloads, name='patientdownload'),
    path('questionanswer/', views.qanda, name='questionanswer'),
    path('tetquest/', views.load_tet, name='tetquest'),
    path('coleraquestion/', views.colara, name='coleraquestion'),
    path('loadcol/', views.lad_col, name='loadcol'),
    path('aquestion/', views.questiana, name='aquestion'),
    path('bquestion/', views.questianb, name='bquestion'),
    path('loada/', views.load_a, name='loada'),
    path('loadb/', views.lad_b, name='loadb'),

]
