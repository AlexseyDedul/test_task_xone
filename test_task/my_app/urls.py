
from rest_framework import routers

from .views import TransactionViewSet, CategoryViewSet, StatisticViewList
from django.urls import path

router = routers.DefaultRouter()
router.register(r'transaction', TransactionViewSet, basename='transaction')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'statistic', StatisticViewList, basename='statistic')

urlpatterns = router.urls

