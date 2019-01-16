"""App1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, include
#from rest_framework.urlpatterns import format_suffix_patterns
from App import views
#from .api import router
#from django.conf import settings
#from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'employees', views.EmployeeViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    ##path('app/', include('App.urls')),
    path('', include('App.urls')),
    #path('2', include('App.urls')),
    #path('categories/', views.CategoryList.as_view()),
    #path('posts/', views.PostList.as_view())
    #path('api/v1/', include(router.urls)),
    path('api/', include(router.urls)),
]


#urlpatterns = format_suffix_patterns(urlpatterns);



