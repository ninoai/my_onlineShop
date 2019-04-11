from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend, filters
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication

from .serializer import GoodsSerializer,CategorySerializer, BannerSerializer, IndexCategorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,mixins,generics
from rest_framework.pagination import PageNumberPagination
from .models import Goods, GoodsCategory, Banner
from .filters import GoodsFilter

class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "p"
    max_page_size = 100



class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,viewsets.GenericViewSet):
    """
    商品列表页，分页，搜索过滤，排序
    """
    queryset = Goods.objects.all().order_by('-add_time')
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination
    authentication_classes = (TokenAuthentication, )
    filter_backends = (DjangoFilterBackend,filters.SearchFilter, filters.OrderingFilter)
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief','goods_desc')
    ordering_fields = ('sold_num', 'add_time')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.click_num += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    list：
        商品分类列表数据
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer

class BannerViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    获取轮播图列表
    """
    serializer_class = BannerSerializer
    queryset = Banner.objects.all().order_by("index")


class IndexCategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    首页商品分类数据
    """
    queryset = GoodsCategory.objects.filter()
    serializer_class = IndexCategorySerializer
