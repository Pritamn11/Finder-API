import csv
import os
from base.models import EventManage


def run():
    file = open('scripts/gg_dataset.csv')
    read_file = csv.reader(file)
    # # Event.objects.all().delete()
    count = 1

    for data in read_file:
        if count == 1:
            pass
        else:
            print(data)
            EventManage.objects.create(event_name=data[0],
                    city_name=data[1],
                    date=data[2],
                    time=data[3],
                    latitude=data[4],
                    longitude=data[5],
                )
        count = count + 1

run()    