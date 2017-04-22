from django.conf.urls import url
from education.views import LectureListView, LectureDayListView, LecturePollFormView


urlpatterns = [
	url(r'^$', LectureListView.as_view(), name="base"),
	url(r'^(?P<lecture_slug>[\w-]+)/$', LectureDayListView.as_view(), name="lecture_detail"),
	url(r'^(?P<lecture_slug>[\w-]+)/(?P<lecture_day>[\w-]+)/$', LecturePollFormView.as_view(), name="lecture_poll"),
]
