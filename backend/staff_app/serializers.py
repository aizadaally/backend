from rest_framework import serializers
from .models import Department, Record, Staff

class StaffSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Staff
        fields = ('__all__')

class RecordSerializer(serializers.ModelSerializer):
    # staff = StaffSerializer()
    # action = serializers.ChoiceField(choices=[("in", 'In'), ('out', 'Out')])
    class Meta:
        model = Record
        fields = ('__all__')

class DepartmentSerializer(serializers.ModelSerializer):
    # staff = StaffSerializer()
    # action = serializers.ChoiceField(choices=[("in", 'In'), ('out', 'Out')])
    class Meta:
        model = Department
        fields = ('__all__')