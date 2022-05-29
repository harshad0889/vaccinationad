from django.db import models


# Create your models here.
class Kids(models.Model):
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


class aknow(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250, null=True)
    view = models.CharField(max_length=250, null=True)


class messagesre(models.Model):
    Id = models.AutoField(primary_key=True)
    Kid_Id = models.IntegerField(null=True)
    vax_name=models.CharField(null=True,max_length=250)
    value = models.CharField(max_length=250, null=True)
    first_vax_date=models.CharField(null=True,max_length=250)
    vaxin_reminder_count=models.CharField(null=True,max_length=250)
