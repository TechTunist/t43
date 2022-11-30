from django.urls import include, path
from . import views


urlpatterns = [
    path('', views.home),
    path('test/', views.testURL),
]
