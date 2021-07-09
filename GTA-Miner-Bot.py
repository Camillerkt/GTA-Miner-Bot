#GTA SAMP Valiant - bot Mine by Camille Rakotoarisoa (https://camillerakoto.fr)

import os
import time
import platform
from pynput.keyboard import Key, Controller
keyboard = Controller()

class Carl:
	def __init__(self, kbrd_keys, start_waiting_time):
		self.kbrd_keys = kbrd_keys
		time.sleep(start_waiting_time)

	def run_forward(self, time_for_running):
		with keyboard.pressed(self.kbrd_keys['run_key']):
			with keyboard.pressed(self.kbrd_keys['straight_key']):
				time.sleep(time_for_running)

	def jump(self):
		with keyboard.pressed(self.kbrd_keys['jump_key']):
			time.sleep(1)

	def run_backward(self, time_for_running):
		with keyboard.pressed(self.kbrd_keys['back_key']):
			time.sleep(time_for_running)

	def mine(self, command):
		keyboard.press(self.kbrd_keys['tchat_key'])
		keyboard.release(self.kbrd_keys['tchat_key'])

		for char in command:
			keyboard.press(char)
			keyboard.release(char)

		keyboard.press(Key.enter)
		keyboard.release(Key.enter)

	def turn_left(self):
		with keyboard.pressed(self.kbrd_keys['left_key']):
			time.sleep(0.25)
		with keyboard.pressed(self.kbrd_keys['back_key']):  
			time.sleep(0.5)
 
 
#Change the Key.something with the key that you use for the action in your game
keyboard_keys_used = { "straight_key": Key.up, "back_key": Key.down, "left_key": Key.left, "jump_key": Key.shift, "run_key": Key.space, "tchat_key": 't' }
seconds_of_waiting_before_starting_the_bot = 5
number_of_blasts = 50

bot = Carl(keyboard_keys_used, seconds_of_waiting_before_starting_the_bot)
#The number in () are the number of seconds doing the action
#time.sleep means pause the person
for i in range(number_of_blasts): 
	bot.run_forward(2)
	time.sleep(0.5)
	#Change /mine with the command that you use for mine
	bot.mine('/mine')
	time.sleep(3)
	bot.turn_left()
	bot.run_backward(1)
	bot.jump()
	bot.run_backward(0.5)
	time.sleep(1)
