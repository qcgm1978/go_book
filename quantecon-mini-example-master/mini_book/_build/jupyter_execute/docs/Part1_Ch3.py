#!/usr/bin/env python
# coding: utf-8

# ## Part 1.Foundations
# ### Chapter 3. Implementing your first Go bot
# 
# #### This chapter covers
# - Implementing a Go board by using Python
# <br>
# 
# - Placing sequences of stones and simulating a game
# - Encoding Go rules for this board to ensure legal moves are played
# - Building a simple bot that can play against a copy of itself
# - Playing a full game against your bot

# In this chapter, you’ll build a flexible library that provides data structures to represent Go games and algorithms that enforce the Go rules. As you saw in the preceding chapter, the rules of Go are simple, but in order to implement them on a computer, you have to consider all the edge cases carefully. If you’re a novice to the game of Go or need a refresher of the rules, make sure you’ve read chapter 2. This chapter is technical and requires a good working knowledge of the Go rules to fully appreciate the details.
# 
# Representing the Go rules is immensely important, because it’s the foundation for creating smart bots. Your bot needs to understand legal and illegal moves before you can teach it good and bad moves.
# 
# At the end of this chapter, you’ll have implemented your first Go bot. This bot is still weak but has all the knowledge about the game of Go it needs to evolve into much stronger versions in the following chapters.
# 
# You’ll start by formally introducing the board and fundamental concepts used to play a game of Go with a computer: what is a player, a stone, or a move? Next, you’ll be concerned with game-play aspects. How can a computer quickly check which stones need to be captured or when the ko rule applies? When and how does a game come to an end? We’ll answer all these questions throughout this chapter.

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
