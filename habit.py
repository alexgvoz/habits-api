currentID = 1

class Habit:
    def __init__(self, title):
        global currentID
        self.id = currentID
        self.title = title
        currentID += 1

    def to_dict(self):
        return {"id": self.id, "title": self.title}