from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Workout(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name="workout_posts")
    updated_on = models.DateTimeField(auto_now=True)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    number_of_exercises = models.IntegerField(default=0, validators=[MinValueValidator(3), MaxValueValidator(8)])
    status = models.IntegerField(choices=STATUS, default=0)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Exercise(models.Model):
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE,
                                related_name="exercises", default="")
    title = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    exercise_number = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(8)])
    body = models.TextField()
    exercise_image = CloudinaryField('image', default='placeholder')
    exercise_muscle_group = CloudinaryField('image', default='placeholder')
    exercise_completed = models.BooleanField(default=False, editable=False)

    class Meta:
        ordering = ['exercise_number']

    def __str__(self):
        return f"{self.body} {self.title}"
