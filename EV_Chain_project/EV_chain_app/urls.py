from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name="home"),   #fn home in views
    path('login',views.Login,name="login"),
    path('user_reg',views.user_reg,name="user_reg"),
    path('charge_center',views.charge_center,name="charge_center"),
    #admin module
    path('adminhome',views.adminhome,name="adminhome"),
    path('adminview_charge',views.adminview_charge,name="adminview_charge"),
    path('adminViewcomplaint',views.adminViewcomplaint,name="adminViewcomplaint"),
    path('adminViewfeedback',views.adminViewfeedback,name="adminViewfeedback"),
    path('adminViewusers',views.adminViewusers,name="adminViewusers"),
    path('block/<id>',views.block,name="block"),
    path('unblock/<id>',views.unblock,name="unblock"),
    path('sendreply/<id>',views.sendreply,name="sendreply"),

    #user module
    path('userhome',views.userhome,name="userhome"),
    path('viewcharging',views.viewcharging,name="viewcharging"),
    path('bookingstatus',views.bookingstatus,name="bookingstatus"),
    path('sendcomplaint',views.sendcomplaint,name="sendcomplaint"),
    path('sendfeedback',views.sendfeedback,name="sendfeedback"),
    path('book_now/<id>',views.book_now,name="book_now"),



    #center module
    path('centerhome',views.centerhome,name="centerhome"),
    path('viewusers',views.viewusers,name="viewusers"),
    path('centerfeedback',views.centerfeedback,name="centerfeedback"),
    path('centercomplaint',views.centercomplaint,name="centercomplaint"),
    path('viewbookings',views.viewbookings,name="viewbookings"),
    path('accept/<id>',views.accept,name="accept"),
    path('reject/<id>',views.reject,name="reject")
]