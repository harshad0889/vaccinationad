# Generated by Django 4.0.4 on 2022-05-28 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagesre',
            name='vaxin_reminder_count',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
