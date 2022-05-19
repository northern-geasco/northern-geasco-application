from tkinter import ttk , Tk , Label , PhotoImage , Button , Entry , LEFT

window=Tk()
icon1=PhotoImage(file='share.png')





labelFrame=Label(window,text='file sender/reciever')
labelFrame.pack()
entry=Entry(window,text='enter the file name',width=80)
entry.pack()
entry2=Entry(window,text='enter the port name',width=80)
entry2.pack()
button=Button(window,text='send',image=icon1)
button.pack()


window.title('File sender reciever GUI')
window.geometry('700x500')
window.mainloop()
