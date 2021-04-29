from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from .models import Developer


@receiver(pre_save, sender=Developer)
def pre_save_developer(sender, instance, **kwargs):
    score = 0

    rating1 = instance.blogs.rating
    w1 = instance.blog_weightage
    print("ratings for blog", rating1)

    rating2 = instance.project.rating
    w2 = instance.project_weightage

    rating3 = instance.question.QARating
    w3 = instance.QA_weightage

    score = rating2*w2*2 + rating1*w1*2 + rating3*w3*2
    instance.score = score
