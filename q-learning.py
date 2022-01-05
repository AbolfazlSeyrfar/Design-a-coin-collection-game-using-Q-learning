# -*- coding: utf-8 -*-
"""
Created on Fri Nov 25 21:47:24 2021
@author: Abolfazl
"""

import numpy as np
import random

np.random.seed(0)
n = 5
G = 3
episode_len = 100
gamma = 0.9
eps = 0.2
# state = (row, col, coins)
# COLLECTION_POINT = top right at (1,5)
# HOME = down left at (5,1)
actions = ['U', 'D', 'L', 'R']
env = np.zeros((n,n))
s0 = (0, 0, 0)


def display(state):
    row, col, coins = state
    grid = np.full((n, n), np.nan)
    grid[0, -1] = 1
    grid[-1, 0] = -1
    grid[row, col] = coins
    print(f'{grid}\n\n')


def reset():
    return s0


def U(state):
    row, col, coins = state
    if row == 0:  # already at the 1st row
        return state, 0
    elif (row, col) == (1, n - 1):  # collect coins
        if coins == G:
            return state, 0
        else:
            coins += 1
            return (row, col, coins), 0
    else:  # just move up
        return (row - 1, col, coins), 0


def D(state):
    row, col, coins = state
    if row == n - 1:  # already at the last row
        return state, 0
    elif (row, col) == (n - 2, 0):  # deposit coins
        if coins == 0:
            return state, 0
        else:
            coins -= 1
            return (row, col, coins), 1
    else:  # just move down
        return (row + 1, col, coins), 0


def R(state):
    row, col, coins = state
    if col == n - 1:  # already at the last col
        return state, 0
    elif (row, col) == (0, n - 2):  # collect coins
        if coins == G:
            return state, 0
        else:
            coins += 1
            return (row, col, coins), 0
    else:  # just move right
        return (row, col + 1, coins), 0


def L(state):
    row, col, coins = state
    if col == 0:  # already at the 1st col
        return state, 0
    elif (row, col) == (n - 1, 1):  # deposit coins
        if coins == 0:
            return state, 0
        else:
            coins -= 1
            return (row, col, coins), 1
    else:  # just move left
        return (row, col - 1, coins), 0


def get_action(q_table, s, eps=0.):
    if random.random() > eps:
        return max(q_table[s], key=q_table[s].get)
    else:
        return random.choice(actions)


def do_action(a, s):
    return globals()[a](s)


def train():
    Q = {}
    for i in range(n):
        for j in range(n):
            for c in range(G + 1):
                Q[(i, j, c)] = {}
    for i in range(n):
        for j in range(n):
            for c in range(G + 1):
                for a in actions:
                    Q[(i, j, c)][a] = np.random.normal()
    lr = 0.9
    num_episodes = 100
    for i in range(num_episodes):
        s = reset()
        for _ in range(episode_len):
            a = get_action(Q, s, eps)
            s1, r = do_action(a, s)
            Q[s][a] = Q[s][a] + lr * (r + gamma * max(Q[s1].values()) - Q[s][a])
            s = s1
    return Q


def play(Q, verbose=False):
    total_r = 0
    s = reset()
    actionlist = []
    for i in range(episode_len):
        a = get_action(Q, s)
        actionlist.append(a)
        s1, r = do_action(a, s)
        total_r1 = total_r + gamma ** i * r
        if verbose:
            print(f'{total_r}, {a}')
            display(s)
        s = s1
        total_r = total_r1
    print(f'{actionlist}')
    return total_r


if __name__ == '__main__':
    Q = train()
    total_r = play(Q, verbose=True)
