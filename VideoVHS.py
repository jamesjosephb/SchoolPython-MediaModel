########################################
# CS217:
# Assignment: Lab 6
# Author: James Burch
# Date: 12/15/2016
# File Name: VideoVHS.py
# Purpose: The purpose of this lab is to write and test a complete OOP that simulates a entertainment system.
########################################

from media import Media
from duration import Duration


class VideoVHS(Media):
    def __init__(self, inTitle = "No title" ,inArtist = "No artist", inWherePurchased = "Unknown",
                 inCost = 0.0, inRunningTime = Duration(), inNumSelections = 1):
        super().__init__(inTitle, inArtist, inWherePurchased, inCost, inRunningTime)
        self.__numSelections = inNumSelections if inNumSelections > 0 else 1
        self.__currentSelection = 1

    def printMedia(self):
        print("___________________________")
        print("\tVideo VHS:")
        super().printMedia()
        print("Number of chapters:", self.__numSelections)

    def play(self):
        print("___________________________")
        if self.isMediaAtEnd() == False:
            print("Video VHS,", self.getTitle(), "by", self.getArtist(),
                  "playing selection:", self.__currentSelection)
            self.isMediaAtBeginning()
            self.__currentSelection += 1
            if self.__currentSelection > self.__numSelections:
                self.isMediaAtEnd()
                self.__currentSelection = self.__numSelections

        else:
            print("Video VHS is at the end -- rewind to enable playing selections")

    def fastForward(self):
        print("___________________________")
        if self.isMediaAtEnd() == False:
            print("Video VHS cassette,", self.getTitle(), "fast forwarding to end")
            self.isMediaAtBeginning()
            self.isMediaAtEnd()
            self.__currentSelection = self.__numSelections
        else:
            print("Video VHS cassette is at the end -- rewind to enable fast forwarding")

    def rewind(self):
        print("___________________________")
        if self.isMediaAtBeginning() == False:
            print("Video VHS cassette,", self.getTitle(), "rewinding to beginning")
            self.isMediaAtBeginning()
            self.isMediaAtEnd()
            self.__currentSelection = 1
        else:
            print("Video VHS cassette is at the beginning -- can't rewind")

