from tabnanny import verbose
from django.db import models


class UniversityCampus(models.Model):
    campus_name = models.CharField(max_length=60, default="", blank=False, null=False)
    state_name = models.CharField(max_length=2, default="", blank=False, null=False)
    campus_id = models.IntegerField(default="", blank=False, null=False)

    objects = models.Manager()

    def __str__(self):
        return f"{self.campus_name}, {self.campus_id}"

    class Meta:
        verbose_name_plural = "University Campus"
