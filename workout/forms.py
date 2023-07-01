from django import forms
from datetime import datetime
from .models import Workout, Exercise
from django.forms import ModelForm


class WorkoutForm(ModelForm):
    """
    Function handle the workout form
    Base-code of function and logic taken from:
    https://github.com/Code-Institute-Solutions/Django3blog
    """
    class Meta:
        model = Workout
        fields = [
            'title', 'featured_image', 'excerpt',
            'number_of_exercises',
            ]


class ExerciseForm(ModelForm):
    """
    Function handle the Exercise form
    Base-code of function and logic taken from:
    https://github.com/Code-Institute-Solutions/Django3blog
    """
    class Meta:
        model = Exercise
        fields = [
            'title', 'body',
            'exercise_image', 'exercise_muscle_group',
            ]


class WorkoutUpdateForm(ModelForm):
    """
    Function handle the update of Workout form
    Difference is number of exercises cant be changed once created
    to ensure wierd bugs wont come from next step with creating exercises
    Base-code of function and logic taken from:
    https://github.com/Code-Institute-Solutions/Django3blog
    """
    class Meta:
        model = Workout
        fields = [
            'title', 'featured_image', 'excerpt',
            'status',
            ]
