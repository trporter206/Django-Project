from django.db import models
from django.utils import timezone
import datetime

class Cocktail(models.Model):
    cocktail_name   = models.CharField(max_length = 50)
    cocktail_image  = models.ImageField
    pub_date        = models.DateTimeField(default=timezone.now())

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

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'
