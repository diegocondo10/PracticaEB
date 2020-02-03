from django.contrib import admin
from django.urls import path
from core.views import subir_imagen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('subir-imagen', subir_imagen),
]
