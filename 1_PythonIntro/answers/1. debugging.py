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
# There are some bugs in the code below, and you have to fix them. Run the code and have a good look at the error message. Fix the bug and run the code again. In the end, you should be able to win the lottery every time (run your code multiple times), if you buy enough tickets.

# %%
def buy_tickets(n,nr_min=0,nr_max=1e9):
    return np.random.randint(nr_min,nr_max,size=n)

def draw_winner(nr_min=0,nr_max=1e9):
    return np.random.randint(nr_min,1e9)

def announce_results(tickets,winner):
    print("Is one of your {} tickets a winner??".format(len(tickets))
    if winner in tickets:
        print("Congratulations: you're a winner!!!!!")
    else
        print(Sorry, better luck next time...")

def play_lottery(ntickets,nr_min=0,nr_max=1e9):
    tickets = Buy_Tickets(nr_min,nr_max,ntickets)
    winner = draw_winner(nr_min,nr_max)
    announce_results(tickets,winner)

play_lottery(ntickets,0,10)


# %% [markdown]
# This line seems to be ok, so have a look at previous lines until you find an error. When you look carefully at the `print` statement in the previous line, you will see that there is a missing `)`.

# %%
def buy_tickets(n,nr_min=0,nr_max=1e9):
    return np.random.randint(nr_min,nr_max,size=n)

def draw_winner(nr_min=0,nr_max=1e9):
    return np.random.randint(nr_min,1e9)

def announce_results(tickets,winner):
    print("Is one of your {} tickets a winner??".format(len(tickets)))
    if winner in tickets:
        print("Congratulations: you're a winner!!!!!")
    else
        print(Sorry, better luck next time...")

def play_lottery(ntickets,nr_min=0,nr_max=1e9):
    tickets = Buy_Tickets(nr_min,nr_max,ntickets)
    winner = draw_winner(nr_min,nr_max)
    announce_results(tickets,winner)

play_lottery(ntickets,0,10)


# %% [markdown]
# There should be a `:` after `else`.

# %%
def buy_tickets(n,nr_min=0,nr_max=1e9):
    return np.random.randint(nr_min,nr_max,size=n)

def draw_winner(nr_min=0,nr_max=1e9):
    return np.random.randint(nr_min,1e9)

def announce_results(tickets,winner):
    print("Is one of your {} tickets a winner??".format(len(tickets)))
    if winner in tickets:
        print("Congratulations: you're a winner!!!!!")
    else:
        print(Sorry, better luck next time...")

def play_lottery(ntickets,nr_min=0,nr_max=1e9):
    tickets = Buy_Tickets(nr_min,nr_max,ntickets)
    winner = draw_winner(nr_min,nr_max)
    announce_results(tickets,winner)

play_lottery(ntickets,0,10)


# %% [markdown]
# The opening `"` is missing.

# %%
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
    tickets = Buy_Tickets(nr_min,nr_max,ntickets)
    winner = draw_winner(nr_min,nr_max)
    announce_results(tickets,winner)

play_lottery(ntickets,0,10)


# %% [markdown]
# The variable `ntickets` does not exist

# %%
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
    tickets = Buy_Tickets(nr_min,nr_max,ntickets)
    winner = draw_winner(nr_min,nr_max)
    announce_results(tickets,winner)

ntickets = 100
play_lottery(ntickets,0,10)


# %% [markdown]
# The name `Buy_Tickets` does not exist; the name `buy_tickets` does. Remember that Python is case sensitive!

# %%
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

ntickets = 100
play_lottery(ntickets,0,10)

# %% [markdown]
# Remember that `np` is commonly used as a shorthand for importing numpy. Numpy has not been imported in this notebook, so that is causing the problem.

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

ntickets = 100
play_lottery(ntickets,0,10)

# %% [markdown]
# Huh, we should be buying 100 tickets. When calling `buy_tickets`, the arguments are mixed up such that the number of tickets bought is set to `nr_min`. 

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
    tickets = buy_tickets(ntickets,nr_min,nr_max)
    winner = draw_winner(nr_min,nr_max)
    announce_results(tickets,winner)

ntickets = 100
play_lottery(ntickets,0,10)

# %% [markdown]
# There are 10 lottery number and we do not win with 100 tickets, strange. Maybe we need to buy even more tickets.

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
    tickets = buy_tickets(ntickets,nr_min,nr_max)
    winner = draw_winner(nr_min,nr_max)
    announce_results(tickets,winner)

ntickets = 10000
play_lottery(ntickets,0,10)

# %% [markdown]
# Ok, this is not making any sense. Remember that with 10000 tickets we expect to with $.1 \cdot 1000 = 100$ times. Looking at the code in more detail, we find an error in `draw_winner`; instead of using `nr_max` from the function arguments, the maximum value is set to 1e9.

# %%
import numpy as np

def buy_tickets(n,nr_min=0,nr_max=1e9):
    return np.random.randint(nr_min,nr_max,size=n)

def draw_winner(nr_min=0,nr_max=1e9):
    return np.random.randint(nr_min,nr_max)

def announce_results(tickets,winner):
    print("Is one of your {} tickets a winner??".format(len(tickets)))
    if winner in tickets:
        print("Congratulations: you're a winner!!!!!")
    else:
        print("Sorry, better luck next time...")

def play_lottery(ntickets,nr_min=0,nr_max=1e9):
    tickets = buy_tickets(ntickets,nr_min,nr_max)
    winner = draw_winner(nr_min,nr_max)
    announce_results(tickets,winner)

ntickets = 10000
play_lottery(ntickets,0,10)

# %% [markdown]
# Yes, we won!
