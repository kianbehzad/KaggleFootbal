from geo import *
from kaggle_environments.envs.football.helpers import *

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


class StickyActions:
    def __init__(self):
        self.top = False
        self.bottom = False
        self.left = False
        self.right = False

        self.top_left = False
        self.top_right = False
        self.bottom_left = False
        self.bottom_right = False

        self.sprint = False
        self.dribble = False

    def update(self, obs):
        self.top = Action.Top in obs['sticky_actions']
        self.bottom = Action.Bottom in obs['sticky_actions']
        self.left = Action.Left in obs['sticky_actions']
        self.right = Action.Right in obs['sticky_actions']
        self.top_left = Action.TopLeft in obs['sticky_actions']
        self.top_right = Action.TopRight in obs['sticky_actions']
        self.bottom_left = Action.BottomLeft in obs['sticky_actions']
        self.bottom_right = Action.BottomRight in obs['sticky_actions']
        self.sprint = Action.Sprint in obs['sticky_actions']
        self.dribble = Action.Dribble in obs['sticky_actions']
