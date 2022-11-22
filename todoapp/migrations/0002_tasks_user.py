# Generated by Django 4.1.3 on 2022-11-21 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.DO_NOTHING, related_name='users_task', to='authapp.users'),
            preserve_default=False,
        ),
    ]
