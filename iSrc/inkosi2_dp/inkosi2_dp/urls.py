"""inkosi2_dp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Api imports
from django.urls import include, path
from rest_framework import routers
from inkosi2_dpa import views
# Template imports
from django.views.generic.base import TemplateView
# Views import
from inkosi2_dpa.views import course_detail_view, course_assignment_view, create_assignment_view, course_view, create_course_view, student_list_view, student_detail_view, student_dashboard_view, student_activity_view, student_activity_detail_view, index_view, inkosi_view


# Variables
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('courses/', course_view),
    path('course/detail/<int:id>/', course_detail_view),
    path('course/detail/assignments', course_assignment_view),
    path('course/create/', create_course_view),
    path('course/create/assignment', create_assignment_view),
    path('student_list/', student_list_view),
    path('student/detail/<int:id>/', student_detail_view),
    path('student/activity', student_activity_view),
    path('student/activity/detail/<int:id>/', student_activity_detail_view),
    path('dalibi/', student_dashboard_view),
    path('inkosi/', inkosi_view),
    path('', index_view, name='index'),
    path('router/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
