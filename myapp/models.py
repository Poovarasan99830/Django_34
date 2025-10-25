from django.db import models

# Create your models here.
class Room(models.Model):
    name = models.CharField(null=False, max_length=100)
    capacity = models.IntegerField(default=1)
    kitchen = models.BooleanField(default=False)
    price = models.FloatField(default=0.0)



class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    


class StudentRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    course = models.CharField(max_length=100)

    def __str__(self):
        return self.name








  

from django.db import models
from django.contrib.auth.models import User

class Register(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
    





# ___________________________________________________________

# 🔹 2. OneToMany (1\:M)

# 👉 Example: **Author ↔ Books**



class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name





class Book(models.Model):
    title = models.CharField(max_length=200,unique=True)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)  # Foreign Key to Author

    def __str__(self):
        return self.title
    


# ___________________________________________________________

# 3. ManyToMany (M\:M)

# 👉 Example: **Student ↔ Courses**


class Course(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=100)
    # courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name
    

