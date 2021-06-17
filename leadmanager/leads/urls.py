from rest_framework import routers, urlpatterns
from .api import LeadViewset

router = routers.DefaultRouter()

# now we register our routes

# param 1: url endpoint, param2: viewSet, param3: name , which we will identify from dynamic url
router.register('api/leads', LeadViewset, 'lead')

urlpatterns = router.urls  # this will simply get the urls we register
