########################################
# CS217:
# Assignment: Lab 6
# Author: James Burch
# Date: 12/15/2016
# File Name: GlobalFunctions.py
# Purpose: The purpose of this lab is to write and test a complete OOP that simulates a entertainment system.
########################################



def displayMainMenu():
    print("1)  Add Media Item to Collection\n"
          "2)  Delete Media Item from Collection\n"
          "3)  Play a Selection\n"
          "4)  Fast Forward a Selection\n"
          "5)  Rewind a Selection\n"
          "6)  List a Specific Media's Details\n"
          "7)  List all Medias Titles\n"
          "8)  Calculate Media Collection Investment\n"
          "9)  Calculate Total Playing Time of Collection\n"
          "10) Terminate Simulation")

def getMenuSelection():
    menuSelect=int(input("Enter your selection:"))
    while menuSelect < 0 or menuSelect > 10:
        menuSelect=int(input("Invalid Option! (Enter selection between 1 and 10):"))
    return menuSelect






