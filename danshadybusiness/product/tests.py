from django.test import TestCase
from product.models import Car, CarReservation, CustomUser
from django.contrib.auth.models import User


class CarTestCase(TestCase):
    def setUp(self):
        Car.objects.create(name="Mustang",price=100.0)
        Car.objects.create(name="Rio",price=50.0)
        rio = Car.objects.get(name = "Rio")


    def test_car_price(self):
        mustang = Car.objects.get(name = "Mustang")
        rio = Car.objects.get(name="Rio")
        self.assertEqual(mustang.price,100.0)
        self.assertEqual(rio.price,50.0)
        self.assertNotEqual(rio.price,100.0)
    
    def test_car_reservation(self):
        mustang = Car.objects.get(name = "Mustang")
        rio = Car.objects.get(name="Rio")
        self.assertEqual(0,len(mustang.carreservation_set.all()))
        self.assertEqual(0,len(rio.carreservation_set.all()))
        self.assertNotEqual(1,len(rio.carreservation_set.all()))

    
    def test_car_name(self):
        mustang = Car.objects.get(name = "Mustang")
        rio = Car.objects.get(name="Rio")
        self.assertEqual("Mustang",mustang.name)
        self.assertEqual("Rio",rio.name)
        self.assertNotEqual("Rio",mustang.name)





class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(email = "michael@gmail.com", first_name = "Michael", last_name = "Hanks", password = "1234", username = "michael")
        User.objects.create(email = "test@gmail.com", first_name = "Test", last_name = "Test", password = "test", username = "test")

    def testCustomUser(self):
        user1 = User.objects.get(email = "michael@gmail.com")
        user2 = CustomUser.objects.get(user = user1)
        self.assertEqual(0, user2.balance)
        user2.addFunds(-5.0)
        user2.save()
        self.assertNotEqual(0,user2.balance)
        self.assertGreater(0,user2.balance)


    def testPassword(self):
        user1 = User.objects.get(email = "michael@gmail.com")
        user2 = User.objects.get(email = "test@gmail.com")
        self.assertNotEqual(user1.password, user2.password)
        self.assertEqual("1234", user1.password)
        self.assertEqual("test", user2.password)



        

# Create your tests here.
