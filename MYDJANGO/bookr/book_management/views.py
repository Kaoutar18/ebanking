from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views import View
from .forms import BookForm
from .models import Book


class BookFormView(FormView):
    template_name = 'book_form.html'
    form_class = BookForm
    success_url = reverse_lazy('form_success')

    # success_url ='/book_management/form_success'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class FormSuccessView(View):
    def get(self, request):
        return HttpResponse("Book record saved successfully")


class BookCreateView(CreateView):
    model = Book
    fields = ['name', 'author']
    template_name = 'book_form.html'
    success_url = reverse_lazy('form_success')
class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookListView(ListView):
        Model = Book
        queryset = Book.objects.order_by('name')
        context_object_name = 'book_list'
        template_name = 'book_list.html'

class BookUpdateView(UpdateView):
        model = Book
        fields =['name','author']
        template_name = 'book_form.html'
        success_url = '/book_management/form_success'

class BookDeleteeView(DeleteView):
    model = Book

    template_name = 'book_delete_form.html'
    success_url = reverse_lazy('Delete_success')
    success_url = '/book_management/delete_success'

class DeleteSucessView(View):
    def get(self, request , *args,**kwargs):
        return HttpResponse("Book record delete successfully")


