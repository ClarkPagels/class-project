from django.core.management.base import BaseCommand
from users.models import ActivityLocation, RestaurantLocation, GasStationLocation


class Command(BaseCommand):
    help = 'Populate activity and restaurant locations'

    def handle(self, *args, **options):
    # Activity
        # outdoors
        ActivityLocation.objects.create(
            name='Humpback Rocks Hike',
            activity_type='outdoor',
            latitude=37.96206823808959,
            longitude=-78.90074052452255,
            approved=True,
        )
        ActivityLocation.objects.create(
            name='Rivanna River Company',
            activity_type='outdoor',
            latitude=38.033290514649785,
            longitude=-78.4607027,
            approved=True,
        )
        ActivityLocation.objects.create(
            name='Birdwood Golf Course',
            activity_type='outdoor',
            latitude=38.044620171100256,
            longitude=-78.53571636746909,
            approved=True,
        )
        ActivityLocation.objects.create(
            name='Shenandoah National Park',
            activity_type='outdoor',
            latitude=38.50339140884468,
            longitude=-78.46452311533002,
            approved=True,
        )
        ActivityLocation.objects.create(
            name='Carter Mountain Orchard',
            activity_type='outdoor',
            latitude=37.991531646716155,
            longitude=-78.47198380111676,
            approved=True,
        )
        ActivityLocation.objects.create(
            name='Chiles Peach Orchard and Farm Market',
            activity_type='outdoor',
            latitude=38.06738265870473,
            longitude=-78.74716855878468,
            approved=True,
        )
        ActivityLocation.objects.create(
            name='Farmers Market at Ix',
            activity_type='outdoor',
            latitude=38.02648805119073,
            longitude=-78.482199416457,
            approved=True,
        )
        ActivityLocation.objects.create(
            name='Brookhill Farm',
            activity_type='outdoor',
            latitude=37.98062996037535,
            longitude=-78.50759812883537,
            approved=True,
        )
        ActivityLocation.objects.create(
            name='Pippin Hill Farm & Vineyards',
            activity_type='outdoor',
            latitude= 37.96232612851903,
            longitude= -78.65802662329213,
            approved=True,
        )


        # indoor

        ActivityLocation.objects.create(
            name='The Fralin Museum of Art',
            activity_type='indoor',
            latitude=38.03845497217195,
            longitude=-78.50307710481056,
            approved=True,
        )
        ActivityLocation.objects.create(
            name='The Jefferson Theater',
            activity_type='indoor',
            latitude=38.0303510322972,
            longitude=-78.48145026248153,
            approved=True,
        )
        ActivityLocation.objects.create(
            name='The Paramount Theater',
            activity_type='indoor',
            latitude=38.03077909718068,
            longitude=-78.48022875878603,
            approved=True,
        )
        ActivityLocation.objects.create(
            name='Cville Escape Room',
            activity_type='indoor',
            latitude=38.029872291978414,
            longitude=-78.47903351830455,
            approved=True,
        )
        ActivityLocation.objects.create(
            name='Lazy Daisy Ceramics',
            activity_type='indoor',
            latitude=38.0161066659408,
            longitude=-78.4735731722803,
            approved=True,
        )


        # educational

        ActivityLocation.objects.create(
            name='Monticello',
            activity_type='educational',
            latitude= 38.00883251461374,
            longitude=-78.4533281489885,
            approved=True,
        )
        ActivityLocation.objects.create(
            name="James Monroe's Highland",
            activity_type='educational',
            latitude=37.98256180108842,
            longitude=-78.45519439742162,
            approved=True,
        )
        ActivityLocation.objects.create(
            name="James Madison's Montpelier",
            activity_type='educational',
            latitude=38.22087827936911,
            longitude=-78.16910711042243,
            approved=True,
        )
        ActivityLocation.objects.create(
            name='Albemarle Charlottesville Historical Society',
            activity_type='educational',
            latitude=38.03193913028156,
            longitude=-78.47999356063373,
            approved=True,
        )


    # Restaurants
        # chinese

        RestaurantLocation.objects.create(
            name='Bang!',
            restaurant_type='Chinese',
            latitude=38.02988974092799,
            longitude=-78.48309957597536,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Marco and Luca Dumplings',
            restaurant_type='Chinese',
            latitude=38.03500281889974,
            longitude=-78.48284631130494,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Peter Chang',
            restaurant_type='Chinese',
            latitude=38.055425377194396,
            longitude=-78.50055513179743,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Taste of China',
            restaurant_type='Chinese',
            latitude=38.124796650596025,
            longitude=-78.45748256227067,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Oriental Express',
            restaurant_type='Chinese',
            latitude=38.14181048521896,
            longitude=-78.43181763951623,
            approved=True,
        )


        # italian

        RestaurantLocation.objects.create(
            name='Tavola',
            restaurant_type='Italian',
            latitude=38.02492899556737,
            longitude=-78.4753775260531,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Vivace',
            restaurant_type='Italian',
            latitude=38.04501571219638,
            longitude=-78.51796167782257,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name="Carmello's",
            restaurant_type='Italian',
            latitude=38.077507682002384,
            longitude=-78.48039510480896,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Luce',
            restaurant_type='Italian',
            latitude=38.03154338322116,
            longitude=-78.4820127606338,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Orzo',
            restaurant_type='Italian',
            latitude=38.03062544488111,
            longitude=-78.4871432857737,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Mona Lisa',
            restaurant_type='Italian',
            latitude=38.03860739989263,
            longitude=-78.4899109711646,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name="Sal's Caffe Italia",
            restaurant_type='Italian',
            latitude=38.03058578292124,
            longitude=-78.4802227183046,
            approved=True,
        )


        # japanese

        RestaurantLocation.objects.create(
            name='Ten',
            restaurant_type='Japanese',
            latitude=38.03059168660791,
            longitude=-78.48098894529221,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Now and Zen',
            restaurant_type='Japanese',
            latitude=38.03229329526113,
            longitude=-78.48168903179827,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Mashumen',
            restaurant_type='Japanese',
            latitude=38.025859355668416,
            longitude=-78.51594698762156,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Kuma Sushi Noodles & Bar',
            restaurant_type='Japanese',
            latitude=38.036303654946295,
            longitude=-78.50026708650618,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Kabuto Sushi & Teppanyaki',
            restaurant_type='Japanese',
            latitude=38.03023844016363,
            longitude=-78.44678163179843,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Sakura Japanese Steakhouse',
            restaurant_type='Japanese',
            latitude=38.13765546370575,
            longitude=-78.44273170648448,
            approved=True,
        )


        # french

        RestaurantLocation.objects.create(
            name='Petit Pois',
            restaurant_type='French',
            latitude=38.030899944089256,
            longitude=-78.48042695878604,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='The Alley Light',
            restaurant_type='French',
            latitude=38.0305892338391,
            longitude=-78.48233697412753,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Fleurie Restaurant',
            restaurant_type='French',
            latitude=39.40219546647638,
            longitude=-78.3918262708483,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Bizou',
            restaurant_type='French',
            latitude=38.03125412028822,
            longitude=-78.48207051534158,
            approved=True,
        )


        # american

        RestaurantLocation.objects.create(
            name='Fitzroy',
            restaurant_type='American',
            latitude=38.03060283014061,
            longitude=-78.48099027597533,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Tavern & Grocery',
            restaurant_type='American',
            latitude=38.03091908778119,
            longitude=-78.48635400296298,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='The Local',
            restaurant_type='American',
            latitude=38.115399970231024,
            longitude=-78.50294366175801,
            approved = True,
        )
        RestaurantLocation.objects.create(
            name='The Virginian',
            restaurant_type='American',
            latitude=38.03543045465599,
            longitude=-78.50072664417696,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Sedona Taphouse',
            restaurant_type='American',
            latitude=38.051299813318465,
            longitude=-78.50570342883539,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Burtons Grill & Bar',
            restaurant_type='American',
            latitude=38.064418500343706,
            longitude=-78.49032228762016,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Matchbox Charlottesville',
            restaurant_type='American',
            latitude=38.06512246366355,
            longitude=-78.49232852810155,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='The Ridley',
            restaurant_type='American',
            latitude=38.032749133302346,
            longitude=-78.4962047569382,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Citizen Burger Bar',
            restaurant_type='American',
            latitude=38.030300634271676,
            longitude=-78.48043217412767,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='The Whiskey Jar',
            restaurant_type='American',
            latitude=38.03153048324202,
            longitude=-78.48282147597523,
            approved=True,
        )


        # indian

        RestaurantLocation.objects.create(
            name='Kanak Indian Kitchen',
            restaurant_type='Indian',
            latitude=38.01182756197498,
            longitude=-78.4989681624823,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Milan Indian Restaurant',
            restaurant_type='Indian',
            latitude=38.06072255905109,
            longitude=-78.49326675582304,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Himalayan Fusion',
            restaurant_type='Indian',
            latitude=38.02963448011732,
            longitude=-78.47801364714007,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Maharaja Fine Indian Cuisine',
            restaurant_type='Indian',
            latitude=38.064494812056914,
            longitude=-78.48879309131564,
            approved=True,
        )


        # middle-eastern

        RestaurantLocation.objects.create(
            name='Sultan Kebab',
            restaurant_type='Middle-Eastern',
            latitude=38.02863196715175,
            longitude=-78.48146460369551,
            approved=True,
        )

        RestaurantLocation.objects.create(
            name='Mezeh Mediterranean Grill',
            restaurant_type='Middle-Eastern',
            latitude=38.096487772844355,
            longitude=-78.471937898549,
            approved=True,
        )

        RestaurantLocation.objects.create(
            name='Afghan Kabob Cville',
            restaurant_type='Middle-Eastern',
            latitude=38.11721950189223,
            longitude=-78.50495404314968,
            approved=True,
        )

        RestaurantLocation.objects.create(
            name='Aromas Cafe',
            restaurant_type='Middle-Eastern',
            latitude=38.02232402618823,
            longitude=-78.53146666746909,
            approved=True,
        )

        RestaurantLocation.objects.create(
            name='Sticks Kebob Shop',
            restaurant_type='Middle-Eastern',
            latitude=38.034003479785454,
            longitude=-78.44765965248027,
            approved=True,
        )

        #spanish

        RestaurantLocation.objects.create(
            name='Asados Wing & Taco Company',
            restaurant_type='Spanish',
            latitude=38.09015869127431,
            longitude=-78.55946134408805,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Mas',
            restaurant_type='Spanish',
            latitude=38.11434018221365,
            longitude=-78.4770954797293,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Zocalo',
            restaurant_type='Spanish',
            latitude=38.030960789466704,
            longitude=-78.4803217606337,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Bebedero',
            restaurant_type='Spanish',
            latitude=38.03123943116962,
            longitude=-78.48234327597534,
            approved=True,
        )
        RestaurantLocation.objects.create(
            name='Guajiros Miami Eatery',
            restaurant_type='Spanish',
            latitude=38.03204818240579,
            longitude=-78.49123894713989,
            approved=True,
        )

    # Gas


        GasStationLocation.objects.create(
            name='Exxon Gas Station',
            latitude=38.03632538920231,
            longitude=-78.48585014917121,
            approved=True,
        )

        GasStationLocation.objects.create(
            name='Citgo',
            latitude=38.03929981629366,
            longitude=-78.48155861477478,
            approved=True,
        )

        GasStationLocation.objects.create(
            name='BP',
            latitude=38.028960453838856,
            longitude=-78.49475071175523,
            approved=True,
        )

        self.stdout.write(self.style.SUCCESS('Locations have been populated.'))
