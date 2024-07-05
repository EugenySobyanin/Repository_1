from django.contrib import admin

from films.models import Genre, Type, Country, Director


admin.site.register(Genre)
admin.site.register(Type)
admin.site.register(Country)
admin.site.register(Director)
