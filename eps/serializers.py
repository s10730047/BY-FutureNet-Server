from rest_framework import serializers
from eps.models import Eps


class EpsSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Eps
        fields = ('id',
                  'StockID',
                  'EPS2021Q1',
                  'EPS2020Q4',
                  'EPS2020Q3',
                  'EPS2020Q2',
                  'EPS2020Q1',
                  'EPS2019Q4',
                  'EPS2019Q3',
                  'EPS2019Q2',
                  'EPS2019Q1'
                  )

