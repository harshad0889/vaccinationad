from hospital import views
from django.urls import path, include

urlpatterns = [
    path('view/', views.view1, name='view'),
    path('regi/', views.regi, name="regi"),
    # path('regis/', views.regno, name="regis"),

    path('login/', views.log, name='login'),
    path('admin_log/', views.Admin_log, name='Admin_login'),
    path('cat1/', views.cat1, name='cat1'),
    path('cat2/', views.cat2, name='cat2'),
    path('cat3/', views.cat3, name='cat3'),
    path('admin_view/', views.admin_view, name='admin_view'),
    path('delete/<product_Id>/', views.delete, name='delete'),
    path('edit/', views.edi, name='edit'),
    path('adult_edi/', views.adult_edi, name='adult_edi'),
    path('vieww/', views.viee, name='vieww'),
    path('editview/<id>/<d>/', views.editvie, name='editview'),
    path('vax_hos_approval_btn/', views.btn, name='vax_hos_approval_btn'),
    path('schedule/', views.shed, name='schedule'),
    path('stockupdate/', views.stock, name='stockupdate'),
    path('newupdate/<product_Id>/', views.stockupdate, name='newupdate'),

]
