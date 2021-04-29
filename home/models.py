from django.db import models

# Create your models here.
from django.db.models import CharField


class Technology(models.Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


class Domain(models.Model):
    name = CharField(max_length=200)

    def __str__(self):
        return self.name


class Question(models.Model):
    name = CharField(max_length=200)
    answer = CharField(max_length=200, default=' ')
    tech = models.CharField(max_length=200, default=' ')
    QARating = models.IntegerField(default=1)
    review = models.CharField(max_length=200, default=' ')

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = CharField(max_length=200)
    tech = CharField(max_length=200)
    rating = models.IntegerField()

    def __str__(self):
        return self.name


class Project(models.Model):
    name = CharField(max_length=200)
    tech = CharField(max_length=200)
    rating = models.IntegerField()

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = CharField(max_length=200)
    email = CharField(max_length=200)
    technology = models.ManyToManyField(Technology, related_name='technology')
    domain = models.ManyToManyField(Domain)
    location = CharField(max_length=200)
    experience = models.IntegerField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    blogs = models.ForeignKey(Blog, on_delete=models.CASCADE)
    project_weightage = models.IntegerField(null=True, blank=True)
    blog_weightage= models.IntegerField(null=True, blank=True)
    QA_weightage= models.IntegerField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = CharField(max_length=200)
    last_name = CharField(max_length=200)
    email = models.EmailField()
    username = CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username
