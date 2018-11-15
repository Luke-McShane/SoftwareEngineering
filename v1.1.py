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

    title = searchBox.get()
    newwin = tk.Tk()
    newwin.geometry("400x400")
    T[]
    T = Text(newwin,height=2, width=30)
    T.pack()
    T.insert(END, search_movie(title)[0])
    btn_addF1 = Button(newwin, text = 'Add to favourites', command='fav')
    btn_addF1.pack()

    T1 = Text(newwin,height=2, width=30)
    T1.pack()
    T1.insert(END, search_movie(title)[1])
    btn_addF2 = Button(newwin, text = 'Add to favourites', command='fav')
    btn_addF2.pack()
    
    T2 = Text(newwin,height=2, width=30)
    T2.pack()
    T2.insert(END, search_movie(title)[2])
    btn_addF3 = Button(newwin, text = 'Add to favourites', command='fav')
    btn_addF3.pack()

    T3 = Text(newwin,height=2, width=30)
    T3.pack()
    T3.insert(END, search_movie(title)[3])
    btn_addF4 = Button(newwin, text = 'Add to favourites', command='fav')
    btn_addF4.pack()

    T4 = Text(newwin,height=2, width=30)
    T4.pack()
    T4.insert(END, search_movie(title)[4])
    btn_addF5 = Button(newwin, text = 'Add to favourites', command='fav')
    btn_addF5.pack()
    
def fav():
        favList = []

        if btn_addF1 == true:
            favList.append(T)

        if btn_addF2 == true:
            favList.append(T1)

        if btn_addF3 == true:
            favList.append(T2)
            
        if btn_addF4 == true:
            favList.append(T3)
            
        if btn_addF5 == true:
            favList.append(T4)
            

        f= open("fav.txt","a+")
        f.write(favList)
        f.close()


def favourites():

    title = searchBox.get()
    newwin2 = tk.Tk()
    newwin2.geometry("400x400")

    f=open("fav.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        
    T = Text(newwin2,height=20, width=30)
    T.pack()
    T.insert(END, contents)

    
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
