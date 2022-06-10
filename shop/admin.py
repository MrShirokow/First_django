from django.contrib import admin
from shop.models import Person, Pet


class PersonAdmin(admin.ModelAdmin):
    pass


class PetAdmin(admin.ModelAdmin):
    pass


admin.site.register(Person, PersonAdmin)
admin.site.register(Pet, PetAdmin)
