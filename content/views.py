from django.shortcuts import render, redirect
from .forms import FormContact
from .models import Contact


def index(request):
    form = FormContact(request.POST or None)
    if form.is_valid():
        form.save()
    if request.method == "POST":
        return redirect('/contact')
    return render(request, 'contact.html', {})


