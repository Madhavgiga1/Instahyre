from spam.views import SpamViewset
from django.urls import path, include
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'spam', SpamViewset)

urlpatterns = [
    path('', include(router.urls)),
]