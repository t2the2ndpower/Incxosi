from django.contrib.auth.models import User, Group
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class UserSerializer(serializers.ModelSerializer):
    courses = serializers.PrimaryKeyRelatedField(many=True, queryset=Courses.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'courses')


class CoursesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Courses
        fields = ('course_id', 'Course_Title', 'Course Description')