from django.views.generic import ListView, DetailView

from .models import PostModel

class BlogListView(ListView):
    model = PostModel
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = PostModel
    template_name = 'post_detail.html'
    context_object_name = 'object'

# Create your views here.
