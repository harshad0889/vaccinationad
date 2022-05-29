from . import views
from django.urls import path

urlpatterns = [

    path('kidslogin/', views.login, name='kidslogin'),

    path('kidsreg/', views.regi, name='kidsreg'),

    path('kidsbase/', views.Base, name='kidsbase'),

    path('kidrequest/', views.addhss, name='kidrequest'),

    path('kidbook/', views.bookin, name='kidbook'),
    path('kidcertificate/', views.boooooo, name='kidcertificate'),
    path('download/', views.download, name='download'),
    path('loadbook/', views.load_book, name='loadbook'),
    path('acknowledgement/<id>/', views.aknowl, name='acknowledgement'),
    path('kidsapprove/<id>/<vax_name>/',views.approve_kid,name='kidsapprove'),

]
