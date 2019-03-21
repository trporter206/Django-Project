from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from .models import Cocktail

class IndexView(generic.ListView):
    template_name = 'barback/index.html'
    context_object_name = 'latest_cocktail_list'

    def get_queryset(self):
        return Cocktail.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
