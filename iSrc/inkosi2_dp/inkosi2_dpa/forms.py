from django import forms
from .models import Course, Course_Assignment


class course_form(forms.ModelForm):
    course_title = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Course Title...'
        }
    ))
    course_description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Course Description...'
        }
    ))
    courseID = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'enter id...'
        }
    ))

    class Meta:
        model = Course
        fields = ("course_title", "course_description",)


class assignment_form(forms.ModelForm): 
    assignment_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Assignment Name...'
        }
    ))

    assignment_description = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Assignment Description...'
        }
    ))
    assignment_due_date = forms.DateField()

    class Meta:
        model = Course_Assignment
        fields = ("assignment_name", "assignment_description", "assignment_due_date",)


