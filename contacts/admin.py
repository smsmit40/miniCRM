from django.contrib import admin
from .models import Contact, Email, Files, Reminder

# Register your models here.

admin.site.register(Contact)
admin.site.register(Email)
admin.site.register(Files)
admin.site.register(Reminder)