from django.shortcuts import render, get_list_or_404,get_object_or_404
from .models import Note
from .forms import *
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import DeleteView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


def home_authenticated(request):
    return render(request, 'dashboard/home_authenticated.html')


def home_not_authenticated(request):
    return render(request, 'dashboard/home_not_authenticated.html')


# using class based view.

# class NoteCreateView(CreateView):
#     template_name = 'dashboard/notes.html'
#     model = Note
#     fields = ['title','description','user']
#     # forms.fields['user'].widget = forms.HiddenInput()
#     success_url = 'notes'
    

# class NotesFormView(FormView):
#     template_name = 'dashboard/notes.html'
#     form_class = NotesForm
#     success_url = 'notes' 
    #def form_valid(self, form):
#         user = self.request.user
#         form.instance.user = user
#         form.save()
#         return super(NotesFormView, self).form_valid(form)
#         # # note = self.request.user
#         # form.save(get)      
#         # # import pdb;pdb.set_trace()
#         # # note = form.save()
#         # # note.user = self.request.user
#         # # note.save()
#         # return super().form_valid(form)


# class NotesFormView(FormView):
#     form_class = NotesForm
#     def get_form(self,form_class):
#         form = super(NotesFormView, self).get_form(form_class)
#         form.fields['user'].widget = forms.HiddenInput()
    # def get_initial(self):
#         initial = super(NotesFormView, self).get_initial()
#         initial['user'] = self.request.user


class NoteCreateView(SuccessMessageMixin,CreateView):
    template_name = 'dashboard/notes.html'
    model = Note
    fields = ['title','description']
    success_url = reverse_lazy('display_notes')
    success_message = "Note Saved Successfully."
    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        form.save()
        return super(NoteCreateView, self).form_valid(form)


class NoteDisplayView(ListView):
    model = Note
    paginate_by = 12
    template_name = 'dashboard/notes_display.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # note = Note.objects.filter(user = self.request.user )
        note = get_list_or_404(Note,user = self.request.user)
        context = {'note': note}
        return context


class NoteDetailView(DetailView):
    model =  Note
    template_name = 'dashboard/notes_detail.html'
    def detail_note(request,pk):
        note = get_object_or_404(Note, id=pk)
    

class NoteUpdateView(SuccessMessageMixin,UpdateView):
    model = Note
    template_name = 'dashboard/note_update.html'
    fields = ['title','description'] 
    success_url = reverse_lazy('display_notes')
    success_message = "Note Updated successfully."
    def update_note(request,pk):
        note = get_object_or_404(Note, id=pk)
    # def get_success_url(self):
    #     return reverse_lazy('display_notes')


class NoteDeleteView(SuccessMessageMixin,DeleteView):
    model = Note
    template_name = 'dashboard/note_delete.html'
    success_messages = "Note Delete Successfully."
    success_url = reverse_lazy('display_notes')
    def delete_note(request,pk):
        note = get_object_or_404(Note, id=pk)

    
# using fuction based view.

# def notes(request):
#     if request.method == "POST":
#         form = NotesForm(request.POST)
#         if form.is_valid():
#             notes = Note(user=request.user,title=request.POST['title'],description=request.POST['description'])
#             notes.save()
#         messages.success(request, f"Note saved from {request.user.username} successfully.")
#         return redirect('notes')
#     else:
#         form = NotesForm
#     notes = Note.objects.filter(user=request.user)
#     context = {'notes': notes,'form': form}
#     return render(request, 'dashboard/notes.html', context)


# def edit_note(request,pk):
#     note = Note.objects.get(id=pk)
#     form = NotesForm(instance=note)
#     if request.method == "POST":
#         form = NotesForm(request.POST, instance=note)
#         if form.is_valid():
#             form.save()
#         messages.success(request, f"Updated Note saved from {request.user.username} successfully.")
#         return redirect('notes')
#     context = {'form':form,}
#     return render(request, 'dashboard/edit_note.html', context)


# def delete_note(request,pk=None):   
#     Note.objects.get(id=pk).delete()
#     messages.success(request, f"Note Deleted from {request.user.username} successfully.")
#     return redirect('display_notes')




# https://www.geeksforgeeks.org/class-based-generic-views-django-create-retrieve-update-delete/