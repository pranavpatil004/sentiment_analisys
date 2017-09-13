from rest_framework import serializers
from models import Stocks


class StockSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stocks
        fields = ('ticker', 'volume')
