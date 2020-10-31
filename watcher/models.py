from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    occupationCount = models.IntegerField(default=0)
    healthContact = models.CharField(max_length=250, null=True)
    policeContact = models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

    def saveNeighborhood(self):
        self.save()

    def deleteNeighborhood(self):
        self.delete()

    @classmethod
    def findNeighborhoodById(cls, pk):
        try:
            neighborhoodObject = Neighborhood.objects.get(id=pk)
            return neighborhoodObject
        except ObjectDoesNotExist:
            message = "Neighborhood does not exist"
            return message

    @classmethod
    def updateNeighborhood(cls, pk, newName, newLocation):
        neighUpdate = cls.findNeighborhoodById(pk)

        if neighUpdate:
            Neighborhood.objects.filter(id=pk).update(
                name=newName, location=newLocation
            )
        else:
            message = "Neighborhood does not exist"
            return message

    @classmethod
    def updateOccupantsCount(cls, pk, newOccCount):
        occupants = cls.findNeighborhoodById(pk)

        if occupants:
            Neighborhood.objects.filter(id=pk).update(occupationCount=newOccCount)
        else:
            message = "Neighborhood does not exist"
            return message


class Profile(models.Model):
    image = CloudinaryField("image", null=True, blank=True)
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, on_delete=CASCADE)  # set user to admin
    neighborhood = models.ForeignKey(Neighborhood, null=True, on_delete=CASCADE)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.name

    def saveProfile(self):
        self.save()

    def deleteProfile(self):
        self.delete()

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


class Business(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, on_delete=CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, null=True, on_delete=CASCADE)
    email = models.EmailField(max_length=150)

    def __str__(self):
        self.name

    def saveBusniess(self):
        self.save()

    def deleteBusiness(self):
        self.delete()

    @classmethod
    def findBusinessById(cls, pk):
        try:
            businessObject = Business.objects.get(id=pk)
            return businessObject
        except ObjectDoesNotExist:
            message = "Business does not exist"
            return message

    @classmethod
    def updateBusiness(cls, pk, newName, newEmail):
        businessUpdate = cls.findBusinessById(pk)

        if businessUpdate:
            Business.objects.filter(id=pk).update(name=newName, email=newEmail)
        else:
            message = "Business does not exist"
            return message
