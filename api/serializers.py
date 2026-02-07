from rest_framework import serializers
from .models import Room, Teacher, Course, Group, Lesson


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = Group
        fields = "__all__"


class LessonSerializer(serializers.ModelSerializer):
    room = serializers.CharField(source='room.name')
    teacher = serializers.CharField(source='teacher.full_name')
    group = serializers.CharField(source='group.name')
    course = serializers.CharField(source='group.course.name')

    class Meta:
        model = Lesson
        fields = (
            'id',
            'room',
            'teacher',
            'group',
            'course',
            'day_type',
            'start_time',
            'end_time',
        )
