from django.contrib import admin
from .models import Appointment


# Register your models here.
class doctor_admin(admin.ModelAdmin):
    List_display = (
        'Name', 'Parent_or_Guardian', 'Issue', 'Detailed_Reason', 'suffering_from', 'Gender', 'Age', 'Blood_group',
        'Availability_slot', 'checkup_on')


admin.site.register(Appointment, doctor_admin)
