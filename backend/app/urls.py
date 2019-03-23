from rest_framework import routers
from .views import UserInfoViewSet, LikeViewSet

router = routers.DefaultRouter()
router.register('userInfo', UserInfoViewSet)
router.register('likes', LikeViewSet)
