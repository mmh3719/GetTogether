# Generated by Django 2.0.12 on 2019-03-18 01:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0047_add_city_population'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventphoto',
            name='uploader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='event_photos', to='events.UserProfile'),
        ),
    ]
