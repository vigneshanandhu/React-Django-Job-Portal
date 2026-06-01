from django.db import models
from django.contrib.auth.models import User
class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=200, blank=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Application(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
        ('hired', 'Hired'),
    ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    applied_at = models.DateTimeField(auto_now_add=True)