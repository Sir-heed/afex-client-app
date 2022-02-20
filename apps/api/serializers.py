from rest_framework import serializers
from apps.crm.models import Client, ClientWallet

class ClientWalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientWallet
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    wallet = ClientWalletSerializer(read_only=True, source='clientwallet')
    class Meta:
        model = Client
        fields = '__all__'