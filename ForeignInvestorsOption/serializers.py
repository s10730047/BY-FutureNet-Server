from rest_framework import serializers
from ForeignInvestorsOption.models import ForeignInvestorsOption


class ForeignInvestorOptionSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = ForeignInvestorsOption
        fields = ('id',
                  'Date',
                  'FuturesClosingPrice',
                  'Fluctuation',
                  'BuyCall',
                  'BuyCallChange',
                  'BuyPut',
                  'BuyPutChange',
                  'SellCall',
                  'SellCallChange',
                  'SellPut',
                  'SellPutChange',
                  'BuyNet',
                  'SellNet',
                  'BuyOpenPosition',
                  'SellOpenPosition')