from django.contrib import admin

from .models import Keeper


class KeeperAdmin(admin.ModelAdmin):
    pass


admin.site.register(Keeper, KeeperAdmin)