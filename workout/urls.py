from . import views
from django.urls import path


urlpatterns = [
    
    path('delete-workout/<str:pk>', views.deleteWorkout, name='delete_workout'),
    path('update-workout/<pk>', views.updateWorkout, name='update_workout'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('<pk>/<e_n>', views.WorkoutAddExercise, name='add_exercises'),
    path('<pk>/<e_n>/update', views.updateExercise, name='update_exercises'),
    path('create_workout/', views.WorkoutCreate, name='create_workout'),
    path('<slug:slug>/', views.WorkoutDetail.as_view(), name='workout_detail'),
    path('my_workout/<slug:slug>/', views.MyWorkoutDetail.as_view(), name='my_workout_detail'),
    path('', views.WorkoutList.as_view(), name='home'),


]