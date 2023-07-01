from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm, WorkoutUpdateForm
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Display Profile page and the workouts made by User
class Profile(View):
    """
    Function handle the display list view of all workouts
    created by request user in user Profile page.
    Base-code of function and logic taken from:
    https://github.com/Code-Institute-Solutions/Django3blog
    """
    def get(self, request, *args, **kwargs):
        queryset = Workout.objects.filter(creator=request.user)
        paginate_by = 3

        return render(request, 'profile.html', {"queryset": queryset, })


# Display Workout list Homescreen and workout details


class WorkoutList(generic.ListView):
    """
    Function handle the display list view of all workouts
    that are Apporoved by admin and in status Publish.
    Base-code of function and logic taken from:
    https://github.com/Code-Institute-Solutions/Django3blog
    """
    queryset = Workout.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class WorkoutDetail(View):
    """
    Function handle the display detail view of all workouts
    that are in Publish status.
    Base-code of function and logic taken from:
    https://github.com/Code-Institute-Solutions/Django3blog
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Workout.objects.filter(status=1)
        workout = get_object_or_404(queryset, slug=slug)
        exercises = workout.exercises.order_by('exercise_number')

        return render(
            request,
            "workout_detail.html",
            {
                "workout": workout,
                "exercises": exercises,
            }
        )


class MyWorkoutDetail(View):
    """
    Function handle the display detail view of all workouts
    created by request user, regardless if draft or not.
    Base-code of function and logic taken from:
    https://github.com/Code-Institute-Solutions/Django3blog
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Workout.objects.filter(creator=request.user)
        workout = get_object_or_404(queryset, slug=slug)
        exercises = workout.exercises.order_by('exercise_number')

        return render(
            request,
            "workout_detail.html",
            {
                "workout": workout,
                "exercises": exercises,
            }
        )


# Create forms section

def WorkoutCreate(request):
    """
    Function handle the creating option of workout.
    Create Workout form html renders.
    User gets prompted to edit form.
    Base-code of function and logic taken from:
    https://github.com/leonardo-simeone/venezuelan-food-cookbook
    """
    form = WorkoutForm()
    if request.method == 'POST':
        form = WorkoutForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.slug = form.instance.title.replace(" ", "-")
            form.instance.creator = request.user
            form.instance.created_on = datetime.datetime.now()
            form.instance.status = False
            form.instance.approved = False
            form.save()
            messages.success(
                request, 'You have successfully created ' +
                form.instance.title +
                'Please await admin to approve content'
                )
            parent = form.instance.pk
            exercise_n = form.instance.number_of_exercises + 1
            return redirect('add_exercises', pk=parent, e_n=exercise_n)
    context = {'form': form}
    return render(request, 'create_workout.html', context)


def WorkoutAddExercise(request, pk, e_n):
    """
    Function handle the adding option of exercise to workout.
    Exercise form html renders for ammount of exercises
    in parent workout. User gets prompted to edit form.
    Base-code of function and logic taken from:
    https://github.com/leonardo-simeone/venezuelan-food-cookbook
    """
    e_n = int(e_n)
    workout = Workout.objects.get(id=pk)
    form = ExerciseForm()
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.workout = workout
            form.instance.slug = form.instance.title.replace(" ", "-")
            form.instance.exercise_number = e_n-1
            form.instance.exercise_completed = False
            form.save()
            messages.success(
                request, 'You have successfully created ' +
                form.instance.title +
                str(form.instance.exercise_number)
                )
            exercise_n = e_n-1
            return redirect('add_exercises', pk=pk, e_n=exercise_n)
    if e_n == 1:
        return redirect('home')
    context = {'form': form, "e_n": e_n - 1}
    return render(request, 'add_exercises.html', context)


# Update forms section

def updateWorkout(request, pk):
    """
    Function handle the update option of workout.
    If user is eligible, edit workout form html renders.
    User gets prompted to edit form.
    Base-code of function and logic taken from:
    https://github.com/leonardo-simeone/venezuelan-food-cookbook
    """
    workout_object = Workout.objects.get(id=pk)
    if workout_object.creator == request.user or request.user.is_superuser:
        form = WorkoutUpdateForm(instance=workout_object)
        if request.method == 'POST':
            form = WorkoutUpdateForm(request.POST, request.FILES,
                                     instance=workout_object)
            if form.is_valid():
                form.save()
                messages.success(
                    request, 'You have successfully updated ' +
                    form.instance.title
                    )
                e_n = form.instance.number_of_exercises - 1
                return redirect('update_exercises', pk=pk, e_n=e_n)
        context = {'form': form}
        return render(request, 'update_workout.html', context)
    else:
        messages.error(
            request, "You don't have permission to update this Workout"
            )
        return redirect('home')


def updateExercise(request, pk, e_n):
    """
    Function handle the update option of exercise.
    Edit exercise form html renders for ammount of exercises
    in parent workout. User gets prompted to edit form.
    Base-code of function and logic taken from:
    https://github.com/leonardo-simeone/venezuelan-food-cookbook
    """
    parent = Exercise.objects.filter(workout__id=pk).count()
    if e_n == "-1":
        return redirect('home')
    e_n = int(e_n)
    if e_n > int(parent):
        e_n = int(parent)-1
    excercise_object = Exercise.objects.filter(workout__id=pk)
    excercise_object = excercise_object[e_n]
    form = ExerciseForm(instance=excercise_object)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES,
                            instance=excercise_object)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'You have successfully updated ' + form.instance.title
                )
            exercise_n = e_n-1
            return redirect('update_exercises', pk=pk, e_n=exercise_n)
    context = {'form': form}
    return render(request, 'update_exercises.html', context)


# Delete forms view

def deleteWorkout(request, pk):
    """
    Function handle the delete option of workout.
    If user is eligible to delete, delete html renders
    User gets prompted to delete or go back.
    Base-code of function and logic taken from:
    https://github.com/leonardo-simeone/venezuelan-food-cookbook
    """
    workout = Workout.objects.get(id=pk)
    if workout.creator == request.user or request.user.is_superuser:
        if request.method == 'POST':
            workout.delete()
            messages.success(
                request, 'You have successfully deleted ' + workout.title
                )
            return redirect('home')

        return render(request, 'delete.html', {'workout': workout})
    else:
        messages.error(
            request, "You don't have permission to delete this Workout"
            )
        return redirect('home')
