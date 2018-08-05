from django.db import models


class ExerciseType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Exercise(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    exercise_type = models.ForeignKey(ExerciseType, on_delete='CASCADE')

class Set(models.Model):
    reps = models.FloatField()
    weight = models.FloatField()
    exercise = models.ForeignKey(Exercise, on_delete='CASCADE')
