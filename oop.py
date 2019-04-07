class Human:
    def __init__(self, name):
        self.name = name
    def say_name(self):
        print(self.name)

nguoi_1 = Human("Hưng")
nguoi_2 = Human("Hưng").say_name()
nguoi_3 = Human("You are")
nguoi_3.name = "I am"
nguoi_3.say_name()