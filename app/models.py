from django.db import models
from django.urls import reverse

class Movies(models.Model):
    title = models.CharField(blank=False, max_length=60)
    is_active = models.BooleanField(default=True, max_length=60)

    class Meta:
        ordering = ('title',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
            return reverse('detail', kwargs={'pk': self.pk})

    def soft_delete(self):
        self.is_active = False
        self.save()

