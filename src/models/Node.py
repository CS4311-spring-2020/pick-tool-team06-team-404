class Node:

    def __init__(self, log_entry):
        self.log_entry = log_entry
        self.icon = log_entry.icon
        self.color = log_entry.type
        self.x = 200
        self.y = 200
        self.rect = None
