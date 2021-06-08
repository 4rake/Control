from django.contrib import admin
from django.urls import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import ListView, DetailView
from main.models import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    # path('News/<int:pk>',
    # ListView.as_view(queryset=News.objects.all().order_by("-date")[:20],
    # template_name="news/posts.html")),
    path('News/<int:pk>',
    DetailView.as_view(model = News,
    template_name="news/post.html"),name='post'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

