from rest_framework import serializers

from skins_cs2.models import Skins


class SkinsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skins
        fields = ['name', 'float', 'rarity', 'pattern']