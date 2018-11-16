#Import Libraries 
import json
import requests
import urllib.request, urllib.parse, urllib.error
import webbrowser

#API KEY OMDB: http://www.omdbapi.com/?i=tt3896198&apikey=e3fdfd9c OR e3fdfd9c
#API KEY THE MOVIE DB: 9d72cb6c12e587c90e7bf6f48c617b44
#Example URLs - OMDB: http://www.omdbapi.com/?i=tt0113375&apikey=e3fdfd9c AND themovieDB: https://api.themoviedb.org/3/movie/550?api_key=9d72cb6c12e587c90e7bf6f48c617b44

#API Keys for OMDB and The Movie DB

apiKeys = ["e3fdfd9c", "9d72cb6c12e587c90e7bf6f48c617b44"]

#Initialise array for movie title or id

movieInfo = ["placeholderTitle", "placeholderID"]

#Initialise array for URL for omdb or moviedb


URL = ["https://www.omdbapi.com/", "https://api.themoviedb.org/3"]

#Function For the URL Generation, function can be called when/if a user wants information from another movie
def GenerateURLBasedOnUserSelection():
    #Allows the parsedURL to be used in other functions (outside this function)
    global parsedURL
    #User Website Selection (OMDb or The Movie DB)
    userWebsiteSelection = input("What website would you like to search?\n 1) Using OMDb \n 2) Using themoviedb\n")

    #If Statement based on User Selection on Title or ID

    if userWebsiteSelection == "1" or userWebsiteSelection == "omdb":
        userSelectionForOMDbORthemoviedb = 0
    elif userWebsiteSelection == "2" or userWebsiteSelection == "the movie database":
        userSelectionForOMDbORthemoviedb = 1

    #User Choice for searching by Title or ID
        
    userSelectionTitleOrID = input("How would you like to search?\n 1) By Title\n 2) By IMDB ID or MOVIEDB ID\n")

    #If Statement Which determines the values for the Title or Movie ID

    if userSelectionTitleOrID == "1" or userSelectionTitleOrID == "title":
        userSelectionForTitleOrID = 0
        movieInfo[0] = input("Please enter the title you want to search by (please use + instead of spaces e.g. the+godfather)\n")
    elif userSelectionTitleOrID == "2" or userSelectionTitleOrID == "imdb id":
        userSelectionForTitleOrID = 1
        movieInfo[1] = input("Please enter the IMDB ID (e.g. tt0068646) or MOVIEDB ID (e.g. 238) you want to search by\n")

    #Initialises array for OMDb URL prefixs
    #?s= being Title of film and ?i= being IMDB ID
        
    urlPrefixOMDb = ["?s=", "?i="]

    #Initialises array for The Movie DB prefixs

    urlPrefixTheMovieDB = ["/search/movie?api_key="+apiKeys[1]+"&query="+movieInfo[userSelectionForTitleOrID], "/movie/"+movieInfo[userSelectionForTitleOrID]+"?api_key="+apiKeys[1]]

    #If Statement That Parses the URLs (based on User Selection) Using The above variables and array indices 

    if userSelectionForOMDbORthemoviedb == 0:
        parsedURL = URL[userSelectionForOMDbORthemoviedb]+urlPrefixOMDb[userSelectionForTitleOrID]+movieInfo[userSelectionForTitleOrID]+"&apikey="+apiKeys[userSelectionForOMDbORthemoviedb]
    elif userSelectionForOMDbORthemoviedb == 1:
        parsedURL = URL[userSelectionForOMDbORthemoviedb]+urlPrefixTheMovieDB[userSelectionForTitleOrID]+"&apikey="+apiKeys[userSelectionForOMDbORthemoviedb]

#Testing Function + Test Print of parsedURL + Open Web Browser To Confirm The JSON is correct

GenerateURLBasedOnUserSelection()

print(parsedURL)

input("Press ENTER to open link in web browser")

webbrowser.open(parsedURL, new=2)


