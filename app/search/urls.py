from django.urls import path
from search.views import SearchByNameView, SearchByPhoneNumberView, UserDetailView

urlpatterns = [
    path('search/name/', SearchByNameView.as_view(), name='search-by-name'),
    path('search/phone/', SearchByPhoneNumberView.as_view(), name='search-by-phone'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
