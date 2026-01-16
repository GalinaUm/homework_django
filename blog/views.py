from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from blog.models import Blog


class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()
        return self.object


class BlogCreateView(CreateView):
    model = Blog
    fields = ("name", "description", "is_published",)
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("name", "description", "is_published",)
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse('blog:blog_details', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:blog_list")
