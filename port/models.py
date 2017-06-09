from django.db import models

class Code(models.Model):
    name = models.CharField(max_length=100)
    discribe = models.TextField(null=True)
    content = models.TextField(null=True)
    pub_time = models.DateTimeField(auto_now = True)
    def __str__(self):
        return self.name

class Port(models.Model):
    pname = models.CharField(max_length=100)
    url = models.TextField()
    data = models.TextField(null=True)
    type = models.IntegerField('0','1')
    result = models.CharField(max_length=500)

# Create your models here.
