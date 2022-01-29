from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # импорт правил из приложения posts
    path('admin/', admin.site.urls),
    path('', include('posts.urls', namespace='posts')),
    path('group/<slug:title>/', include('posts.urls', namespace='posts')),
]
