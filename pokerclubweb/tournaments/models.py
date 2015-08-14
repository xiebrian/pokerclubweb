from django.db import models
from users.models import Student

class Tournament(models.Model):
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	registered_students = models.ManyToManyField(Student)
	location = models.TextField()

class TournamentResult(models.Model):
	tournament = models.ForeignKey('Tournament')
	student = models.ForeignKey('users.Student')
	place = models.PositiveSmallIntegerField()