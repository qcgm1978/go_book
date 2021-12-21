#!/usr/bin/env python
# coding: utf-8

# #### 3.1. Representing a game of Go in Python
# The game of Go is played on a square board. Usually, beginners start playing on a 9 × 9 or 13 × 13 board, and advanced and pro players play on a 19 × 19 board. But in principle, Go can be played on a board of any size. Implementing a square grid for the game is fairly simple, but you’ll need to take care of a lot of intricacies down the line.
# 
# You represent a Go game in Python by building a module we’ll call dlgo step-by-step. Throughout the chapter, you’ll be asked to create files and implement classes and functions that will eventually lead to your first bot. All the code from this and later chapters can be found on GitHub at http://mng.bz/gYPe.
# 
# Although you should definitely clone this repository for reference, we strongly encourage you to follow along by creating the files from scratch to see how the library builds up piece by piece. The master branch of our GitHub repository contains all the code used in this book (and more). From this chapter on, there’s additionally a specific Git branch for each chapter that has only the code you need for the given chapter. For instance, the code for this chapter can be found in branch chapter_3. The next chapters follow the same naming convention. Note that we’ve included extensive tests for most of the code found here and in later chapters in the GitHub repository.
# 
# To build a Python library to represent Go, you need a data model that’s flexible enough to support a few use cases:
# 
# - Track the progress of a game you’re playing against a human opponent.
# - Track the progress of a game between two bots. This might seem to be exactly the same as the preceding point, but as it turns out, a few subtle differences exist. Most notably, naive bots have a hard time recognizing when the game is over. Playing two simple bots against each other is an important technique used in later chapters, so it’s worth calling out here.
# - Compare many prospective sequences from the same board position.
# - Import game records and generate training data from them.
# 
# First, create a new folder, dlgo, and place an empty \__init__.py file into it to initiate it as a Python module. Also, create two additional files called gotypes.py and goboard_slow.py in which you’ll put all board- and game-play functionality. Your folder structure at this point should look as follows:

# 
# __dlgo__\
# $~~~~~~$ \_\___init____.$\color{brown}{\text{py}}$
# \
# $~~~~~~$ __gotypes__.$\color{brown}\text{py}$\
# $~~~~~~$ __goboard_slow__.$\color{brown}\text{py}$

# Black and white players take turns in Go, and you use `enum` to represent the different-colored stones. A `Player` is either `black` or `white`. After a player places a stone, you can switch the color by calling the `other` method on a `Player` instance. Put this `Player` class into gotypes.py.
# 
# 

# In[1]:


# Listing 3.1. Using an enum to represent players

import enum


class Player(enum.Enum):
    """ 
    >>> Player.black.value
    1
    """
    black = 1
    white = 2

    @property
    def other(self):
        return Player.black if self == Player.white else Player.white


# In[2]:


import doctest
doctest.testmod()

