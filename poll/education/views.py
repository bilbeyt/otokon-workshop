# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse_lazy
from education.models import Lecture, LectureDay, LecturePoll
from education.forms import PollForm
from django.utils import timezone


class LectureListView(ListView):
    model = Lecture
    template_name = "education/lecture_list.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LectureListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LectureListView, self).get_context_data(**kwargs)
        context["lecture_list"] = Lecture.objects.all()
        return context


class LectureDayListView(ListView):
    model = LectureDay
    template_name = "education/lecture_day_list.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LectureDayListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LectureDayListView, self).get_context_data(**kwargs)
        lecture_slug = str(self.kwargs.get("lecture_slug"))
        context["lecture_day_list"] = LectureDay.objects.filter(lecture__slug=lecture_slug)
        return context


class LecturePollFormView(FormView):
    form_class = PollForm
    template_name = "education/lecture_poll.html"
    success_url = reverse_lazy("base")

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LecturePollFormView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LecturePollFormView, self).get_context_data(**kwargs)
        lecture_slug = self.kwargs.get("lecture_slug")
        lecture_day = self.kwargs.get("lecture_day")
        lecture_day = LectureDay.objects.get(lecture__slug=lecture_slug, day=lecture_day)
        context['lecture_day'] = lecture_day
        context['check'] = lecture_day.is_available
        return context

    def form_valid(self, form):
        code = form.cleaned_data.get("code")
        lecture_slug = self.kwargs.get("lecture_slug")
        lecture_day = self.kwargs.get("lecture_day")
        lecture_day = LectureDay.objects.get(lecture__slug=lecture_slug, day=lecture_day)
        student = self.request.user
        if lecture_day.code == code:
            LecturePoll.objects.create(lecture_day=lecture_day, student=student, is_attended=True)
            messages.success(self.request, "Successfully added")
        else:
            messages.error(self.request, "Code Error")
        return super(LecturePollFormView, self).form_valid(form)
