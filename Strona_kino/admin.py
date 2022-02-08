from django.contrib import admin
from .models import Film , Bilet , User , Ankieta , Wybor , Rezerwacja

#admin.site.register(Film)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['imie','nazwisko']


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['tytul','kategoria', 'jezyk', 'status', 'data_wydania','wyswietlenia' ]


@admin.register(Bilet)
class BiletAdmin(admin.ModelAdmin):
    list_display = ['rezerwacja']


@admin.register(Rezerwacja)
class RezerwacjaAdmin(admin.ModelAdmin):
    list_display = ['rodzaj_biletu','cena_biletu','ilosc_biletow','data_zakupu']


@admin.register(Ankieta)
class AnkietaAdmin(admin.ModelAdmin):
    list_display = ['pytanie', 'data_publikacji']


@admin.register(Wybor)
class WyborAdmin(admin.ModelAdmin):
    list_display = ['ankieta', 'odpowiedz', 'glosy']