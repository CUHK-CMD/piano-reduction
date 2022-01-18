from gym import Env
from gym.spaces import Discrete, Box
import numpy as np
import math
from itertools import combinations
from datetime import datetime
from music21 import *

# from stable_baselines3 import DQN
from collections import deque
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.layers import Dense, Input, Flatten
from tensorflow.keras.optimizers import Adam
import random
import tqdm
from env_noOctave import SegmentationEnv
from DQNSolver import DQNSolver
from DQNLSTMSolver import DQNLSTMSolver
import pandas as pd


def round_offset(offset):
    return ((offset * 2) // 1) / 2


import glob

training_pieces = []
for piece in glob.glob("./normal/training/*"):
    training_pieces.append(piece)
# testing_pieces = []
# for piece in glob.glob('./testing/*'):
#     testing_pieces.append(piece)

env = SegmentationEnv(training_pieces)
agent = DQNLSTMSolver(env, n_episodes=3000, batch_size=64, timesteps=3)
loss = agent.run()

agent.model.save("dqn_lstm_4")
df = pd.DataFrame({"loss": loss})
df.to_csv("loss_dqnlstm_4.csv")

print("Training done!")
# env = SegmentationEnv(testing_pieces)

# for i in range(len(testing_pieces)):
#     obs = env.reset(i)
#     total_reward = 0
#     while True:
#         obs = obs.reshape((1, 12, 7))
#         action = np.argmax(agent.model.predict(obs))
#         obs, reward, done, info = env.step(action)
#         #env.render()
#         total_reward += reward
#         if done:
#             break
#     print(f"Piece {testing_pieces[i]}, total reward = {total_reward}")

# Changes:
# 1. Use huber loss
# 2. add observation with roughness
# 3. averaging the different cases
# 4,
