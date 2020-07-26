########################################
# CS217:
# Assignment: Lab 6
# Author: James Burch
# Date: 12/15/2016
# File Name: Lab 6.py
# Purpose: The purpose of this lab is to write and test a complete OOP that simulates a entertainment system.
########################################

from mediaCollection import MediaCollection
from GlobalFunctions import *

def main():
    newName = input("Enter the name of your media collection: ")
    myMediaCollection = MediaCollection(newName)
    menuChoice = 0
    while menuChoice != 10:
        print("___________________________________________________________")
        print("Welcome to the", myMediaCollection.getCollectionName(), "Media collection Menu")
        print("___________________________________________________________")
        displayMainMenu()
        menuChoice = getMenuSelection()
        if menuChoice == 1:
            myMediaCollection.addMedia()
        elif menuChoice ==2:
            myMediaCollection.deleteMedia()
        elif menuChoice ==3:
            myMediaCollection.play()
        elif menuChoice == 4:
            myMediaCollection.fastForward()
        elif menuChoice == 5:
            myMediaCollection.rewind()
        elif menuChoice == 6:
            myMediaCollection.printMediaDetails()
        elif menuChoice == 8:
            myMediaCollection.calculateTotalCollectionInvestment()
        elif menuChoice == 9:
            myMediaCollection.totalPlayingTime()
        elif menuChoice == 10:
            print("Terminating simulation")
            print("Thank you for playing the Entertainment Media collection Simulation")

main()








'''
C:\AppData\Local\Programs\Python\Python35-32\python.exe "E:/school/Python 3/Labs/Lab 6/Lab 6.py"
Enter the name of your media collection: My Entertaining Entertainment Collection
___________________________________________________________
Welcome to the My Entertaining Entertainment Collection Media collection Menu
___________________________________________________________
1)  Add Media Item to Collection
2)  Delete Media Item from Collection
3)  Play a Selection
4)  Fast Forward a Selection
5)  Rewind a Selection
6)  List a Specific Media's Details
7)  List all Medias Titles
8)  Calculate Media Collection Investment
9)  Calculate Total Playing Time of Collection
10) Terminate Simulation
Enter your selection:1
___________________________
Here are the valid media types:
	1: Audio Cassette
	2: Audio CD
	3: Video VHS
	4: Video DVD

Enter a media type selection (1 to 4):1
Enter the title of your  Audio Cassette :Play Deep
Next enter the media's artist: The Outfield
Next enter where the media was purchased:
Now enter the cost of the media,$ 9.99
Next enter the media's total running time(minutes): 36
Finally, enter the number of items on the media: 10
___________________________________________________________
Welcome to the My Entertaining Entertainment Collection Media collection Menu
___________________________________________________________
1)  Add Media Item to Collection
2)  Delete Media Item from Collection
3)  Play a Selection
4)  Fast Forward a Selection
5)  Rewind a Selection
6)  List a Specific Media's Details
7)  List all Medias Titles
8)  Calculate Media Collection Investment
9)  Calculate Total Playing Time of Collection
10) Terminate Simulation
Enter your selection:1
___________________________
Here are the valid media types:
	1: Audio Cassette
	2: Audio CD
	3: Video VHS
	4: Video DVD

Enter a media type selection (1 to 4):2
Enter the title of your  Audio CD :There is Nothing Left to Lose
Next enter the media's artist: Foo Fighters
Next enter where the media was purchased: Best Buy
Now enter the cost of the media,$ 14.99
Next enter the media's total running time(minutes): 42
Finally, enter the number of items on the media: 11
___________________________________________________________
Welcome to the My Entertaining Entertainment Collection Media collection Menu
___________________________________________________________
1)  Add Media Item to Collection
2)  Delete Media Item from Collection
3)  Play a Selection
4)  Fast Forward a Selection
5)  Rewind a Selection
6)  List a Specific Media's Details
7)  List all Medias Titles
8)  Calculate Media Collection Investment
9)  Calculate Total Playing Time of Collection
10) Terminate Simulation
Enter your selection:1
___________________________
Here are the valid media types:
	1: Audio Cassette
	2: Audio CD
	3: Video VHS
	4: Video DVD

Enter a media type selection (1 to 4):3
Enter the title of your  Video VHS :The Lion King
Next enter the media's artist: Disney
Next enter where the media was purchased: WalMart
Now enter the cost of the media,$ 8.50
Next enter the media's total running time(minutes): 89
Finally, enter the number of items on the media: 9
___________________________________________________________
Welcome to the My Entertaining Entertainment Collection Media collection Menu
___________________________________________________________
1)  Add Media Item to Collection
2)  Delete Media Item from Collection
3)  Play a Selection
4)  Fast Forward a Selection
5)  Rewind a Selection
6)  List a Specific Media's Details
7)  List all Medias Titles
8)  Calculate Media Collection Investment
9)  Calculate Total Playing Time of Collection
10) Terminate Simulation
Enter your selection:1
___________________________
Here are the valid media types:
	1: Audio Cassette
	2: Audio CD
	3: Video VHS
	4: Video DVD

Enter a media type selection (1 to 4):4
Enter the title of your  Videa DVD :A Knight's Tale
Next enter the media's artist: DreamWorks
Next enter where the media was purchased: Amazon
Now enter the cost of the media,$ 2.99
Next enter the media's total running time(minutes): 109
Finally, enter the number of items on the media: 12
___________________________________________________________
Welcome to the My Entertaining Entertainment Collection Media collection Menu
___________________________________________________________
1)  Add Media Item to Collection
2)  Delete Media Item from Collection
3)  Play a Selection
4)  Fast Forward a Selection
5)  Rewind a Selection
6)  List a Specific Media's Details
7)  List all Medias Titles
8)  Calculate Media Collection Investment
9)  Calculate Total Playing Time of Collection
10) Terminate Simulation
Enter your selection:2
___________________________
___________________________
 Here are the titles of the media currently in the collection:
	 1  Play Deep
	 2  There is Nothing Left to Lose
	 3  The Lion King
	 4  A Knight's Tale
Enter your selection: 3
___________________________________________________________
Welcome to the My Entertaining Entertainment Collection Media collection Menu
___________________________________________________________
1)  Add Media Item to Collection
2)  Delete Media Item from Collection
3)  Play a Selection
4)  Fast Forward a Selection
5)  Rewind a Selection
6)  List a Specific Media's Details
7)  List all Medias Titles
8)  Calculate Media Collection Investment
9)  Calculate Total Playing Time of Collection
10) Terminate Simulation
Enter your selection:3
___________________________
___________________________
 Here are the titles of the media currently in the collection:
	 1  Play Deep
	 2  There is Nothing Left to Lose
	 3  A Knight's Tale
Enter your selection: 3
___________________________
Video DVD, A Knight's Tale by DreamWorks playing chapters: 1
___________________________________________________________
Welcome to the My Entertaining Entertainment Collection Media collection Menu
___________________________________________________________
1)  Add Media Item to Collection
2)  Delete Media Item from Collection
3)  Play a Selection
4)  Fast Forward a Selection
5)  Rewind a Selection
6)  List a Specific Media's Details
7)  List all Medias Titles
8)  Calculate Media Collection Investment
9)  Calculate Total Playing Time of Collection
10) Terminate Simulation
Enter your selection:4
___________________________
___________________________
 Here are the titles of the media currently in the collection:
	 1  Play Deep
	 2  There is Nothing Left to Lose
	 3  A Knight's Tale
Enter your selection: 3
___________________________
Audio CD , A Knight's Tale fast forwarding to end
___________________________________________________________
Welcome to the My Entertaining Entertainment Collection Media collection Menu
___________________________________________________________
1)  Add Media Item to Collection
2)  Delete Media Item from Collection
3)  Play a Selection
4)  Fast Forward a Selection
5)  Rewind a Selection
6)  List a Specific Media's Details
7)  List all Medias Titles
8)  Calculate Media Collection Investment
9)  Calculate Total Playing Time of Collection
10) Terminate Simulation
Enter your selection:5
___________________________
___________________________
 Here are the titles of the media currently in the collection:
	 1  Play Deep
	 2  There is Nothing Left to Lose
	 3  A Knight's Tale
Enter your selection: 3
___________________________
Here are the valid media types:
	1: Audio Cassette
	2: Audio CD
	3: Video VHS
	4: Video DVD
Errant entry -- re-enter selection: 1
___________________________
Audio cassette is at the beginning -- can't rewind
___________________________________________________________
Welcome to the My Entertaining Entertainment Collection Media collection Menu
___________________________________________________________
1)  Add Media Item to Collection
2)  Delete Media Item from Collection
3)  Play a Selection
4)  Fast Forward a Selection
5)  Rewind a Selection
6)  List a Specific Media's Details
7)  List all Medias Titles
8)  Calculate Media Collection Investment
9)  Calculate Total Playing Time of Collection
10) Terminate Simulation
Enter your selection:6
___________________________
 Here are the titles of the media currently in the collection:
	 1  Play Deep
	 2  There is Nothing Left to Lose
	 3  A Knight's Tale
Enter your selection: 2
___________________________
	Audio CD:
Title:            	 There is Nothing Left to Lose
ArtistL           	 Foo Fighters
Where purchased:  	 Best Buy
Cost:             	 14.99
Running time:     	 00 : 42
Number of tracks: 11
___________________________________________________________
Welcome to the My Entertaining Entertainment Collection Media collection Menu
___________________________________________________________
1)  Add Media Item to Collection
2)  Delete Media Item from Collection
3)  Play a Selection
4)  Fast Forward a Selection
5)  Rewind a Selection
6)  List a Specific Media's Details
7)  List all Medias Titles
8)  Calculate Media Collection Investment
9)  Calculate Total Playing Time of Collection
10) Terminate Simulation
Enter your selection:7
___________________________________________________________
Welcome to the My Entertaining Entertainment Collection Media collection Menu
___________________________________________________________
1)  Add Media Item to Collection
2)  Delete Media Item from Collection
3)  Play a Selection
4)  Fast Forward a Selection
5)  Rewind a Selection
6)  List a Specific Media's Details
7)  List all Medias Titles
8)  Calculate Media Collection Investment
9)  Calculate Total Playing Time of Collection
10) Terminate Simulation
Enter your selection:8
___________________________
The total investment cost of collection = $ 27.97
___________________________________________________________
Welcome to the My Entertaining Entertainment Collection Media collection Menu
___________________________________________________________
1)  Add Media Item to Collection
2)  Delete Media Item from Collection
3)  Play a Selection
4)  Fast Forward a Selection
5)  Rewind a Selection
6)  List a Specific Media's Details
7)  List all Medias Titles
8)  Calculate Media Collection Investment
9)  Calculate Total Playing Time of Collection
10) Terminate Simulation
Enter your selection:9
___________________________
Total collection Time = 03 : 07
___________________________________________________________
Welcome to the My Entertaining Entertainment Collection Media collection Menu
___________________________________________________________
1)  Add Media Item to Collection
2)  Delete Media Item from Collection
3)  Play a Selection
4)  Fast Forward a Selection
5)  Rewind a Selection
6)  List a Specific Media's Details
7)  List all Medias Titles
8)  Calculate Media Collection Investment
9)  Calculate Total Playing Time of Collection
10) Terminate Simulation
Enter your selection:34
Invalid Option! (Enter selection between 1 and 10):10
Terminating simulation
Thank you for playing the Entertainment Media collection Simulation
'''