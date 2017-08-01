#!/usr/bin/env python2
#import random module to generate random number and time module for stopping the code at key points

import random
import time

#set variable values

rock = 1
paper = 2
scissors = 3

#rule dictionaries

names = { rock: "Rock", paper: "Paper", scissors: "Scissors" }
rules = { rock: scissors, paper: rock, scissors: paper }

#scores

player_score = 0
computer_score = 0

#start game

def start():
    print "Let's play the game."
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(1,3)
    result(player, computer)
    return play_again()

def move():
    while True:
        print
        player = raw_input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print "Oops! Please enter valid number."

def result (player, computer):
    print "1..."
    time.sleep(1)
    print "2..."
    time.sleep(1)
    print "3!"
    time.sleep(0.5)
    print "Computer threw {0}!".format(names[computer])
    global player_score, computer_score
    if player == computer:
        print "Tie game."
    else:
        if rules[player] == computer:
            print "You win"
            player_score += 1
        else:
            print "You lose"
            computer_score += 1

def play_again():
    answer = raw_input("Would you like to play again? y/n: ")
    if answer in ("y", "Y", "Yes", "yes"):
        return answer
    else:
        print "Thank you for playing, Bye!"

def scores():
    global player_score, computer_score
    print "HIGH SCORES"
    print "Player: ", player_score
    print "Computer: ", computer_score

if __name__ ==  "__main__":
    start()
