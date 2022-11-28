from django.db import models

# Create your models here.
subclass = (('Fever', 'Cold/Cough/Fever'),
            ('migraine', 'Migraine'),
            ('sugar', 'Sugar/Blood pressure'),
            ('skin', 'Rashes/skin issues'),
            ('digestion', 'Digestion Issues'),
            ('others', 'Other issue'))

sex = (('male', 'Male'),
       ('female', 'Female'),
       ('others', 'Others'),
       ('not', 'Not like to disclose'))

Timing = (('mrg10', 'Mrg 10-11'),
          ('mrg11', 'Mrg 11-12'),
          ('aft12', 'Aft 12-01'))


class Appointment(models.Model):
    Name = models.CharField(max_length=30, null=False)
    Parent_or_Guardian = models.CharField(max_length=40, null=False)
    Issue = models.CharField(max_length=50, choices=subclass, default='Fever')
    Detailed_Reason = models.TextField(max_length=500, null=False)
    suffering_from = models.DateField(auto_now_add=True, null=False)
    Gender = models.CharField(max_length=50, choices=sex)
    Age = models.IntegerField(null=False)
    Blood_group = models.CharField(max_length=10, null=False)
    Availability_slot = models.CharField(max_length=30, choices=Timing, default='mrg10')
    checkup_on = models.DateField(auto_now_add=True, null=False)
