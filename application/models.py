from django.db import models

# Create your models here.


class UserProfile(models.Model):
    name = models.CharField(default="TestUser", max_length=200)

    def __str__(self):
        return self.name


class BlogMetadata(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, blank=True, null=True)
    title = models.TextField()
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_data(self):
        dict = {}
        dict["user_name"] = self.user.name
        dict["title"] = self.title
        dict["body"] = self.body
