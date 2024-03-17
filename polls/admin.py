from django.contrib import admin

from .models import Poll


class PollAdmin(admin.ModelAdmin):
    None


admin.site.register(Poll, PollAdmin)
