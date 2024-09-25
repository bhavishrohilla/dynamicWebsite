from django.db import models

class Summary(models.Model):
    content = models.TextField()

class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.TextField()

    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    start_date = models.CharField(max_length=50)
    end_date = models.CharField(max_length=50, blank=True, null=True)  
    # Make this field optional
    description = models.TextField()

    def __str__(self):
        return self.company

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    graduation_date = models.CharField(max_length=50)
    gpa = models.CharField(max_length=90)

    def __str__(self):
        return self.institution