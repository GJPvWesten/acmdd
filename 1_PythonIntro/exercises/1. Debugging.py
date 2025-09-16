# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.2
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Let's play the lottery 
#
# because writing grant proposals just doesn't work

# %% [markdown]
# There are some bugs in the code below, and you have to fix them. Run the code and have a good look at the error message. Fix the bug and run the code again. In the end, you should be able to win the lottery, if you buy enough tickets.

# %%
import numpy as np 

def buy_tickets(n,nr_min=0,nr_max=1e9):
    return np.random.randint(nr_min,nr_max,size=n)

def draw_winner(nr_min=0,nr_max=1e9):
    return np.random.randint(nr_min,1e9)

def announce_results(tickets,winner):
    print("Is one of your {} tickets a winner??".format(len(tickets)))
    if winner in tickets:
        print("Congratulations: you're a winner!!!!!")
    else:
        print("Sorry, better luck next time...")

def play_lottery(ntickets,nr_min=0,nr_max=1e9):
    tickets = buy_tickets(nr_min,nr_max,ntickets)
    winner = draw_winner(nr_min,nr_max)
    announce_results(tickets,winner)

# First, define how many tickets you want. Let's say 100.
ntickets = 100

play_lottery(ntickets,0,10)

# %% [markdown]
# Notes for next year:
#
# * missing import may be too hard
# * functions are pretty complicated, make more explicit

# %%

# %%
