# Generated by Django 3.2 on 2021-04-18 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='QA_weightage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='developer',
            name='blog_weightage',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='developer',
            name='project_weightage',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
