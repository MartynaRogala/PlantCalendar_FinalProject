# E1
import datetime
import numpy as np
from datetime import timedelta
import pandas as pd
from ClassAction import Action

start = datetime.date(2021, 1, 1)
end = datetime.date(2021, 1, 16)

watering = 4
adding_fertilizer = 8
adding_hormone = 12
photo_interval = 5

timedelta_watering_interval = timedelta(days=watering)
timedelta_adding_fertilizer = timedelta(days=adding_fertilizer)
timedelta_adding_hormones = timedelta(days=adding_hormone)
timedelta_photo_interval = timedelta(days=photo_interval)

experiment_duration = end - start


def day_counter(start_date, end_date, interval):
    list = []
    while start_date <= end_date:
        start_date += interval
        list.append(start_date.strftime("%Y/%m/%d"))
    return list


list_watering = day_counter(start, end, timedelta_watering_interval)
list_fertilizer = day_counter(start, end, timedelta_adding_fertilizer)
list_hormone = day_counter(start, end, timedelta_adding_hormones)
list_photo = day_counter(start, end, timedelta_photo_interval)

list_of_events = list_watering + list_fertilizer + list_hormone + list_photo
print(list_of_events)
len = len(list_of_events)
print(len)

# list_of_events.sort(key=lambda x: x.date)
# print(list_of_events)


print("Normal watering: \n", list_watering)
print("Fertilizer watering:\n", list_fertilizer)
print("Hormone watering:\n", list_hormone)
print("Photo of the plants:\n", list_photo)


# Constructing DataFrame from a dictionary.
D = {"watering": list_watering, "fertilizer": list_fertilizer, "hormone": list_hormone, "photo": list_photo}
print("Dictionary:\n", D)
D_df = pd.DataFrame({key: pd.Series(value) for key, value in D.items()})
print("DataFrame: \n", D_df)

for i in D:

# for i in D_df.index:
#     print(D_df.get(i))


# Constructing DataFrame from a list of dictionaries.
# dictionary_watering = dict.fromkeys(list_watering, "watering")
# dictionary_fertilizer = dict.fromkeys(list_fertilizer, "fertilizer")
# dictionary_hormone = dict.fromkeys(list_hormone, "hormone")
# dictionary_photo = dict.fromkeys(list_photo, "photo")
#
# L = [dictionary_watering,dictionary_fertilizer,dictionary_hormone,dictionary_photo]
# df5 = pd.DataFrame(L, columns=['watering','fertilizer','hormone','photo'])   # 'columns' for proper column ordering
#
# print(df5)

# print(len(dictionary_watering.keys()))
# print(len(dictionary_fertilizer.keys()))
# print(len(dictionary_hormone.keys()))
# print(len(dictionary_photo.keys()))
#
#
# zip_dictionary = {**dictionary_watering, **dictionary_fertilizer, **dictionary_hormone, **dictionary_photo}
# print(zip_dictionary)
# print(len(zip_dictionary.keys()))
# print(sorted(zip_dictionary))
