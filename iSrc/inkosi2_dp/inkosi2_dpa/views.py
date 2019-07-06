# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
# from django.http import HttpResponse


# Create your views here.
def index(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    return render(request, "index.html", {})


def course_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    return render(request, "courses.html", {})


def course_detail_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    return render(request, "course_detail.html", {})


def create_course_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    return render(request, "create_course.html", {})


def student_list_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    return render(request, "student_list.html", {})


def student_detail_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    return render(request, "student_detail.html", {})


def student_activity_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    return render(request, "student_activity.html", {})


def student_activity_detail_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    return render(request, "student_activity_detail.html", {})


def student_dashboard_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    return render(request, "student_dashboard.html", {})


def inkosi_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    return render(request, "inkosi.html", {})
