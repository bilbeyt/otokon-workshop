# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.db import models
import uuid


class Lecture(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    lecturer = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
	return self.name


def lecture_code_handler():
    return str(uuid.uuid4().hex.upper()[0:4])


class LectureDay(models.Model):
    lecture = models.ForeignKey(Lecture)
    day = models.PositiveIntegerField()
    is_available = models.BooleanField(default=False)
    code = models.CharField(max_length=10, default=lecture_code_handler, unique=True)

    def __str__(self):
         return "{}-Day #{}".format(self.lecture.name, self.day)


class LecturePoll(models.Model):
    lecture_day = models.ForeignKey(LectureDay)
    student = models.ForeignKey(User)
    is_attended = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}-{}".format(self.lecture_day.lecture.name, self.lecture_day.day, self.student.username)


@receiver(pre_save, sender=Lecture)
def lecture_slug_handler(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)
