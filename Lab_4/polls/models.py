from django.db import models

from polls.constants import INSURANCE_TYPE, OBJECT_TYPE
from MyAuth.models import User


# Create your models here.


class Office(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=50)
	phone = models.CharField(max_length=13)


class Insurance(models.Model):
	insurance_type = models.CharField(
		max_length=20,
		default="GEN",
		choices=INSURANCE_TYPE
	)
	minimal_cost = models.IntegerField()
	duration = models.DurationField()
	percentage = models.FloatField()


class Object(models.Model):
	object_type = models.CharField(
		max_length=20,
		choices=OBJECT_TYPE
	)
	description = models.TextField()


class Agent(models.Model):
	office = models.ForeignKey(
		to=Office,
		null=True,
		on_delete=models.SET_NULL,
	)
	user = models.OneToOneField(
		to=User,
		limit_choices_to={"is_staff": True},
		null=True,
		on_delete=models.CASCADE,

	)

	def __str__(self):
		return f'[#{self.id}] {self.user.name + " " + self.user.surname}'


class Contract(models.Model):
	client = models.ForeignKey(
		to=User,
		on_delete=models.CASCADE,
	)
	agent = models.ForeignKey(
		to=Agent,
		null=True,
		on_delete=models.SET_NULL,
	)
	insurance = models.ForeignKey(
		to=Insurance,
		null=True,
		on_delete=models.SET_NULL,
	)
	object = models.OneToOneField(
		to=Object,
		on_delete=models.CASCADE,
	)
	sign_date = models.DateTimeField(auto_now=True)
	cost = models.CharField(max_length=60)
