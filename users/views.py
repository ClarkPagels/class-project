from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import UserPreferencesForm, NewAdminForm, NewLocationForm
from .models import ActivityLocation, RestaurantLocation, CustomUser, Itinerary, GasStationLocation
from django.contrib import messages
from django.contrib.auth import get_user_model
import random


def home(request):
    if request.user.is_authenticated:
        if request.user.is_admin_user:
            return render(request, "admin_home.html")
        else:
            return render(request, "user_home.html")
    else:
        return render(request, "home.html")

# Used ChatGPT to learn how to use login_required()
@login_required()
def logout_view(request):
    logout(request)
    return redirect("/")


@login_required()
def map(request):
    latest_itinerary = Itinerary.objects.latest("id")

    activity = latest_itinerary.activity.name
    activity_lat = latest_itinerary.activity.latitude
    activity_long = latest_itinerary.activity.longitude
    gas = latest_itinerary.gas_station.name
    gas_lat = latest_itinerary.gas_station.latitude
    gas_long = latest_itinerary.gas_station.longitude
    restaurant_lat = latest_itinerary.restaurant.latitude
    restaurant_long = latest_itinerary.restaurant.longitude
    restaurant = latest_itinerary.restaurant.name
    context = {
        "google_api_key": settings.GOOGLE_API_KEY,
        "activity": activity,
        "activity_lat": float(activity_lat),
        "activity_long": float(activity_long),
        "gas": gas,
        "gas_lat": float(gas_lat),
        "gas_long": float(gas_long),
        "restaurant": restaurant,
        "restaurant_lat": float(restaurant_lat),
        "restaurant_long": float(restaurant_long),
    }
    return render(request, 'map.html', context)


@login_required()
def submit_preferences(request):
    global selected_gas_station
    if request.method == 'POST':
        form = UserPreferencesForm(request.POST)
        if form.is_valid():
            user_preferences = form.save(commit=False)
            user_preferences.user = request.user
            user_preferences.save()

            user_activity_type = user_preferences.activity_type
            user_restaurant_style = user_preferences.restaurant_style

            # Activities
            activities = ActivityLocation.objects.filter(activity_type=user_activity_type, approved=True)

            # Restaurants
            restaurants = RestaurantLocation.objects.filter(restaurant_type=user_restaurant_style, approved=True)

            # Gas Station
            all_gas_stations = GasStationLocation.objects.all()

            gas_stations_list = list(all_gas_stations)

            if gas_stations_list:
                selected_gas_station = random.choice(gas_stations_list)

            start_minutes = user_preferences.time_start.hour * 60 + user_preferences.time_start.minute
            end_minutes = user_preferences.time_end.hour * 60 + user_preferences.time_end.minute
            total_duration = end_minutes - start_minutes

            activity_duration = total_duration // 2
            restaurant_duration = total_duration // 2

            # Create itinerary
            itinerary = Itinerary(
                user=request.user,
                activity=random.choice(activities),
                restaurant=random.choice(restaurants),
                gas_station=selected_gas_station,
                activity_duration_hours=activity_duration // 60,
                activity_duration_minutes=activity_duration % 60,
                restaurant_duration_hours=restaurant_duration // 60,
                restaurant_duration_minutes=restaurant_duration % 60,
                gas_station_duration_minutes=15,
            )
            itinerary.save()

            return redirect('users:itinerary')
        else:
            error_messages = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"Error in {field}: {error}")
            return render(request, 'create_itinerary.html', {'form': form, 'error_messages': error_messages})
    else:
        form = UserPreferencesForm()

    return render(request, 'create_itinerary.html', {'form': form, 'error_messages': []})


@login_required()
def pick_random_location(user_type, user_dict):
    if user_type in user_dict:
        locations_list = user_dict[user_type]

        if locations_list:
            random_location = random.choice(locations_list)
            return random_location
        else:
            return None  # No locations for the given type
    else:
        return None  # Invalid activity type


@login_required()
def display_itinerary(request):
    user_itinerary = Itinerary.objects.filter(user=request.user).last()

    if user_itinerary:
        context = {
            'itinerary': user_itinerary,
        }
    else:
        context = {
            'itinerary': None,
            'message': 'No itinerary found.' 
        }
    return render(request, 'itinerary.html', context)



@login_required()
# allows admins to add other admins to the database by submitting the user's email
def admin_approve_admin(request):
    User = get_user_model()
    # users = User.objects.all()

    if request.method == 'POST':
        form = NewAdminForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['user_email']
            try:
                email = CustomUser.objects.get(email=user_email)
                # search database for user's email with the inputted email
                # if it exists check if user is already an admin
                # if yes return msg
                # if no make user admin
                # if user.email doesn't exist-> return error msg
                if email.is_admin_user:
                    # if it exists check if user is already an admin
                    # if yes return msg
                    # return HttpResponse("User is already an admin!")
                    messages.error(request, 'User is already an admin!')
                else:
                    email.is_admin_user = True
                    # post_save.disconnect(update_user_role, sender=CustomUser)
                    email.save()
                    # post_save.connect(update_user_role, sender=CustomUser)
            except CustomUser.DoesNotExist:
                # return HttpResponse("no such user")
                messages.error(request, 'No such user exists!')
                # return render(request, "admin_approve_admin.html",
                #               {"error_message": "No such user exists!",},)
                # don't break the app

    # return message user is already an admin
    else:
        form = NewAdminForm()

    context = {}
    context['form'] = form
    return render(request, "admin_approve_admin.html", context)


@login_required()
def submit_review(request):
    if request.method == 'POST':
        form = NewLocationForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            location_type = form.cleaned_data['location_type']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']

            if location_type == 'activity':
                activity_type = form.cleaned_data['activity_type']
                new_location, created = ActivityLocation.objects.get_or_create(
                    name=name,
                    activity_type=activity_type,
                    latitude=latitude,
                    longitude=longitude,
                    approved=False
                )
            elif location_type == 'restaurant':
                restaurant_type = form.cleaned_data['restaurant_type']
                new_location, created = RestaurantLocation.objects.get_or_create(
                    name=name,
                    restaurant_type=restaurant_type,
                    latitude=latitude,
                    longitude=longitude,
                    approved=False
                )

            # Check if the object was created and then save it
            if created:
                new_location.save()

            return redirect('users:submit_review')

    else:
        form = NewLocationForm()

    return render(request, 'new_location_form.html', {'form': form})


@login_required()
def admin_approve_reviews(request):
    if not request.user.is_admin_user:
        return redirect('users:home')

    pending_locations = {
        'activity': ActivityLocation.objects.filter(approved=False),
        'restaurant': RestaurantLocation.objects.filter(approved=False),
    }

    if request.method == 'POST':
        location_id = request.POST.get('location_id')
        location_type = request.POST.get('location_type')
        action = request.POST.get('action')

        if location_type not in pending_locations:
            messages.error(request, 'Invalid location type provided.')
            return redirect('users:admin_approve_reviews')

        location = pending_locations[location_type].get(id=location_id)

        if action == 'approve':
            location.approved = True
            location.save()
            messages.success(request, 'Location approved successfully.')
        elif action == 'delete':
            location.delete()
            messages.success(request, 'Location deleted successfully.')

        return redirect('users:admin_approve_reviews')

    context_pending_locations = [item for sublist in pending_locations.values() for item in sublist]
    return render(request, 'admin_approve_location.html', {'pending_locations': context_pending_locations})


@login_required()
def all_locations(request):
    filter_by = request.GET.get('filter_by', None)
    approved_filter = request.GET.get('approved', 'all')
    order_by = request.GET.get('order_by', 'name')
    order = request.GET.get('order', 'asc')

    activity_locations = ActivityLocation.objects.filter(approved=True)
    restaurant_locations = RestaurantLocation.objects.filter(approved=True)
    gas_station_locations = GasStationLocation.objects.filter(approved=True)

    if filter_by == 'activity':
        activity_locations = apply_filters(activity_locations, approved_filter, order_by, order)
        restaurant_locations = []
        gas_station_locations = []
    elif filter_by == 'restaurant':
        restaurant_locations = apply_filters(restaurant_locations, approved_filter, order_by, order)
        activity_locations = []
        gas_station_locations = []
    elif filter_by == 'gas_station':
        gas_station_locations = apply_filters(gas_station_locations, approved_filter, order_by, order)
        activity_locations = []
        restaurant_locations = []
    else:
        activity_locations = apply_filters(activity_locations, approved_filter, order_by, order)
        restaurant_locations = apply_filters(restaurant_locations, approved_filter, order_by, order)
        gas_station_locations = apply_filters(gas_station_locations, approved_filter, order_by, order)

    return render(request, 'all_locations.html', {
        'activity_locations': activity_locations,
        'restaurant_locations': restaurant_locations,
        'gas_station_locations': gas_station_locations,
        'filter_by': filter_by,
        'approved_filter': approved_filter,
        'order_by': order_by,
        'order': order,
    })


def apply_filters(queryset, approved_filter, order_by, order):
    if approved_filter == 'yes':
        queryset = queryset.filter(approved=True)
    elif approved_filter == 'no':
        queryset = queryset.filter(approved=False)

    if order == 'asc':
        queryset = queryset.order_by(order_by)
    elif order == 'desc':
        queryset = queryset.order_by(f'-{order_by}')

    return queryset
