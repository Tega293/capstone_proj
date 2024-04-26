from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .serializers import CustomUserSerializer
from rest_framework import status,exceptions



class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    

    def get(self, request):
        user = request.user
        serialized_user = CustomUserSerializer(user).data
        if request.user.is_authenticated:
            return Response(serialized_user, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)