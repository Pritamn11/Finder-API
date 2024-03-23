from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import EventManage
from .serializers import EventManageSerializer
from rest_framework import serializers
from datetime import datetime, timedelta
from rest_framework.exceptions import APIException
from .external_api import get_weather_conditions, calculate_distance
from math import ceil
# Create your views here.


class EventManageListCreate(generics.ListCreateAPIView):
    queryset = EventManage.objects.all()
    serializer_class = EventManageSerializer


class EventResponseSerializer(serializers.Serializer):
    events = EventManageSerializer(many=True)
    page = serializers.IntegerField()
    pageSize = serializers.IntegerField()
    totalEvents = serializers.IntegerField()
    totalPages = serializers.IntegerField()


class EventFinderApi(APIView):

    def get(self,request,user_latitude,user_longitude,date,*args, **kwargs):
        try:
            start_date = datetime.strptime(date, '%Y-%m-%d')
            end_date = start_date + timedelta(days=14)

            filtered_events = EventManage.objects.filter(date__range=(start_date, end_date)).order_by('date')
            
            event_data = []
            for event in filtered_events:
                event_name = event.event_name
                city = event.city_name
                date = event.date
                latitude = event.latitude
                longitude = event.longitude

                weather_report = get_weather_conditions(city=city, date=date)
                distance_data = calculate_distance(user_latitude=user_latitude, user_longitude=user_longitude, event_latitude=latitude, event_longitude=longitude)
                event_data.append({
                    'event_name': event_name,
                    'city_name': city,
                    'date': date,
                    'weather': weather_report['weather'],
                    "distance_km": distance_data['distance']
                    
                })

            totalEvents = filtered_events.count()
            pageSize = len(event_data)
                
            response_data = {
            'events': event_data,
            'page': 2,
            'pageSize': pageSize,
            'totalEvents': totalEvents,
            'totalPages': ceil(totalEvents / pageSize)
        }
        
            serializer = EventResponseSerializer(data=response_data)
            serializer.is_valid()  
            return Response(serializer.data)
        except ValueError:
            return Response({'error': 'Invalid date format. Please provide the date in the format YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            raise Response({'error': 'An unexpected error occurred.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



# @api_view(['GET' , 'POST' , 'PUT'])
# def test(request):
#     courses = { 
#     'course_name':'Python',
#     'learn' : ['flask' , 'Django', 'Tornado','FastAPI'],
#     'course_provider' : 'Scaler'
#     }

#     if request.method == 'GET' :
#         print( 'YOU HIT A GET METHOD' )
#         print(request.GET.get('search'))     # http://127.0.0.1:8000/test/?search=pritam
#         return Response (courses)
#     elif request.method == 'POST':
#         data = request.data
#         print('******')
#         print (data['name'])
#         print('******')
#         print( 'YOU HIT A POST METHOD' )
#         return Response (courses)
#     elif request.method =='PUT':
#         print('YOU HIT A PUT METHOD' )
#         return Response (courses)

