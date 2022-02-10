from cgitb import handler
from short_url.views import index, pageNotFound
from django.contrib import admin
from django.urls import path


urlpatterns = [
    path( 'admin/', admin.site.urls ),
    path( '', index ),
]

handler404 = pageNotFound
