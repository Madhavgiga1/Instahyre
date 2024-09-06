from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Spam
from spam.serializers import SpamReportSerializer
from rest_framework.response import Response
from rest_framework import status

class SpamViewset(viewsets.ModelViewSet):
    serializer_class = SpamReportSerializer
    queryset = Spam.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        phone_number = serializer.validated_data['phone_number']
        user = self.request.user

        spam_report = Spam(phone_number=phone_number, reported_by=user)
        spam_report.save()

        return Response({'message': 'Number marked as spam'}, status=status.HTTP_201_CREATED)
