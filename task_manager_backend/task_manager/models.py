from django.db import models

# Create your models here.


class TaskModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    priority = models.CharField(max_length=50, choices=
                                (('High','High'),
                                 ('Low','Low'),
                                 ('Medium','Medium')
                                 ))
    deadline = models.DateField()
    status =  models.CharField(max_length=50, choices=
                                (('Not-started','Not-started'),
                                 ('In-progess','In-progress'),
                                 ('Completed','Completed')
                                  ))
    
    
    
