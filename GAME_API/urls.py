"""GAME_API URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from GAME_API.views import urls_list_view, open_api_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    # ADMIN
    path('admin/', admin.site.urls),
    # OPENAPI
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # MODELS
    path('', include('ammunition.urls')),
    path('', include('arch_sessions.urls')),
    path('', include('attachments.urls')),
    path('', include('firearms.urls')),
    path('', include('maps.urls')),
    path('', include('players.urls')),
    path('', include('sessions.urls')),
    # path('', include('skins.urls')), # FIXME
    path('', include('supplies.urls')),
    path('', include('throwables.urls')),
    path('', include('users.urls')),
]
