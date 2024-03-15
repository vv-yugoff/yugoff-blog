from django.contrib import admin
from .models import PortfolioItem
from.models import SkillsItem

# Register your models here.

admin.site.register(PortfolioItem)
admin.site.register(SkillsItem)