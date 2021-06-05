from django.contrib import admin

from ..models import Dialog


class DialogAdmin(admin.ModelAdmin):
    pass


admin.site.register(Dialog, DialogAdmin)
