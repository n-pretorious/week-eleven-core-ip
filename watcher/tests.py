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
        
    def testFindNeighborhoodById(self):
        neighborhood = Neighborhood.findNeighborhoodById(self.neighborhood.pk)
        self.assertEqual(neighborhood, self.neighborhood)
        
    def testUpdateNeighborhood(self):
        newName = 'Place C'
        newLocation = 'Inside place C'
        
        Neighborhood.updateNeighborhood(self.neighborhood.id, newName, newLocation)
        updatedNeighborhood = Neighborhood.findNeighborhoodById(self.neighborhood.id)
        self.assertEqual(updatedNeighborhood.name,'Place C')
        self.assertEqual(updatedNeighborhood.location,'Inside place C')
        
    def testUpdateOccupants(self):
        newCount = 10
        
        Neighborhood.updateOccupantsCount(self.neighborhood.id, newCount)
        updatedNeighborhood = Neighborhood.findNeighborhoodById(self.neighborhood.id)
        self.assertEqual(updatedNeighborhood.occupationCount, 10)


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
        
    def testFindBusinessById(self):
        business = Business.findBusinessById(self.business.pk)
        self.assertEqual(business, self.business)
        
    def testUpdateBusiness(self):
        newName = 'Ooliskia Wapi'
        newEmail = 'nimeskia@business.com'
        
        Business.updateBusiness(self.business.id, newName, newEmail)
        updatedBusiness = Business.findBusinessById(self.business.id)
        self.assertEqual(updatedBusiness.name, 'Ooliskia Wapi')
        self.assertEqual(updatedBusiness.email, 'nimeskia@business.com')