from django.core.management.base import BaseCommand
from users.models import Student
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Populates DB with fake students. Sets all passwords to: "password"'

    def handle(self, *args, **options):
        users = [
            ['test1', 'John', 'Doe', 'test1@gmail.com'],
            ['test2', 'Jane', 'Dame', 'test2@gmail.com'],
            ['test3', 'Jacob', 'Dacob', 'test3@gmail.com'],
        ]

        g = Group.objects.get(name='student_group')

        for u in users:
            user = User(username=u[0], first_name=u[1], last_name=u[2], email=u[3])
            user.set_password('password')
            user.save()
            student = Student(user=user)
            student.save()
            g.user_set.add(user)