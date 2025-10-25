
from django import forms

# class StudentRegistrationForm(forms.Form):
#     name = forms.CharField(max_length=100)
#     email = forms.EmailField()
#     age = forms.IntegerField()
#     course = forms.CharField(max_length=100)





from .models import StudentRegistration

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = '__all__'


from django.contrib.auth.models import User        
class registerForm(forms.ModelForm):
   class Meta:
       model=User
       fields=["username","email","password"]




from django import forms
from django.contrib.auth.models import User
from .models import Register
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['bio', 'avatar']