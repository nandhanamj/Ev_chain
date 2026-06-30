from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from EV_chain_app.models import *

# Create your views here.
# def home(req):
#       return HttpResponse("Hello")  #visualize



def home(request):
    return render(request,'home.html')

def Login(request):

    if 'submit' in request.POST:
        username=request.POST['username']
        password=request.POST['password']
        a=login.objects.get(username=username,password=password)
        request.session['login_id']=a.pk

        
        if a.user_type=='admin':
            return HttpResponse("<script>alert('login successfull');window.location='/adminhome'</script>")
        elif a.user_type=='user':
                    c=user.objects.get(login_id=request.session['login_id'])
                    request.session['user']=c.pk
                    return HttpResponse("<script>alert('login successfull');window.location='/userhome'</script>")
        elif a.user_type=='charging_center':
                    d=charging_center.objects.get(login_id=request.session['login_id'])
                    request.session['center']=d.pk
                    return HttpResponse("<script>alert('login successfull');window.location='/centerhome'</script>")
    return render(request,'login.html')

def user_reg(request):

    if 'submit' in request.POST:
        fname=request.POST['first_name']
        lname=request.POST['last_name']
        place=request.POST['place']
        post=request.POST['post']
        pin=request.POST['pin']
        gender=request.POST['gender']
        phno=request.POST['phone']
        email=request.POST['email']
        uname=request.POST['username']
        password=request.POST['password']

        print

        a=login(username=uname,password=password,user_type='user')
        a.save()

        b=user(fname=fname,lname=lname,place=place,post=post,pin=pin,gender=gender,phone=phno,email=email,login_id=a.pk)
        b.save()

    return render(request,'user_reg.html')

def charge_center(request):
    if 'submit' in request.POST:
        cname=request.POST['center_name']
        cplace=request.POST['center_place']
        lati=request.POST['center_latitude']
        longi=request.POST['center_longitude']
        c_phno=request.POST['center_phone']
        c_email=request.POST['center_email']
        username=request.POST['center_username']
        password=request.POST['center_password']
        d=login(username=username,password=password,user_type='pending')
        d.save()
        c=charging_center(center_name=cname,center_phone=c_phno,center_email=c_email,lati=lati,longi=longi,center_place=cplace,login_id=d.pk)
        c.save()
    return render(request,'charging_center.html')


#admin module
def adminhome(request):
    return render(request,'admin_home.html')
def adminview_charge(request):
    a=charging_center.objects.all()

    return render(request,'admin_view_chargeCenter.html',{'a':a})
def adminViewcomplaint(request):
    b=complaint.objects.all()

    return render(request,'admin_complaint_view.html',{'b':b})
def adminViewfeedback(request):
    c=feedback.objects.all()
    return render(request,'admin_view_feedback.html',{'c':c})
def adminViewusers(request):
    d=user.objects.all()
    return render(request,'admin_view_users.html',{'d':d})
def block(request,id):
    a=login.objects.get(login_id=id)
    a.user_type='Blocked'
    a.save()
    return HttpResponse("<script>alert('Blocked successfully');window.location='/adminhome'</script>")

def unblock(request,id):
    a=login.objects.get(login_id=id)
    a.user_type='charging_center'
    a.save()
    return HttpResponse("<script>alert('Center request accepted successfully');window.location='/adminhome'</script>")

def sendreply(request,id):
    x=complaint.objects.get(complaint_id=id)
    if 'submit' in request.POST:
        reply=request.POST['reply']

        x.reply=reply
        x.save()
        return HttpResponse("<script>alert('Send reply successfully');window.location='/adminViewcomplaint'</script>")
    return render(request,'sendrep.html')

#user module
def userhome(request):
    return render(request,'user_home.html')
def viewcharging(request):
    a=charging_center.objects.all()
    return render(request,'view_charging_center.html',{'a':a})
def bookingstatus(request):
    a=booking.objects.all()
    return render(request,'view_booking_status.html',{'a':a})


def book_now(request,id):
    if 'submit' in request.POST:

        dates=request.POST['date']
        times=request.POST['time']
        b=booking(date=dates,time=times,status='pending',user_id=request.session['user'],center_id=id)
        b.save()
    return render(request,'book_now.html')


def sendcomplaint(request):
    if 'submit' in request.POST:
        complaints=request.POST['complaint']
        c=complaint(complaint=complaints,reply='pending',complaint_date=datetime.now(),login_id=request.session['user'])
        c.save()
    a=complaint.objects.filter(login_id=request.session['user'])
    return render(request,'sendComplaint_reply.html',{'a':a})
def sendfeedback(request):
    if 'submit' in request.POST:
        feedbacks=request.POST['feedback']
        c=feedback(feedback=feedbacks,feedback_date=datetime.now(),login_id=request.session['user'])
        c.save()
    return render(request,'send_feedback.html')


#center module
def centerhome(request):
    return render(request,'charging_home.html')
def centercomplaint(request):
    if 'submit' in request.POST:
        complaints=request.POST['complaint']
        c=complaint(complaint=complaints,reply='pending',complaint_date=datetime.now(),login_id=request.session['center'])
        c.save()
    a=complaint.objects.filter(login_id=request.session['center'])
    return render(request,'centercomplaints.html',{'a':a})
def centerfeedback(request):
    if 'submit' in request.POST:
        feedbacks=request.POST['feedback']
        c=feedback(feedback=feedbacks,feedback_date=datetime.now(),login_id=request.session['center'])
        c.save()
    return render(request,'centerfeedback.html')
def viewusers(request):
    d=user.objects.all()
    return render(request,'view_users.html',{'d':d})
def viewbookings(request):
    a=booking.objects.filter(center_id=request.session['center'])
    return render(request,'viewbookings.html',{'a':a})
def accept(request,id):
    a=booking.objects.get(booking_id=id)
    a.status='Accepted'
    a.save()
    return HttpResponse("<script>alert('Accepted successfully');window.location='/centerhome'</script>")
def reject(request,id):
    a=booking.objects.get(booking_id=id)
    a.status='Rejected'
    a.save()
    return HttpResponse("<script>alert('Rejected successfully');window.location='/centerhome'</script>")