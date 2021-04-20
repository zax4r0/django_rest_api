from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    Detaails = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# I konw this is not correct LOL i will add later
# also i have to app password and sessions auth nd many more
# will add step by step
