# Generated by Django 2.0.6 on 2019-03-11 14:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageURL', models.CharField(default='', max_length=800)),
                ('name', models.CharField(default='', max_length=200)),
                ('shortDescription', models.CharField(default='', max_length=200)),
                ('dateCreated', models.DateField(default=django.utils.timezone.now)),
                ('creatorOfRecipe', models.CharField(default='Grunt', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MealDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(default='', max_length=800)),
                ('name', models.CharField(default='', max_length=200)),
                ('ingredients', models.IntegerField(default=0)),
                ('dateCreated', models.DateField(default=django.utils.timezone.now)),
                ('creatorOfRecipe', models.CharField(default='Grunt', max_length=200)),
            ],
        ),
    ]
