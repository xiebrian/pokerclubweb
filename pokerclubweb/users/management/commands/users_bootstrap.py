from django.core.management.base import BaseCommand
from users.models import Student, Sponsor
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Populates DB with fake students and sponsors. Sets all passwords to: "password"'

    def handle(self, *args, **options):
        students = [
            ['student1', 'John', 'Doe', 'test1@gmail.com'],
            ['student2', 'Jane', 'Dame', 'test2@gmail.com'],
            ['student3', 'Jacob', 'Dacob', 'test3@gmail.com'],
        ]

        sponsors = [
            ['sponsor1', 'John', 'DoeSponsor', 'sponsor1@gmail.com'],
            ['sponsor2', 'Jane', 'DameSponsor', 'sponsor2@gmail.com'],
            ['sponsor3', 'Jacob', 'DacobSponsor', 'sponsor3@gmail.com'],
        ]

        g = Group.objects.get(name='student_group')

        for u in students:
            user = User(username=u[0], first_name=u[1], last_name=u[2], email=u[3])
            user.set_password('password')
            user.save()
            student = Student(user=user)
            student.save()
            g.user_set.add(user)

        g = Group.objects.get(name='sponsor_group')

        for u in sponsors:
            user = User(username=u[0], first_name=u[1], last_name=u[2], email=u[3])
            user.set_password('password')
            user.save()
            sponsor = Sponsor(user=user, logo='img/profile_default.png', home_page_url='http://www.google.com')
            sponsor.save()
            g.user_set.add(user)