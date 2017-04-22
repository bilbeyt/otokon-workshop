# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from education.models import Lecture, LectureDay, LecturePoll


class LectureAdmin(admin.ModelAdmin):
    list_filter = ['lecturer', 'created']
    list_display = ["name", "lecturer", "created", "slug"]
    exclude = ["slug"]


class LectureDayAdmin(admin.ModelAdmin):
    list_filter = ['lecture', 'is_available', ]
    list_display = ['lecture', 'day', 'is_available', 'code']
    exclude = ["code"]

class LecturePollAdmin(admin.ModelAdmin):
    list_filter = ['lecture_day', 'student', 'is_attended']

admin.site.register(Lecture, LectureAdmin)
admin.site.register(LectureDay, LectureDayAdmin)
admin.site.register(LecturePoll, LecturePollAdmin)
