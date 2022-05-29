from django.db import models
from datetime import date, time


# Create your models here.

class Hospital(models.Model):
    Id = models.AutoField(primary_key=True)
    RegisterNumber = models.CharField(max_length=50, unique=True)
    Password = models.CharField(max_length=50)
    Name = models.CharField(max_length=250, null=True)
    Email = models.EmailField(null=True)
    Address = models.CharField(max_length=250)

    def __str__(self):
        return self.Name


class Single(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250, null=True)
    VaccineNumber = models.CharField(max_length=50)
    Details = models.CharField(max_length=250)
    Duration = models.CharField(max_length=250)
    Number_of_vaccine = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.Name


class Multi(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250, null=True)
    VaccineNumber = models.CharField(max_length=50)
    Details = models.CharField(max_length=250)
    Duration = models.CharField(max_length=250)
    Number_of_vaccine = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.Name


class Child(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250, null=True)
    VaccineNumber = models.CharField(max_length=50, null=True)
    Details = models.CharField(max_length=250, null=True)
    Duration = models.CharField(max_length=250, null=True)
    Number_of_vaccine = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.Name


class Injection(models.Model):
    Id = models.AutoField(primary_key=True)
    Patient_Id = models.IntegerField()
    Kid_Id = models.IntegerField(null=True)

    Child_or_adult = models.IntegerField()
    Vaccine_Dose = models.IntegerField()
    Name = models.CharField(max_length=50, null=True)
    RegisterNumber = models.CharField(max_length=50, unique=True)
    Date = models.CharField(max_length=50, null=True)
    Time = models.CharField(max_length=50, null=True)
    NextDate = models.CharField(max_length=50, null=True)
    NextTime = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.Name


class Single1(models.Model):
    objects = None
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, null=True)
    Date = models.CharField(max_length=250)
    Dosage = models.IntegerField()
    Patient_Id = models.CharField(max_length=50, null=True)
    vacc_type = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.Name


class Multi1(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, null=True)
    Date = models.CharField(max_length=250)
    Dosage = models.IntegerField(null=True)
    Patient_Id = models.CharField(max_length=50, null=True)
    vacc_type = models.CharField(max_length=50, null=True)
    Time = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.Name


class Child1(models.Model):
    objects = None
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50, null=True)
    Date = models.DateField(max_length=250)
    Dosage = models.IntegerField()
    Patient_Id = models.CharField(max_length=50, null=True)
    vacc_type = models.CharField(max_length=50, null=True)
    Time = models.TimeField(max_length=50, null=True)

    def __str__(self):
        return self.Name


class hospital_record(models.Model):
    Id = models.AutoField(primary_key=True)
    Object = models.CharField(max_length=250, null=True)
    Cleaned_obj_not = models.CharField(max_length=250, null=True)
    Tetenus = models.CharField(max_length=250, null=True)
    Caused_obj_Clean_not = models.CharField(max_length=250, null=True)
    Reaction = models.CharField(max_length=250, null=True)
    Alurgies = models.CharField(max_length=250, null=True)
    Patient_Id = models.CharField(max_length=50, null=True)


class colera_record(models.Model):
    Id = models.AutoField(primary_key=True)
    Object = models.CharField(max_length=250, null=True)
    Cleaned_obj_not = models.CharField(max_length=250, null=True)
    Tetenus = models.CharField(max_length=250, null=True)
    Caused_obj_Clean_not = models.CharField(max_length=250, null=True)
    Reaction = models.CharField(max_length=250, null=True)
    Alurgies = models.CharField(max_length=250, null=True)
    Patient_Id = models.CharField(max_length=50, null=True)


class questiana_record(models.Model):
    Id = models.AutoField(primary_key=True)
    q1 = models.CharField(max_length=250, null=True)
    q2 = models.CharField(max_length=250, null=True)
    q3 = models.CharField(max_length=250, null=True)
    q4 = models.CharField(max_length=250, null=True)
    q5 = models.CharField(max_length=250, null=True)
    q6 = models.CharField(max_length=250, null=True)
    q7 = models.CharField(max_length=250, null=True)
    q8 = models.CharField(max_length=250, null=True)
    q9 = models.CharField(max_length=250, null=True)
    Patient_Id = models.CharField(max_length=50, null=True)


class questianb_record(models.Model):
    Id = models.AutoField(primary_key=True)
    q1 = models.CharField(max_length=250, null=True)
    q2 = models.CharField(max_length=250, null=True)
    q3 = models.CharField(max_length=250, null=True)
    q4 = models.CharField(max_length=250, null=True)
    q5 = models.CharField(max_length=250, null=True)
    q6 = models.CharField(max_length=250, null=True)
    q7 = models.CharField(max_length=250, null=True)
    q8 = models.CharField(max_length=250, null=True)
    q9 = models.CharField(max_length=250, null=True)
    Patient_Id = models.CharField(max_length=50, null=True)


class vaccinated_or_not(models.Model):
    Id = models.AutoField(primary_key=True)
    Patient_Id = models.CharField(max_length=50, null=True)
    vaccinated_or_not = models.CharField(max_length=250, null=True)


class hos_dose(models.Model):
    adult_child = models.CharField(max_length=50, null=True)
    vaccine_dose = models.CharField(max_length=50, null=True)
    Registernumber = models.CharField(max_length=50, null=True)
    date = models.CharField(max_length=50, null=True)
    vaccinename = models.CharField(max_length=250, null=True)
