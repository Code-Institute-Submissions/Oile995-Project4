from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Workout, Exercise
from .forms import WorkoutForm, ExerciseForm
import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
        # exercise_count = workout.exercises.count()
        # exercises_done = exercises.exercise_completed.count()

        liked = False
        if workout.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        # if exercises_done == exercise_count:
        #     workout_done = True

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

    def progressbar(self, request, slug, *args, **kwargs):
        queryset = Workout.objects.filter(status=1)
        workout = get_object_or_404(queryset, slug=slug)
        exercise_count = workout.excercise.count()
        exercises_done = workout.exercises.exercise_completed.count()
       

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
            return redirect('edit_workout')

    context = {'form': form}
    return render(request, 'create_workout.html', context)

def WorkoutAddExercise(request):
    print("add extercise")
    workout = Workout.objects.all()
    form = ExerciseForm()
    if request.method == 'POST':
        form = ExerciseForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.creator = request.user
            form.save()
            messages.success(
                request, 'You have successfully created ' + form.instance.title
                )
            return redirect('home')

    context = {'form': form,'workout': workout}
    return render(request, 'edit_workout.html', context)

def workouts(request):
    workouts = Workout.objects.all()
    context = {'workouts': workouts}
    return render(request, 'edit_workout.html', context)

def modules(request):
    exercise_numbers = request.GET.get('workout')
    print(exercise_numbers)
    context = {'exercise_numbers': range(int(exercise_numbers))}
    return render(request, 'partials/modules.html', context)