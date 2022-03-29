from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from .forms import NotesForm
from .models import Note
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class NotesListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/notes_list.html"  # not necessary if we follow name convention
    login_url = "/login"

    def get_queryset(self):
        return self.request.user.notes.all()


class NotesCreateView(CreateView):
    model = Note
    form_class = NotesForm
    success_url = "/notes"
    template_name = "notes/notes_form.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesUpdateView(UpdateView):
    model = Note
    form_class = NotesForm
    success_url = "/notes"
    template_name = "notes/notes_form.html"


class NotesDeleteView(DeleteView):
    model = Note
    success_url = "/notes"
    template_name = "notes/note_delete.html"


class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = "notes/note_detail.html"
