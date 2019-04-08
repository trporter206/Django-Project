from django.test import TestCase
from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Cocktail
from django.contrib.auth.models import User
import datetime

class CocktailModelTests(TestCase):
    def test_was_published_recently_with_future_q(self):
        time = timezone.now() + datetime.timedelta(days=30)
        future_cocktail = Cocktail(pub_date=time)
        self.assertIs(future_cocktail.was_published_recently(), False)

    def test_was_published_recently_with_old_cocktail(self):
        time = timezone.now() - datetime.timedelta(days=2, seconds=1)
        old_cocktail = Cocktail(pub_date=time)
        self.assertIs(old_cocktail.was_published_recently(), False)

    def test_was_published_recently_with_recent_cocktail(self):
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_cocktail = Cocktail(pub_date=time)
        self.assertIs(recent_cocktail.was_published_recently(), True)

def create_cocktail(cocktail_name, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Cocktail.objects.create(cocktail_name=cocktail_name, pub_date=time)

class CocktailIndexViewTests(TestCase):
    def test_no_cocktails(self):
        response = self.client.get(reverse('barback:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No cocktails are available.")
        self.assertQuerysetEqual(response.context['latest_cocktail_list'], [])

    def test_past_cocktail(self):
        create_cocktail(cocktail_name="Past cocktail.", days=-30)
        response = self.client.get(reverse('barback:index'))
        self.assertQuerysetEqual(
            response.context['latest_cocktail_list'],
            ['<Cocktail: Past cocktail.>']
        )

    def test_future_cocktail(self):
        create_cocktail(cocktail_name="Future cocktail.", days=30)
        response = self.client.get(reverse('barback:index'))
        self.assertContains(response, "No cocktails are available.")
        self.assertQuerysetEqual(response.context['latest_cocktail_list'], [])

    def test_future_cocktail_and_past_cocktail(self):
        create_cocktail(cocktail_name="Past cocktail.", days=-30)
        create_cocktail(cocktail_name="Future cocktail.", days=30)
        response = self.client.get(reverse('barback:index'))
        self.assertQuerysetEqual(
            response.context['latest_cocktail_list'],
            ['<Cocktail: Past cocktail.>']
        )

    def test_two_past_cocktails(self):
        create_cocktail(cocktail_name="Past cocktail 1.", days=-30)
        create_cocktail(cocktail_name="Past cocktail 2.", days=-5)
        response = self.client.get(reverse('barback:index'))
        self.assertQuerysetEqual(
            response.context['latest_cocktail_list'],
            ['<Cocktail: Past cocktail 2.>', '<Cocktail: Past cocktail 1.>']
        )

class CocktailDetailViewTests(TestCase):
    def test_future_cocktail(self):
        future_cocktail = create_cocktail(cocktail_name='future cocktail', days=5)
        url = reverse('barback:detail', args=(future_cocktail.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_cocktail(self):
        past_cocktail = create_cocktail(cocktail_name='past cocktail', days=-5)
        url = reverse('barback:detail', args=(past_cocktail.id,))
        response = self.client.get(url)
        self.assertContains(response, past_cocktail.cocktail_name)
