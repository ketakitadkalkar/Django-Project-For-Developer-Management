# Generated by Django 3.2 on 2021-04-14 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tech', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('tech', models.CharField(max_length=200)),
                ('rating', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('answer', models.CharField(default=' ', max_length=200)),
                ('tech', models.CharField(default=' ', max_length=200)),
                ('QARating', models.IntegerField(default=1)),
                ('review', models.CharField(default=' ', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('experience', models.IntegerField()),
                ('score', models.FloatField(blank=True, null=True)),
                ('blogs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.blog')),
                ('domain', models.ManyToManyField(to='home.Domain')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.project')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.question')),
                ('technology', models.ManyToManyField(related_name='technology', to='home.Technology')),
            ],
        ),
    ]
