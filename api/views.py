from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Room, Teacher, Course, Group, Lesson
from .serializers import (
    RoomSerializer,
    TeacherSerializer,
    CourseSerializer,
    GroupSerializer,
    LessonSerializer
)


@api_view(["GET"])
def timetable(request):
    day_type = request.GET.get("day_type", "toq")

    lessons = Lesson.objects.filter(
        day_type=day_type
    ).order_by("start_time")

    serializer = LessonSerializer(lessons, many=True)
    return Response(serializer.data)


class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class TeacherViewSet(ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class GroupViewSet(ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class LessonViewSet(ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
