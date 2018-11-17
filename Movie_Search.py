from tkinter import *
from tkinter import messagebox
import json
import urllib.request, urllib.parse, urllib.error
import tkinter as tk
import requests



###########################################################################
window = Tk()
window.geometry("530x530")
window.configure(background='palegreen4')

window.title('Movie Finder')


list = []

label = Label(window,text = 'Please enter a movie to search for:', background='palegreen4')
label.pack(padx = 10, pady = 50)

def OMDB_Search(title):
    key = 'c5f36360'
    serviceurl = 'http://www.omdbapi.com/?'
    apikey = '&apikey='+key

    url = serviceurl + apikey + '&s=' + title
    json_data = requests.get(url).json()


    for item in json_data['Search']:

        list.append("Movie: " + item['Title'] + "\n" + "Released: " + item['Year'])

    return list


def TMDB_Search(title):
    key = '399f6191c9956c7ac44da18aa4461125'
    serviceurl = 'https://api.themoviedb.org/3/search/movie?'
    apikey = 'apikey='+key

    url = 'https://api.themoviedb.org/3/search/movie?api_key=399f6191c9956c7ac44da18aa4461125&query=' + title
    json_data = requests.get(url).json()
    

    for item in json_data['results']:

        list.append("Movie: " + item['title'] + "\n" + "Released: " + item['release_date'])

    return list

def result1():
    
    title = searchBox.get()
    newwin = tk.Tk()
    newwin.geometry("500x500")
    newwin.configure(background='palegreen4')
    newwin.title('Movie Search Results')
    
    try:
        T = Text(newwin,height=2, width=40)
        T.pack()
        T.insert(END, OMDB_Search(title)[0])
        btn_addF1 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(OMDB_Search(title)[0]))
        btn_addF1.pack()

        T1 = Text(newwin,height=2, width=40)
        T1.pack()
        T1.insert(END, OMDB_Search(title)[1])
        btn_addF2 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(OMDB_Search(title)[1]))
        btn_addF2.pack()

        T2 = Text(newwin,height=2, width=40)
        T2.pack()
        T2.insert(END, OMDB_Search(title)[2])
        btn_addF3 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(OMDB_Search(title)[2]))
        btn_addF3.pack()

        T3 = Text(newwin,height=2, width=40)
        T3.pack()
        T3.insert(END, OMDB_Search(title)[3])
        btn_addF4 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(OMDB_Search(title)[3]))
        btn_addF4.pack()

        T4 = Text(newwin,height=2, width=40)
        T4.pack()
        T4.insert(END, OMDB_Search(title)[4])
        btn_addF5 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(OMDB_Search(title)[4]))
        btn_addF5.pack()

        T5 = Text(newwin,height=2, width=40)
        T5.pack()
        T5.insert(END, OMDB_Search(title)[5])
        btn_addF6 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(OMDB_Search(title)[5]))
        btn_addF6.pack()

        T6 = Text(newwin,height=2, width=40)
        T6.pack()
        T6.insert(END, OMDB_Search(title)[6])
        btn_addF7 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(OMDB_Search(title)[6]))
        btn_addF7.pack()

        T7 = Text(newwin,height=2, width=40)
        T7.pack()
        T7.insert(END, OMDB_Search(title)[7])
        btn_addF8 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(OMDB_Search(title)[7]))
        btn_addF8.pack()


    except:
        newwin.destroy()
        messagebox.showerror("Error!", "Movie Not Found")
        
def result2():

    title = searchBox.get()
    newwin = tk.Tk()
    newwin.geometry("500x500")
    newwin.configure(background='palegreen4')
    newwin.title('Movie Search Results')
    
    try:
        T = Text(newwin,height=2, width=40)
        T.pack()
        T.insert(END, TMDB_Search(title)[0])
        btn_addF1 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(TMDB_Search(title)[0]))
        btn_addF1.pack()

        T1 = Text(newwin,height=2, width=40)
        T1.pack()
        T1.insert(END, TMDB_Search(title)[1])
        btn_addF2 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(TMDB_Search(title)[1]))
        btn_addF2.pack()

        T2 = Text(newwin,height=2, width=40)
        T2.pack()
        T2.insert(END, TMDB_Search(title)[2])
        btn_addF3 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(TMDB_Search(title)[2]))
        btn_addF3.pack()

        T3 = Text(newwin,height=2, width=40)
        T3.pack()
        T3.insert(END, TMDB_Search(title)[3])
        btn_addF4 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(TMDB_Search(title)[3]))
        btn_addF4.pack()

        T4 = Text(newwin,height=2, width=40)
        T4.pack()
        T4.insert(END, TMDB_Search(title)[4])
        btn_addF5 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(TMDB_Search(title)[4]))
        btn_addF5.pack()
        
        T5 = Text(newwin,height=2, width=40)
        T5.pack()
        T5.insert(END, TMDB_Search(title)[5])
        btn_addF6 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(TMDB_Search(title)[5]))
        btn_addF6.pack()

        T6 = Text(newwin,height=2, width=40)
        T6.pack()
        T6.insert(END, TMDB_Search(title)[6])
        btn_addF7 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(TMDB_Search(title)[6]))
        btn_addF7.pack()

        T7 = Text(newwin,height=2, width=40)
        T7.pack()
        T7.insert(END, TMDB_Search(title)[7])
        btn_addF8 = Button(newwin, text = 'Add to wishlist', command=lambda : wish(TMDB_Search(title)[7]))
        btn_addF8.pack()
        
    except:
        newwin.destroy()
        messagebox.showerror("Error!", "Movie Not Found")
        

    
def wish(movie_to_add):
    f = open("wish.txt","a+")
    f.write(movie_to_add + '\n')
    f.close()
    messagebox.showinfo("Success!", "Your movie has been added to your wish list!")

def wish_list():

    title = searchBox.get()
    newwin2 = tk.Tk()
    newwin2.geometry("700x650")
    newwin2.configure(background='palegreen4')
    newwin2.title("Wish List")
    
    label = Label(newwin2,text = 'Welcome to your wish list!\n\nYou can edit the list yourself here by highlighting the movie followed by the backspace key on your keyboard.\n\n Do not forget to press update!', background='palegreen4')
    label.pack(padx = 10, pady = 50)
                  
    f = open("wish.txt", "r")

    contents = f.read()

    T = Text(newwin2,height=20, width=30)
    T.pack(padx = 30, pady = 50)
    T.insert(END, contents)

    sub = Button(newwin2, text = 'Update List', command=lambda : update_wlist(T.get('1.0', 'end-1c')))
    sub.pack()

    f.close()

def update_wlist(change):
    f = open("wish.txt","a+")
    f.truncate(0)
    f.write(change)
    messagebox.showinfo("Success!", "Your wish list has been updated!")


#Search box
searchBox = Entry(window, bd = 4, width=30)
searchBox.pack()
searchBox.delete(0, END)
searchBox.insert(0, "")
searchBox.pack(padx = 50, pady = 30)

#Search button for OMDB
btn_search = Button(window, height = 3 ,width = 20, text = 'Search OMDB', command=result1)
btn_search.pack(padx = 130, pady = 5)

#Search Button for TMDB
btn_search = Button(window, height = 3 ,width = 20, text = 'Search TMDB', command=result2)
btn_search.pack(padx = 135, pady = 5)

#Wish list
btn_search = Button(window, height = 3 ,width = 20, text = 'Wish List', command=wish_list)
btn_search.pack(padx = 140, pady = 5)

#Exit button
btn_end = Button(window, height = 3 ,width = 20, text = 'Exit', command=exit)
btn_end.pack(padx = 145, pady = 5)

window.mainloop()
