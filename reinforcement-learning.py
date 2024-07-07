import numpy as np
import random
import time
import gym

env = gym.make("Taxi-v3")
state = env.reset()
env.render()
print("Current state is  :", state)

state_size = env.observation_space.n

action_size = env.action_space.n

q_table = np.zeros((state_size, action_size))
episodes = 100000
learning_rate = 0.1
gamma = 0.7
epsilon = 0.1

def greedy_policy(state, table):
    z = np.random.random()
    if z > epsilon:
        action = np.argmax(table[state])
    else:
        action = env.action_space.sample()
    return action


deltas = []
for episode in range(1, episodes+1):
    state = env.reset()
    done = False
    step = 0
    change_t = 0
    
    if episode % 5000 == 0:
        print("Episode: {}".format(episode))
    while not done:
        #env.render()
        action = greedy_policy(state, q_table)
        new_state, reward, done, info = env.step(action)
        old_q = q_table[state, action]
        
        #Update
        q_table[state, action] += learning_rate * (reward + gamma * np.max(q_table[new_state, :]) - q_table[state, action])
        change_t = max(change_t, np.abs(q_table[state][action] - old_q))
        state = new_state
    deltas.append(change_t)
    if deltas[-1] < 0.000000001:
        break
    episode += 1
print("Maximum Difference is :", deltas[-1])

state = env.reset()
env.render()

from IPython.display import clear_output
import time

done = False
cumulative_reward = 0

while(done==False):
    best_action = np.argmax(q_table[state, :])
    
    state, reward, done, _ = env.step(best_action)
    
    cumulative_reward += reward
    time.sleep(0.5)
    clear_output(wait=True)
    env.render()
    print('Episode Reward :', cumulative_reward)
