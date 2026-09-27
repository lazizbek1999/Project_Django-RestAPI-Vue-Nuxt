from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=150)
    descr = models.TextField(max_length=250,blank=True,null=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='task_images/',blank=True,null=True)
    def __str__(self):
        return self.title