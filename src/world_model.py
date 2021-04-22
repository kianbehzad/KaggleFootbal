from geo import *
from kaggle_environments.envs.football.helpers import *


class WorldModel:
    def __init__(self):
        self.ball = Ball()
        self.our = list()
        self.opp = list()
        self.playmake = Agent()
        self.playmake_stickyactions = StickyActions()
        self.ball_ownership = False

    def our_num(self):
        """returns number of our active agents"""
        return len(self.our)

    def opp_num(self):
        """returns number of opp active agents"""
        return len(self.opp)

    def update_wm(self, obs):
        """update world model object with a given observation from environment"""

        self.ball.pos = Point(obs['ball'][0], obs['ball'][1], obs['ball'][2])
        self.ball.vel = Point(obs['ball_direction'][0], obs['ball_direction'][1], obs['ball_direction'][2])
        self.ball.rotation = Point(obs['ball_rotation'][0], obs['ball_rotation'][1], obs['ball_rotation'][2])

        Nour = len(obs['left_team'])
        for i in range(Nour):
            if not obs['left_team_active'][i]:
                continue
            agent = Agent()
            pos = obs['left_team'][i]
            agent.pos = Point(pos[0], pos[1], 0)
            vel = obs['left_team_direction'][i]
            agent.vel = Point(vel[0], vel[1], 0)
            agent.tiredness = obs['left_team_tired_factor'][i]
            agent.has_yellowcard = obs['left_team_yellow_card'][i]
            agent.id = i

            self.our.append(agent)

        Nopp = len(obs['right_team'])
        for i in range(Nopp):
            if not obs['right_team_active'][i]:
                continue
            agent = Agent()
            pos = obs['right_team'][i]
            agent.pos = Point(pos[0], pos[1], 0)
            vel = obs['right_team_direction'][i]
            agent.vel = Point(vel[0], vel[1], 0)
            agent.tiredness = obs['right_team_tired_factor'][i]
            agent.has_yellowcard = obs['right_team_yellow_card'][i]
            agent.id = i
            self.opp.append(agent)

        for agent in self.our:
            if agent.id == obs['active']:
                self.playmake = agent
                self.playmake_stickyactions.update(obs)

        self.ball_ownership = obs['ball_owned_team'] == 0


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
