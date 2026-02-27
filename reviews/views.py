from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Review
from .serializers import ReviewSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_review(request):
    serializer = ReviewSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save(student=request.user)
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)

@api_view(['GET'])
def course_reviews(request, course_id):
    reviews = Review.objects.filter(course_id=course_id)
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)