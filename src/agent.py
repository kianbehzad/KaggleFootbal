from kaggle_environments.envs.football.helpers import *
from world_model import WorldModel

@human_readable_agent
def agent(obs):
    wm = WorldModel()
    wm.update_wm(obs)

    # Make sure player is running.
    if not wm.playmake_stickyactions.sprint:
        return Action.Sprint
    # We always control left team (observations and actions
    # are mirrored appropriately by the environment).
    controlled_player_pos = wm.playmake.pos
    # Does the player we control have the ball?
    if wm.ball_ownership:
        # Shot if we are 'close' to the goal (based on 'x' coordinate).
        if controlled_player_pos.r[0] > 0.5:
            return Action.Shot
        # Run towards the goal otherwise.
        return Action.Right
    else:
        # Run towards the ball.
        if wm.ball.pos.r[0] > controlled_player_pos.r[0] + 0.05:
            return Action.Right
        if wm.ball.pos.r[0] < controlled_player_pos.r[0] - 0.05:
            return Action.Left
        if wm.ball.pos.r[1] > controlled_player_pos.r[1] + 0.05:
            return Action.Bottom
        if wm.ball.pos.r[1] < controlled_player_pos.r[1] - 0.05:
            return Action.Top
        # Try to take over the ball if close to the ball.
        return Action.Slide