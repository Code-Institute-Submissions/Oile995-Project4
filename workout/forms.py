from django import forms
from datetime import datetime
from .models import Workout, Exercise, Comment
from django.forms import ModelForm



class WorkoutForm(ModelForm):

    class Meta:
        model = Workout
        fields = [
            'title', 'featured_image', 'excerpt',
            'number_of_exercises',  
            ]


class ExerciseForm(ModelForm):
    class Meta:
        model = Exercise
        fields = [
            'title', 'body',
            'exercise_image', 'exercise_muscle_group', 
            ]

class WorkoutUpdateForm(ModelForm):

    class Meta:
        model = Workout
        fields = [
            'title', 'featured_image', 'excerpt',
            'status', 
            ]