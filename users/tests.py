from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase, Client
from .models import Itinerary, ActivityLocation, RestaurantLocation, GasStationLocation
from django.utils import timezone
from django.core.management import call_command
from django.contrib.messages import get_messages


class GoogleLoginTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        call_command('collectstatic', verbosity=0, interactive=False)
        self.user = get_user_model().objects.create_user(
            username='regular_user',
            email='regular@example.com',
            password='password123',
            first_name='John',
            last_name='Doe',
        )

        self.admin_user = get_user_model().objects.create_user(
            username='admin_user',
            email='cs3240.super@gmail.com',
            password='adminpassword123',
            first_name='Admin',
            last_name='User',
        )
    def test_regular_user_login(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('users:home'))
        self.assertTemplateUsed(response, 'user_home.html')
        self.assertContains(response, 'Welcome User, John Doe!')

##############test admin user login#################
    def test_admin_user_login(self):
        # Directly log in the admin user (bypassing Google OAuth)
        self.client.force_login(self.admin_user)

        # Test application behavior after login
        response = self.client.get(reverse('users:home'))
        self.assertTemplateUsed(response, 'admin_home.html')
        self.assertContains(response, 'Welcome Admin, Admin User!')

############test Google Map#############################
class MapViewTestCase(TestCase):
    def setUp(self):
      
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')  # Use create_user instead of create
        self.client = Client()
        self.client.force_login(self.user)

        self.map_url = reverse('users:map')

        activity = ActivityLocation.objects.create(
            name="Hiking Trail",
            activity_type='outdoor',
            latitude=40.7128,
            longitude=-74.0060,
            approved=True
        )
        restaurant = RestaurantLocation.objects.create(
            name="Chinese Restaurant",
            restaurant_type='Chinese',
            latitude=40.7128,
            longitude=-74.0060,
            approved=True
        )
        gas_station = GasStationLocation.objects.create(
            name="Gas2",
            latitude=40.7128,
            longitude=-74.0060,
            approved=True
        )

        Itinerary.objects.create(
            user=self.user,
            activity=activity,
            restaurant=restaurant,
            gas_station=gas_station
        )

    def test_map_view_with_latest_itinerary(self):
        response = self.client.get(self.map_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'map.html')

###################test submit preference form#################################
class SubmitPreferencesTestCase(TestCase):
    def setUp(self):
       
        User = get_user_model()
        self.user = User.objects.create(username='testuser', password='12345')
        self.client = Client()
        self.client.force_login(self.user)
        activity1 = ActivityLocation.objects.create(
            name="Hiking Trail",
            activity_type='outdoor',
            latitude=40.7128,
            longitude=-74.0060,
            approved=True
        )
        activity2 = ActivityLocation.objects.create(
            name="Tennis",
            activity_type='outdoor',
            latitude=43.7128,
            longitude=-44.0060,
            approved=True
        )
        restaurant1 = RestaurantLocation.objects.create(
            name="Chinese Restaurant",
            restaurant_type='Chinese',
            latitude=40.7128,
            longitude=-74.0060,
            approved=True
        )
        restaurant2 = RestaurantLocation.objects.create(
            name="Italian Restaurant",
            restaurant_type='Italian',
            latitude=33.7128,
            longitude=-14.0060,
            approved=True
        )
        gas_station1 = GasStationLocation.objects.create(
            name="Gas2",
            latitude=40.7128,
            longitude=-74.0060,
            approved=True
        )
        gas_station2 = GasStationLocation.objects.create(
            name="Gas2",
            latitude=66.7128,
            longitude=-77.0060,
            approved=True
        )
        Itinerary.objects.create(
            user=self.user,
            activity=activity1,
            restaurant=restaurant1,
            gas_station=gas_station1
        )
        Itinerary.objects.create(
            user=self.user,
            activity=activity2,
            restaurant=restaurant2,
            gas_station=gas_station2
        )

    
    def test_valid_form_submission(self):
        form_data = {
            'date': timezone.now().date().strftime('%Y-%m-%d'),
            'time_start': '10:00',
            'time_end': '18:00',
            'activity_type': 'outdoor',
            'restaurant_style': 'Chinese'
        }
        response = self.client.post(reverse('users:form'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Itinerary.objects.filter(user=self.user).exists())

    def test_invalid_form_end_time_before_start_time(self):
        form_data = {
            'date': timezone.now().date().strftime('%Y-%m-%d'),
            'time_start': '18:00',
            'time_end': '10:00',
            'activity_type': 'outdoor',
            'restaurant_style': 'Chinese'
        }
        response = self.client.post(reverse('users:form'), form_data)
        self.assertEqual(response.status_code, 200) #Does not redirect as the end time is before the start time.
        


##################Test display itinerary###################################
class DisplayItineraryTestCase(TestCase):
    def setUp(self):
        # Create a test user
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.force_login(self.user)

        # Create test data for ActivityLocation, RestaurantLocation, GasStationLocation
        activity = ActivityLocation.objects.create(name="Hiking Trail", activity_type='outdoor', latitude=40.7128, longitude=-74.0060, approved=True)
        restaurant = RestaurantLocation.objects.create(name="Golden Dragon", restaurant_type='Chinese', latitude=40.7130, longitude=-74.0070, approved=True)
        gas_station = GasStationLocation.objects.create(name="Main Street Gas", latitude=40.7140, longitude=-74.0080, approved=True)

        # Create an itinerary for the test user
        Itinerary.objects.create(
            user=self.user,
            activity=activity,
            restaurant=restaurant,
            gas_station=gas_station,
            activity_duration_hours=2,
            activity_duration_minutes=30,
            restaurant_duration_hours=1,
            restaurant_duration_minutes=45,
            gas_station_duration_minutes=15,
        )

    def test_display_itinerary_with_existing_itinerary(self):
        response = self.client.get(reverse('users:itinerary'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'itinerary.html')
        self.assertIn('itinerary', response.context)
        self.assertEqual(response.context['itinerary'], Itinerary.objects.filter(user=self.user).last())

    def test_display_itinerary_with_no_itinerary(self):
        Itinerary.objects.filter(user=self.user).delete()
        response = self.client.get(reverse('users:itinerary'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'itinerary.html')
        self.assertIn('itinerary', response.context)  
        self.assertIsNone(response.context['itinerary']) 
        self.assertIn('message', response.context)



######################Test Submit Propostion################################
class SubmitReviewTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.force_login(self.user)

    def test_valid_activity_submission(self):
        form_data = {
            'name': 'Eat at Ohill',
            'location_type': 'activity',
            'activity_type': 'outdoor',
            'latitude': 4.2328,
            'longitude': 32.1260
        }
        response = self.client.post(reverse('users:submit_review'), form_data)
        self.assertEqual(response.status_code, 302) 
        self.assertTrue(ActivityLocation.objects.filter(name='Eat at Ohill').exists())

    def test_valid_restaurant_submission(self):
        form_data = {
            'name': 'French Restaurant',
            'location_type': 'restaurant',
            'restaurant_type': 'French',
            'latitude': 43.3228,
            'longitude': -71.1260
        }
        response = self.client.post(reverse('users:submit_review'), form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(RestaurantLocation.objects.filter(name='French Restaurant').exists())


    def test_invalid_form_submission(self):
        form_data = {
            'name': '',  
            'location_type': 'activity',
            'activity_type': 'outdoor',
            'latitude': 40.7128,
            'longitude': -74.0060
        }
        response = self.client.post(reverse('users:submit_review'), form_data)
        self.assertNotEqual(response.status_code, 302)
        self.assertFalse(ActivityLocation.objects.filter(latitude=40.7128, longitude=-74.0060).exists())

    def test_form_display_on_get_request(self):
        response = self.client.get(reverse('users:submit_review'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_location_form.html')


#####################Test Admin Approve the proposition#######################
class AdminApproveTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')

        self.admin_user = User.objects.create_user(username='adminuser', password='admin12345', is_admin_user=True)

        self.client = Client()

        ActivityLocation.objects.create(name="Unapproved Activity", activity_type='outdoor', latitude=11.7128, longitude=-12.0060, approved=False)
        RestaurantLocation.objects.create(name="Unapproved Restaurant", restaurant_type='American', latitude=13.7130, longitude=-14.0070, approved=False)

    def test_admin_can_approve_location(self):
        self.client.force_login(self.admin_user)
        activity = ActivityLocation.objects.get(name="Unapproved Activity")

        response = self.client.post(reverse('users:admin_approve_reviews'), {
            'location_id': activity.id,
            'location_type': 'activity',
            'action': 'approve'
        })

        activity.refresh_from_db()
        self.assertTrue(activity.approved)
        self.assertEqual(response.status_code, 302)

    def test_admin_can_delete_location(self):
        self.client.force_login(self.admin_user)
        restaurant = RestaurantLocation.objects.get(name="Unapproved Restaurant")

        response = self.client.post(reverse('users:admin_approve_reviews'), {
            'location_id': restaurant.id,
            'location_type': 'restaurant',
            'action': 'delete'
        })

        self.assertFalse(RestaurantLocation.objects.filter(id=restaurant.id).exists())
        self.assertEqual(response.status_code, 302)

#######################Test All Locations########################
class AllLocationsViewTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()
        self.client.force_login(self.user)

        activity = ActivityLocation.objects.create(name="Hiking Trail", activity_type='outdoor', latitude=40.7128, longitude=-74.0060, approved=True)
        restaurant = RestaurantLocation.objects.create(name="Golden Dragon", restaurant_type='Chinese', latitude=40.7130, longitude=-74.0070, approved=True)
        gas_station = GasStationLocation.objects.create(name="Main Street Gas", latitude=40.7140, longitude=-74.0080, approved=True)

        Itinerary.objects.create(
            user=self.user,
            activity=activity,
            restaurant=restaurant,
            gas_station=gas_station,
            activity_duration_hours=2,
            activity_duration_minutes=30,
            restaurant_duration_hours=1,
            restaurant_duration_minutes=45,
            gas_station_duration_minutes=15,
        )
        
    def test_default_behavior(self):
        response = self.client.get(reverse('users:all_locations'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['activity_locations']), ActivityLocation.objects.count())
        self.assertEqual(len(response.context['restaurant_locations']), RestaurantLocation.objects.count())
        self.assertEqual(len(response.context['gas_station_locations']), GasStationLocation.objects.count())
        self.assertTemplateUsed(response, 'all_locations.html')

    def test_filter_by_activity(self):
        response = self.client.get(reverse('users:all_locations') + '?filter_by=activity')
        self.assertEqual(response.status_code, 200)
        #Check only present the activity location but not restarurant locations and gas stations
        self.assertGreater(len(response.context['activity_locations']), 0)
        self.assertEqual(len(response.context['restaurant_locations']), 0)
        self.assertEqual(len(response.context['gas_station_locations']), 0)

    def test_filter_by_restaurant(self):
        response = self.client.get(reverse('users:all_locations') + '?filter_by=restaurant')
        self.assertEqual(response.status_code, 200)

        self.assertGreater(len(response.context['restaurant_locations']), 0)
        self.assertEqual(len(response.context['activity_locations']), 0)
        self.assertEqual(len(response.context['gas_station_locations']), 0)

    def test_filter_by_restaurant(self):
        response = self.client.get(reverse('users:all_locations') + '?filter_by=gas_station')
        self.assertEqual(response.status_code, 200)

        self.assertGreater(len(response.context['gas_station_locations']), 0)
        self.assertEqual(len(response.context['activity_locations']), 0)
        self.assertEqual(len(response.context['restaurant_locations']), 0)

###############################Test Admin Approve Admin######################################
class AdminApproveAdminTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        User = get_user_model()
        self.admin_user = User.objects.create_user(username='adminuser', email='admin@example.com', password='12345', is_admin_user=True)
        self.non_admin_user = User.objects.create_user(username='nonadmin', email='nonadmin@example.com', password='12345', is_admin_user=False)
        self.client.force_login(self.admin_user)

    def test_successful_admin_promotion(self):
        form_data = {'user_email': self.non_admin_user.email}
        response = self.client.post(reverse('users:admin_approve_admin'), form_data)
        self.non_admin_user.refresh_from_db()
        self.assertTrue(self.non_admin_user.is_admin_user)
        
    def test_promotion_of_existing_admin(self):
        form_data = {'user_email': self.admin_user.email}
        response = self.client.post(reverse('users:admin_approve_admin'), form_data)
        messages_list = list(get_messages(response.wsgi_request))
        messages_str = [message.message for message in messages_list]
        self.assertIn('User is already an admin!', messages_str)

    def test_nonexistent_user_promotion(self):
        form_data = {'user_email': 'nonexistent@example.com'}
        response = self.client.post(reverse('users:admin_approve_admin'), form_data)

        messages_list = list(get_messages(response.wsgi_request))
        messages_str = [message.message for message in messages_list]

        self.assertIn('No such user exists!', messages_str)
