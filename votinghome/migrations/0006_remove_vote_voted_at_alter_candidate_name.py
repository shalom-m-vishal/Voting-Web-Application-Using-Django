# Generated by Django 5.0.3 on 2024-03-30 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votinghome', '0005_remove_candidate_election_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='voted_at',
        ),
        migrations.AlterField(
            model_name='candidate',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
