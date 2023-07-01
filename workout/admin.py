from django.contrib import admin
from .models import Workout, Exercise
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Workout)
class WorkoutAdmin(SummernoteModelAdmin):
    """
    Function handle the Admin page view
    Base-code of function and logic taken from:
    https://github.com/Code-Institute-Solutions/Django3blog
    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on', 'approved')
    summernote_fields = ('content')
    actions = ['approve_workout']

    def approve_workout(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Exercise)
class ExerciseAdmin(SummernoteModelAdmin):
    """
    Function handle the Admin page view
    Base-code of function and logic taken from:
    https://github.com/Code-Institute-Solutions/Django3blog
    """
    list_display = ('title', 'workout')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body')
