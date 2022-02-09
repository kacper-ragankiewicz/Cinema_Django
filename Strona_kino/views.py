from audioop import reverse
from pyexpat.errors import messages
from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout
from django.contrib import admin
from Strona_kino.models import Film
from .forms import NewUserForm




class FilmLista(ListView):
    model = Film




class FilmDetale(DetailView):
    model = Film




def login_site(request):
    return render(request, 'Strona_kino/login_site.html')




@csrf_exempt
def rejestracja(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("main:homepage")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="Strona_kino/register.html", context={"register_form":form})


# def logout(request):
#     return HttpResponse(content, status=401)
#








