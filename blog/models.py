from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=14)
    slug = models.CharField(max_length=130)
    timeStamp = models.DateTimeField(blank=True)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to = 'blog/images', default = "")
    
    def __str__(self):
        return self.title + " by " + self.author

class Contact(models.Model):
     sno = models.AutoField(primary_key=True)
     name = models.CharField(max_length=255)
     phone = models.CharField(max_length=13)
     email = models.CharField(max_length=100)
     content = models.TextField()
     timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
     

     def __str__(self):
          return "Message from " + self.name + ' - ' + self.email


class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    #user=models.CharField(max_length=14)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp= models.DateTimeField(default=now)

    def __str__(self):
        return "Comment by " + ' - ' + self.post.author
        



