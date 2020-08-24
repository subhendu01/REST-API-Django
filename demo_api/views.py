from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import JobApplicant
from .serializers import JobApplicantSerializer

class JobApplicantList(APIView):
    def get(self,request):
        applicant_list = JobApplicant.objects.all()
        serializer = JobApplicantSerializer(applicant_list, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = JobApplicantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


