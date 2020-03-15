from django.contrib import admin
from . import models
# Register your models here


admin.site.register(models.Subject)
admin.site.register(models.Teacher)
admin.site.register(models.Relatives)
admin.site.register(models.Student)
admin.site.register(models.Classroom)
