# _*_ coding: utf-8 _*_
__author__ = 'SimonWvW'
__date__ = '2018/12/5 12:34'

from django.conf.urls import url, include

from .views import CourseListView, CourseDetailView, ChapterInfoView, CommentsView, AddCommentsView

urlpatterns = [
    #课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),

    # 课程详情页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name="course_detail"),

    # 章节详情
    url(r'^info/(?P<chapter_id>\d+)/$', ChapterInfoView.as_view(), name="course_info"),

    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name="course_comments"),

    # 添加课程评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name="add_comment"),
]