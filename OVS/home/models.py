from django.db import models

# Create your models here.
# Not Required now
# class Voter(models.Model):

#     id=models.AutoField(primary_key=True)
#     usrname=models.CharField(max_length=20)
#     password=models.CharField(max_length=20)

#     def __str__(self):
#         return self.name

class Candidate(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=20,default="")
    promise=models.CharField(max_length=200,default="")
    image=models.ImageField(upload_to='home/media',default="")
    votes=models.IntegerField(default=0)

    def __str__(self):
        return self.username
    
  
