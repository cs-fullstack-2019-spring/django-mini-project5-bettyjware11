# Generated by Django 2.0.6 on 2019-03-11 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CodeSchoolRecipeApp', '0006_auto_20190311_1721'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipemodel',
            name='foreignkeyToUser',
        ),
    ]