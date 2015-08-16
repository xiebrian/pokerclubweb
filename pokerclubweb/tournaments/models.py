from django.db import models
from users.models import Student
from django.core.exceptions import ValidationError

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    registered_students = models.ManyToManyField(Student, blank=True)
    places = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=500)
    results_available = models.BooleanField(default=False)

    def clean_fields(self, exclude=None):
        if self.start_time > self.end_time:
            raise ValidationError({'end_time': ['End time must be after start time',]})
        if self.places < 1:
            raise ValidationError({'places': ['Places must be at least 1',]})

    def __unicode__(self):
        return self.name

class TournamentResult(models.Model):
    tournament = models.ForeignKey('Tournament')
    student = models.ForeignKey('users.Student', blank=True, null=True)
    place = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = (('tournament', 'place'),('tournament','student'))

    def __unicode__(self):
        return self.intToWord(self.place) + ' place for ' + self.tournament.name

    @staticmethod
    def intToWord(num):
        value = str(num)
        if (len(value) > 1):
            # Check for special case: 11 - 13 are all "th".
            # So if the second to last digit is 1, it is "th".
            secondToLastDigit = value[-2]
            if(secondToLastDigit == '1'):
                return value + "th"

        lastDigit = value[-1]
        if lastDigit == '1':
            suffix = "st"
        elif lastDigit == '2':
            suffix = "nd"
        elif lastDigit == '3':
            suffix = "rd"
        else:
            suffix = "th"
        
        return value + suffix