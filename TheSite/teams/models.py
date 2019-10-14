from django.db import models


class Team(models.Model):
    name_text = models.CharField(max_length=200)
    time_text = models.CharField(max_length=200)
    city_text = models.CharField(max_length=200)
    news_int = models.IntegerField(default=0)
    def __str__(self):
        return self.name_text


class Person(models.Model):
    question = models.ForeignKey(Team, on_delete=models.CASCADE)
    firstname_text = models.CharField(max_length=200, null=True)
    lastname_text = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.lastname_text


class News(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title_text = models.TextField(max_length=200)  # Field name made lowercase.
    posttime_text = models.TextField(max_length=200)  # Field name made lowercase.
    author_text = models.TextField(max_length=200)  # Field name made lowercase.
    content_text = models.TextField(max_length=200000)  # Field name made lowercase.

    def __str__(self):
        return self.title_text


class cNews(models.Model):
    cid = models.IntegerField(default=0)
    title_text = models.TextField(max_length=200)  # Field name made lowercase.
    posttime_text = models.TextField(max_length=200)  # Field name made lowercase.
    author_text = models.TextField(max_length=200)  # Field name made lowercase.
    content_text = models.TextField(max_length=200000)  # Field name made lowercase.

    def __str__(self):
        return self.title_text
