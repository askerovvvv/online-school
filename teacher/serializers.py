from rest_framework import serializers

from teacher.models import TeacherInformation


class TeacherInfoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = TeacherInformation
        fields = "__all__"

