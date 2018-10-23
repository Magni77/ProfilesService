from rest_framework.fields import CharField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from profiles.models import Profile


class ProfileSerializer(ModelSerializer):
    full_name = SerializerMethodField()

    class Meta:
        model = Profile
        fields = '__all__'

    def get_full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"


class BasicProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'first_name',
            'last_name',
            'photo'
        )
