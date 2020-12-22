from tkinter import *
from PIL import ImageTk,Image
import pymysql
from AddRecord import addRecord
from AddEmployee import AddEmployee
from DeleteRecord import deleteRecord
from tkinter import messagebox

def Employee():

	root = Tk()
	root.title("Retro Records Rental")
	root.minsize(width=400,height=400)
	size = [400,400] #Resolution
	sw = root.winfo_screenwidth()
	sh = root.winfo_screenheight()
	x = int((sw/2) - (size[0]/2))
	y = int((sh/2) - (size[1]/2))
	root.geometry(f'{size[0]}x{size[1]}+{x}+{y}')


	Canvas1 = Canvas(root)
	Canvas1.config(bg="orange")
	Canvas1.pack(expand=True,fill=BOTH)

	titleFrame = Frame(root,bg="#FFBB00",bd=5)
	titleFrame.place(relx=0.2,rely=0.03,relwidth=0.6,relheight=0.16)

	titleLabel = Label(titleFrame, text="   What do you want \nto change?", bg='black', fg='white', font=('Courier',15))
	titleLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

	btn1 = Button(root,text="Add Record",bg='black', fg='white', command=addRecord)
	btn1.place(relx=0.28,rely=0.3, relwidth=0.45,relheight=0.1)
	    
	btn2 = Button(root,text="Delete Record",bg='black', fg='white', command=deleteRecord)
	btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
	    
	btn3 = Button(root,text="AddEmployee",bg='black', fg='white', command =AddEmployee)
	btn3.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

	quitBtn = Button(root,text="Quit",bg='gray', fg='white', command=root.destroy)
	quitBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)


