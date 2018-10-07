from django.urls import path

from . import views

app_name = "App"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('1/', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('impressum/', views.ImpressumView.as_view(), name='impressum'),
]
