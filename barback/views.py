from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic, View
from django.utils import timezone
from .models import Cocktail, UserProfile
from django.db import models
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.urls import reverse
import datetime
from .forms import CocktailForm, UserForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

class IndexView(generic.ListView):
    template_name = 'barback/index.html'
    context_object_name = 'latest_cocktail_list'

    def get_queryset(self):
        return Cocktail.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')

class DetailView(generic.DetailView):
    model = Cocktail
    template_name = 'barback/detail.html'

    def get_queryset(self):
        return Cocktail.objects.filter(pub_date__lte=timezone.now())

class CreateView(generic.edit.CreateView):
    model = Cocktail
    fields = ['cocktail_name',
              'cocktail_type',
              'cocktail_image',
              'cocktail_info',
              'cocktail_steps',
              'virgin',
              ]

class AboutView(generic.TemplateView):
    template_name = "barback/about.html"

def register(request):
    template_name = 'registration/registration_form.html'
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('barback:index')
    else:
        form = UserForm()
        return render(request, template_name, {'form': form})

def save(request, cocktail_id):
    form = CocktailForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully Created")
        return HttpResponseRedirect(reverse('barback:detail', args=(cocktail.id,)))

def delete(request, cocktail_id):
    model = get_object_or_404(Cocktail, pk=cocktail_id)
    model.delete()
    return HttpResponseRedirect(reverse('barback:index'))

def logout_view(request):
    logout(request)
    return redirect('barback:index')

def profile(request):
    args = {'user': request.user}
    return render(request, 'barback/profile.html', args)
