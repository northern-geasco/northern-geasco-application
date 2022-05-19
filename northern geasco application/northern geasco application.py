from tkinter import *
from tkinter import ttk , messagebox , LabelFrame
import platform
import socket
from subprocess import Popen

window = Tk ()


# all functions
def find_people():
    password = '1234'
    pass_grab = entry1.get ()
    if pass_grab == password:
        nbox = messagebox.askyesno ( 'Search results' , 'Correct password' )
        entry1.destroy ()
        button4.destroy ()
        searchBar.destroy ()
        lbl.destroy ()
        button5.config ( state=NORMAL )
        button6.config ( state=NORMAL )
        button7.config ( state=NORMAL )
        button9.config(state=NORMAL)
        f = open ( 'about northern geasco.txt' , 'r' )
        line = f.readline ()
        print ( line )
        h3 = ttk.Label ( frame2 , text='see the console below for outputs' )
        h3.pack ()

    else:
            try:
                hostname = socket.gethostname ()
                local_ip = socket.gethostbyname ( hostname )
                my_system = platform.uname ()
                sys_info = my_system.system
                print('your sys info is')
                print('=============')
                print(local_ip)
                print(sys_info)
                print('=============')
                print('ya noob youre gonna get hacked')

            except:
                print('The error is')
                print(local_ip)
                print(sys_info)




def help_func():
    nbox2 = messagebox.askyesnocancel ( 'Info dialog' ,
                                        'hello welcome to the help dialog if you have found any bugs in this program please report it!' )


def info_func():
    nbox3 = messagebox.askyesnocancel ( 'about dialog' ,
                                        'hello welcome to the info dialog you can roport anything at ngoc.com' )


def credits_func():
    nbox4 = messagebox.askyesnocancel ( 'credits' ,
                                        'The main credits goes to:Rishabh Singh The master of Python and Ngoc software department' )


def Exit_func():
    exit ()


def contribute():
    nbox = messagebox.askyesnocancel ( 'Contribution' , 'you can contribute at www.ngoc.com/contribute' )


def settings():
    button8 = ttk.Button ( frame2 , text='exit' , image=icon6 )
    button8.pack ( side=LEFT )
    button9 = ttk.Button ( frame2 , text='disable all systems' , command=disable )
    button9.pack ( side=LEFT )
    button10 = ttk.Button ( frame2 , text='enable super-pro mode' )
    button10.pack ( side=LEFT )
    button11 = ttk.Button ( frame2 , text='enable hyper-security mode' )
    button11.pack ( side=LEFT )


def disable():
    entry1.destroy ()
    button4.destroy ()
    searchBar.destroy ()
    lbl.destroy ()
    label1.destroy ()
    frame3.destroy ()


def insta_users():
    treeview = ttk.Treeview ( frame2 )
    treeview.pack ()

    treeview.insert ( '' , '0' , 'item1' , text='Rishabh singh' )
    treeview.insert ( '' , '0' , 'item2' , text='Nco dev' )
    treeview.insert ( '' , '0' , 'item3' , text='Nco securities' )
    treeview.insert ( '' , '0' , 'item4' , text='nco software dept' )
    treeview.move ( 'item4' , 'item1' , 'end' )
    button8 = ttk.Button ( frame2 , text='exit' , image=icon6 )
    button8.pack ()
def share():
    Popen(r'python C:\Users\rishabh\Desktop\northern geasco application\file sender\file sender.py')

# end


menuBar = Menu ( window )
File = Menu ( menuBar , tearoff=0 )
menuBar.add_cascade ( label='File' , menu=File )
File.add_command ( label='services' )
File.add_separator ()
File.add_command ( label='contact' )
edit = Menu ( menuBar , tearoff=0 )
menuBar.add_cascade ( label='Edit' , menu=edit )
edit.add_command ( label='Settings' , command=settings )
edit.add_command ( label='style' )
edit.add_command ( label='contribution' , command=contribute )
edit.add_separator ()
edit.add_command ( label='Exit' , command=Exit_func )
about_help = Menu ( menuBar , tearoff=0 )
about_help.add_command ( label='credits' , command=credits_func )
about_help.add_command ( label='help' , command=help_func )
about_help.add_command ( label='info' , command=info_func )
menuBar.add_cascade ( label='about&help' , menu=about_help )

pw = ttk.PanedWindow ( window , orient=HORIZONTAL )
pw.pack ( fill=BOTH , expand=True )
frame = ttk.Frame ( pw , width=100 , height=500 , relief=SUNKEN )
frame2 = ttk.Frame ( pw , width=100 , height=500 , relief=SUNKEN )
pw.add ( frame , weight=1 )
pw.add ( frame2 , weight=3 )

label1 = ttk.Label ( frame2 , text='northern geasco appplication' , font=(('Times') , 18) )
label1.pack ()

searchBar = LabelFrame ( frame2 , text='Enter your password' , padx=20 , pady=20 )
lbl = Label ( searchBar , text='Search bar' )
searchBar.pack ( side=TOP , padx=20 )
entry1 = Entry ( searchBar )
entry1.pack ( side=LEFT , padx=10 )
entry1.config ( show='*' )
button4 = ttk.Button ( searchBar , text='pass' , command=find_people )
button4.pack ( side=LEFT , padx=10 )

icon = PhotoImage ( file='info.png' )
icon2 = PhotoImage ( file='interrogation.png' )
icon3 = PhotoImage ( file='settings.png' )
icon4 = PhotoImage ( file='encrypted.png' )
icon5 = PhotoImage ( file='users.png' )
icon6 = PhotoImage ( file='button.png' )
icon7 = PhotoImage ( file='upload.png' )
icon8=PhotoImage(file='share.png')

frame3 = Frame ( frame2 , height=300 , width=300 , bg='red' , bd='7' , relief=SUNKEN )
frame3.pack ( fill=X )
button5 = ttk.Button ( frame3 , text='Settings' , image=icon3 , command=settings )
button5.pack ( side=LEFT )
button6 = ttk.Button ( frame3 , text='security' , image=icon4 , command=settings )
button6.pack ( side=LEFT )
button7 = ttk.Button ( frame3 , text='users' , image=icon5 , command=insta_users )
button7.pack ( side=LEFT )
textBox = Text ( frame3 )
button5.config ( state=DISABLED )
button6.config ( state=DISABLED )
button7.config ( state=DISABLED )

tabs = ttk.Notebook ( frame )
tabs.pack ( fill=BOTH , expand=True )
tab1 = ttk.Frame ( tabs )
tab2 = ttk.Frame ( tabs )
tabs.add ( tab1 , text='help' , image=icon )
tabs.add ( tab2 , text='about' , image=icon2 )

h1 = Label ( tab1 , text='If you need help you can get help by clicking this button' )
h1.pack ()

button1 = ttk.Button ( tab1 , text='help' , image=icon , command=help_func )
button1.pack ()

h2 = Label ( tab2 , text='all the info is here' )
h2.pack ()

button8 = ttk.Button ( tab2 , image=icon2 , command=info_func )
button8.pack ()

button9=ttk.Button(frame3,image=icon8)
button9.pack(side=LEFT)
button9.config(state=DISABLED)

statusBar = Label ( frame2 , text='Status:Ok' )
statusBar.pack ( side=BOTTOM , fill=X )

window.config ( menu=menuBar )
window.maxsize ( width=1350 , height=900 )
window.minsize ( width=800 , height=600 )
window.title ( 'Northern geasco application' )
window.geometry ( '500x500' )
window.mainloop ()
