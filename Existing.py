from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from Record import Record
import pymysql



mypass = "admin" #Password for database
mydatabase="RetroRecords" #Database Name
myusr = "admin" #Username for database

con = pymysql.connect(host="localhost",user=myusr,password=mypass,database=mydatabase)
cur = con.cursor()


def ExistingCus():

	global UsnEnt,PssEnt,root

	root = Tk()
	root.title("Retro Record Rental")
	root.geometry("400x400")
	root.minsize(width=400,height=400)
	root.resizable(True, True)

	Canvas1 = Canvas(root)
	Canvas1.config(bg="green")
	Canvas1.pack(expand=True,fill=BOTH)

	headingtxt = "Enter your Username\n and Password"

	headingFrame = Frame(Canvas1,bg="#FFBB00",bd=5)
	headingFrame.place(relx=0.13,rely=0.1,relwidth=0.75,relheight=0.25)
	headingLabel = Label(headingFrame, text = headingtxt, bg='black', fg='white', font=('Courier',15), anchor=CENTER)
	headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

	labelFrame = Frame(root,bg='black')
	labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

	UsnLable = Label(labelFrame,text="Username: ", bg='black', fg='white')
	UsnLable.place(relx=0.05,rely=0.2, relheight=0.25)
	UsnEnt = Entry(labelFrame)
	UsnEnt.place(relx=0.3,rely=0.2, relwidth=0.62, relheight=0.25)

	PssLable = Label(labelFrame,text="Password: ", bg='black', fg='white')
	PssLable.place(relx=0.05,rely=0.6, relheight=0.25)
	PssEnt = Entry(labelFrame,show="*")
	PssEnt.place(relx=0.3,rely=0.6, relwidth=0.62, relheight=0.25)

	SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=lambda:[Login()])
	SubmitBtn.place(relx=0.1,rely=0.9, relwidth=0.18,relheight=0.08)
    
	quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
	quitBtn.place(relx=0.72,rely=0.9, relwidth=0.18,relheight=0.08)

def Login():
	arr = []
	UN = UsnEnt.get()
	PS = PssEnt.get()
	try:
		cur.execute( "select * from Customer where CUsr = \'"+UN+"\'")
		arr.append(cur.fetchall())
		arr = arr[0][0]
		Username = arr[2]
		Password = arr[3]
		if UN == Username and PS == Password:
			messagebox.showinfo(title='Welcome',message="Welcome "+arr[1])
			root.destroy()
			f = open("CID.txt", "w")
			f.write(str(arr[0]))
			f.close()
			Record()
		else:
			messagebox.showerror(title='Error',message="Wrong Username or Password")

	except:
		messagebox.showerror(title='Error',message="Username not found")
	


	