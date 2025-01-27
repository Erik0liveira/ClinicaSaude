from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('paginas.urls')),  # Inclui as URLs do app 'paginas'
     path('cadastro/', include('cadastro.urls')), 
]
