from django.db import models
from users.models import Student

class Tournament(models.Model):
	name = models.CharField(max_length=100)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	registered_students = models.ManyToManyField(Student)
	places = models.PositiveSmallIntegerField()
	location = models.CharField(max_length=500)

class TournamentResult(models.Model):
	tournament = models.ForeignKey('Tournament')
	student = models.ForeignKey('users.Student')
	place = models.PositiveSmallIntegerField()