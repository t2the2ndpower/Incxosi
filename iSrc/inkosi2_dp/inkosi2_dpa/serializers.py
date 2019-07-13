from django.contrib.auth.models import User, Group
from inkosi2_dpa.models import Course, Course_Assignment
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


# class UserSerializer(serializers.ModelSerializer):
#     courses = serializers.PrimaryKeyRelatedField(many=True, queryset=courses.objects.all())

#     class Meta:
#         model = User
#         fields = ('id', 'username', 'courses')


class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course
        fields = (
            'courseID',
            'url',
            'course_title',
            'course_description',
            'course_ownerID',
            'course_created_date'
            )


class CourseAssignmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Course_Assignment
        fields = (
            'course_assignmentID',
            'url',
            'related_courseID',
            'assignment_name',
            'assignment_number',
            'assignment_description',
            'assignment_due_date',
            'assignment_created_date',
            'assignment_created_by'
        )
