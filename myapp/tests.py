from django.test import TestCase,Client

# Create your tests here.
from .models import Airport, Flight

class FlightTestCase(TestCase):
    def setUp(self):
        a1 = Airport.objects.create(code="AAA", city="Addis Ababa")
        a2 = Airport.objects.create(code="BBB", city="Bangalore")

        Flight.objects.create(origin=a1, destination=a2, duration=100)
        Flight.objects.create(origin=a1, destination=a1, duration=200)
        Flight.objects.create(origin=a1, destination=a2, duration=-100)  

    def test_departures_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.departures.count(), 3)  
    def test_arrivals_count(self):
        a = Airport.objects.get(code="AAA")
        self.assertEqual(a.arrivals.count(), 1) 

    def test_valid_flight(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = Flight.objects.get(origin=a1, destination=a2, duration=100)
        self.assertTrue(f.is_valid_flight())

    def test_invalid_flight_same_origin_destination(self):
        a1 = Airport.objects.get(code="AAA")
        f = Flight.objects.get(origin=a1, destination=a1, duration=200)
        self.assertFalse(f.is_valid_flight())

    def test_invalid_flight_negative_duration(self):
        a1 = Airport.objects.get(code="AAA")
        a2 = Airport.objects.get(code="BBB")
        f = Flight.objects.get(origin=a1, destination=a2, duration=-100)
        self.assertFalse(f.is_valid_flight())

    def test_index(self):
        c =  Client()
        response = c.get("/")

        self.assertEqual(response.status_code,200)

    def test_login(self):
        c = Client()
        response = c.post("/login",{
            "username":"seif",
            "password":"123"
        })
        self.assertEqual(response.status_code,200)
        
    def test_about(self):
        c = Client()
        response = c.get("/about")
        self.assertTemplateUsed(response,"myapp/about.html")

 
