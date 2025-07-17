"""core URL Configuration

The `urlpatterns` list routes URLs to views. For now, only the admin site is included.
"""
from django.contrib import admin
from django.urls import path

# PUBLIC_INTERFACE
urlpatterns = [
    path('admin/', admin.site.urls),
]
