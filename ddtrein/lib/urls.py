from django.urls import path

from .views import creatе_library

urlpatterns = [
    path('', creatе_library)
]
