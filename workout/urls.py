from . import views
from django.urls import path


urlpatterns = [
    path('', views.WorkoutList.as_view(), name='home'),
    path('<pk>', views.updateWorkout, name='update_workout'),
    path('<pk>/<e_n>', views.WorkoutAddExercise, name='add_exercises'),
    path('<pk>/<e_n>/update', views.updateExercise, name='update_exercises'),
    path('delete-workout/<str:pk>/', views.deleteWorkout, name='delete_workout'),
    path('create_workout/', views.WorkoutCreate, name='create_workout'),
    path('<slug:slug>/', views.WorkoutDetail.as_view(), name='workout_detail'),


]