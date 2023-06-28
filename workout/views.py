from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
# from .forms import PostForm


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        exercises = post.exercises.order_by('exercise_number')
        # exercise_count = post.exercises.count()
        # exercises_done = exercises.exercise_completed.count()

        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        # if exercises_done == exercise_count:
        #     workout_done = True

        return render(
            request,
            "workout_detail.html",
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "exercises": exercises,
            }
        )

    def progressbar(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        workout = get_object_or_404(queryset, slug=slug)
        exercise_count = workout.excercise.count()
        exercises_done = workout.exercises.exercise_completed.count()
       


# class PostCreate(View):
#     model = Post
#     template_name = 'create_post.html'
