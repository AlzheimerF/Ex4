from django.contrib import admin
from . import models

admin.site.register(models.CheckerForSelling)
admin.site.register(models.CheckerForBuying)
