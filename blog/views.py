from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from blog.models import Blog


class BlogListView(ListView):
    model = Blog

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_counter += 1
        self.object.save()

        if self.object.views_counter == 100 and self.request.user.is_authenticated:
            send_mail(
                'Количество просмотров = 100',
                'Вашу заметку посмотрели 100 раз, поздравляем!',
                settings.EMAIL_HOST_USER,
                [self.request.user.email],
                fail_silently=True,
            )
        return self.object



class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    fields = ("name", "description", "is_published",)
    permission_required = 'blog.add_blog'
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    fields = ("name", "description", "is_published",)
    permission_required = 'blog.change_blog'
    success_url = reverse_lazy("blog:blog_list")

    def get_success_url(self):
        return reverse('blog:blog_details', args=[self.kwargs.get('pk')])


class BlogDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Blog
    permission_required = 'blog.delete_blog'
    success_url = reverse_lazy("blog:blog_list")
