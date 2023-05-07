"""
URL configuration for howcooking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from User_Entery import views as UserEntry
from User_website import views as UserWebsite
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', UserWebsite.index, name="index"),
    path('signup', UserEntry.Signup_User, name="signup"),
    path('login', UserEntry.Login_User, name="login"),
    path('logout', UserEntry.User_logout, name="logout"),
    path('home', UserWebsite.Home_page, name="home page"),
    path('add_recipe', UserWebsite.add_Recipe, name ="add recipe"),
    path('account', UserEntry.User_account, name="user account"),
    path('contact', UserWebsite.User_contact, name="contact"), 
    path('<slug:recipe>', UserWebsite.cooking, name="cooking")
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)