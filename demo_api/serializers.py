from rest_framework import serializers
from .models import JobApplicant

class JobApplicantSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplicant
        # fields = {'first_name','last_name'} # for specific field
        fields = "__all__"