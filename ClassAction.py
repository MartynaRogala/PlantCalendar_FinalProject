from datetime import datetime


class Action:
    def __init__(self, date, action_description, date_format):
        self.date = datetime.strptime(date, date_format)
        self.action_description = action_description

    def __repr__(self):
        return "{},{}".format(self.date, self.action_description)
