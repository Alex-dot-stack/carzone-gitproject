from django.contrib import admin
from .models import Team
from django.utils.html import format_html


# hier wird Übersicht festgelegt wie Einträge angezeigt werden, was anklickbar ist usw
class TeamAdmin(admin.ModelAdmin):
    # wir wollen dass Fotoa cuh angezeigt wird in Übersicht
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.photo.url))
    thumbnail.short_description = 'photo' # Spaltenname ändern

    # was angezeigt wird auf Übersicht in Datenbank
    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')

    # was anklickbar ist
    list_display_links = ('first_name','id', 'thumbnail')

    # Suchfeld kann eingebaut werden - automatisch in DJango Framework built in
    search_fields = ('first_name', 'last_name', 'designation')

    # Filter Funktion einbauen
    list_filter = ('designation',)

# Register your models here. - Datenbank(einträge) registrieren
admin.site.register(Team, TeamAdmin)