from django.core.management.base import BaseCommand
from users.models import Member, Sponsor
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Populates DB with fake members and sponsors. Sets all passwords to: "password"'

    def handle(self, *args, **options):
        members = [
            ['member1', 'John', 'Doe', 'test1@gmail.com'],
            ['member2', 'Jane', 'Dame', 'test2@gmail.com'],
            ['member3', 'Jacob', 'Dacob', 'test3@gmail.com'],
        ]

        sponsors = [
            ['sponsor1', 'John', 'DoeSponsor', 'sponsor1@gmail.com', 'Google'],
            ['sponsor2', 'Jane', 'DameSponsor', 'sponsor2@gmail.com', 'Myspace'],
            ['sponsor3', 'Jacob', 'DacobSponsor', 'sponsor3@gmail.com', 'Facebook'],
        ]

        g = Group.objects.get(name='member_group')

        for u in members:
            user = User(username=u[0], first_name=u[1], last_name=u[2], email=u[3])
            user.set_password('password')
            user.save()
            member = Member(user=user)
            member.save()
            g.user_set.add(user)

        g = Group.objects.get(name='sponsor_group')

        for u in sponsors:
            user = User(username=u[0], first_name=u[1], last_name=u[2], email=u[3])
            user.set_password('password')
            user.save()
            sponsor = Sponsor(user=user, home_page_url='http://www.google.com', company_name=u[4])
            sponsor.save()
            g.user_set.add(user)