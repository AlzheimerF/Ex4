from rest_framework import serializers
from . import models

class CheckerS(serializers.ModelSerializer):

    class Meta:
        model = models.CheckerForSelling
        fields = '__all__'


class CheckerB(serializers.ModelSerializer):

    class Meta:
        model = models.CheckerForBuying
        fields = '__all__'

