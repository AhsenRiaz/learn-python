import gym
import numpy as np
import random
from IPython.display import clear_output
from time import sleep

# Creating thr env
env = gym.make("Taxi-v2").env
env.s = 328
# Setting the number of iterations, penalties and reward to zero,
epochs = 0
penalties, reward = 0, 0
frames = []
done = False
while not done:
action = env.action_space.sample()
state, reward, done, info = env.step(action)
if reward == -10:
penalties += 1
# Put each rendered frame into the dictionary for animation
frames.append({
'frame': env.render(mode='ansi'),
'state': state,
'action': action,
'reward': reward
}
)
epochs += 1
print("Timesteps taken: {}".format(epochs))
print("Penalties incurred: {}".format(penalties))
# Printing all the possible actions, states, rewards.
def frames(frames):
for i, frame in enumerate(frames):
clear_output(wait=True)
print(frame['frame'].getvalue())
print(f"Timestep: {i + 1}")
print(f"State: {frame['state']}")
print(f"Action: {frame['action']}")
print(f"Reward: {frame['reward']}")
sleep(.1)
frames(frames)


# Init Taxi-V2 Env
env = gym.make("Taxi-v2").env
# Init arbitary values
q_table = np.zeros([env.observation_space.n, env.action_space.n])
# Hyperparameters
alpha = 0.1
gamma = 0.6
epsilon = 0.1
all_epochs = []
all_penalties = []
for i in range(1, 100001):
state = env.reset()
# Init Vars
epochs, penalties, reward, = 0, 0, 0
done = False

while not done:
if random.uniform(0, 1) < epsilon:
# Check the action space
action = env.action_space.sample()
else:
# Check the learned values
action = np.argmax(q_table[state])
next_state, reward, done, info = env.step(action)
old_value = q_table[state, action]
next_max = np.max(q_table[next_state])
# Update the new value
new_value = (1 - alpha) * old_value + alpha * \
(reward + gamma * next_max)
q_table[state, action] = new_value
if reward == -10:
penalties += 1
state = next_state
epochs += 1
if i % 100 == 0:
clear_output(wait=True)
print("Episode: {i}")
print("Training finished.")
