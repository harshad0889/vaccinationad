from django.db import models


# Create your models here.
class register(models.Model):
    Id = models.AutoField(primary_key=True)
    RegisterNumber = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=50)
    Name = models.CharField(max_length=250, null=True)
    Email = models.EmailField(null=True)
    Address = models.CharField(max_length=250)
    Age = models.CharField(max_length=250, null=True)
    Dob = models.CharField(max_length=250, null=True)
    Phone = models.CharField(max_length=250, null=True)
    Aadhar = models.CharField(max_length=250, null=True)


    def __str__(self):
        return self.Name


class mydata(models.Model):
    Id = models.AutoField(primary_key=True)
    User_Id = models.IntegerField(null=True)
    File = models.FileField(null=True)
    Vaccinated = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.Vaccinated


class post1(models.Model):
    Id = models.AutoField(primary_key=True)
    File = models.FileField(null=True)

    def __str__(self):
        return self.Id


from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField()
