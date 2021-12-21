#!/usr/bin/env python
# coding: utf-8

# ## Part 1.Foundations
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
