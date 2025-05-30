from django.db import models


class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(default="", blank=True, null=True)

    objects = models.Manager()

    def __str__(self):
        # Returns the input value of the title and instructor name field as a tuple
        # to display in the browser instead of the default titles
        display_course = "{0.title}: {0.instructor_name}"
        return display_course.format(self)

    class Meta:
        verbose_name_plural = "UniversityClasses"
