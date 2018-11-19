#Software Engineering Group Project - Movie Search.
#Group C13.

#Imported libraries.
from tkinter import *
from tkinter import messagebox
import json
import urllib.request, urllib.parse, urllib.error
import tkinter as tk
import requests
import sys


###########################################################################

#Create main window with the set specifications.
window = Tk()
window.geometry("530x530")
window.configure(background='palegreen4')
#Title of the main window
window.title('Movie Finder')


#Text on the main window.
label = Label(window,text = 'Please enter a movie to search for:', background='palegreen4')
label.pack(padx = 10, pady = 50)

#OMDB movie search code.
def OMDB_Search(title):
    #Sets the api key.
    key = 'c5f36360'
    serviceurl = 'http://www.omdbapi.com/?'
    apikey = '&apikey='+key
    list = []
    #Retrieves the data.
    url = serviceurl + apikey + '&s=' + title
    json_data = requests.get(url).json()

    #Writes out the data retrieved in the format set below.
    for item in json_data['Search']:
        #Adds the select text to the list.
        list.append("Movie: " + item['Title'] + "\n" + "Released: " + item['Year'])
        
    #Returns the list when this function is called.
    return list


def TMDB_Search(title):
    #Sets the api key.
    key = '399f6191c9956c7ac44da18aa4461125'
    serviceurl = 'https://api.themoviedb.org/3/search/movie?'
    apikey = 'apikey='+key
    list = []
    #Retrieves the data.
    url = 'https://api.themoviedb.org/3/search/movie?api_key=399f6191c9956c7ac44da18aa4461125&query=' + title
    json_data = requests.get(url).json()
    
    #Writes out the data retrieved in the format set below.
    for item in json_data['results']:
        #Adds the select text to the list.
        list.append("Movie: " + item['title'] + "\n" + "Released: " + item['release_date'])

    #Returns the list when this function is called.
    return list

#Function for OMDB results.
def result1():
    #Retrieves the text from the search box.
    title = searchBox.get()
    #Creates the new window for the OMDB results with the set specifications.
    newwin = tk.Tk()
    newwin.geometry("600x600")
    newwin.configure(background='palegreen4')
    #Sets the title of the new window.
    newwin.title('Movie Search Results')
    
    #Hides the main window.
    window.iconify()

    #If movie results are found.
    try:
        #Creates a text box in the new window using tkinter.
        T = Text(newwin,height=2, width=40)
        T.pack()
        #Inserts the result data into this text box.
        T.insert(END, OMDB_Search(title)[0])
        #When the button is pressed, it will call the wish function which saves only this text box data to the external text file.
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

        #Exit button which closes the new window and reshows the main window.
        btn_end = Button(newwin, height = 3 ,width = 20, text = 'Exit', command=lambda : [window.deiconify(), newwin.destroy()])
        btn_end.pack()
        
    #If movie results are not found display an error.    
    except:
        #Closes the new window.
        newwin.destroy()
        #Displays error message if no results are found.
        messagebox.showerror("Error!", "Movie Not Found")
        

#Function for TMDB results. 
def result2():
    #Retrieves the text from the search box.
    title = searchBox.get()
    #Creates the new window for the TMDB results with the set specifications.
    newwin = tk.Tk()
    newwin.geometry("600x600")
    newwin.configure(background='palegreen4')
    #Sets the title of the new window.
    newwin.title('Movie Search Results')
    
    #Hides the main window.
    window.iconify()

    #If movie results are found.
    try:
        #Creates a text box in the new window using tkinter.
        T = Text(newwin,height=2, width=40)
        T.pack()
        #Inserts the result data into this text box.
        T.insert(END, TMDB_Search(title)[0])
        #When the button is pressed, it will call the wish function which saves only this text box data to the external txt file.
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

        #Exit button which closes the new window and reshows the main window.
        btn_end = Button(newwin, height = 3 ,width = 20, text = 'Exit', command=lambda : [window.deiconify(), newwin.destroy()])
        btn_end.pack()

    #If movie results are not found display an error. 
    except:
        #Closes the new window.
        newwin.destroy()
        #Displays error message if no results are found.
        messagebox.showerror("Error!", "Movie Not Found")

#Function to write the movie selected to the wish list. (text file)
def wish(movie_to_add):
    #Opens the wish list to append.
    f = open("wish.txt","a+")
    #Writes the movie selected to the text file.
    f.write(movie_to_add + '\n')
    #Closes the text file.
    f.close()
    #Displays a message saying if it was successfully added.
    messagebox.showinfo("Success!", "Movie added to your wish list!")

#Defines the wish list function.
def wish_list():
    #Creates a new window for the wish list to appear with the specifications set.
    newwin2 = tk.Tk()
    newwin2.geometry("700x700")
    newwin2.configure(background='palegreen4')
    #Name of the window.
    newwin2.title("Wish List")
    #Hides the main window.
    window.iconify()

    #Displays instructions to the user in the form of text in a label above the wish list.
    label = Label(newwin2,text = 'Welcome to your wish list!\n\nYou can edit the list yourself here by highlighting the movie followed by the backspace key on your keyboard.\n\n Do not forget to press update!', background='palegreen4')
    label.pack(padx = 10, pady = 50)

    #Opens the wish list for reading.              
    f = open("wish.txt", "r")

    #Assigns the read data to a variable to call later on.
    contents = f.read()

    #A text box is created to display the contents from the text file. (Wish list)
    T = Text(newwin2,height=20, width=30)
    T.pack(padx = 30, pady = 50)
    T.insert(END, contents)

    #Creates a new button which updates the list from the update_wlist function.
    sub = Button(newwin2, text = 'Update List', command=lambda : update_wlist(T.get('1.0', 'end-1c')))
    sub.pack()

    #Closes the file.
    f.close()

    #Exit button which closes the new window and reshows the main window.
    btn_end = Button(newwin2, height = 3 ,width = 20, text = 'Exit', command=lambda : [window.deiconify(), newwin2.destroy()])
    btn_end.pack(padx = 145, pady = 5)

#The function to open the wish list and delete the data and write the changes from the wish list window.
def update_wlist(change):
    #Opens the wish list text file.
    f = open("wish.txt","a+")
    #Deletes the data currently in the text file.
    f.truncate(0)
    #Writes the updated list from the wish list window.
    f.write(change)
    #Message box saying the update has been successful.
    messagebox.showinfo("Success!", "Your wish list has been updated!")


#Search box button.
searchBox = Entry(window, bd = 4, width=30)
searchBox.pack()
searchBox.delete(0, END)
searchBox.insert(0, "")
searchBox.pack(padx = 50, pady = 30)

#Search button for OMDB.
btn_search = Button(window, height = 3 ,width = 20, text = 'Search OMDB', command=result1)
btn_search.pack(padx = 130, pady = 5)

#Search Button for TMDB.
btn_search = Button(window, height = 3 ,width = 20, text = 'Search TMDB', command=result2)
btn_search.pack(padx = 135, pady = 5)

#Wish list button.
btn_search = Button(window, height = 3 ,width = 20, text = 'Wish List', command=wish_list)
btn_search.pack(padx = 140, pady = 5)

#Exit button.
btn_end = Button(window, height = 3 ,width = 20, text = 'Exit', command=exit)
btn_end.pack(padx = 145, pady = 5)

#Loops the main window.
window.mainloop()
