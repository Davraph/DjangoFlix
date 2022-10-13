# Generated by Django 3.2b1 on 2021-03-17 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlists', '0008_tvshowproxy_tvshowseasonproxy'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='type',
            field=models.CharField(choices=[('MOV', 'Movie'), ('TVS', 'TV Show'), ('SEA', 'Season'), ('PLY', 'Playlist')], default='PLY', max_length=3),
        ),
    ]
