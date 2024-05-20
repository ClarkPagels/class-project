from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    is_admin_user = models.BooleanField(default=False)


class ActivityLocation(models.Model):
    name = models.CharField(max_length=255)
    activity_type = models.CharField(
        max_length=50,
        choices=[
            ('outdoor', 'Outdoor'),
            ('indoor', 'Indoor'),
            ('educational', 'Educational'),
        ],
        default='outdoor'
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    approved = models.BooleanField(default=False)

    @property
    def location_type_display(self):
        return 'activity'

    def __str__(self):
        return self.name


class RestaurantLocation(models.Model):
    name = models.CharField(max_length=255)
    restaurant_type = models.CharField(
        max_length=50,
        choices=[
            ('Chinese', 'Chinese'),
            ('Italian', 'Italian'),
            ('Japanese', 'Japanese'),
            ('French', 'French'),
            ('American', 'American'),
            ('Indian', 'Indian'),
            ('Middle-Eastern', 'Middle-Eastern'),
        ]
    )
    latitude = models.FloatField()
    longitude = models.FloatField()
    approved = models.BooleanField(default=False)

    @property
    def location_type_display(self):
        return 'restaurant'
    def __str__(self):
        return self.name


class GasStationLocation(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    approved = models.BooleanField(default=False)

    @property
    def location_type_display(self):
        return 'gas_station'

    def __str__(self):
        return self.name


class UserPreferences(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=False)
    time_start = models.TimeField(auto_now_add=False)
    time_end = models.TimeField(auto_now_add=False)
    activity_type = models.CharField(
        max_length=50,
        choices=[
            ('outdoor', 'Outdoor'),
            ('indoor', 'Indoor'),
            ('educational', 'Educational'),
        ],
        default='outdoor'
    )
    restaurant_style = models.CharField(
        max_length=50,
        choices=[
            ('Chinese', 'Chinese'),
            ('Italian', 'Italian'),
            ('Japanese', 'Japanese'),
            ('French', 'French'),
            ('American', 'American'),
            ('Indian', 'Indian'),
            ('Middle-Eastern', 'Middle-Eastern'),
            ('Spanish', 'Spanish')
        ],
        default='Chinese'
    )

    def __str__(self):
        return f"Preferences for {self.user.username}"


class Itinerary(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date = models.DateTimeField #and this?
    activity = models.ForeignKey(ActivityLocation, related_name='itinerary_activities', on_delete=models.CASCADE)
    restaurant = models.ForeignKey(RestaurantLocation, related_name='itinerary_restaurants', on_delete=models.CASCADE)
    gas_station = models.ForeignKey(GasStationLocation, related_name='itinerary_gas_station', on_delete=models.CASCADE)
    activity_duration_hours = models.PositiveIntegerField(default=1)
    activity_duration_minutes = models.PositiveIntegerField(default=0)
    restaurant_duration_hours = models.PositiveIntegerField(default=1)
    restaurant_duration_minutes = models.PositiveIntegerField(default=0)
    gas_station_duration_minutes = models.PositiveIntegerField(default=15)

    def __str__(self):
        return f"Itinerary for {self.user.username}"

