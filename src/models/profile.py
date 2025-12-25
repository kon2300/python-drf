from django.conf import settings
from django.db import models


class Profile(models.Model):
    """
    User に紐づくプロフィール情報
    """

    class Meta:
        db_table = "profiles"
        verbose_name = "プロフィール"
        verbose_name_plural = "プロフィール"
        ordering = ["id"]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )

    display_name = models.CharField(
        max_length=100,
        verbose_name="表示名",
    )

    detail = models.TextField(
        max_length=500,
        blank=True,
        verbose_name="詳細",
    )

    def __str__(self) -> str:
        return f"Profile(user_id={self.user_id}, display_name={self.display_name})"
