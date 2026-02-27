from django.urls import path
from .views import add_review, course_reviews

urlpatterns = [
    path('reviews/', add_review),
    path('courses/<int:course_id>/reviews/', course_reviews),
]