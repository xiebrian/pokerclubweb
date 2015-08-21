from django.core.management.base import BaseCommand
from users.models import Member, Sponsor, Admin
from django.contrib.auth.models import User, Group

class Command(BaseCommand):
    help = 'Populates DB with fake members and sponsors. Sets all passwords to: "password"'

    def handle(self, *args, **options):
        members = [
            ['member1', 'John', 'Doe', 'test1@gmail.com'],
            ['member2', 'Jane', 'Dame', 'test2@gmail.com'],
            ['member3', 'Jacob', 'Dacob', 'test3@gmail.com'],
        ]

        admins = [
            ['admin1', 'John', 'Doe', 'test1@gmail.com', 'President'],
            ['admin2', 'Jane', 'Dame', 'test2@gmail.com', 'Vice President'],
            ['admin3', 'Jacob', 'Dacob', 'test3@gmail.com', 'Treasurer'],
        ]

        sponsors = [
            ['sponsor1', 'John', 'DoeSponsor', 'sponsor1@gmail.com', 'Google'],
            ['sponsor2', 'Jane', 'DameSponsor', 'sponsor2@gmail.com', 'Myspace'],
            ['sponsor3', 'Jacob', 'DacobSponsor', 'sponsor3@gmail.com', 'Facebook'],
        ]

        g = Group.objects.get(name='member_group')

        for u in members:
            user, created = User.objects.get_or_create(username=u[0], first_name=u[1], last_name=u[2], email=u[3])
            user.set_password('password')
            user.save()
            member, created = Member.objects.get_or_create(user=user)
            member.save()
            member = Member.objects.filter(user=user)
            member.update(pokerstars_username="pokerstars"+str(user.id))
            g.user_set.add(user)

        g = Group.objects.get(name='admin_group')

        for u in admins:
            user, created = User.objects.get_or_create(username=u[0], first_name=u[1], last_name=u[2], email=u[3])
            user.set_password('password')
            user.save()
            admin, created = Admin.objects.get_or_create(user=user)
            admin.save()
            admin = Admin.objects.filter(user=user)
            admin.update(position=u[4], pokerstars_username="pokerstars"+str(user.id))

            g.user_set.add(user)

        g = Group.objects.get(name='sponsor_group')

        for level in Sponsor.LEVEL_CHOICES:
            for u in sponsors:
                user, created = User.objects.get_or_create(username=u[0]+level[0], first_name=u[1], last_name=u[2], email=u[3])
                user.set_password('password')
                user.save()
                sponsor, created = Sponsor.objects.get_or_create(user=user)
                sponsor.save()
                sponsor = Sponsor.objects.filter(user=user)
                sponsor.update(home_page_url='http://www.google.com', company_name=u[4], level=level[0])

                g.user_set.add(user)