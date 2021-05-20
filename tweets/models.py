from django.db import models


class Tweet(models.Model):
    tweet = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tweet
