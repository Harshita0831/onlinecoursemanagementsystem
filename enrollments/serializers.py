from rest_framework import serializers
from .models import Enrollment, LectureProgress

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class LectureProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = LectureProgress
        fields = '__all__'

