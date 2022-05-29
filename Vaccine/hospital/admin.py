from django.contrib import admin

# Register your models here.
from hospital.models import Hospital
from hospital.models import Single
from hospital.models import Multi
from hospital.models import Child
from hospital.models import Injection
from .models import Single1
from .models import Multi1
from .models import Child1
from .models import hospital_record
from .models import colera_record, hos_dose, questianb_record, questiana_record

admin.site.register(Hospital),
admin.site.register(Single),
admin.site.register(Multi),
admin.site.register(Child),
admin.site.register(Injection),
admin.site.register(Single1),
admin.site.register(Multi1),
admin.site.register(Child1),
admin.site.register(hospital_record),
admin.site.register(colera_record),
admin.site.register(hos_dose),
admin.site.register(questiana_record),
admin.site.register(questianb_record),
