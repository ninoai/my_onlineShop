# -*- coding:utf-8 -*-
__author__ = 'catherine'
__date__ = '2019/4/2 3:43 PM'
from rest_framework import serializers
from .models import UserFav, UserLeavingMessage,UserAddress
from rest_framework.validators import UniqueTogetherValidator
from goods.serializer import GoodsSerializer

class UserFavDetailSerializer(serializers.ModelSerializer):

    goods = GoodsSerializer()
    class Meta:
        model = UserFav
        fields = ("goods", "id")

class UserFavSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    class Meta:
        model = UserFav

        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user','goods'),
                message ="已经收藏"
            )
        ]
        fields =("user", "goods", "id")

class LeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    class Meta:
        model = UserLeavingMessage
        fields = ("user","message_type", "subject","message","file","id", "add_time")

class AddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    class Meta:
        model = UserAddress
        fields = ("user", "province", "city", "district", "address", "signer_name", "signer_mobile","add_time")
