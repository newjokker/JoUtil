import gym
import numpy as np

env = gym.make('FrozenLake-v1')

# 设置超参数
alpha = 0.1  # 学习率
gamma = 0.99  # 折扣率
epsilon = 0.1  # ε-greedy算法中的ε
q_table = np.zeros([env.observation_space.n, env.action_space.n])  # 初始化Q表

# 训练模型
for i_episode in range(1000):
    state = env.reset()[0]
    for t in range(100):
        env.render()
        if np.random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(q_table[state, :])
        next_state, reward, done, info = env.step(action)
        q_table[state, action] = (1 - alpha) * q_table[state, action] + alpha * (
                reward + gamma * np.max(q_table[next_state, :]))
        state = next_state
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break

# 测试模型
total_reward = 0
state = env.reset()
while True:
    env.render()
    action = np.argmax(q_table[state, :])
    state, reward, done, info = env.step(action)
    total_reward += reward
    if done:
        print("Total reward:", total_reward)
        break

env.close()
