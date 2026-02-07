from django.contrib import admin
from .models import Room, Teacher, Course, Group, Lesson

admin.site.register(Room)
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Lesson)
