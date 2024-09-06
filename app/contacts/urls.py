from django.urls import path,include
from contacts import views
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('', views.ContactViewSet)

urlpatterns = [
    path('', include(router.urls)),
]