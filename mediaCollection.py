########################################
# CS217:
# Assignment: Lab 6
# Author: James Burch
# Date: 12/15/2016
# File Name: mediaCollection.py
# Purpose: The purpose of this lab is to write and test a complete OOP that simulates a entertainment system.
########################################

from VideoDVD import *
from VideoVHS import *
from AudioCD import *
from audioCassette import *
from duration import Duration

class MediaCollection:
    def __init__(self, inCollectionName = None):
        if inCollectionName == None:
            self.__collectionName = input("Enter the name of the media collection: ")
        else:
            self.__collectionName = inCollectionName if len(inCollectionName) > 0 else "Unknown"
        self.__theCollection = []
        self.__MEDIA = ("Audio Cassette", "Audio CD" , "Video VHS" , "Videa DVD")

    def addMedia(self):
        media = self.__getMedia()
        self.__theCollection.append(media)

    # A hidden(i.e., private) method called by public method, addMedia(), to
    # interactively select a media type, input its data items and then build
    # and return an appropriate media object

    def __getMedia(self):
        mediaNum=-1
        while not(1 <= mediaNum <= 4):
            self.__displayMediaTypeMenu()
            mediaNum = int(input("\nEnter a media type selection (1 to 4):"))
        print("Enter the title of your ", self.__MEDIA[mediaNum-1],":", end='')
        title = input()
        artist = input("Next enter the media's artist: ")
        wherePurchased = input("Next enter where the media was purchased: ")
        cost = float(input("Now enter the cost of the media,$ "))
        while cost < 0.0: cost = float(input("Erant entry -- re-enter the cost (>= 0.0: "))
        minutes = int(input("Next enter the media's total running time(minutes): "))
        while minutes < 1: minutes = int(input("Errant entry -- re-enter running time in minutes( >= ): "))
        numItems = int(input("Finally, enter the number of items on the media: "))
        while numItems < 1: numItems = int(input("Errant entry -- re-enter number of items on media( >=1 ):"))
        if mediaNum == 1: return AudioCassette(title, artist, wherePurchased, cost, Duration(minutes), numItems)
        elif  mediaNum == 2: return AudioCD(title, artist, wherePurchased, cost, Duration(minutes), numItems)
        elif mediaNum == 3: return VideoVHS(title, artist, wherePurchased, cost, Duration(minutes), numItems)
        else: return VideoDVD(title, artist, wherePurchased, cost, Duration(minutes), numItems)

    # Another private method called by private method, __get Media()
    # This method lists the valid media types that can be added to the collection

    def __displayMediaTypeMenu(self):
        print("___________________________\nHere are the valid media types:")
        print("\t1: Audio Cassette")
        print("\t2: Audio CD")
        print("\t3: Video VHS")
        print("\t4: Video DVD")


    def __getMediaChoice(self):
        choice = int(input("Enter your selection: "))
        while not(1 <= choice <= len(self.__theCollection)):
            self.__displayMediaTypeMenu()
            choice = int(input("Errant entry -- re-enter selection: "))
        return choice



    def listMediaTitles(self):
        print("___________________________\n Here are the titles of the media currently in the collection: ")
        count = 1
        for aMedia in self.__theCollection:
            print('\t', count,"",aMedia.getTitle())
            count +=1


    def play(self):
        print("___________________________")
        self.listMediaTitles()
        choice = self.__getMediaChoice()
        self.__theCollection[choice - 1].play()

    def deleteMedia(self):
        print("___________________________")
        self.listMediaTitles()
        choice = self.__getMediaChoice()
        self.__theCollection.pop(choice - 1)

    def fastForward(self):
        print("___________________________")
        self.listMediaTitles()
        choice = self.__getMediaChoice()
        self.__theCollection[choice-1].fastForward()

    def rewind(self):
        print("___________________________")
        self.listMediaTitles()
        choice = self.__getMediaChoice()
        self.__theCollection[choice-1].rewind()

    def printMediaDetails(self):
        self.listMediaTitles()
        choice = self.__getMediaChoice()
        self.__theCollection[choice-1].printMedia()

    def calculateTotalCollectionInvestment(self):
        collectionCost = 0.0
        for media in range(len(self.__theCollection)):
            collectionCost += self.__theCollection[media].getCost()
        return print("___________________________\nThe total investment cost of collection = $",collectionCost)


    def totalPlayingTime(self):
        totalTime = 0.0
        for media in range(len(self.__theCollection)):
            totalTime += self.__theCollection[media].getRunningTime().getMinutes()
            totalTime = int(totalTime)
        return print("___________________________\nTotal collection Time =", Duration(totalTime))

    def setCollectionName(self, newName):
        self.__collectionName = newName

    def getCollectionName(self):
        return self.__collectionName

    def getCurrentMCSize(self):
        return len(self.__theCollection)



