from rest_framework import routers
from .api import *


router = routers.DefaultRouter()
router.register('dictribution', DictributionViewSet, 'dictribution')
router.register('film', FilmViewSet, 'film')
router.register('activity', ActivityViewSet, 'activity')
router.register('message', MessageViewSet, 'message')

urlpatterns = router.urls
