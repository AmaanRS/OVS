# Generated by Django 4.2.2 on 2023-06-22 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_candidate_delete_voter'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='promise',
            field=models.CharField(default='', max_length=200),
        ),
    ]