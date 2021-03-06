from django.db import models
from django.contrib.auth.models import User

from nightreads.utils import TimeStampMixin


class Tag(TimeStampMixin):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Post(TimeStampMixin):
    title = models.CharField(max_length=300)
    url = models.URLField()

    added_by = models.ForeignKey(User)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return "{} - {}".format(self.id, self.title[:10])
