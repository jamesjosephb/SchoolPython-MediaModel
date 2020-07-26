########################################
# CS217:
# Assignment: Lab 6
# Author: James Burch
# Date: 12/15/2016
# File Name: duration.py
# Purpose: The purpose of this lab is to write and test a complete OOP that simulates a entertainment system.
########################################


class Duration:
    def __init__(self, inMinutes = 1):
        self.setMinutes(inMinutes)

    def setMinutes(self, newMinutes):
        self.__minutes = newMinutes if newMinutes >= 1 else 1

    def getMinutes(self):
        return self.__minutes

    def __str__(self): #return string formatted as. HH:MM
        return "{:02d} : {:02d}".format(self.__minutes//60, self.__minutes%60)



if __name__ == '__main__':
    minutes = Duration(90)
    print(minutes)