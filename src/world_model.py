from geo import *

class Ball:
    def __init__(self):
        self.vel = Point(0, 0, 0)
        self.pos = Point(0, 0, 0)
        self.rotation = Point(0, 0, 0)


class Agent:
    def __init__(self):
        self.pos = Point(0, 0, 0)
        self.vel = Point(0, 0, 0)
        self.tiredness = 0.0
        self.has_yellowcard = False
        self.id = -1