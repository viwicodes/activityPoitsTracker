from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Student Profile
class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="student_profile")
    name = models.CharField(max_length=100, default="")
    email = models.EmailField()
    ph = models.CharField(max_length=12)
    sem = models.CharField(max_length=2)
    points = models.IntegerField(default=0)
    role = models.CharField(max_length=10, default="")

@receiver(post_save, sender=User)
def create_student_profile(sender, instance, created, **kwargs):
    if created:
        StudentProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_student_profile(sender, instance, **kwargs):
    instance.student_profile.save()


# Teacher Profile
class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="teacher_profile")
    name = models.CharField(max_length=100, default="")
    email = models.EmailField()
    ph = models.CharField(max_length=12)
    sem = models.CharField(max_length=2)
    points = models.IntegerField(default=0)
    role = models.CharField(max_length=10, default="")

@receiver(post_save, sender=User)
def create_teacher_profile(sender, instance, created, **kwargs):
    if created:
        TeacherProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_teacher_profile(sender, instance, **kwargs):
    instance.teacher_profile.save()

