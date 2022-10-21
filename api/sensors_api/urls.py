from django.urls import path
from sensors_api.views import SensorsAPIView,ReadingsAPIView

urlpatterns = [
	path('sensors/', SensorsAPIView.as_view(), name='sensors'),
    path('readings/', ReadingsAPIView.as_view(), name='readings'),
]

#    for next time, turn extra_info into end-points like so:
#    path('readings/<str:metric>', ReadingsAPIView.as_view(), name='readings'),