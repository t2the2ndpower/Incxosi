from __future__ import unicode_literals
from django.contrib import admin


# Change Header Here
admin.site.site_header = 'Welcome to the Inkosi App Admin Area'


# Register your models here.
from .models import IUser, Course, Course_Assignment, Student_Course_Assignment, Student_Activity_Type, Student_Activity


class InkosiUserAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'user_cell', 'user_email']

class InkosiCourseAdmin(admin.ModelAdmin):
    list_display = ['course_title', 'course_created_date', 'course_ownerID']

class InkosiAssignmentAdmin(admin.ModelAdmin):
    list_display = ['assignment_name', 'assignment_created_date', 'assignment_due_date', 'related_courseID']
        #list_display_links = ['related_courseID']



class InkosiTypeAdmin(admin.ModelAdmin):
    list_display = ['student_activity_type', 'student_activity_typeID']

class InkosiStuActAdmin(admin.ModelAdmin):
    list_display = ['activity_type', 'activity_details', 'created_date']

class InkosiStuCourseAsgnAdm(admin.ModelAdmin):
    list_display = ['student_course_assignmentID', 'isStarted', 'start_date', 'complete_date', 'stu_course_asgn_created_date']


admin.site.register(IUser, InkosiUserAdmin)
admin.site.register(Course, InkosiCourseAdmin)
admin.site.register(Course_Assignment, InkosiAssignmentAdmin)
admin.site.register(Student_Course_Assignment, InkosiStuCourseAsgnAdm)
admin.site.register(Student_Activity_Type, InkosiTypeAdmin)
admin.site.register(Student_Activity, InkosiStuActAdmin)


