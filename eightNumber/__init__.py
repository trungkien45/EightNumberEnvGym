from gym.envs.registration import register

register(
    id='eightNumber-v0',
    entry_point='eightNumber.envs:Eightnumber',
)