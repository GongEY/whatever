import gym

env = gym.make('Taxi-v2')

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
alpha = 0.2
gamma = 0.7
num_episodes = 2000

for i in range(num_episodes):

    state = env.reset()
    done = False

    j = 0
    #The Q-Table learning algorithm
    while not done and j < 250:
        j += 1
        action = random_argmax(Q[state, :])

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
        print("\n")
        print("#### {} action".format(time + 2))
        env.render()
        print("END")
        break