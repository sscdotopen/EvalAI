# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-02 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("participants", "0005_remove_participantteam_challenge"),
        ("challenges", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="participant_teams",
            field=models.ManyToManyField(to="participants.ParticipantTeam"),
        )
    ]
