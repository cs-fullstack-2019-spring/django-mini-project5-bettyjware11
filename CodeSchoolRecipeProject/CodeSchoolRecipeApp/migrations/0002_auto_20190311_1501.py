# Generated by Django 2.0.6 on 2019-03-11 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CodeSchoolRecipeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MealModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictureURL', models.CharField(default='', max_length=800)),
                ('shortDescription', models.CharField(default='', max_length=200)),
                ('dateCreated', models.DateField(default=django.utils.timezone.now)),
                ('creatorOfRecipe', models.CharField(default='Grunt', max_length=200)),
                ('directions', models.CharField(default='', max_length=1000)),
                ('ingredients', models.IntegerField(default=0)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Meal',
        ),
        migrations.DeleteModel(
            name='MealDetails',
        ),
    ]
