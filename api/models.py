from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Course(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Lesson(models.Model):

    DAY_TYPE_CHOICES = (
        ('toq', 'Toq'),
        ('juft', 'Juft'),
        ('boshqa', 'Boshqa'),
    )

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    day_type = models.CharField(max_length=10, choices=DAY_TYPE_CHOICES)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        ordering = ['start_time']

    def __str__(self):
        return f"{self.group} | {self.room} | {self.start_time}"
