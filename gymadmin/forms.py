from django import forms
from gyms.models import Gym,User
from django.core.exceptions import ValidationError

class GymForm(forms.Form):
	name=forms.CharField(max_length=200)
	location=forms.CharField(max_length=200)
	price=forms.IntegerField(label="average cost")
	rating=forms.IntegerField()
	summary=forms.CharField(widget=forms.Textarea)
	featured_photos=forms.ImageField(required=False)
	user=forms.IntegerField()

	def clean_price(self):
		price=self.cleaned_data['price']
		if price<200:
			raise ValidationError("price cant be less than {}.".format(price))
		return price

	def clean_user(self):
		user_id=self.cleaned_data['user']
		user=User.objects.filter(pk=user_id).first()

		return user

	def save(self):
		gym=Gym.objects.create(
			name= self.cleaned_data["name"],
			location= self.cleaned_data["location"],
			price= self.cleaned_data["price"],
			rating= self.cleaned_data["rating"],
			summary= self.cleaned_data["summary"],
			featured_photos= self.cleaned_data["featured_photos"],
			user= self.cleaned_data["user"],)
		return gym