from django.contrib import admin
from minime import models


class UrlAdmin(admin.ModelAdmin):
    list_display = [
        "hash",
        "created",
        "has_password",
    ]

    @admin.display(boolean=True, description="Has a password?")
    def has_password(self, obj) -> bool:
        return obj.password is not None


admin.register(models.Url, UrlAdmin)
