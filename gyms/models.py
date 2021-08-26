from django.db import models

# Create your models here.
class User(models.Model):
	full_name=models.CharField(max_length=200)
	username=models.CharField(max_length=200,unique=True)
	email=models.CharField(default="",max_length=200,unique=True)
	phone_number=models.CharField(default="",max_length=200)
	address=models.CharField(default="",max_length=200)
	pan_vat_number=models.CharField(default="",max_length=200)
	password=models.CharField(max_length=200)
	user_type=models.IntegerField(default=0)
	status=models.CharField(max_length=40)
	token=models.CharField(default="",max_length=200)
	profile_complete = models.IntegerField(default=0)
	image = models.ImageField(default="")

class Gym(models.Model):
	name=models.CharField(max_length=200)
	location=models.CharField(max_length=200)
	price=models.IntegerField()
	rating=models.IntegerField()
	summary=models.TextField()
	featured_photos=models.CharField(max_length=200,blank=True,null=True)

	user=models.ForeignKey(User,on_delete=models.CASCADE)

class UserGymRating(models.Model):
	review=models.TextField()
	rating=models.IntegerField()
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	gym=models.ForeignKey(Gym,on_delete=models.CASCADE)
		


	
	
	


