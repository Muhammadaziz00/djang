from django.db import models

# Create your models here.
class Setting(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name = "Название курса",
    )

    description = models.TextField(
        verbose_name="Описание курса",
    )

    logo = models.ImageField(
        upload_to = "logo",
        verbose_name = "лаготип курса"
    )
    phone = models.CharField(
        max_length = 255,
        verbose_name = "телеыонный номер"
    )
    email = models.EmailField(
        verbose_name = "почта"
    )
    locate = models.CharField(
        max_length = 255,
        verbose_name="адрес"
    )
    facebook = models.URLField(
        verbose_name="сслылка на facebook"
    )
    instagram = models.URLField(
        verbose_name="сслыка на instagram"
    )
    youtube = models.URLField(
        verbose_name="ссылка на youtube"
    )
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "настройка"
        verbose_name_plural = "настройки"
