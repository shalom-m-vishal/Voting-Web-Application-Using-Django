# Generated by Django 5.0.3 on 2024-03-30 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votinglogin', '0003_loginattempt'),
    ]

    operations = [
        migrations.CreateModel(
            name='loginForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='loginattempt',
            name='user',
        ),
        migrations.DeleteModel(
            name='CustomSession',
        ),
        migrations.DeleteModel(
            name='LoginAttempt',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
