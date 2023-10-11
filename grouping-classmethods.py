# how to call class methods using the class name or an instance of the class

import random


class Teacher:

    groups = ["Group 1", "Group 2", "Group 3", "Group 4"]
    # decorator

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.groups))


# calling a class method using class name
Teacher.sort("Melvin")


teacher = Teacher()
# calling a class method using an instance of our class
teacher.sort("Eunice")
print(teacher.groups)

# The class acts as a container for the functionality tteacher we need.
