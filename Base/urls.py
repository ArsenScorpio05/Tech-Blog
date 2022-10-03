from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.welcomePage, name='home'),
    path('about/', views.aboutPage, name='about'),
    path('blog/', views.blogArticles, name='articles'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)