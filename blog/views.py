from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.core.mail import send_mail
from django.conf import settings

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
        if self.object.views_counter == 100:
            send_mail(
                'Количество просмотров = 100',
                'Вашу заметку посмотрели 100 раз, поздравляем!',
                settings.EMAIL_HOST_USER,
                [self.request.user.email],
                fail_silently=False,  # Set to True to suppress exceptions
            )

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
