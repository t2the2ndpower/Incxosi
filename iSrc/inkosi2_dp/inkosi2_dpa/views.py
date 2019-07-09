# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Course, Course_Assignment
# from django.http import HttpResponse
from .forms import course_form, assignment_form


# Create your views here.
def index_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>") 
    return render(request, "index.html", {})


def course_view(request, *args, **kwargs):
    queryset = Course.objects.all()

    context = {
        'object_list': queryset,
    }

    return render(request, "courses.html", context)


def course_detail_view(request, *args, **kwargs):
    obj = Course.objects.get(id=1)

    context = {
        'object': obj,
    }

    return render(request, "course_detail.html", context)


def course_assignment_view(request, *args, **kwargs):
    # obj = Course.objects.get(id=id)
    queryset = Course_Assignment.objects.all()

    context = {
        # 'object': obj,
        'object_list': queryset,
    }

    return render(request, "course_assignments_list.html", context)


def create_course_view(request, *args, **kwargs):
    form = course_form(request.POST or None)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        form = course_form()
    context = {
        "course_title": "New Course Created!",
        "course_description": "New Course Description Created!",
        "form": form,
        }
    return render(request, "create_course.html", context)


def create_assignment_view(request, *args, **kwargs):
    form = assignment_form(request.POST or None)
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        form = assignment_form()
    context = {
        "assignment_name": "New Course Assignment Created!",
        "assignment_description": "New Course Assignment Description Created!",
        "assignment_due_date": "1990-12-12",
        "form": form,
        }
    return render(request, "create_assignments.html", context)


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
