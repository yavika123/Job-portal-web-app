from django.db import models

# Create your models here.
class Job(models.Model):
    title=models.CharField(max_length=200)
    company=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    salary=models.IntegerField()
    descriptin=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    def  __str__(self):
        return self.title

        
class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name