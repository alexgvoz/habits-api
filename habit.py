current_id = 1

class Habit:
    def __init__(self, title):
        global current_id
        self.id = current_id
        self.title = title
        current_id += 1

    def to_dict(self):
        return {"id": self.id, "title": self.title}