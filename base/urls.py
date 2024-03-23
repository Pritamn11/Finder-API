from django.urls import path 
from . import views 

urlpatterns = [
    path('api/', views.EventManageListCreate.as_view(), name='eventmanage'),
    path('event/find/<str:user_latitude>/<str:user_longitude>/<str:date>', views.EventFinderApi.as_view(), name='event_find'),

]