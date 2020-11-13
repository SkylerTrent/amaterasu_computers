from django.contrib import admin
from .models import Giveaway, Has_Voted

# Register your models here.
admin.site.register(Giveaway)
admin.site.register(Has_Voted)
