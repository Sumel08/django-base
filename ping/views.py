from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions

from oauth2_provider.contrib.rest_framework import OAuth2Authentication

from . import serializers
from . import models
from . import dao
from facebook_auth import util

import facebook
# Create your views here.

class PingViewSet(viewsets.GenericViewSet):
    # serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    # authentication_classes = [OAuth2Authentication]
    #################################Servicios Generales#########################################
    ####################################CONSUMER#############################################
    serializer_class = serializers.PingDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [OAuth2Authentication]
    queryset = models.PingData.objects.all()

    def list(self, request):
        # # The following code is for testing facebook login with oauth social
        # print('Lemus Acá!!!!')
        # print(request.user)
        #
        # graph = facebook.GraphAPI('EAAK9u5tazckBAD9ggqeUllvGS6np5yklVXd53fuzY3f8YihsBF6WFc7NmYRR3ZCGuGJobj3eZAjbxBn4x8k57V6tTAzQaMkq1znJswVX1U5lLMv6DdQmvYCikbFV4dVorFs4kdgxfJQBwuczmZA5rhyTtUZAyZAYiEpVVZBcZBWkdiGb3Kmsx4osUq1xRZAY0CIZD')
        # args = {'fields': 'id,name,email,last_name,first_name,picture,age_range,gender'}
        #
        # profile = graph.get_object("me", **args)
        # print(profile)
        serializer = serializers.PingDataGETSerializer()
        try:
            result = serializer.list()
            return util.createResponse(True, 200, result, '')
        except Exception as err:
            return util.createResponse(False, 500, {}, str(err))

    def create(self, request):
        serializer = serializers.PingDataPOSTSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            result = serializer.create()
            return util.createResponse(True, 200, result, '')
        except Exception as err:
            return util.createResponse(False, 500, {}, str(err))

    def retrieve(self, request, pk):
        context = {
            'id': pk
        }
        serializer = serializers.PingDataGETSerializer(context=context)
        try:
            result = serializer.retrieve()
            return util.createResponse(True, 200, result, '')
        except models.PingData.DoesNotExist as err:
            return util.createResponse(False, 404, {}, str(err))
        except Exception as err:
            return util.createResponse(False, 500, {}, str(err))

    def partial_update(self, request, pk):
        context = {
            'id': pk
        }
        serializer = serializers.PingDataPATCHSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        try:
            result = serializer.partial_update()
            return util.createResponse(True, 200, result, '')
        except models.PingData.DoesNotExist as err:
            return util.createResponse(False, 404, {}, str(err))
        except Exception as err:
            return util.createResponse(False, 500, {}, str(err))

    def delete(self, request, pk):
        context = {
            'id': pk
        }
        serializer = serializers.PingDataPATCHSerializer(context=context)
        try:
            result = serializer.delete()
            return util.createResponse(True, 200, result, '')
        except models.PingData.DoesNotExist as err:
            return util.createResponse(False, 404, {}, str(err))
        except Exception as err:
            return util.createResponse(False, 500, {}, str(err))
