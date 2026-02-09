from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RoomViewSet,
    TeacherViewSet,
    CourseViewSet,
    GroupViewSet,
    LessonViewSet,
    timetable,
)

router = DefaultRouter()
router.register("rooms", RoomViewSet)
router.register("teachers", TeacherViewSet)
router.register("courses", CourseViewSet)
router.register("groups", GroupViewSet)
router.register("lessons", LessonViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("timetable/", timetable),
]
