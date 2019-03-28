from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.utils import timezone
from .models import Cocktail
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse


class IndexView(generic.ListView):
    template_name = 'barback/index.html'
    context_object_name = 'latest_cocktail_list'

    def get_queryset(self):
        return Cocktail.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Cocktail
    template_name = 'barback/detail.html'

    def get_queryset(self):
        return Cocktail.objects.filter(pub_date__lte=timezone.now())

class CreateView(generic.edit.CreateView):
    model = Cocktail
    fields = ['cocktail_name', 'cocktail_type']

def save(request, cocktail_id):
    cocktail = get_object_or_404(Cocktail, pk=cocktail_id)
    try:
        created_name     = cocktail.cocktail_name.get(pk=request.POST['cocktail_name'])
        created_type     = cocktail.cocktail_type.get(pk=request.POST['cocktail_type'])
        created_pub_date = cocktail.cocktail_pub_date.get(pk=request.POST['cocktail_pub_date'])
    except (KeyError, Cocktail.DoesNotExist):
        return render(request, 'barback/cocktail_form.html', {
            'cocktail': cocktail,
            'error_message': "You didn't create a cocktail.",
        })
    else:
        created_name.save()
        created_type.save()
        created_pub_date.save()
        # return HttpResponseRedirect(reverse('barback:detail', args=(cocktail.id,)))
