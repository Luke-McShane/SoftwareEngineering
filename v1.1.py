from tkinter import *
import json
import urllib.request, urllib.parse, urllib.error
import tkinter as tk
import requests




###########################################################################

window = Tk()
window.geometry("350x350")

window.title('Movie Finder')

label = Label(window,text = 'Please enter a movie to search for:')
label.pack(padx = 10, pady = 50)


def search_movie(title):
    key = 'c5f36360'
    serviceurl = 'http://www.omdbapi.com/?'
    apikey = '&apikey='+key
    
    url = serviceurl + apikey + '&s=' + title
    json_data = requests.get(url).json()
    list = []

    for item in json_data['Search']:
        
        list.append("Movie: " + item['Title'] + "\n" + "Released: " + item['Year'])

    return list

def result():

    title = searchBox.get()
    newwin = tk.Tk()
    newwin.geometry("400x400")

    T = Text(newwin,height=2, width=30)
    T.pack()
    T.insert(END, search_movie(title)[0])
    btn_addF1 = Button(newwin, text = 'Add to favourites', command=fav(search_movie(title)[0]))
    btn_addF1.pack()

    T1 = Text(newwin,height=2, width=30)
    T1.pack()
    T1.insert(END, search_movie(title)[1])
    btn_addF2 = Button(newwin, text = 'Add to favourites', command=fav(search_movie(title)[1]))
    btn_addF2.pack()
    
    T2 = Text(newwin,height=2, width=30)
    T2.pack()
    T2.insert(END, search_movie(title)[2])
    btn_addF3 = Button(newwin, text = 'Add to favourites', command=fav(search_movie(title)[2]))
    btn_addF3.pack()

    T3 = Text(newwin,height=2, width=30)
    T3.pack()
    T3.insert(END, search_movie(title)[3])
    btn_addF4 = Button(newwin, text = 'Add to favourites', command=fav(search_movie(title)[3]))
    btn_addF4.pack()

    T4 = Text(newwin,height=2, width=30)
    T4.pack()
    T4.insert(END, search_movie(title)[4])
    btn_addF5 = Button(newwin, text = 'Add to favourites', command=fav(search_movie(title)[4]))
    btn_addF5.pack()

def fav(movie_to_add):
    
            

    f= open("fav.txt","a+")
    f.write(movie_to_add + '\n')
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

#Favourites
btn_search = Button(window, text = 'Favourites', command=favourites)
btn_search.pack(padx = 135, pady = 20)

#Exit button
btn_end = Button(window, text = 'Exit', command=exit)
btn_end.pack(padx = 150, pady = 20)

window.mainloop()
