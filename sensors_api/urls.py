from django.urls import path
from sensors_api.views import SensorsAPIView,ReadingsAPIView

urlpatterns = [
	path('sensors/', SensorsAPIView.as_view()),
    path('readings/', ReadingsAPIView.as_view()),
]