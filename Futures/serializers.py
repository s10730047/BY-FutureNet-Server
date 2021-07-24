from rest_framework import serializers
from Futures.models import Future


class FutureSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Future
        fields = ('id',
                  'Date',
                  'TAIEX',
                  'Fluctuation',
                  'ForeignInvestors',
                  'InvestmentTrust',
                  'Dealer',
                  'Margin',
                  'MarginChange',
                  'ShortSelling',
                  'ShortSellingChang',
                  'FuturesLongOpenPosition',
                  'FuturesShortOpenPosition',
                  'FuturesNet',
                  'FuturesLongVary',
                  'FuturesShortVary')