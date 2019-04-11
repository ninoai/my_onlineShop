# -*- coding:utf-8 -*-
from django.forms import model_to_dict

__author__ = 'catherine'
__date__ = '2019/3/27 4:04 PM'
from django.views.generic.base import View
from goods.models import Goods
from django.views.generic import ListView

class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        # json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        import json
        from  django.core import serializers
        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)
        from  django.http import JsonResponse
        return JsonResponse(json_data, safe=False)
