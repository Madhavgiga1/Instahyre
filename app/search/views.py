from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from core.models import User
from search.serializers import UserSerializer

class SearchByNameView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        if not query:
            return User.objects.none()
        
        # First search for names starting with the query, then names containing the query
        queryset = User.objects.filter(Q(name__istartswith=query) | Q(name__icontains=query)).distinct()
        return queryset

class SearchByPhoneNumberView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        if not query:
            return User.objects.none()
        
        queryset = User.objects.filter(phone_number=query).distinct()
        return queryset

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.email and request.user in instance.contacts.all():
            return super().retrieve(request, *args, **kwargs)
        else:
            data = self.get_serializer(instance).data
            data.pop('email', None)
            return Response(data)
