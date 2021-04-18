from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mock-up/', include('mockapp.urls')),   # for mock-up
    path('', include('analysisapp.urls')),
]
