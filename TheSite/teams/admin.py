from django.contrib import admin
from .models import Team, Person
# Register your models here.


class PersonInline(admin.StackedInline):
    model = Person
    extra = 15


class TeamAdmin(admin.ModelAdmin):
    fields = ['name_text', 'time_text', 'city_text']
    inlines = [PersonInline]


admin.site.register(Team, TeamAdmin)
