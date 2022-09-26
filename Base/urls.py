from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcomePage, name='home'),
    path('about/', views.aboutPage, name='about'),
    path('blog/', views.blogArticles, name='articles'),
]