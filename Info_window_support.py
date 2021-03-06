#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Aug 04, 2021 09:42:00 AM CAT  platform: Windows NT

import sys
import pyperclip as cp
import requests as rq
import Ace_currency_convertor_support as ac
import tkinter.messagebox as msg


try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global forename_var
    forename_var = tk.StringVar()
    global api_key_var
    api_key_var = tk.StringVar()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    root.iconbitmap('icon.ico')
    w.forename_entry.focus()

def copy_link():
    '''Function copies the currency freak link to clipboard'''
    
    #link
    link = 'https://currencyfreaks.com/signup.html'
    
    #copying to clipboard
    cp.copy(link)
    
    #displaying message to user
    msg.showinfo('Success',
                 'Link has been copied to clipboard successfully')

def submit():
    '''Function sets the variables in currency convertor to their
    right values'''
    global top_level
    
    #testing the internet connection before submission
    if ac.internet_test():
        pass
    else:
        msg.showerror('Internet error',
                      'Your account can not be set up\nBecause there is no internet connection\nPlease connect to the internet and try again')
        return

    #getting values from entry boxes
    forename = forename_var.get()
    apikey = api_key_var.get()
    
    #opening the details file
    #the details file stores username and api key temporaly for
    #the main program
    with open('name.txt', 'w') as name:
        #checking if forename and apikey meet required criteria
        
        #forename checking
        if len(forename) > 2 and forename.isalpha():
            forename = forename.capitalize()
            name.write(forename) 
        else:
            msg.showerror('Name error', 
                          'Please enter a valid name\nName should not contain symbols or numbers e.g Ay3')
            forename_var.set('')
            #if the name is invalid the function does not submit
            #anything and just stops executing
            return
        
        #apikey checking
        if len(apikey) == 32 and apikey.isalnum():
            site = 'https://api.currencyfreaks.com/latest?apikey='+apikey
            response = rq.get(site)
            results = response.json()
            try:
                if results['success'] == False:
                    msg.showerror('API key error',
                                  'Provided API key is invalid\nMake sure api key was copied correctly\ne.g characters should be 32')
                    api_key_var.set('')
            except:
                #writing the key to a seperate file
                with open('key_file', 'w') as key:
                    key.write(apikey)
                #allowing the one time exception
                destroy_window()


        else:
            msg.showerror('API key error', 
                          'Provided API key is invalid\nMake sure API key was copied correctly\ne.g characters should be 32')
            api_key_var.set('')
            #also if api key is incorrect function stops 
            #executing
            return
        
        
# An additional function----------------------------------------
# the paste key function------------------

def paste_key():
    '''Function pastes the copied key by user into the entry box
    for the key'''
    
    #pasting to the api entry window
    #making sure it work with try/except clause to prevent
    #hidden exceptions
    try:
        api_key_var.set(str(cp.paste()))
    except:
        msg.showerror('API key error',
                      'API key copied is invalid\n Make sure you copied the API key from\nwww.currencyfreaks.com')
        api_key_var.set('')
        
def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

    
if __name__ == '__main__':
    import Info_window
    Info_window.vp_start_gui()




