from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from ViewRecords import ViewRecord
from ReturnRecord import ReturnRecord
import pymysql

def Record():
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
	Canvas1.config(bg="blue")
	Canvas1.pack(expand=True,fill=BOTH)

	str = "Record Record Rental"
	headingtxt = "Welcome to the\n "+ str

	headingFrame = Frame(Canvas1,bg="#FFBB00",bd=5)
	headingFrame.place(relx=0.13,rely=0.05,relwidth=0.75,relheight=0.25)


	headingLabel = Label(headingFrame, text = headingtxt, bg='black', fg='white', font=('Courier',15), anchor=CENTER)
	headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

	ViewBtn = Button(Canvas1,text="View\n Records",bg='black', fg='white', command=lambda:[ViewRecord()])
	ViewBtn.place(relx=0.24,rely=0.35, relwidth=0.55,relheight=0.2)

	ReturnBtn = Button(Canvas1,text="Return\n Records",bg='black', fg='white', command=lambda:[ReturnRecord()])
	ReturnBtn.place(relx=0.24,rely=0.60, relwidth=0.55,relheight=0.2)

	quitBtn = Button(root,text="Quit",bg='gray', fg='white', command=root.destroy)
	quitBtn.place(relx=0.42,rely=0.9, relwidth=0.18,relheight=0.08)
