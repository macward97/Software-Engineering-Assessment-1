#API KEY OMDB: http://www.omdbapi.com/?i=tt3896198&apikey=e3fdfd9c OR e3fdfd9c
#API KEY THE MOVIE DB: 9d72cb6c12e587c90e7bf6f48c617b44
#Example URLs - OMDB: http://www.omdbapi.com/?i=tt0113375&apikey=e3fdfd9c AND themovieDB: https://api.themoviedb.org/3/movie/550?api_key=9d72cb6c12e587c90e7bf6f48c617b44
#Import Necessary Libraries

import json
import requests
import urllib.request, urllib.parse, urllib.error
import webbrowser
import http.client
import imdb
import sys
import time
import random

#API Keys for OMDB and The Movie DB

apiKeys = ["e3fdfd9c", "9d72cb6c12e587c90e7bf6f48c617b44"]

#Initialise array for movie title or id

movieInfo = ["placeholderTitle", "placeholderID", ""]

jSONData = []

#Initialise array for URL for omdb or moviedb

URL = ["https://www.omdbapi.com/", "https://api.themoviedb.org/3"]

#Initialises array for OMDb URL prefixs
#?s= being Title of film and ?i= being IMDB ID
#?s= prefix is now redundant because of the Title to IMDBID converter 
        
urlPrefixOMDb = ["?s=", "?i="]

#Function for generating random IMDB ID for random film selection

def GenerateIMDBID():

    imdbObject = imdb.IMDb()

    for x in range(1):
        movieInfo[1] = ("tt" + str(random.randint(0o000001,5734576)))

    

    UserInputParseTitle()
    print (movieInfo[1]);

    #searchResult = imdbObject.search_movie(movieInfo[1])
    
    #For Loop which places the real formatted film title into an array to take out of wishlist.txt.
    
    #for item in searchResult:
           #movieInfo[0] = str(item['title'])
           #movieInfo[1] = str("tt"+item.movieID)
           #break;

    return;

#Function for Parsing Title for Wishlist Films

def UserInputParseTitle():

    #Initialise IMDB object for accessing IMDB's database (hence no need for API Key for this specific instance)
    
    imdbObject = imdb.IMDb()
    
    #Searches Using the title inputted by user
    
    searchResult = imdbObject.search_movie(movieInfo[0])
    
    #For Loop which places the real formatted film title into an array to take out of wishlist.txt.
    
    for item in searchResult:
           movieInfo[0] = str(item['title'])
           movieInfo[2] = str(item['year'])
           break;

    return;

#Function for Acquiring Title when Searching for Film

def GetMovieTitle():

    for k,v in returnedJSON.items():
        movieInfo[0] = (v);
        #print (movieInfo[0]);
        break;

    return;

#Function for viewing WishList and Comments

def ViewUserWishList():

    print("||||||||||||||||||||||||||||||||||||||||||||");
    print("What would you like to do with your wishlist?")
    print("||||||||||||||||||||||||||||||||||||||||||||");
    wishlistSelection = input("1) View your list of films\n2) Remove a specific film\n3) Clear the entire wishlist\n4) Comments Facility\n5) Go back to Intro Screen\n")

    if wishlistSelection == "1" or wishlistSelection == "view":

        #Opens Up wishlist.txt and reads it into a variable
        
        file = open("wishlist.txt","r")
        data = file.read();
        print (data);
        file.close();

        ViewUserWishList()
        
    elif wishlistSelection == "2" or wishlistSelection == "remove":

        #Using the Title inputted, the real title will be returned from UserInputParseTitle()
        #Using the lines function, if a line has the inputted title in the wishlist.txt file, that line will be removed thus removing that film entry

        movieInfo[0] = input("Please type in the film you wish to remove from the wishlist\n")
        UserInputParseTitle()
        print (movieInfo[0]);

        file = open("wishlist.txt","r+")
        d = file.readlines()
        file.seek(0)
        for i in d:
            if i != movieInfo[0]+"\n":
                file.write(i)
        file.truncate()
        file.close()

        ViewUserWishList()

    elif wishlistSelection == "3" or wishlistSelection == "clear":

        #Clears text file by overwriting it with blank file

        open('wishlist.txt', 'w').close()
        print("Wish List is now cleared");

        ViewUserWishList()

    elif wishlistSelection == "4" or wishlistSelection == "comments":

        #Comments Facility

        print("||||||||||||||||||||||||||||||||||||||||||||");
        print("What would you like to do with comments?")
        print("||||||||||||||||||||||||||||||||||||||||||||");
        
        commentsSelection = input("1) Make a comment on a film\n2) View your comments\n3) Clear all comments\n")

        if commentsSelection == "1" or commentsSelection == "make":

            #Writes the comment with the user specified title and release date as well as the name of the user into comments.txt

            movieInfo[0] = input("Please type in the film you wish to make a comment on\n")
            UserInputParseTitle()
            comment = input("Please type in the comment you wish to make on this film\n");
            name = input("Please type in your name\n");

            with open("comments.txt", "a") as file:
               file.write(movieInfo[0]+" ("+movieInfo[2]+")"+" - "+"User "+name+" said: "+"'"+comment+"'"+"\n")
               file.close()

            ViewUserWishList
        
        elif commentsSelection == "2" or commentsSelection == "view":

            #Opens Up comments.txt and reads it into a variable
        
            file = open("comments.txt","r")
            data = file.read();
            print (data);
            file.close();

            ViewUserWishList

        elif commentsSelection == "3" or commentsSelection == "clear":

            #Clears text file by overwriting it with blank file
        
            open('comments.txt', 'w').close()
            print("Comments are now cleared");

            ViewUserWishList
            

    elif wishlistSelection == "5" or wishlistSelection == "back":

        #Goes back to start of program

        GenerateURLBasedOnUserSelection()

    GenerateURLBasedOnUserSelection()

#Function for Adding Searched Film to WishList

def AddToWishList():

    #Writes title of film into wishlist.txt and goes to start of program

    print("Film is now added into your wishlist which you can view by going back to the intro screen");

    with open("wishlist.txt", "a") as file:
       file.write(movieInfo[0]+"\n")
       file.close()

    GenerateURLBasedOnUserSelection()

#Function for Converting User Specific Title into the First Result's IMDB ID (for better accuracy when extracting data). This function uses IMDBpy functions
    
def ConvertTitleToIMDBID():

    #Initialise IMDB object for accessing IMDB's database (hence no need for API Key for this specific instance)
    
    imdbObject = imdb.IMDb()
    
    #Searches Using the Title inputted by user
    
    searchResult = imdbObject.search_movie(movieInfo[0])
    
    #For Loop which places the movieID of the searched movie (if title is valid) into an array. Only obtains the first result for accuracy, breaks after one loop. Obtained ID is also converted to string and has the prefix tt applied to it for use in URL parsing.
    
    for item in searchResult:
           movieInfo[1] = str("tt"+item.movieID)
           break;

    return;

#Main Function For the URL Generation/Parsing
        
def GenerateURLBasedOnUserSelection():

    #Allows the parsedURL to be used in other functions (outside this function)
    
    global parsedURL
    global userSelectionForOMDbORthemoviedb
    parsedURL = None;
    print("||||||||||||||||||||||||||||||||||||||||||||");
    print("Welcome to our Movie Information Client!\nDo you want to search or view your wish list?")
    print("||||||||||||||||||||||||||||||||||||||||||||");
    introductionSelection = input("1) Search for a film\n2) View your Wish List\n3) Exit The Program\n")
    

    #If Statement based on User Selection on Introduction Query

    if introductionSelection == "1" or introductionSelection == "search":
        print("FILM SEARCH");
        
    elif introductionSelection == "2" or introductionSelection == "wish list":
        
        ViewUserWishList()
    elif introductionSelection == "3" or introductionSelection == "exit":
        
        sys.exit()
        
    
    #User Website Selection (OMDb/IMDb or The Movie DB)
    
    userWebsiteSelection = input("What website would you like to search?\n 1) Using OMDb \n 2) Using themoviedb\n")

    #If Statement based on User Selection on OMDb or The Movie DB

    if userWebsiteSelection == "1" or userWebsiteSelection == "omdb":
        userSelectionForOMDbORthemoviedb = 0
    elif userWebsiteSelection == "2" or userWebsiteSelection == "the movie database":
        userSelectionForOMDbORthemoviedb = 1

    #User Choice for searching by Title or ID
        
    userSelectionTitleOrID = input("How would you like to search?\n 1) By Title\n 2) By IMDB ID\n 3) By Generated Random IMDbID\n")

    #If Statement Which determines the values for the Title or Movie ID

    if userSelectionTitleOrID == "1" or userSelectionTitleOrID == "title":
        movieInfo[0] = input("Please enter the title you want to search by (e.g. The Godfather) \n")
        #When Title is converted to ID (ConvertTitleToIMDBID()), the URL parsing will use the ID instead of the title
        ConvertTitleToIMDBID()
        userSelectionForTitleOrID = 1
    elif userSelectionTitleOrID == "2" or userSelectionTitleOrID == "imdb id":
        userSelectionForTitleOrID = 1
        movieInfo[1] = input("Please enter the IMDB ID (e.g. tt0068646) you want to search by\n")
    elif userSelectionTitleOrID == "3" or userSelectionTitleOrID == "random":
        userSelectionForTitleOrID = 1
        userSelectionForOMDbORthemoviedb = 0
        GenerateIMDBID()
        
        

    #Initialises array for The Movie DB prefixs

    urlPrefixTheMovieDB = ["/search/movie?api_key="+apiKeys[1]+"&query="+movieInfo[userSelectionForTitleOrID], "/movie/"+movieInfo[userSelectionForTitleOrID]+"?api_key="+apiKeys[1]]

    #If Statement That Parses the URLs (based on User Selection) Using The above variables and array indices

    if userSelectionForOMDbORthemoviedb == 0:
        parsedURL = URL[userSelectionForOMDbORthemoviedb]+urlPrefixOMDb[userSelectionForTitleOrID]+movieInfo[userSelectionForTitleOrID]+"&apikey="+apiKeys[userSelectionForOMDbORthemoviedb]
    elif userSelectionForOMDbORthemoviedb == 1:
        parsedURL = URL[userSelectionForOMDbORthemoviedb]+urlPrefixTheMovieDB[userSelectionForTitleOrID]+"&apikey="+apiKeys[userSelectionForOMDbORthemoviedb]

    JSONAssigner()
    
    
def Test():
    

    while movieInfo[0] == "#DUPE#" or movieInfo[1] == "#DUPE#" or movieInfo[1] == "False" or movieInfo[0] == "False":
        print("Error with RANDOM ID generation, returning to main menu")
        GenerateURLBasedOnUserSelection()
        print (movieInfo[0]);
        if movieInfo[0] != "#DUPE#" or movieInfo[1] != "#DUPE#" or movieInfo[1] != "False" or movieInfo[0] != "False":
            JSONAssigner()
            

        
    JSONAssigner()

#Function for Parsing JSON from URL and then Printing it and writing it to a text file. Also queries user on wanting to add film to wishlist

def JSONAssigner():

    global returnedJSON;    

    with urllib.request.urlopen(parsedURL) as url:
        returnedJSON = json.loads(url.read().decode())

    if userSelectionForOMDbORthemoviedb == 0:
        GetMovieTitle()
    elif userSelectionForOMDbORthemoviedb == 1:
        UserInputParseTitle()

    if movieInfo[0] == "#DUPE#" or movieInfo[1] == "#DUPE#" or movieInfo[1] == "False" or movieInfo[0] == "False":
        Test()
        
    
    for k,v in returnedJSON.items():
        print(k+":",v)

    for k, v in returnedJSON.items():
        jSONData.append({k:v})

    #if movieInfo[0] == "#DUPE#" or movieInfo[1] == "#DUPE#" or movieInfo[1] == "False" or movieInfo[0] == "False":
            #UserInputParseTitle()
            #Test()
    else:
        print("ID Tested")


    
        
        
    #print(json.dumps(jSONData))

    file = open("wishlistFilmsInfo/"+movieInfo[0]+".txt", "w+");

    file = file.write(str(jSONData));

    #file.close();
    
    print("||||||||||||||||||||||||||||||||||||||||||||");
    print("Do you want to add this film to your wishlist?");
    print("||||||||||||||||||||||||||||||||||||||||||||");
    addToWishList = input("1) No\n2) Yes\n")
    
    
    if addToWishList == "1" or addToWishList == "no":
        GenerateURLBasedOnUserSelection()
    elif addToWishList == "2" or addToWishList == "yes":
        AddToWishList()
        
#Called Function when Program Starts

GenerateURLBasedOnUserSelection()



