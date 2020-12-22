from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from Existing import ExistingCus
from CreateCus import CreateCus
import pymysql

def CusLogin():

	#Creates Window
	root = Tk()
	root.title("Retro Record Rental")
	size = [400,400] #Resolution

	sw = root.winfo_screenwidth()
	sh = root.winfo_screenheight()

	x = int((sw/2) - (size[0]/2))
	y = int((sh/2) - (size[1]/2))

	root.geometry(f'{size[0]}x{size[1]}+{x}+{y}')
	root.minsize(width=400,height=400)
	root.resizable(True, True)

	Canvas1 = Canvas(root)
	Canvas1.config(bg="pink")
	Canvas1.pack(expand=True,fill=BOTH)

	headingtxt = "Are you an existing\n Customer or a new one"

	headingFrame = Frame(Canvas1,bg="#FFBB00",bd=5)
	headingFrame.place(relx=0.13,rely=0.05,relwidth=0.75,relheight=0.25)


	headingLabel = Label(headingFrame, text = headingtxt, bg='black', fg='white', font=('Courier',15), anchor=CENTER)
	headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

	ExistingBtn = Button(Canvas1,text="Existing Customer",bg='black', fg='white', command=lambda:[root.destroy(),ExistingCus()])
	ExistingBtn.place(relx=0.24,rely=0.35, relwidth=0.50,relheight=0.2)

	NewBtn = Button(Canvas1,text="New Customer",bg='black', fg='white', command=lambda:[root.destroy(),CreateCus()])
	NewBtn.place(relx=0.24,rely=0.6, relwidth=0.50,relheight=0.2)

	quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
	quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
	
	root.mainloop()


