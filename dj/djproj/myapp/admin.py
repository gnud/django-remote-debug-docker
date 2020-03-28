from django.contrib import admin
from myapp import models as myapp_models


# Register your models here.

@admin.register(myapp_models.Contacts)
class UserAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

