from django.db import models

# Create your models here.

class login(models.Model):
    login_id=models.AutoField(primary_key=True) #incrementing values
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    user_type=models.CharField(max_length=100)

class user(models.Model):
    user_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    post=models.CharField(max_length=100)
    pin=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    phone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)

class charging_center(models.Model):
    center_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    center_name=models.CharField(max_length=100)
    center_phone=models.CharField(max_length=100)
    center_email=models.CharField(max_length=100)
    lati=models.CharField(max_length=100)
    longi=models.CharField(max_length=100)
    center_place=models.CharField(max_length=100)

class booking(models.Model):
    booking_id=models.AutoField(primary_key=True)
    center=models.ForeignKey(charging_center,on_delete=models.CASCADE)
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    date=models.CharField(max_length=100)
    time=models.CharField(max_length=100)
    status=models.CharField(max_length=100)



class feedback(models.Model):
    feedback_id=models.AutoField(primary_key=True)
    login=models.ForeignKey(login,on_delete=models.CASCADE)
    feedback=models.CharField(max_length=100)
    feedback_date=models.CharField(max_length=100)


class complaint(models.Model):
    complaint_id=models.AutoField(primary_key=True)
    complaint=models.CharField(max_length=100)
    reply=models.CharField(max_length=100)
    complaint_date=models.CharField(max_length=100)
    login=models.ForeignKey(login,on_delete=models.CASCADE)