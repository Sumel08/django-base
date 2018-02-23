from rest_framework import serializers
from . import models
from . import dao

class PingDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PingData
        fields = '__all__'

class PingDataGETSerializer(serializers.Serializer):

    def retrieve(self):
        ping_dao = dao.PingDao()
        result = ping_dao.retrieve(self.context.get('id'))
        return PingDataSerializer(result).data

    def list(self):
        ping_dao = dao.PingDao()
        result = ping_dao.list()
        return PingDataSerializer(result, many=True).data

class PingDataPOSTSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PingData
        fields = ('first_name', 'last_name')
        extra_kwargs = {
            'first_name': {
                'required': True
            },
            'last_name': {
                'required': True
            }
        }

    def create(self):
        ping_dao = dao.PingDao()
        result = ping_dao.create(self.data)

        return PingDataSerializer(result).data

class PingDataPATCHSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PingData
        fields = ('first_name', 'last_name')
        extra_kwargs = {
            'first_name': {
                'required': False
            },
            'last_name': {
                'required': False
            }
        }

    def partial_update(self):
        ping_dao = dao.PingDao()
        result = ping_dao.update(self.context.get('id'), self.data)

        return PingDataSerializer(result).data

    def delete(self):
        ping_dao = dao.PingDao()
        result = ping_dao.delete(self.context.get('id'))

        return PingDataSerializer(result).data
