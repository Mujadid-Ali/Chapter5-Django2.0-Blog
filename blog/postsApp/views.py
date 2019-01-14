from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PostModel

class BlogListView(ListView):
    model = PostModel
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = PostModel
    template_name = 'post_detail.html'
    context_object_name = 'object'
class BlogCreateView(CreateView):
    model = PostModel
    template_name = 'post_new.html'
    fields = '__all__'
class BlogUpdateView(UpdateView):
    model = PostModel
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteVIew(DeleteView):
    model = PostModel
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')
# Create your views here.
