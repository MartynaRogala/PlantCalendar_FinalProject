class Action:

    def __init__(self, date, action_description):
        self.date = date
        self.action_description = action_description

    def __repr__(self):
        return "{},{}".format(self.date, self.action_description)

    def printValues(self):
        print("date: " + self.date + " action: " + self.action_description)


