from django.db import models
from polymorphic.models import PolymorphicModel


class Page(models.Model):
    lang = models.CharField('Language', max_length=9)
    path = models.CharField(max_length=99)
    title = models.CharField(max_length=99, blank=True)
    description = models.CharField(max_length=999, blank=True)


class Block(PolymorphicModel):
    page = models.ForeignKey(Page, models.CASCADE)

    class Meta:
        order_with_respect_to = 'page'


class Heading(Block):

    LEVEL_CHOICES = [(i, i) for i in range(1, 7)]

    content = models.CharField(max_length=99)
    level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)


class Text(Block):
    content = models.CharField(max_length=99)
