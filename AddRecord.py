from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

def recordRegister():
	
	RID = recordInfo1.get()
	title = recordInfo2.get()
	artist = recordInfo3.get()
	stock = recordInfo4.get()

	insertRecords = "INSERT INTO Records (RID, Name, Artist, Stock) VALUES ('"+RID+"', '"+title+"', '"+artist+"', '"+stock+"')"

	try:
		cur.execute(insertRecords)
		con.commit()
		messagebox.showinfo('Success',"Record added successfully")
	except:
		messagebox.showinfo("Error","Can't add data into Database")
	root.destroy()
	
def addRecord(): 
	
	global recordInfo1,recordInfo2,recordInfo3,recordInfo4,recordInfo5,recordInfo6,Canvas1,con,cur,recordTable,root
	
	root = Tk()
	root.title("Library")
	root.minsize(width=400,height=400)
	root.geometry("600x500")

	
	mypass = "admin"
	mydatabase="RetroRecords"
	myusr = "admin"

	con = pymysql.connect(host="localhost",user=myusr,password=mypass,database=mydatabase)
	cur = con.cursor()

	Canvas1 = Canvas(root)
	
	Canvas1.config(bg="#ff6e40")
	Canvas1.pack(expand=True,fill=BOTH)
		
	headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
	headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

	headingLabel = Label(headingFrame1, text="Add Records", bg='black', fg='white', font=('Courier',15))
	headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)


	labelFrame = Frame(root,bg='black')
	labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)
		
	# Record ID
	lb1 = Label(labelFrame,text="Record ID : ", bg='black', fg='white')
	lb1.place(relx=0.05,rely=0.125, relheight=0.08)
		
	recordInfo1 = Entry(labelFrame)
	recordInfo1.place(relx=0.3,rely=0.1, relwidth=0.62, relheight=0.12)
		
	# Title
	lb2 = Label(labelFrame,text="Title : ", bg='black', fg='white')
	lb2.place(relx=0.05,rely=0.325, relheight=0.08)
		
	recordInfo2 = Entry(labelFrame)
	recordInfo2.place(relx=0.3,rely=0.3, relwidth=0.62, relheight=0.12)
		
	# Record Artist
	lb3 = Label(labelFrame,text="Artist : ", bg='black', fg='white')
	lb3.place(relx=0.05,rely=0.525, relheight=0.08)
		
	recordInfo3 = Entry(labelFrame)
	recordInfo3.place(relx=0.3,rely=0.5, relwidth=0.62, relheight=0.12)

	# Record Stock
	lb4 = Label(labelFrame,text="Stock : ", bg='black', fg='white')
	lb4.place(relx=0.05,rely=0.725, relheight=0.08)
		
	recordInfo4 = Entry(labelFrame)
	recordInfo4.place(relx=0.3,rely=0.7, relwidth=0.62, relheight=0.12)

	#Submit Button
	SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',command=recordRegister)
	SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.18,relheight=0.08)
	
	quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
	quitBtn.place(relx=0.53,rely=0.9, relwidth=0.18,relheight=0.08)
	
	root.mainloop()
