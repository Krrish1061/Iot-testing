from rest_framework import serializers
from .models import SensorValue, MachineDescription


class SensorValueSerializer(serializers.ModelSerializer):
    cboard = serializers.PrimaryKeyRelatedField(
        queryset=MachineDescription.objects.all(), source="machine_id"
    )
    field1 = serializers.FloatField(source="temperature")
    field2 = serializers.FloatField(source="humidity")
    field3 = serializers.ChoiceField(
        choices=SensorValue.is_power_available, source="mains"
    )

    class Meta:
        model = SensorValue
        fields = [
            "cboard",
            "field1",
            "field2",
            "field3",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["machine_id"] = data.pop("cboard")
        data["temperature"] = data.pop("field1")
        data["humidity"] = data.pop("field2")
        data["mains"] = data.pop("field3")
        return data
