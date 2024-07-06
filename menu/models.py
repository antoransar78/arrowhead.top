from django.db import models
from django.utils import timezone


# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='menu_images/')
    

    def __str__(self):
        return self.name

class SliderItem(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Slider_images/')
    

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    RATINGS = [
        ('excellent', 'Excellent'),
        ('super', 'Super'),
        ('good', 'Good'),
        ('okey', 'Okey'),
        ('not satisfactory', 'Not Satisfactory'),
    ]

    CATEGORY = [
        ('steak', 'Steak'),
        ('platter', 'Platter'),
        ('chicken', 'Chicken'),
        ('Table Top', 'Table Top'),
    ]
    REASON = [
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('By Friend', 'By Friend'),
        ('Google Reviews', 'Google Reviews'),
    ]
    HEARD = [
        ('First Visit', 'First Visit'),
        ('Second Visit', 'Second Visit'),
        ('Third Visit', 'Third Visit'),
        ('Multiple Visit', 'Multiple Visit'),
    ]
    
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=False, null=True)
    service_rating = models.CharField(max_length=16, blank=False, choices=RATINGS)
    food_rating = models.CharField(max_length=16, choices=RATINGS)
    drinks_rating = models.CharField(max_length=16, choices=RATINGS)
    ambience_rating = models.CharField(max_length=16, choices=RATINGS)
    cleanliness_rating = models.CharField(max_length=16, choices=RATINGS)
    comments = models.TextField(blank=True, null=True)
    order = models.CharField(max_length=16, choices=CATEGORY)
    compliments = models.TextField(blank=True, null=True)
    visit_reason = models.CharField(max_length=100, choices=REASON)
    heard_about_us = models.CharField(max_length=100, choices=HEARD)
    

    def __str__(self):
        return f'{self.first_name} {self.last_name}'