from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Student, Admin, Sponsor

# # Define an inline admin descriptor for Student model
# # which acts a bit like a singleton
# class StudentInline(admin.StackedInline):
#     model = Student
#     can_delete = False
#     verbose_name_plural = 'Student'

# class AdminInline(admin.StackedInline):
#     model = Admin
#     can_delete = False
#     verbose_name_plural = 'Admin'


# # Define a new User admin
# class UserAdmin(UserAdmin):
#     inlines = (StudentInline, AdminInline)

# # Re-register UserAdmin
# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
admin.site.register(Student)
admin.site.register(Admin)
admin.site.register(Sponsor)