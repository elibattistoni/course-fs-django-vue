from django.db import models


# class Journalist(models.Model):
#     first_name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=60)
#     biography = models.TextField(blank=True)

#     def __str__(self):
#         return f"{ self.first_name } { self.last_name }"


class Article(models.Model):
    # author = models.ForeignKey(
    #     Journalist, on_delete=models.CASCADE, related_name="articles"
    # )
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    body = models.TextField()
    location = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    #! datetime stamps
    #! created automatically when a new instance of the model Article is created
    created_at = models.DateTimeField(auto_now_add=True)
    #! automatically set every time an instance is saved
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{ self.author } { self.title }"
