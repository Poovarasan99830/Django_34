from turtle import pd
from unicodedata import name
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def home(request, number):
    # return HttpResponse(f"This is home page {name}")
    return render(request, 'home.html', {'get_number1': number, 'get_number2': number + 1})


def about(request):
    return render(request, 'app1.html')

def order(request):
    return render(request, 'order.html')
   
def contact(request):
    return render(request, 'contact.html')

    

def student_info(request,roll):
    student = {'name': 'Ravi', 'roll': roll, 'course': 'Python Full Stack'}
    return render(request, 'student.html', {'student': student})



def course_list(request,data):
    courses = ['Python', 'Django', 'Flask', 'HTML', 'CSS']
    mark =data
    return render(request, 'student.html', {'courses': courses, 'mark': mark})



# ________________________________________________________________________________


def product_detail(request,id):
    product = [
        {'id': 1, 'name': 'Laptop', 'price': 55000},
        {'id': 2, 'name': 'Mouse', 'price': 800},
        {'id': 3, 'name': 'Keyboard', 'price': 1500},
    ]
    result = next((item for item in product if item["id"] == id), "data not found")
    return render(request, 'product.html', {'get_product': result})



# ________________________________________________________________________________


def login(request):
    print(request.method)
    print(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return render(request, 'login.html', {'username': username, 'password': password})
    else:
        return render(request, 'login.html')
    



# ________________________________________________________________________________




from .models import Product

def product_list(request):
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_price = request.POST.get('price')
        get_description = request.POST.get('description')
        Product.objects.create(name=get_name, price=get_price, description=get_description)
        print(type(get_price))
        return HttpResponse("data send to database...")
    else:
        return render(request, 'product_list.html')
#        return render(request, 'product_list.html', {'products': Product.objects.all()})
#    else:
#        return render(request, 'product_list.html', {'products': Product.objects.all()})



# ________________________________________________________________________________



from .models import StudentRegistration

def student_registration(request):
    print(request.POST)
    if request.method == 'POST':
        get_name = request.POST['name']
        get_email = request.POST['email']
        get_age = request.POST['age']
        get_course = request.POST['course']
        StudentRegistration.objects.create(name=get_name, email=get_email, age=get_age, course=get_course)
        return HttpResponse("data saved to database...")
    else:
        return render(request, 'stu_reg.html')






# ________________________________________________________________________________


from .forms import StudentRegistrationForm

# def student(request):
#     if request.method == 'POST':
#         form = StudentRegistrationForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
#             age = form.cleaned_data['age']
#             course = form.cleaned_data['course']
#             StudentRegistration.objects.create(name=name, email=email, age=age, course=course)
#             return HttpResponse("data saved to database...")
#     else:
#         form = StudentRegistrationForm()
#     return render(request, 'django_stu_form.html', {'form': form})



# def student(request):
#     if request.method == 'POST':
#         form = StudentRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse("Data saved to database...")
#     else:
#         form = StudentRegistrationForm()
#     return render(request, 'django_stu_form.html', {'form': form})


# from django.db.models.functions import Lower
# from django.db.models import Avg, Sum
# from django.db.models import Q



# ________________________________________________________________________________



# def StudentList(request):
    # students = StudentRegistration.objects.all()
    # students = StudentRegistration.objects.get(id=5)
    # students=StudentRegistration.objects.filter(name="varun")
    # students = StudentRegistration.objects.filter(age__gte=34)
    # students = StudentRegistration.objects.exclude(name="varun")



    # students = StudentRegistration.objects.get(id=5)
    # students.name = "ssss"
    # students.save()
    
    # StudentRegistration.objects.filter(name="ssss").update(name="movie")


    # students = StudentRegistration.objects.get(id=4)
    # students.delete()
    # StudentRegistration.objects.filter(name="movie").delete()



    # students = StudentRegistration.objects.all().order_by('name')
    # students = StudentRegistration.objects.all().order_by(Lower('name'))

    
    # students = StudentRegistration.objects.filter(name__iexact="sam")
    # students = StudentRegistration.objects.all()[:2]
    # students = StudentRegistration.objects.count()

    # students= StudentRegistration.objects.filter(name="sam").exists()
    # students = StudentRegistration.objects.aggregate(Avg('age'), Sum('age'))


    # students = StudentRegistration.objects.values('course').distinct()
    # students = StudentRegistration.objects.values('course', 'name')


    # students = StudentRegistration.objects.values('age')


   

    # #  OR condition
    # students = StudentRegistration.objects.filter(Q(name="arun") & Q(age__gte=18))

    # #  AND condition
    # students = StudentRegistration.objects.filter(Q(name="Arun") & Q(age__gte=18))

 


    # return render(request, 'app1.html', {'students': students})






# ________________________________________________________________________________



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse


from django.db.models import Q
from django.db.models.functions import Lower

from .models import StudentRegistration
from .forms import StudentRegistrationForm

# ✅ CREATE
def student_create(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentRegistrationForm()
    return render(request, 'django_stu_form.html', {'form': form})


# ✅ READ (LIST + SEARCH + FILTER + ORDER)
def student_list(request):
    students = StudentRegistration.objects.all()

    # 🔍 Search
    search_query = request.GET.get('search', '')
    if search_query:
        students = students.filter(Q(name__icontains=search_query) | Q(course__icontains=search_query))

    # 🎯 Filter by Course
    course_filter = request.GET.get('course', '')
    if course_filter:
        students = students.filter(course__iexact=course_filter)

    # 🔼🔽 Order by
    order_by = request.GET.get('order_by', '')
    if order_by:
        students = students.order_by(order_by)
    else:
        students = students.order_by(Lower('name'))

    return render(request, 'student_list.html', {'students': students})



# ✅ UPDATE
def student_update(request, pk):
    student = get_object_or_404(StudentRegistration, pk=pk)
    print(student)
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentRegistrationForm(instance=student)
    return render(request, 'django_stu_form.html', {'form': form})


# ✅ DELETE
def student_delete(request, pk):
    student = get_object_or_404(StudentRegistration, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, f"✅ Student '{student.name}' deleted successfully!")
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})


#_______________________________________________________________________________

# from .forms import registerForm

# def register(request):
#     if request.method=="POST":
#         form=registerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login_view')
        
#     else:
#         form=registerForm()
#         return render(request,"register.html",{"form":form})
    


# _______________________________________________________________________________

# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# ------------------------------
# 🔹 Login View
# ------------------------------
# def login_view(request):
#     print(request.POST)
#     if request.method == 'POST':
#         get_username = request.POST.get('username')
#         get_password = int(request.POST.get('password'))
        
#         data=User.objects.filter(password=get_password)
        
#         print("Authenticate......:",data)
#         if data is not None:
#             # login(request, user)
#             print(data)
#             return redirect('student_list')
#         else:
#             HttpResponse('Invalid username or password.')

#     return render(request, 'login.html')




# _______________________________________________________________________________



from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, RegisterForm
from .models import Register

# ------------------------------
# 🔹 Register View
# ------------------------------
def register_view(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        profile_form = RegisterForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')
    else:
        user_form = UserRegisterForm()
        profile_form = RegisterForm()

    return render(request, 'register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# ------------------------------
# 🔹 Login View
# ------------------------------
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')


# ------------------------------
# 🔹 Logout View
# ------------------------------
def logout_view(request):
    logout(request)
    return redirect('login')




# ------------------------------
# 🔹 Profile View
# ------------------------------
@login_required
def profile_view(request):
    profile, created = Register.objects.get_or_create(user=request.user)
    return render(request, 'profile.html', {'profile': profile})





#______________________________________________________________
# 4
from .models import Author,Book
from .models import Student,Course

def display(request):
    # data=Book.objects.all()
    # data = Book.objects.select_related('author').all()

    # student = Student.objects.get(id=1)
    # courses = student.courses.all()

    student = Student.objects.prefetch_related('courses').get(id=4)
    courses = student.courses.all()

    return render(request,"display.html",{"get_data":courses})








