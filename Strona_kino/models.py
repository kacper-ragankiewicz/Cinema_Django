from django.db import models
from django.db.models import Model

CATEGORY_CHOICE = (
    ('AKCJA', 'AKCJA'),
    ('BIOGRAFIA', 'BIOGRAFICZNY'),
    ('DRAMAT', 'DRAMAT'),
    ('FANTASY', 'FANTASY'),
    ('KOMEDIA', 'KOMEDIA'),
    ('ROMANS', 'ROMANS'),
)
LANGUAGE_CHOICE = (
    ('PL', 'POLSKI'),
    ('EN', 'ENGLISH'),
    ('RU', 'РУССКИЙ'),
)
STATUS_CHOICES = (
    ('ND', 'NIEDAWNO DODANE'),
    ('NO', 'NAJCZĘŚCIEJ OGLĄDANE'),
    ('TR', 'NAJLEPIEJ OCENIANE')
)
BILET_CHOICE = (
    ('N', 'NORMALNY'),
    ('U', 'ULGOWY'),
    ('R', 'RODZINNY')
)

class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    imie = models.CharField("Imię użytkownika", max_length=30)
    nazwisko = models.CharField("Nazwisko użytkownika", max_length=30)
    email = models.EmailField("Adres email użytkownika", max_length=100)

    def __str__(self):
        return self.imie


class Ankieta(models.Model):
    id = models.BigAutoField(primary_key=True)
    pytanie = models.CharField(max_length=200)
    data_publikacji = models.DateTimeField('Data publikacji')

    def __str__(self):
        return self.pytanie


class Wybor(models.Model):
    id = models.BigAutoField(primary_key=True)
    ankieta = models.ForeignKey(Ankieta, on_delete=models.CASCADE)
    odpowiedz = models.CharField(max_length=200)
    glosy = models.PositiveIntegerField(default=0)



class Film(models.Model):
    id = models.BigAutoField(primary_key=True)
    tytul = models.CharField("Tytuł filmu", max_length=100)
    opis = models.TextField("Opis filmu", max_length=1000, blank=True, null=True)
    obraz = models.ImageField(upload_to='Strona_kino', blank=True, null=True)
    kategoria = models.CharField(choices=CATEGORY_CHOICE, max_length=15)
    jezyk = models.CharField(choices=LANGUAGE_CHOICE, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    data_wydania = models.IntegerField(default=0)
    wyswietlenia = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.tytul


class Rezerwacja(models.Model):
    id = models.BigAutoField(primary_key=True)
    rodzaj_biletu = models.CharField(choices=BILET_CHOICE, max_length=10)
    cena_biletu = models.PositiveIntegerField(default=0)
    ilosc_biletow = models.PositiveIntegerField(default=0)
    data_zakupu = models.DateTimeField('Data zakupu')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film = models.ForeignKey(Film, on_delete=models.CASCADE)



class Bilet(models.Model):
    id = models.BigAutoField(primary_key=True)
    rezerwacja = models.ForeignKey(Rezerwacja, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, blank=True, null=True)
    film = models.ManyToManyField(Film)