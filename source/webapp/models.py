from django.db import models

DEFAULT_STATUS = 'active'
STATUS_CHOICES = (
    (DEFAULT_STATUS, ' Активно'),
    ('blocked', 'Заблокирвано'),
)


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя автора')
    email = models.EmailField(max_length=100, verbose_name='Электронная почта')
    text = models.TextField(max_length=2000, verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=20, verbose_name='Статус',
                              choices=STATUS_CHOICES, default=DEFAULT_STATUS)

    def __str__(self):
        return f'{self.name} - {self.text}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
