from gym.envs.registration import register

register(
    id='cheetah-hw4_part2-v0',
    entry_point='rob831.hw4_part2.envs.cheetah:HalfCheetahEnv',
    max_episode_steps=1000,
)
from rob831.hw4_part2.envs.cheetah.cheetah import HalfCheetahEnv
