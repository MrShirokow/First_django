from django.urls import re_path
from skyeng.internal.views import ThemeListView, ThemeDetailView, LevelDetailView, CategoryListView, WordDetailView, WordListView


urlpatterns = [
    re_path(r'^themes/?$', ThemeListView.as_view()),
    re_path(r'^themes/(?P<theme_id>[0-9]*)/?$', ThemeDetailView.as_view()),
    re_path(r'^levels/?$', LevelDetailView.as_view()),
    re_path(r'^categories/?$', CategoryListView.as_view()),
    re_path(r'^words/?$', WordListView.as_view()),
    re_path(r'^words/(?P<word_id>[0-9]*)/?$', WordDetailView.as_view())
]
