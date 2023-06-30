from django.contrib import admin
from .models import Workout, Comment, Exercise
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Workout)
class WorkoutAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('content')
    actions = ['approve_workout']

    def approve_workout(self, request, queryset):
        queryset.update(approved=True)

@admin.register(Exercise)
class ExerciseAdmin(SummernoteModelAdmin):
    list_display = ('title', 'workout')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('body')



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'workout', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')