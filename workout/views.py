from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm, WorkoutUpdateForm
import datetime
from django.db.models import F
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Display Workout list Homescreen and workout details

class WorkoutList(generic.ListView):
    model = Workout
    queryset = Workout.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class WorkoutDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Workout.objects.filter(status=1)
        workout = get_object_or_404(queryset, slug=slug)
        comments = workout.comments.filter(approved=True).order_by('created_on')
        exercises = workout.exercises.order_by('exercise_number')

        liked = False
        if workout.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "workout_detail.html",
            {
                "workout": workout,
                "comments": comments,
                "liked": liked,
                "exercises": exercises,
            }
        )

#Create forms section   

def WorkoutCreate(request):
    form = WorkoutForm()
    if request.method == 'POST':
        form = WorkoutForm(request.POST, request.FILES)
        form.instance.status = True
        print(form.errors)
        if form.is_valid():
            form.instance.slug = form.instance.title.replace(" ", "-")
            form.instance.creator = request.user
            form.instance.created_on = datetime.datetime.now()
            form.instance.approved = False
            form.save()
            messages.success(
                request, 'You have successfully created ' + form.instance.title
                )
            parent = form.instance.pk
            exercise_n = form.instance.number_of_exercises +1
            return redirect('add_exercises',pk=parent, e_n=exercise_n)

    context = {'form': form}
    return render(request, 'create_workout.html', context)


def WorkoutAddExercise(request, pk, e_n):
    e_n = int(e_n)
    workout = Workout.objects.get(id=pk)
    form = ExerciseForm()
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            form.instance.workout = workout
            form.instance.slug = form.instance.title.replace(" ", "-")
            form.instance.exercise_number = e_n-1
            form.instance.exercise_completed = False
            form.save()
            messages.success(
                request, 'You have successfully created ' + form.instance.title + 
                str(form.instance.exercise_number)
                )
            exercise_n = e_n-1
            return redirect('add_exercises', pk=pk, e_n=exercise_n)
    if e_n == 1:
        return redirect('home')
    context = {'form': form, "e_n":e_n-1}
    return render(request, 'add_exercises.html', context)

# Update forms section

def updateWorkout(request, pk):
    workout_object = Workout.objects.get(id=pk)
    if workout_object.creator != request.user:
        if request.user.is_superuser:
            form = WorkoutUpdateForm(instance=workout_object)
            if request.method == 'POST':
                form = WorkoutUpdateForm(request.POST, request.FILES, instance=workout_object)
                print(form.errors)
                if form.is_valid():
                    form.save()
                    messages.success(
                        request, 'You have successfully updated ' + form.instance.title
                        )
                    e_n = form.instance.number_of_exercises -1
                    return redirect('update_exercises', pk=pk, e_n=e_n)
            context = {'form': form}
            return render(request, 'update_workout.html', context)
        else:
            messages.error(
                request, "You don't have permission to update this Workout"
                )
            return redirect('home')
    

def updateExercise(request, pk, e_n):
    if e_n == "-1":
        return redirect('home')
    e_n = int(e_n)
    excercise_object = Exercise.objects.filter(workout__id=pk)
    excercise_object= excercise_object[e_n]
    form = ExerciseForm(instance=excercise_object)
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES, instance=excercise_object)
        print(form.errors)
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
    workout = Workout.objects.get(id=pk)
    if workout.creator != request.user:
        if request.user.is_superuser:
            if request.method == 'POST':
                workout.delete()
                messages.success(
                    request, 'You have successfully deleted ' + workout.title
                    )
                return redirect('home')

            return render(request, 'delete.html', {'workout': workout})
        else:
            messages.error(
                request, "You don't have permission to delete this recipe"
                )
            return redirect('home')