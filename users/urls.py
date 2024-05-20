from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path("", views.home, name='home'),
    path('logout/', views.logout_view, name='logout_view'),
    path('map/', views.map, name='map'),
    path('form/', views.submit_preferences, name='form'),
    path('new_location/', views.submit_review, name='submit_review'),
    path('admin_approve_location/', views.admin_approve_reviews, name='admin_approve_reviews'),
    path('admin_approve_admin/', views.admin_approve_admin, name='admin_approve_admin'),
    path("itinerary/", views.display_itinerary, name='itinerary'),
    path("all_locations/", views.all_locations, name='all_locations'),
]
