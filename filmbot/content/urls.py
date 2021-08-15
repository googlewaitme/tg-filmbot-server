from rest_framework import routers
from .api import *


router = routers.DefaultRouter()
router.register('api/dictribution', DictributionViewSet, 'dictribution')
router.register('api/film', FilmViewSet, 'film')
router.register('api/activity', ActivityViewSet, 'activity')
router.register('api/message', MessageViewSet, 'message')

urlpatterns = router.urls
