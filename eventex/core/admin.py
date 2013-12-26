# contact: utf-8
from django.contrib import admin
from eventex.core.models import Speaker, Contact

class ContactInLine(admin.TabularInLine):
    model = Contact
    extra = 1


class SpeakserAdmin(admin.ModelAdmin):
    inlines = [ContactInLine, ]
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Speaker, SpeakerAdmin)
