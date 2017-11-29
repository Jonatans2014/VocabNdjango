from django.db import models


""" Model to store data personal details from users  """
class User(models.Model):
    User_Auth_ID = models.IntegerField()
    User_Name = models.CharField(max_length=100)
    Age = models.IntegerField()
    User_Picture = models.ImageField()
    Email = models.EmailField(max_length=100)
    Gender = models.CharField(max_length=100)


    def __str__(self):
        return '%s' % (self.User_Name)


""" Model to store data Classfications from users  """
class Classification(models.Model):

    Classification = models.CharField(max_length=100)
    User = models.ManyToManyField(User, related_name='Classification')


    def __str__(self):
            return '%s' % (self.Classification)

""" Model to store words from users  """
class Word(models.Model):
    Class_Name = models.ForeignKey(Classification, related_name='Word', on_delete=models.CASCADE)
    Word = models.CharField(max_length=100)

    def __str__(self):
        return '%s' % (self.Word)



