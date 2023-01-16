from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Food(models.Model):
    fid = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=500)
    calories = models.FloatField()
    protein = models.FloatField()
    carbs = models.FloatField()
    def __str__(self):
        return self.item_name
    
    
class Activities(models.Model):
    aid = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=500)
    burnout_cal = models.CharField(max_length=25)
    def __str__(self):
        return self.activity_name
    
class UserFood(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    fooditem = models.ForeignKey(Food,on_delete=models.CASCADE)
    fintake = models.FloatField()
    activity = models.ForeignKey(Activities,on_delete=models.CASCADE)
    ahours = models.CharField(max_length=25)
    def __str__(self):
        return self.user.username