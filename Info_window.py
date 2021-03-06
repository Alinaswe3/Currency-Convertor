#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#    Aug 04, 2021 09:41:53 AM CAT  platform: Windows NT

import sys
import Ace_currency_convertor_support as ac

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

import Info_window_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    Info_window_support.set_Tk_var()
    top = first_time_window (root)
    Info_window_support.init(root, top)
    root.mainloop()

w = None
def create_first_time_window(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_first_time_window(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    Info_window_support.set_Tk_var()
    top = first_time_window (w)
    Info_window_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_first_time_window():
    global w
    w.destroy()
    w = None

class first_time_window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("532x229+383+142")
        top.minsize(120, 1)
        top.maxsize(2736, 749)
        top.resizable(0,  0)
        top.title("ACE Currency Convertor")
        top.configure(background="#107aef")

        self.ace_tech_logo = ttk.Label(top)
        self.ace_tech_logo.place(relx=0.038, rely=0.044, height=24, width=86)
        self.ace_tech_logo.configure(background="#107aef")
        self.ace_tech_logo.configure(foreground="#ffffff")
        self.ace_tech_logo.configure(font="-family {Nirmala UI} -size 14 -weight bold")
        self.ace_tech_logo.configure(relief="flat")
        self.ace_tech_logo.configure(anchor='w')
        self.ace_tech_logo.configure(justify='left')
        self.ace_tech_logo.configure(text='''ACE Tech''')

        self.submit_btn = tk.Button(top)
        self.submit_btn.place(relx=0.432, rely=0.699, height=34, width=87)
        self.submit_btn.configure(activebackground="#107aef")
        self.submit_btn.configure(activeforeground="white")
        self.submit_btn.configure(activeforeground="#ffffff")
        self.submit_btn.configure(background="#107aef")
        self.submit_btn.configure(disabledforeground="#a3a3a3")
        self.submit_btn.configure(font="-family {Calibri} -size 16 -weight bold")
        self.submit_btn.configure(foreground="#ffffff")
        self.submit_btn.configure(highlightbackground="#d9d9d9")
        self.submit_btn.configure(highlightcolor="black")
        self.submit_btn.configure(pady="0")
        self.submit_btn.configure(text='''SUBMIT''')
        self.submit_btn.configure(relief='ridge')
        self.tooltip_font = "TkDefaultFont"
        self.submit_btn_tooltip = \
        ToolTip(self.submit_btn, self.tooltip_font, '''Click to submit information and start converting currencies''')
        self.submit_btn.configure(command=lambda:Info_window_support.submit())

        self.api_key_label = ttk.Label(top)
        self.api_key_label.place(relx=0.075, rely=0.437, height=19, width=61)
        self.api_key_label.configure(background="#107aef")
        self.api_key_label.configure(foreground="#ffffff")
        self.api_key_label.configure(font="-family {Calibri} -size 12 -weight bold")
        self.api_key_label.configure(relief="flat")
        self.api_key_label.configure(anchor='w')
        self.api_key_label.configure(justify='left')
        self.api_key_label.configure(text='''API KEY:''')

        self.forename_label = ttk.Label(top)
        self.forename_label.place(relx=0.075, rely=0.262, height=19, width=85)
        self.forename_label.configure(background="#107aef")
        self.forename_label.configure(foreground="#ffffff")
        self.forename_label.configure(font="-family {Calibri} -size 12 -weight bold")
        self.forename_label.configure(relief="flat")
        self.forename_label.configure(anchor='w')
        self.forename_label.configure(justify='left')
        self.forename_label.configure(text='''FORENAME:''')

        self.forename_entry = tk.Entry(top)
        self.forename_entry.place(relx=0.244, rely=0.262, height=20
                , relwidth=0.308)
        self.forename_entry.configure(background="white")
        self.forename_entry.configure(disabledforeground="#a3a3a3")
        self.forename_entry.configure(font="-family {Calibri} -size 12 -weight bold")
        self.forename_entry.configure(foreground="#000000")
        self.forename_entry.configure(insertbackground="black")
        self.forename_entry.configure(textvariable=Info_window_support.forename_var)
        self.tooltip_font = "TkDefaultFont"
        self.forename_entry_tooltip = \
        ToolTip(self.forename_entry, self.tooltip_font, '''Entery your first name only''')

        self.api_entry = tk.Entry(top)
        self.api_entry.place(relx=0.244, rely=0.437, height=20, relwidth=0.703)
        self.api_entry.configure(background="white")
        self.api_entry.configure(disabledforeground="#a3a3a3")
        self.api_entry.configure(font="-family {Calibri} -size 12 -weight bold")
        self.api_entry.configure(foreground="#000000")
        self.api_entry.configure(insertbackground="black")
        self.api_entry.configure(textvariable=Info_window_support.api_key_var)
        self.tooltip_font = "TkDefaultFont"
        self.api_entry_tooltip = \
        ToolTip(self.api_entry, self.tooltip_font, '''Enter your API key''')

        self.copy_link_btn = tk.Button(top)
        self.copy_link_btn.place(relx=0.771, rely=0.533, height=24, width=94)
        self.copy_link_btn.configure(activebackground="#107aef")
        self.copy_link_btn.configure(activeforeground="white")
        self.copy_link_btn.configure(activeforeground="#ffffff")
        self.copy_link_btn.configure(background="#107aef")
        self.copy_link_btn.configure(disabledforeground="#a3a3a3")
        self.copy_link_btn.configure(font="-family {Calibri} -size 12 -weight bold")
        self.copy_link_btn.configure(foreground="#ffffff")
        self.copy_link_btn.configure(highlightbackground="#d9d9d9")
        self.copy_link_btn.configure(highlightcolor="black")
        self.copy_link_btn.configure(pady="0")
        self.copy_link_btn.configure(text='''COPY LINK''')
        self.copy_link_btn.configure(relief='ridge')
        self.tooltip_font = "TkDefaultFont"
        self.copy_link_btn_tooltip = \
        ToolTip(self.copy_link_btn, self.tooltip_font, '''Click to copy the link to the site with API to clipboard''')
        self.copy_link_btn.configure(command=lambda:Info_window_support.copy_link())
        
        #my own paste key button
        self.paste_key_btn = tk.Button(top)
        self.paste_key_btn.place(relx=0.244, rely=0.533, height=24, width=94)
        self.paste_key_btn.configure(activebackground="#107aef")
        self.paste_key_btn.configure(activeforeground="white")
        self.paste_key_btn.configure(activeforeground="#ffffff")
        self.paste_key_btn.configure(background="#107aef")
        self.paste_key_btn.configure(disabledforeground="#a3a3a3")
        self.paste_key_btn.configure(font="-family {Calibri} -size 12 -weight bold")
        self.paste_key_btn.configure(foreground="#ffffff")
        self.paste_key_btn.configure(highlightbackground="#d9d9d9")
        self.paste_key_btn.configure(highlightcolor="black")
        self.paste_key_btn.configure(pady="0")
        self.paste_key_btn.configure(text='''PASTE KEY''')
        self.paste_key_btn.configure(relief='ridge')
        self.tooltip_font = "TkDefaultFont"
        self.copy_link_btn_tooltip = \
        ToolTip(self.paste_key_btn, self.tooltip_font, '''Click to paste copied key into API key entry box''')
        self.paste_key_btn.configure(command=lambda:Info_window_support.paste_key())        

# ======================================================
# Support code for Balloon Help (also called tooltips).
# Found the original code at:
# http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
# Modified by Rozen to remove Tkinter import statements and to receive
# the font as an argument.
# ======================================================

from time import time, localtime, strftime

class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=0.5, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          tooltip_font: Font to be used
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in milliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()

    def update(self, msg):
        """
        Updates the Tooltip with a new message. Added by Rozen
        """
        self.msgVar.set(msg)

# ===========================================================
#                   End of Class ToolTip
# ===========================================================

if __name__ == '__main__':
    vp_start_gui()





