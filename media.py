########################################
# CS217:
# Assignment: Lab 6
# Author: James Burch
# Date: 12/15/2016
# File Name: media.py
# Purpose: The purpose of this lab is to write and test a complete OOP that simulates a entertainment system.
########################################


from mediaCollection import *
from duration import Duration
from abc import ABCMeta, abstractmethod

class Media(metaclass = ABCMeta): #An Abstract Base Class
    def __init__(self, inTitle = "No title" ,inArtist = "No artist", inWherePurchased = "Unknown",
                 inCost = 0.0, inRunningTime = Duration()):
        self.__title = inTitle if len(inTitle)>0 else "No title"
        self.__artist = inArtist if len(inArtist) > 0 else "No Artist"
        self.__wherePurchased = inWherePurchased if len(inWherePurchased) > 0 else "Unknown"
        self.__cost = inCost if inCost >= 0.0 else 0.0
        self.__runningTime = inRunningTime
        self.__mediaAtBeginning = True
        self.__mediaAtEnd = False

    def __str__(self):
        return self.__title + '\n' + self.__artist + '\n' + self.__wherePurchased + "\n$" +\
            str(self.__cost) + '\n' + str(self.__runningTime)

    def getTitle(self):
        return self.__title
    def getArtist(self):
        return self.__artist
    def getWherePurchased(self):
        return self.__wherePurchased
    def getCost(self):
        return self.__cost
    def getRunningTime(self):
        return self.__runningTime
    def isMediaAtBeginning(self):
        return self.__mediaAtBeginning
    def isMediaAtEnd(self):
        return self.__mediaAtEnd

    def printMedia(self): #Prints common data fields to console output
        print("Title:            \t",self.__title)
        print("ArtistL           \t",self.__artist)
        print("Where purchased:  \t",self.__wherePurchased)
        print("Cost:             \t",str(self.__cost))
        print("Running time:     \t",str(self.__runningTime))

    @abstractmethod
    def play(self): # Can only play a media item if it is NOT at its end
        pass

    @abstractmethod
    def fastForward(self): # Can only fast-forward a media item if it is NOT at its end
       pass

    @abstractmethod
    def rewind(self): # Can only rewind a media item if it is NOT at its beginning
        pass