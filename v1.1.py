from tkinter import *
import json
import urllib.request, urllib.parse, urllib.error
import tkinter as tk
import requests


omdb_key = 'c5f36360'
omdb_serviceurl = 'http://www.omdbapi.com/?'
omdb_apikey = '&apikey='+ omdb_key

###########################################################################

window = Tk()
window.geometry("350x350")

window.title('Movie Finder')

label = Label(window,text = 'Please enter a movie to search for:')
label.pack(padx = 10, pady = 50)


def search_movie(title):

    omdb_url = omdb_serviceurl + omdb_apikey + '&s=' + title
    json_data = requests.get(url).json()


    for item in json_data['Search']:
        
        return ("Movie: " + item['Title'] + "\n" + "Released: " + item['Year'])



def result():

    title = searchBox.get()
    newwin = tk.Tk()
    newwin.geometry("400x400")
    T = Text(newwin)
    T.pack()
    T.insert(END, search_movie(title))

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
