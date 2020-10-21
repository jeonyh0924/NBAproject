from rest_framework import serializers

from .models import Player, Team


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['team', 'playin_time', 'FGP', 'T3PP', 'FTP', 'PPG', 'RPG', 'APG', 'BPG', 'name', 'back_number',
                  'position', 'first_name', 'last_name', 'height', 'weight', 'born', 'hometown', 'nba_debut',
                  'image']


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'team_image']
