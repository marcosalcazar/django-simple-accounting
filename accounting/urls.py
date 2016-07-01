# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(
        regex="^Account/~create/$",
        view=views.AccountCreateView.as_view(),
        name='Account_create',
    ),
    url(
        regex="^Account/(?P<pk>\d+)/~delete/$",
        view=views.AccountDeleteView.as_view(),
        name='Account_delete',
    ),
    url(
        regex="^Account/(?P<pk>\d+)/$",
        view=views.AccountDetailView.as_view(),
        name='Account_detail',
    ),
    url(
        regex="^Account/(?P<pk>\d+)/~update/$",
        view=views.AccountUpdateView.as_view(),
        name='Account_update',
    ),
    url(
        regex="^Account/$",
        view=views.AccountListView.as_view(),
        name='Account_list',
    ),
	url(
        regex="^JournalEntry/~create/$",
        view=views.JournalEntryCreateView.as_view(),
        name='JournalEntry_create',
    ),
    url(
        regex="^JournalEntry/(?P<pk>\d+)/~delete/$",
        view=views.JournalEntryDeleteView.as_view(),
        name='JournalEntry_delete',
    ),
    url(
        regex="^JournalEntry/(?P<pk>\d+)/$",
        view=views.JournalEntryDetailView.as_view(),
        name='JournalEntry_detail',
    ),
    url(
        regex="^JournalEntry/(?P<pk>\d+)/~update/$",
        view=views.JournalEntryUpdateView.as_view(),
        name='JournalEntry_update',
    ),
    url(
        regex="^JournalEntry/$",
        view=views.JournalEntryListView.as_view(),
        name='JournalEntry_list',
    ),
	url(
        regex="^_JournalEntryDetail/~create/$",
        view=views._JournalEntryDetailCreateView.as_view(),
        name='_JournalEntryDetail_create',
    ),
    url(
        regex="^_JournalEntryDetail/(?P<pk>\d+)/~delete/$",
        view=views._JournalEntryDetailDeleteView.as_view(),
        name='_JournalEntryDetail_delete',
    ),
    url(
        regex="^_JournalEntryDetail/(?P<pk>\d+)/$",
        view=views._JournalEntryDetailDetailView.as_view(),
        name='_JournalEntryDetail_detail',
    ),
    url(
        regex="^_JournalEntryDetail/(?P<pk>\d+)/~update/$",
        view=views._JournalEntryDetailUpdateView.as_view(),
        name='_JournalEntryDetail_update',
    ),
    url(
        regex="^_JournalEntryDetail/$",
        view=views._JournalEntryDetailListView.as_view(),
        name='_JournalEntryDetail_list',
    ),
	]