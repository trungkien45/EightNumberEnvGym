import gym
import numpy
from gym import spaces


class Eightnumber(gym.Env):
    """Custom Environment that follows gym interface"""
    metadata = {'render.modes': ['human']}
    """
    ACTION[0]: UP
    ACTION[1]: DOWN
    ACTION[2]: LEFT
    ACTION[3]: RIGHT
    """
    ACTION = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    T = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]]
    WIN = 9

    def __init__(self):
        # Define action and observation space
        # They must be gym.spaces objects
        array = numpy.array(self.T).flatten()
        numpy.random.shuffle(array)
        while (array.reshape(3, 3) == self.T).all() or not EightNum.isSolvable(array):
            numpy.random.shuffle(array)
        self.currentArray = array.reshape(3, 3)
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.MultiDiscrete([[9,9,9],
                                                       [9,9,9],
                                                       [9,9,9]])
        
        
    def step(self, action):
        """Run one timestep of the environment's dynamics. When end of
        episode is reached, you are responsible for calling `reset()`
        to reset this environment's state."""
        newArr = self.currentArray
        action1 = self.ACTION[action]
        x = numpy.where(newArr == 0)[0][0]
        y = numpy.where(newArr == 0)[1][0]

        x1 = x + action1[0]
        y1 = y + action1[1]

        if x1 < 0:
            x1 = 0
        if x1 > 2:
            x1 = 2
        if y1 < 0:
            y1 = 0
        if y1 > 2:
            y1 = 2
        newArr[x][y], newArr[x1][y1] = newArr[x1][y1], newArr[x][y]
        reward = numpy.sum(newArr == self.T)+0.0
        self.currentArray = newArr
        done = bool(reward == self.WIN)
        observation = self.currentArray
        return observation, reward, done, {}

    def reset(self):
        """Resets the state of the environment and returns an initial observation."""
        array = numpy.array(self.T).flatten()
        numpy.random.shuffle(array)
        while (array.reshape(3, 3) == self.T).all() or not EightNum.isSolvable(array):
            numpy.random.shuffle(array)
        self.currentArray = array.reshape(3, 3)
        observation = self.currentArray
        return observation  # reward, done, info can't be included

    def render(self, mode='human'):
        print(self.currentArray)
        
    def close(self):
        pass


class EightNum:
    @staticmethod
    def __getInvCount(array):
        inv_count = 0
        arr = array.flatten()
        for i in range(0, len(arr)-1):
            for j in range(i+1, len(arr)):
                if arr[i] != 0 and arr[j] != 0 and arr[i] > arr[j]:
                    inv_count += 1
        return inv_count

    @staticmethod
    def isSolvable(array):
        invCount = EightNum.__getInvCount(array)
        return (invCount % 2) == 0
