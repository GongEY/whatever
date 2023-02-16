# -*- coding: utf8 -*-
#!/usr/bin/python

import gym
from gym.envs.registration import register

register(
	id='FrozenLake8x8-v3',
	entry_point='gym.envs.toy_text:FrozenLakeEnv',
	kwargs={'map_name': '8x8',
			'is_slippery':True}
)

env = gym.make('FrozenLake8x8-v3')

# Your code start here...

import numpy as np
import random as rd

def random_argmax(vector) : #random argmax
    m = np.amax(vector)
    indices = np.nonzero(vector == m)[0]
    return rd.choice(indices)

#Initializing table with all zeros
Q = np.zeros([env.observation_space.n, env.action_space.n])

# Set learning parameters
alpha = 0.3
gamma = 0.8
num_episodes = 10000

for i in range(num_episodes):

    state = env.reset()
    done = False

    j = 0
    #The Q-Table learning algorithm
    while not done and j < 250:
        j += 1
        action = random_argmax(Q[state, :])
        if done and reward == None:
            reward = -1
        newState, reward, done, info = env.step(action)

        Q[state, action] = (1-alpha) * Q[state, action] + alpha*(reward + gamma*np.max(Q[newState, :]))
        #Q[state, action] = reward + gamma * np.max(Q[newState, :])
        state = newState


# Printing
state = env.reset()
time = -1
while time < num_episodes:
    time = time+1
    print("\n")
    print("#### {} action".format(time+1))
    env.render()
    action = random_argmax(Q[state, :])
    state, reward, done, info = env.step(action)
    #print(done)
    #print(state)
    #print(info)

    if done:
        #print(done)
        print(reward)
        print("\n")
        print("#### {} action".format(time + 2))
        env.render()
        print("END")
        break