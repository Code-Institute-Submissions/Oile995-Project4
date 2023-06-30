from . import views
from django.urls import path


urlpatterns = [
    path('', views.WorkoutList.as_view(), name='home'),
    path('<pk>/<e_n>', views.WorkoutAddExercise, name='edit_workout'),
    path('create_workout/', views.WorkoutCreate, name='create_workout'),
    path('<slug:slug>/', views.WorkoutDetail.as_view(), name='workout_detail'),


]