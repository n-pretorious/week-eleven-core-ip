from watcher.models import Business, Neighborhood, Profile
from django.test import TestCase

# Create your tests here.
class TestNeighborhood(TestCase):
    def setUp(self):
        self.neighborhood = Neighborhood(
            name="Place A", location="Inside place A", occupationCount=0
        )

        self.neighborhood.save()

    def testInstance(self):
        self.assertIsInstance(self.neighborhood, Neighborhood)

    def testNeighborhoodSave(self):
        self.neighborhood.saveNeighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) > 0)

    def testNeighborhoodSave(self):
        self.neighborhood.saveNeighborhood()
        self.neighborhood.deleteNeighborhood()
        neighborhood = Neighborhood.objects.all()
        self.assertTrue(len(neighborhood) == 0)


class TestProfile(TestCase):
    def setUp(self):
        self.profile = Profile(
            image="image.jpeg",
            name="User A",
            # user =
            # neighborhood=Neighborhood(
            #     name="Place B", location="Inside place B", occupationCount=0
            # ),
            email="usera@test.com",
        )

        self.profile.save()

    def testInstance(self):
        self.assertIsInstance(self.profile, Profile)

    def testProfileSave(self):
        self.profile.saveProfile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def testProfileDelete(self):
        self.profile.saveProfile()
        self.profile.deleteProfile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) == 0)


class TestBusiness(TestCase):
    def setUp(self):
        self.business = Business(
            name="Best business in town", email="emailus@business.com"
        )

        self.business.save()

    def testInstance(self):
        self.assertIsInstance(self.business, Business)

    def testBusinessSave(self):
        self.business.saveBusniess()
        business = Business.objects.all()
        self.assertTrue(len(business) > 0)

    def testBusinessDelete(self):
        self.business.saveBusniess()
        self.business.deleteBusiness()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)