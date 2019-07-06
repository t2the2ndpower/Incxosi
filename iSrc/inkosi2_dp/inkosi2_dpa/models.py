from __future__ import unicode_literals
from django.db import models
from django.utils.deconstruct import deconstructible


# Create your models here.
class IUser(models.Model):
    user_name = models.CharField(max_length=30, blank=False)
    user_email = models.EmailField(blank=False)
    user_cell = models.IntegerField(blank=False)
    userID = models.IntegerField(auto_created=True, unique=True)
    user_pic = models.URLField()
    user_created_date = models.DateField(auto_now=True)


@deconstructible
class Course(models.Model):
    courseID = models.IntegerField(auto_created=True, unique=True)
    course_title = models.CharField(max_length=80, blank=False)
    course_description = models.CharField(max_length=10000, blank=False)
    course_ownerID = models.ForeignKey(IUser, on_delete=models.CASCADE)
    course_created_date = models.DateField(auto_now=True) 

@deconstructible
class Course_Assignment(models.Model):
    related_courseID = models.ForeignKey(Course, on_delete=models.CASCADE)   
    course_assignmentID = models.IntegerField(auto_created=True, unique=True)    
    assignment_name = models.CharField(max_length=80, blank=False)
    assignment_number = models.IntegerField(auto_created=True)
    assignment_description = models.CharField(max_length=10000, blank=False)
    assignment_due_date = models.DateField()
    assignment_inkosi = models.ForeignKey(IUser, on_delete=models.CASCADE)
    assignment_created_date = models.DateField(auto_now=True)


@deconstructible
class Student_Course_Assignment(models.Model):
    student_course_assignmentID = models.IntegerField(auto_created=True, unique=True)
    related_studentID = models.ForeignKey(IUser, on_delete=models.CASCADE)
    related_courseID = models.ForeignKey(Course)
    related_assignmentID = models.ForeignKey(Course_Assignment, on_delete=models.CASCADE)
    start_date = models.DateField()
    complete_date = models.DateField(blank=True)
    isStarted = models.BooleanField(default=0)
    stu_course_asgn_created_date = models.DateField(auto_now=True)


class Student_Activity_Type(models.Model):
    student_activity_typeID = models.IntegerField(auto_created=True, unique=True)
    student_activity_type = models.CharField(max_length=20, blank=False)


@deconstructible
class Student_Activity(models.Model):
    student_activityID = models.IntegerField(auto_created=True, unique=True)
    related_studentID = models.ForeignKey(IUser, on_delete=models.CASCADE)
    related_student_course_assignmentID = models.ForeignKey(Student_Course_Assignment, on_delete=models.CASCADE)
    activity_type = models.ForeignKey(Student_Activity_Type)
    activity_details = models.CharField(max_length=10000, blank=False)
    created_date = models.DateField(auto_now=True)


