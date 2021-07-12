# E1
import datetime
import numpy as np
from datetime import timedelta
import pandas as pd
from ClassAction import Action

start = datetime.date(2021, 1, 1)
end = datetime.date(2021, 1, 16)

watering = 2
adding_fertilizer = 4
adding_hormone = 8
photo_interval = 5

timedelta_watering_interval = timedelta(days=watering)
timedelta_adding_fertilizer = timedelta(days=adding_fertilizer)
timedelta_adding_hormones = timedelta(days=adding_hormone)
timedelta_photo_interval = timedelta(days=photo_interval)

experiment_duration = end - start


def day_counter(start_date, end_date, interval, description):
    list = []
    while start_date <= end_date:
        start_date += interval
        list.append(Action(start_date.strftime("%Y/%m/%d"), action_description=description))
    return list


list_watering = day_counter(start, end, timedelta_watering_interval, "watering")
list_fertilizer = day_counter(start, end, timedelta_adding_fertilizer, "adding fertilizer")
list_hormone = day_counter(start, end, timedelta_adding_hormones, "adding hormone")
list_photo = day_counter(start, end, timedelta_photo_interval, "taking photo")

list_of_events = list_watering + list_fertilizer + list_hormone + list_photo

# date = input("Enter date in YYYY-MM-DD format: ")
# year, month, day = map(int, date.split('-'))
# given_date = datetime.date(year, month, day).strftime("%Y/%m/%d")
given_date = datetime.date(2021,1,5).strftime("%Y/%m/%d")

No_action = False
print("Task to do in", given_date, ":")
for i in list_of_events:
    if given_date == i.date:
        print(i.action_description)
        No_action = True
if not No_action:
    print("There are no tasks scheduled for this day")

pd.read_csv("plant.csv")
