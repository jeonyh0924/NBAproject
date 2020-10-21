from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView

from members.models import Player, Team
from members.serializers import PlayerSerializer, TeamSerializer


class PlayerList(APIView):
    # def get_objects(self, pk):
    #     try:
    #         return Player.objects.get(pk=pk)
    #     except Player.DoesNotExist:
    #         raise Http404

    def get(self, request, format=None):
        player = Player.objects.all()
        serializer = PlayerSerializer(player, many=True)
        return Response(serializer.data)


class PlayerDetail(APIView):
    def get_objects(self, pk):
        try:
            return Player.objects.get(pk=pk)
        except Player.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        player = self.get_objects(pk)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)


class TeamList(APIView):
    def get(self, request, format=None):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)


class TeamDetail(APIView):
    def get_objects(self, pk):
        try:
            return Team.objects.get(pk=pk)
        except Team.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        team = self.get_objects(pk)
        serializer = TeamSerializer(team)
        return Response(serializer.data)
