class Node:

    def __init__(self, log_entry):
        self.log_entry = log_entry
        self.icon = None
        self.x = 200
        self.y = 200

    def move(self, x, y):
        self.x = x
        self.y = y
