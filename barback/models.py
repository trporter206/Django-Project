from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user        = models.OneToOneField(User, on_delete=models.CASCADE)
    city        = models.CharField(max_length=100, default='')
    bartender   = models.BooleanField(null=True)
    email       = models.EmailField(default='')
    first_name  = models.CharField(max_length=100, blank=True, null=True)
    last_name   = models.CharField(max_length=100, blank=True, null=True)
    username    = models.CharField(max_length=100)

class Cocktail(models.Model):
    cocktail_name   = models.CharField(max_length = 50)
    cocktail_image  = models.ImageField(upload_to="cocktail_images/", blank=True, null=True)
    pub_date        = models.DateTimeField(auto_now=True)
    cocktail_info   = models.CharField(max_length = 200, blank=True, null=True)
    cocktail_steps  = models.CharField(max_length = 1000, blank=True, null=True)
    virgin          = models.BooleanField(null=True)
    user            = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    public          = models.BooleanField(null=True)
    likes           = models.IntegerField(null=True, default=0)

    cocktail_type_choices = (
        ('WHISKEY', 'Whiskey'),
        ('VODKA', 'Vodka'),
        ('TEQUILA', 'Tequila'),
        ('GIN', 'Gin'),
        ('VIRGIN', 'Virgin'),
    )
    cocktail_type = models.CharField(max_length = 10, choices = cocktail_type_choices)

    def __str__(self):
        return self.cocktail_name

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=2) <= self.pub_date <= now

    def get_absolute_url(self):
        return reverse("barback:detail", kwargs={"id": self.id})

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
