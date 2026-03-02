from django.db import models

class Volunteer(models.Model):
    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    phone = models.CharField(max_length=30)
    telegram = models.CharField(max_length=100, blank=True)
    email = models.EmailField()
    study_work = models.CharField(max_length=255)

    english_level = models.CharField(max_length=100)
    additional_languages = models.CharField(max_length=255, blank=True)

    has_experience = models.BooleanField(default=False)
    previous_experience = models.TextField(blank=True)

    why_volunteer = models.TextField()
    cv_file = models.FileField(upload_to='cvs/')

    def __str__(self):
        return self.full_name