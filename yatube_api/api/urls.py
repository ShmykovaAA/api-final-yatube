from django.urls import path, include

urlpatterns = [
    path('v1/jwt/', include('djoser.urls')),
    path('v1/jwt/', include('djoser.urls.jwt')),
]
