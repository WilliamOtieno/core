import json

from rest_framework import serializers

from .models import Visual, KenyanCase


class VisualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visual
        fields = '__all__'

    def to_representation(self, instance):
        """
        Convert data stored as String to Json
        """""
        data = super(VisualSerializer, self).to_representation(instance)

        recovery = json.loads(data.pop('recovery', None).replace("\'", "\""))
        death = json.loads(data.pop('death', None).replace("\'", "\""))
        case = json.loads(data.pop('case', None).replace("\'", "\""))

        extra_data = {
            "case": case,
            "recovery": recovery,
            "death": death
        }
        data.update(extra_data)
        return data


class KenyanCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = KenyanCase
        fields = '__all__'
