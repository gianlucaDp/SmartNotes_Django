from django.shortcuts import render, get_object_or_404
from .models import Note
from django.views.generic import ListView, DetailView


class NotesListView(ListView):
    model = Note
    context_object_name = "notes"
    template_name = "notes/notes_list.html"  # not necessary if we follow name convention


class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note"
    template_name = "notes/note_detail.html"
