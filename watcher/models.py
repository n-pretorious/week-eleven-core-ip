from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    occupationCount = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def saveNeighborhood(self):
        self.save()

    def deleteNeighborhood(self):
        self.delete()


class Profile(models.Model):
    image = CloudinaryField("image", null=True)
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