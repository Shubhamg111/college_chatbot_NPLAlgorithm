
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    is_student = models.BooleanField(default=True)
    student_id = models.CharField(max_length=20, blank=True, null=True)
    faculty_id = models.CharField(max_length=20, blank=True, null=True)
    enrollment_year = models.PositiveIntegerField(blank=True, null=True)
    graduation_year = models.PositiveIntegerField(blank=True, null=True)
    course = models.CharField(max_length=100, blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    office_location = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)


from django.conf import settings
from django.db import models

class ChatMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()
    response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    conversation_id = models.CharField(max_length=255,null=True) 

    def __str__(self):
        return f'{self.user.username} - {self.message[:50]}'
