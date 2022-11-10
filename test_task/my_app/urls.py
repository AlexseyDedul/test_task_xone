
from rest_framework import routers

from .views import TransactionViewList, CategoryViewList

router = routers.DefaultRouter()
router.register(r'transaction', TransactionViewList, basename='transaction')
router.register(r'category', CategoryViewList, basename='category')

urlpatterns = router.urls

