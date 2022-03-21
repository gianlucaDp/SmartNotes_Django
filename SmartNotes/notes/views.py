from django.shortcuts import render, get_object_or_404

from .forms import NotesForm
from .models import Note
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView


class NotesListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/notes_list.html"  # not necessary if we follow name convention


class NotesCreateView(CreateView):
    model = Note
    form_class = NotesForm
    success_url = "/notes"
    template_name = "notes/notes_form.html"


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
