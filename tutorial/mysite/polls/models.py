from django.db import models
from django.utils import timezone

import datetime

# Create your models here.

class Question(models.Model): # For question database table
    question_text = models.CharField('question_text',max_length=200)
    pub_date = models.DateTimeField('date_published')

    def __str__(self) -> str: # represntation of object in django shell
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model): #for choice database table 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('choice_text', max_length=200)
    votes = models.IntegerField('votes', default=0)
    
    def __str__(self) -> str:
        return self.choice_text

