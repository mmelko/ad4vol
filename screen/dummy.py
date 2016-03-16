from screen.abstract import AbstractSreen
import os

'''
@Author mmelko 
Dummy screen implementation, mainly for testing purposes. Dummy screen shows
 information directly to console output '''

class DummyScreen (AbstractSreen):

    def display_string(self, string):
        print string

    def clean_screen(self):
        os.system('clear')
