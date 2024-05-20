from django import forms
from django.forms import TimeInput, DateInput

from .models import UserPreferences
from django.utils import timezone


class UserPreferencesForm(forms.ModelForm):
    class Meta:
        model = UserPreferences
        fields = ['date', 'time_start', 'time_end', 'activity_type', 'restaurant_style']

    def clean_date(self):
        date = self.cleaned_data['date']

        if date < timezone.now().date():
            raise forms.ValidationError("Date must be today or in the future.")

        return date

    def clean(self):
        cleaned_data = super().clean()
        time_start = cleaned_data.get('time_start')
        time_end = cleaned_data.get('time_end')

        if time_start and time_end and time_start >= time_end:
            raise forms.ValidationError("End time must be after start time.")

    date = forms.DateField(
        widget=DateInput(attrs={'type': 'date'}))
    time_start = forms.TimeField(
        widget=TimeInput(attrs={'type': 'time'}))
    time_end = forms.TimeField(
        widget=TimeInput(attrs={'type': 'time'}))

    ACTIVITY_CHOICES = [
        ('outdoor', 'Outdoor'),
        ('indoor', 'Indoor'),
        ('educational', 'Educational'),
    ]
    activity_type = forms.ChoiceField(
        choices=ACTIVITY_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    RESTAURANT_CHOICES = [
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Japanese', 'Japanese'),
        ('French', 'French'),
        ('American', 'American'),
        ('Indian', 'Indian'),
        ('Middle-Eastern', 'Middle-Eastern'),
    ]
    restaurant_style = forms.ChoiceField(
        choices=RESTAURANT_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )


class NewAdminForm(forms.Form):
    user_email = forms.CharField(
        max_length=500,
        label="User's email",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

# Add a search functionality
# Add a filter functionality
ORDER_CHOICES = [
    ('asc', 'Ascending'),
    ('desc', 'Descending')
]


class ReviewSearchForm(forms.Form):
    SEARCH_FIELDS = (
        ('place__name', 'Place Name'),
        ('review', 'Review'),
        ('rating', 'Rating'),
    )

    search_field = forms.ChoiceField(choices=SEARCH_FIELDS, widget=forms.Select(), required=True)
    search_query = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Search...'}), required=True)

    filter_by = forms.ChoiceField(choices=[
        ('created_at', 'Posted Date'),
        ('rating', 'Rating'),
    ], required=False, label="Filter by")

    order = forms.ChoiceField(choices=ORDER_CHOICES, required=False, label="Order")


class NewLocationForm(forms.Form):
    LOCATION_TYPE_CHOICES = [
        ('activity', 'Activity'),
        ('restaurant', 'Restaurant'),
    ]
    ACTIVITY_TYPE_CHOICES = [
        ('outdoor', 'Outdoor'),
        ('indoor', 'Indoor'),
        ('educational', 'Educational'),
    ]

    RESTAURANT_TYPE_CHOICES = [
        ('Chinese', 'Chinese'),
        ('Italian', 'Italian'),
        ('Japanese', 'Japanese'),
        ('French', 'French'),
        ('American', 'American'),
        ('Indian', 'Indian'),
        ('Middle-Eastern', 'Middle-Eastern'),
    ]

    name = forms.CharField(label='Location Name', max_length=255)
    location_type = forms.ChoiceField(label='Location Type', choices=LOCATION_TYPE_CHOICES)
    activity_type = forms.ChoiceField(label='Activity Type', choices=ACTIVITY_TYPE_CHOICES, required=False)
    restaurant_type = forms.ChoiceField(label='Restaurant Type', choices=RESTAURANT_TYPE_CHOICES, required=False)
    latitude = forms.FloatField(widget=forms.HiddenInput())
    longitude = forms.FloatField(widget=forms.HiddenInput())
