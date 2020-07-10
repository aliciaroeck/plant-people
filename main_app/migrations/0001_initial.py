# Generated by Django 3.0.8 on 2020-07-10 19:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('full_name', models.CharField(max_length=50)),
                ('bio', models.TextField(blank=True, max_length=1000)),
                ('date_joined', models.DateField(default=django.utils.timezone.now)),
                ('image', models.ImageField(default='images/avatar.jpg', upload_to='images/profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
