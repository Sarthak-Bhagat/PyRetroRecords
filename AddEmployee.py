from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "admin"
mydatabase="RetroRecords"
myusr = "admin"

con = pymysql.connect(host="localhost",user=myusr,password=mypass,database=mydatabase)
cur = con.cursor()

def AddEmployee():

	global NameEnt, UsnEnt, PssEnt,root

	root = Tk()
	root.title("Employee Only")
	root.geometry("400x400")
	root.minsize(width=400,height=400)
	root.resizable(True, True)

	Canvas1 = Canvas(root)
	Canvas1.config(bg="green")
	Canvas1.pack(expand=True,fill=BOTH)

	headingtxt = "New Employee"

	headingFrame = Frame(Canvas1,bg="#FFBB00",bd=5)
	headingFrame.place(relx=0.13,rely=0.1,relwidth=0.75,relheight=0.25)


	headingLabel = Label(headingFrame, text = headingtxt, bg='black', fg='white', font=('Courier',15), anchor=CENTER)
	headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

	labelFrame = Frame(root,bg='black')
	labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

	NameLable = Label(labelFrame,text="Your Name: ", bg='black', fg='white')
	NameLable.place(relx=0.05,rely=0.15, relheight=0.175)
	NameEnt = Entry(labelFrame)
	NameEnt.place(relx=0.3,rely=0.15, relwidth=0.62, relheight=0.125)

	UsnLable = Label(labelFrame,text="Username: ", bg='black', fg='white')
	UsnLable.place(relx=0.05,rely=0.35, relheight=0.125)
	UsnEnt = Entry(labelFrame)
	UsnEnt.place(relx=0.3,rely=0.35, relwidth=0.62, relheight=0.125)

	PssLable = Label(labelFrame,text="Password: ", bg='black', fg='white')
	PssLable.place(relx=0.05,rely=0.55, relheight=0.125)
	PssEnt = Entry(labelFrame)
	PssEnt.place(relx=0.3,rely=0.55, relwidth=0.62, relheight=0.125)

	PhoneLB = Label(labelFrame,text="Phone No.: ", bg='black', fg='white')
	PhoneLB.place(relx=0.05,rely=0.75, relheight=0.125)
	PhoneEN = Entry(labelFrame)
	PhoneEN.place(relx=0.3,rely=0.75, relwidth=0.62, relheight=0.125)

	SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=lambda:[Add()])
	SubmitBtn.place(relx=0.1,rely=0.9, relwidth=0.18,relheight=0.08)
    
	quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
	quitBtn.place(relx=0.72,rely=0.9, relwidth=0.18,relheight=0.08)



def Add():
	name = NameEnt.get()
	username = UsnEnt.get()
	password = PssEnt.get()
	k = name+' has been added'
	cur.execute( "INSERT INTO Employee(Name, EUsr, EPas, Phone_No) VALUES(\'"+name+"\',\'"+username+"\',\'"+password+"\',\'"+Phone_No+"\')")

	con.commit()
	messagebox.showinfo(title='Success', message=k)
	root.destroy()

