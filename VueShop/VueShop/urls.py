"""VueShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.contrib import admin
from django.conf.urls import url,include
from django.views.generic import TemplateView
from rest_framework_jwt.views import obtain_jwt_token

import xadmin
from VueShop.settings import MEDIA_ROOT

from django.views.static import serve
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from goods.views import GoodsListViewSet,CategoryViewSet,BannerViewSet,IndexCategoryViewSet
from rest_framework.routers import DefaultRouter
from users.views import SmsCodeViewSet,UserViewSet
from user_operation.views import UserFavViewset,LeavingMessageViewSet,AddressViewSet
from trade.views import ShoppingCartViewSet,OrderViewSet, AlipayView

router = DefaultRouter()
#配置goods的url
router.register(r'goods', GoodsListViewSet, base_name="goods")
#配置category的url
router.register(r'categorys', CategoryViewSet, base_name="categorys")
#
#router.register(r'code', SmsCodeViewSet, base_name="codes")
#
router.register(r'users', UserViewSet, base_name="users")
#收藏
router.register(r'userfav', UserFavViewset, base_name="userfavs")
#用户留言
router.register(r'message', LeavingMessageViewSet, base_name="message")
#收货地址
router.register(r'address', AddressViewSet, base_name="address")
#购物车url
router.register(r'shopcarts', ShoppingCartViewSet, base_name="shopcarts")
#订单相关
router.register(r'orders', OrderViewSet, base_name="orders")
#轮播图url
router.register(r'banners', BannerViewSet, base_name="banners")

#首页商品系列数据
router.register(r'indexgoods', IndexCategoryViewSet, base_name="indexgoods")



goods_list = GoodsListViewSet.as_view({
    'get':'list',
})

urlpatterns = [
    url('^xadmin/', xadmin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    #商品列表页
    url(r'^', include(router.urls)),
    url(r'^index/', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'doc/', include_docs_urls(title="fresh")),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^api-token-auth/', views.obtain_auth_token),
    # jwt的认证接口
    url(r'^login/', obtain_jwt_token),
    url(r'^alipay/return/', AlipayView.as_view(), name="alipay"),
    url(r'^ueditor/', include('DjangoUeditor.urls')),
]
