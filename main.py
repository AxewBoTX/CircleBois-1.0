import pygame,os,time
from game import*

game = Game()

while game.running == True:
	#Checking if the Player is Starting the Game
	if game.starting == True:
		if game.playing == False:
			if game.won == False:
				if game.lost == False:
					game.starting_window()
	#Checking if the Player is Playering the Game
	if game.starting == False:
		if game.playing == True:
			if game.won == False:
				if game.lost == False:
					game.game_window()
	#Checking if the Player WON the Game
	if game.starting == False:
		if game.playing == False:
			if game.won == True:
				if game.lost == False:
					game.won_window()
	#Checking if the Player LOST the Game
	if game.starting == False:
		if game.playing == False:
			if game.won == False:
				if game.lost == True:
					game.lost_window()
