class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype
    def driving(self):
        print("car is used for driving")

class audi(Car):
    def __init__(self, windows, doors, enginetype,speed):
        super().__init__(windows,doors,enginetype)
        self.speed=speed

audiq7=audi(4,5,"petrol",60)
print(audiq7.windows)
print(audiq7.doors)
print(audiq7.enginetype)
audiq7.driving()
