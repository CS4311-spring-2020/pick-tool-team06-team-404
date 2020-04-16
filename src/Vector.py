from src import LogEntry


class Vector:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.root_dir = ''
        self.log_entries = []
