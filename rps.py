#!/usr/bin/env python2
#import random module to generate random number and time module for stopping the code at key points

import random
import time

#set variable values

rock = 1
paper = 2
scissors = 3

#rule dictionaries

names = {rock: "ROCK", paper: "PAPER", scissors: "SCISSORS"}
rules = {rock: scissors, scissors: paper, paper: rock }

#scores

player_score = 0
computer_score = 0

#start game

def start() :
    print "wanna play rock, paper, scissors?"
    while game():
        pass
    scores()

def game():
    player = move()
    computer = random.randint(1, 3)   #using random module
    result(player, computer)
    return play_again()

def move():
    while True:
        print 
        player = raw_input("Rock = 1\nPaper = 2\nScissors = 3\nMake A Move")
        try:
            player = int(player)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        print "please enter correct response!!"

def result():
    print "1..."
    time.sleep(1)
    print "2..."
    time.sleep(1)
    print "3!!"
    time.sleep(0.5)
    print "Computer threw {0}!".format(name[computer])  
    global player_score, computer_score
    if player == computer:
        print "Tie..."
    else:
        if rules[player] == computer:
            print "You Win!!"
            player_score += 1
        else :              
            print "HAHAHAHAHA, You LOSE!!"
            computer_score += 1

def play_again():
    answer = raw_input("Come on be a sport, play again, yes/no?")
    if answer in ("yes", "Yes","y","Y"):
        return answer
    else:
        print "See You next time!"

def scores():
    print "HIGH SCORES"
    print "player:", player_score
    print "computer:", computer_score

if __name__ == 'main' :
    start()    
