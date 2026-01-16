from django.db import models

class Blog(models.Model):
    name = models.CharField(max_length=1000, verbose_name="Заголовок", help_text="заголовок")
    description = models.TextField(
        verbose_name="Ваша заметка", blank=True, null=True, help_text="Сообщение"
    )
    image = models.ImageField(
        upload_to="image/product/",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    is_published = models.BooleanField(
        default=False,
        verbose_name="Опубликовано"
    )

    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"
        ordering = ["name"]

    def __str__(self):
        return self.name



# дата создания,
# признак публикации (булевое поле),
# количество просмотров.