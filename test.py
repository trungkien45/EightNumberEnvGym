from eightNumber.envs.eightNumber import Eightnumber
env = Eightnumber()
# for _ in range(10):
#     env.step(env.action_space.sample())
print(env.observation_space.low)
#env.render()
#env.step(env.action_space.sample())
#env.render()