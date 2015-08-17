from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Member, Admin, Sponsor

# # Define an inline admin descriptor for Member model
# # which acts a bit like a singleton
# class MemberInline(admin.StackedInline):
#     model = Member
#     can_delete = False
#     verbose_name_plural = 'Member'

# class AdminInline(admin.StackedInline):
#     model = Admin
#     can_delete = False
#     verbose_name_plural = 'Admin'


# # Define a new User admin
# class UserAdmin(UserAdmin):
#     inlines = (MemberInline, AdminInline)

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(Member)
admin.site.register(Admin)
admin.site.register(Sponsor)