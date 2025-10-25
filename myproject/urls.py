"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
# from myapp import  views
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('home/<int:number>/', views.home, name='home'),
#     path('about/', views.about ,name='about'),
#     path("order/", views.order ,name='order'),
#     path("contact/", views.contact ,name='contact'),
#     path("student/<str:roll>/", views.student_info ,name='student'),
#     path("courses/<int:data>/", views.course_list ,name='courses'),
#     path("product/<int:id>/", views.product_detail ,name='product'),
#     path("login/", views.login ,name='login'),
#     path("add_product/", views.product_list ,name='add_product'),
#     path("reg/", views.student_registration ,name='student_registration'),
#     path("students/", views.student,name='student_list'),
#     path("students_list/", views.StudentList,name='students'),

    

# ]



from django.urls import path,include
from myapp import views
from django.contrib import admin


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('list/', views.student_list, name='student_list'),
#     path('add/', views.student_create, name='student_create'),
#     path('edit/<int:pk>/', views.student_update, name='student_update'),
#     path('delete/<int:pk>/', views.student_delete, name='student_delete'),
   



#     path('register/', views.register_view, name='register'),
#     path('login/', views.login_view, name='login'),
#     path('logout/', views.logout_view, name='logout'),
#     path('profile/', views.profile_view, name='profile'),
# ]


# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('myapp.urls')),
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drfapp import views
from midapp import views


# router = DefaultRouter()
# router.register(r'students',views.StudentViewSet)

urlpatterns = [
    # path('CRUD_api/', include(router.urls)),
    # path("Jwt_Auth/",include('drfapp.urls')),
    path('home/',views.index)
    
]