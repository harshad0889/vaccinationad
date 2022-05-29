# Generated by Django 4.0.4 on 2022-05-25 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=250, null=True)),
                ('VaccineNumber', models.CharField(max_length=50, null=True)),
                ('Details', models.CharField(max_length=250, null=True)),
                ('Duration', models.CharField(max_length=250, null=True)),
                ('Number_of_vaccine', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Child1',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Date', models.DateField(max_length=250)),
                ('Dosage', models.IntegerField()),
                ('Patient_Id', models.CharField(max_length=50, null=True)),
                ('vacc_type', models.CharField(max_length=50, null=True)),
                ('Time', models.TimeField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='colera_record',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Object', models.CharField(max_length=250, null=True)),
                ('Cleaned_obj_not', models.CharField(max_length=250, null=True)),
                ('Tetenus', models.CharField(max_length=250, null=True)),
                ('Caused_obj_Clean_not', models.CharField(max_length=250, null=True)),
                ('Reaction', models.CharField(max_length=250, null=True)),
                ('Alurgies', models.CharField(max_length=250, null=True)),
                ('Patient_Id', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='hos_dose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adult_child', models.CharField(max_length=50, null=True)),
                ('vaccine_dose', models.CharField(max_length=50, null=True)),
                ('Registernumber', models.CharField(max_length=50, null=True)),
                ('date', models.CharField(max_length=50, null=True)),
                ('vaccinename', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('RegisterNumber', models.CharField(max_length=50, unique=True)),
                ('Password', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=250, null=True)),
                ('Email', models.EmailField(max_length=254, null=True)),
                ('Address', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='hospital_record',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Object', models.CharField(max_length=250, null=True)),
                ('Cleaned_obj_not', models.CharField(max_length=250, null=True)),
                ('Tetenus', models.CharField(max_length=250, null=True)),
                ('Caused_obj_Clean_not', models.CharField(max_length=250, null=True)),
                ('Reaction', models.CharField(max_length=250, null=True)),
                ('Alurgies', models.CharField(max_length=250, null=True)),
                ('Patient_Id', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Injection',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Patient_Id', models.IntegerField()),
                ('Kid_Id', models.IntegerField(null=True)),
                ('Child_or_adult', models.IntegerField()),
                ('Vaccine_Dose', models.IntegerField()),
                ('Name', models.CharField(max_length=50, null=True)),
                ('RegisterNumber', models.CharField(max_length=50, unique=True)),
                ('Date', models.CharField(max_length=50, null=True)),
                ('Time', models.CharField(max_length=50, null=True)),
                ('NextDate', models.CharField(max_length=50, null=True)),
                ('NextTime', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Multi',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=250, null=True)),
                ('VaccineNumber', models.CharField(max_length=50)),
                ('Details', models.CharField(max_length=250)),
                ('Duration', models.CharField(max_length=250)),
                ('Number_of_vaccine', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Multi1',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Date', models.CharField(max_length=250)),
                ('Dosage', models.IntegerField(null=True)),
                ('Patient_Id', models.CharField(max_length=50, null=True)),
                ('vacc_type', models.CharField(max_length=50, null=True)),
                ('Time', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Single',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=250, null=True)),
                ('VaccineNumber', models.CharField(max_length=50)),
                ('Details', models.CharField(max_length=250)),
                ('Duration', models.CharField(max_length=250)),
                ('Number_of_vaccine', models.CharField(max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Single1',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=50, null=True)),
                ('Date', models.CharField(max_length=250)),
                ('Dosage', models.IntegerField()),
                ('Patient_Id', models.CharField(max_length=50, null=True)),
                ('vacc_type', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='vaccinated_or_not',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('Patient_Id', models.CharField(max_length=50, null=True)),
                ('vaccinated_or_not', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]
