import random


class Teacher:
    def __init__(self):
        self.groups = ["Group 1", "Group 2", "Group 3", "Group 4"]

    def sort(self, name):
        print(name, "is in", random.choice(self.groups))


teacher = Teacher()
teacher.sort("Esther")