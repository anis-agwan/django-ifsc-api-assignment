from rest_framework import serializers
from .models import Bank, Branch

class BranchSerializer(serializers.HyperlinkedModelSerializer):
    bank = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Branch
        fields = (
            'id', 'ifsc_code', 'branchName', 'bank', 'branchAddress', 'branchCity', 'branchDistrict', 'branchState'
        )