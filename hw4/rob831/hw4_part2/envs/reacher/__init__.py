from gym.envs.registration import register

register(
    id='reacher-hw4_part2-v0',
    entry_point='rob831.hw4_part2.envs.reacher:Reacher7DOFEnv',
    max_episode_steps=500,
)
from rob831.hw4_part2.envs.reacher.reacher_env import Reacher7DOFEnv
