from django.contrib import admin

# Register your models here.
from .models import StudentRegistration

admin.site.register(StudentRegistration)



# ________________________________________________

from .models import Author,Book

admin.site.register(Author)
admin.site.register(Book)



# ________________________________________________

from .models import Course,Student

admin.site.register(Course)
# admin.site.register(Student)


# ________________________________________________

# ADMIN PAGE customization

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    # filter_horizontal = ("courses",)



# ________________________________________________

