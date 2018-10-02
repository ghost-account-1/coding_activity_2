from django.db import models

class Movies(models.Model):
    title = models.CharField(blank=False, max_length=60)
    is_active = models.BooleanField(default=False, max_length=60)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title
