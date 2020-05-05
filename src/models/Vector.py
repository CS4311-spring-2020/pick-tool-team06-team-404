class Vector:

    def __init__(self, name, description):
        self.id = None
        self.name = name
        self.description = description
        self.log_entries = set()
        self.log_visible = set()
        self.nodes = []
        self.relationships = []
