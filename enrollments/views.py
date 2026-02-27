from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Enrollment, LectureProgress
from .serializers import EnrollmentSerializer, LectureProgressSerializer
from courses.models import Course

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def enroll_course(request):
    course_id = request.data.get('course')

    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({"error": "Course not found"}, status=404)

    enrollment, created = Enrollment.objects.get_or_create(
        student=request.user,
        course=course
    )

    serializer = EnrollmentSerializer(enrollment)
    return Response(serializer.data, status=201 if created else 200)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_courses(request):
    enrollments = Enrollment.objects.filter(student=request.user)
    serializer = EnrollmentSerializer(enrollments, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_progress(request):
    serializer = LectureProgressSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)