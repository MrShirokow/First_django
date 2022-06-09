from django.contrib import admin
from shop.models import Person, Animal


class PersonAdmin(admin.ModelAdmin):
    pass

class AnimalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Animal, AnimalAdmin)