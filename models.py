from django.db import models

# Create your models here.
class book(models.Model):
    Book_name=models.CharField(max_length=100)
    Author_name=models.CharField(max_length=100)
    Book_price = models.FloatField()
    Number_of_copies = models.PositiveIntegerField()
    



    book_assigned_to=models.CharField(max_length=100,default="anything")
    book_assigned_date=models.CharField(max_length=100,default="anything")



def __str__(self):
        return self.Book_name
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', null=True)
    author = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.question_text




class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
