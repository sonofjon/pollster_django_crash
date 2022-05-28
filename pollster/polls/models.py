from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    answer_text = models.CharField(max_length=1000, default=None)
    image = models.ImageField(upload_to="images/", default=None)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
