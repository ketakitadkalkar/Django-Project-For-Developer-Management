from django.contrib import admin


# Register your models here.
from home.models import *

admin.site.register(Question)
admin.site.register(Domain)
admin.site.register(Technology)
admin.site.register(Developer)
admin.site.register(Blog)
admin.site.register(Project)
admin.site.register(Employee)