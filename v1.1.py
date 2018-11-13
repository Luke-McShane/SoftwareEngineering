from tkinter import *
import json
import urllib.request, urllib.parse, urllib.error
import tkinter as tk #Shortens having to write tkinter each time
import requests # Needed to grab data from the API


omdb_key = 'c5f36360'
omdb_serviceurl = 'http://www.omdbapi.com/?'
omdb_apikey = '&apikey='+ omdb_key 
# Above is all needed inforamation to query an API
###########################################################################

window = Tk() #Overall Window
window.geometry("350x350") #Size

window.title('Movie Finder') #Title

label = Label(window,text = 'Please enter a movie to search for:')
label.pack(padx = 10, pady = 50)


def search_movie(title): #"Function" to search for movies

    omdb_url = omdb_serviceurl + omdb_apikey + '&s=' + title #Combined as one URL to pull JSON data from the API | '&s=' specifies to search for a movie | Check API website for other options, poosibly for extras?
    json_data = requests.get(omdb_url).json() #Actual Request


    for item in json_data['Search']: #Loop to itterate through results
        
        return ("Movie: " + item['Title'] + "\n" + "Released: " + item['Year']) # Itteriates for each of of the items in the JSON query | Grabs title and release year | 



def result():

    title = searchBox.get() #Gets the input from the search box
    newwin = tk.Tk() #Creates singular box to put data in | Possibly put this in search function to make several boxes instead | Need to figure out how to do variable(1),variable(2)... etc|
    newwin.geometry("400x400") #Size of box
    T = Text(newwin) #Looking for text to put in box
    T.pack() 
    T.insert(END, search_movie(title)) # Puts text grabbed from search in search_movie fucntion |

#Search box
searchBox = Entry(window)
searchBox.pack()
searchBox.delete(0, END)
searchBox.insert(0, "")


#Search button
btn_search = Button(window, text = 'Search', command=result)
btn_search.pack(padx = 120, pady = 20)


#Exit button
btn_end = Button(window, text = 'Exit', command=exit)
btn_end.pack(padx = 150, pady = 20)

window.mainloop()
