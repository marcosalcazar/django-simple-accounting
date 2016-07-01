# -*- coding: utf-8 -*-
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    UpdateView,
    ListView
)

from .models import (
	Account,
	JournalEntry,
	_JournalEntryDetail,
)


class AccountCreateView(CreateView):

    model = Account


class AccountDeleteView(DeleteView):

    model = Account


class AccountDetailView(DetailView):

    model = Account


class AccountUpdateView(UpdateView):

    model = Account


class AccountListView(ListView):

    model = Account


class JournalEntryCreateView(CreateView):

    model = JournalEntry


class JournalEntryDeleteView(DeleteView):

    model = JournalEntry


class JournalEntryDetailView(DetailView):

    model = JournalEntry


class JournalEntryUpdateView(UpdateView):

    model = JournalEntry


class JournalEntryListView(ListView):

    model = JournalEntry


class _JournalEntryDetailCreateView(CreateView):

    model = _JournalEntryDetail


class _JournalEntryDetailDeleteView(DeleteView):

    model = _JournalEntryDetail


class _JournalEntryDetailDetailView(DetailView):

    model = _JournalEntryDetail


class _JournalEntryDetailUpdateView(UpdateView):

    model = _JournalEntryDetail


class _JournalEntryDetailListView(ListView):

    model = _JournalEntryDetail

