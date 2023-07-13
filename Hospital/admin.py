from django.contrib import admin

from Hospital.models import Appointmet, Doctor, Patient

# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appointmet)
