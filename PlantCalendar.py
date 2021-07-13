import csv
from datetime import timedelta
from datetime import datetime
import pandas as pd


# Class for object called "Action":
class Action:
    def __init__(self, date, action_description, date_format):
        self.date = datetime.strptime(date, date_format)
        self.action_description = action_description

    def __repr__(self):
        return "{},{}".format(self.date, self.action_description)


# Starting data :
dateFormat = "%d.%m.%Y"
name_of_experiment = ""
start = datetime.strptime('1.1.2001', dateFormat)
end = datetime.strptime('1.1.2001', dateFormat)
watering = 0
adding_fertilizer = 0
adding_hormone = 0
photo_interval = 0

# Uploading data from csv file:
with open('plant.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        split = row[0].split(';')
        if line_count == 0:
            name_of_experiment = str(split[1])
        elif line_count == 1:
            start = datetime.strptime(split[1], dateFormat)
        elif line_count == 2:
            end = datetime.strptime(split[1], dateFormat)
        elif line_count == 3:
            watering = int(split[1])
        elif line_count == 4:
            adding_fertilizer = int(split[1])
        elif line_count == 5:
            adding_hormone = int(split[1])
        elif line_count == 6:
            photo_interval = int(split[1])
        line_count += 1

# Creating variables of time intervals of every action:
timedelta_watering_interval = timedelta(days=watering)
timedelta_adding_fertilizer = timedelta(days=adding_fertilizer)
timedelta_adding_hormones = timedelta(days=adding_hormone)
timedelta_photo_interval = timedelta(days=photo_interval)


# Creating a tool for making list of dates with their action description:
def day_counter(start_date, end_date, interval, description):
    """
    Creates a list of actions consisted of date and description.
    Data is created by adding subsequent dates every given interval.
    """
    list = []
    while start_date <= end_date:
        start_date += interval
        list.append(Action(start_date.strftime(dateFormat), description, dateFormat))
    return list


# Creating list of dates with their description:
actions = ["water the plants", "add fertilizer", "add hormones", "take photo"]
list_watering = day_counter(start, end, timedelta_watering_interval, actions[0])
list_fertilizer = day_counter(start, end, timedelta_adding_fertilizer, actions[1])
list_hormone = day_counter(start, end, timedelta_adding_hormones, actions[2])
list_photo = day_counter(start, end, timedelta_photo_interval, actions[3])

# Creating one list which contains dates with all actions:
list_of_events = list_watering + list_fertilizer + list_hormone + list_photo

# Inputing date by User to see what tasks needs to be done:
date = input("Enter date in DD.MM.YYYY format: ")
given_date = datetime.strptime(date, dateFormat)

# Creating loop for getting type of task for particular day:
action_existence = False
print("*" * 70, "\n\nTask to do in", "{:%Y-%m-%d}".format(given_date), ":")
for i in list_of_events:
    if given_date == i.date:
        action_existence = True
        print(i.action_description)
print("\n")
if not action_existence:
    print("There are no tasks scheduled for this day \n")

print("*" * 70)
# Additional operations on data:
experiment_duration = end - start

list_watering_before_date = day_counter(start, given_date, timedelta_watering_interval, actions[0])
list_fertilizer_before_date = day_counter(start, given_date, timedelta_adding_fertilizer, actions[1])
list_hormone_before_date = day_counter(start, given_date, timedelta_adding_hormones, actions[2])
list_photo_before_date = day_counter(start, given_date, timedelta_photo_interval, actions[3])

list_watering_after_date = day_counter(given_date, end, timedelta_watering_interval, actions[0])
list_fertilizer_after_date = day_counter(given_date, end, timedelta_adding_fertilizer, actions[1])
list_hormone_after_date = day_counter(given_date, end, timedelta_adding_hormones, actions[2])
list_photo_after_date = day_counter(given_date, end, timedelta_photo_interval, actions[3])

watering_before_date = len(list_watering_before_date)
fertilizer_before_date = len(list_fertilizer_before_date)
hormone_before_date = len(list_hormone_before_date)
photo_before_date = len(list_photo_before_date)

watering_after_date = len(list_watering_after_date)
fertilizer_after_date = len(list_fertilizer_after_date)
hormone_after_date = len(list_hormone_after_date)
photo_after_date = len(list_photo_after_date)

# Displaying information about experiment:
print("\nExperiment", name_of_experiment, "information:\n")
print("Beginning of the experiment: ", "{:%Y-%m-%d}".format(start))
print("Termination of rhe experiment: ", "{:%Y-%m-%d}".format(end))
print("Experiment duration: ", experiment_duration.days, "days")
print("\nTask day intervals:\n - Watering:", timedelta_watering_interval.days, "\n - Adding fertilizer:",
      timedelta_adding_fertilizer.days, "\n - Adding hormone:", timedelta_adding_hormones.days, "\n - Taking photos:",
      timedelta_photo_interval.days)
print("\nAmount of particular task during experiment:\n - Watering:", len(list_watering), "\n - Adding fertilizer:",
      len(list_fertilizer), "\n - Adding hormone:", len(list_hormone), "\n - Taking photos:", len(list_photo))
print("\nCompleted tasks until", "{:%Y-%m-%d}".format(given_date), ":\n - Watering:", watering_before_date,
      "\n - Adding fertilizer:",
      fertilizer_before_date, "\n - Adding hormone:", hormone_before_date, "\n - Taking photos:", photo_before_date)
print("\nTasks to be performed after", "{:%Y-%m-%d}".format(given_date), ":\n - Watering:", watering_after_date,
      "\n - Adding fertilizer:",
      fertilizer_after_date, "\n - Adding hormone:", hormone_after_date, "\n - Taking photos:", photo_after_date,"\n")

# Creating variables for making DataFrame from data:
w = []
f = []
h = []
p = []

for i in list_of_events:
    if i.action_description == actions[0]:
        w.append("{:%Y-%m-%d}".format(i.date))
    if i.action_description == actions[1]:
        f.append("{:%Y-%m-%d}".format(i.date))
    if i.action_description == actions[2]:
        h.append("{:%Y-%m-%d}".format(i.date))
    if i.action_description == actions[3]:
        p.append("{:%Y-%m-%d}".format(i.date))

# Creating DataFrame from dictionary:
D = {actions[0]: w, actions[1]: f, actions[2]: h, actions[3]: p}
D_df = pd.DataFrame({key: pd.Series(value) for key, value in D.items()})
print("*" * 70,"\n\nDates and actions: \n\n", D_df)
