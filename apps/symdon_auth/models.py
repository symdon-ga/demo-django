from django.db import models

from django.contrib.auth import get_user_model


# Create your models here.
class UserLink(models.Model):
    class Meta:
        db_table = "userlink"
        unique_together = (
            "kind",
            "realm",
            "sub",
        )

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    kind = models.CharField(max_length=50, default="symdon")
    realm = models.CharField(max_length=50, default="")
    sub = models.CharField(max_length=50)

    access_token = models.CharField(max_length=500, default="")
    refresh_token = models.CharField(max_length=500, default="")

    def __str__(self):
        return f"{self.user.id} - {self.kind} / {self.realm} / {self.sub}"

    def clear_tokens(self):
        self.access_token = ""
        self.refresh_token = ""
        return self
