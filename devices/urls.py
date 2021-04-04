from django.urls import path, include
from devices import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'devices', views.Devices)


urlpatterns = [
    path('send_update/', views.SendUpdate.as_view()),
    path('get_data/', views.GetData.as_view()),

]+ router.urls