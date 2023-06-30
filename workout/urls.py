from . import views
from django.urls import path


urlpatterns = [
    path('', views.WorkoutList.as_view(), name='home'),
    path('edit_workout/', views.workouts, name='edit_workout'),
    path('modules/', views.modules, name='modules'),
    path('create_workout/', views.WorkoutCreate, name='create_workout'),
    path('<slug:slug>/', views.WorkoutDetail.as_view(), name='workout_detail'),


]