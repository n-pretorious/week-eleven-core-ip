from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User

# Create your models here.
class Neighborhood(models.Model):
  name = models.CharField(max_length=150)
  location = models.CharField(max_length=100)
  occupationCount = models.IntegerField()

class Profile(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, null=True, on_delete=CASCADE) # set user to admin
    neighborhood = models.ForeignKey(Neighborhood, null=True, on_delete=CASCADE)
    email = models.EmailField(max_length=250)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})
