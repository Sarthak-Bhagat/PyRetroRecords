from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "admin"
mydatabase="RetroRecords"
myusr = "admin"

con = pymysql.connect(host="localhost",user=myusr,password=mypass,database=mydatabase)
cur = con.cursor()

def Return(RecordID):
	unrent_it = "UPDATE Records SET Stock = Stock + 1 WHERE RID = "+RecordID
	cur.execute(unrent_it)
	con.commit()
	messagebox.showinfo(title='Success',message="Thank you for returning\nthe record disk safely")	
	return_it = "UPDATE RENTED SET NRENTED = NRENTED - 1 WHERE RID = "+RecordID+" AND CID = "+CID
	cur.execute(return_it)
	con.commit()

	check_it = "SELECT NRENTED FROM RENTED WHERE RID = "+RecordID+" AND CID = "+CID
	cur.execute(check_it)
	con.commit()
	k = cur.fetchall()[0][0]
	if k < 1:
		delete_it = "DELETE FROM RENTED WHERE RID = "+RecordID+" AND CID = "+CID
		cur.execute(delete_it)
		con.commit()
	root.destroy()
	ReturnRecord()


	


def ReturnRecord(): 
	
	global root,CID

	root = Tk()
	root.title("Retro Record Rental")
	root.minsize(width=400,height=400)

	size = [600,600] #Resolution

	sw = root.winfo_screenwidth()
	sh = root.winfo_screenheight()

	x = int((sw/2) - (size[0]/2))
	y = int((sh/2) - (size[1]/2))

	root.geometry(f'{size[0]}x{size[1]}+{x}+{y}')


	Canvas1 = Canvas(root) 
	Canvas1.config(bg="#12a4d9")
	Canvas1.pack(expand=True,fill=BOTH)
		
		
	headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
	headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
		
	headingLabel = Label(headingFrame1, text="Records Rented\nby You", bg='black', fg='white', font=('Courier',15))
	headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
	
	labelFrame = Frame(root,bg='black')
	labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
	
	
	
	Label(labelFrame, text="RID \tN\t Title",bg='black',fg='white').place(relx=0.07,rely=0.1)


	Label(labelFrame, text="---------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)

	arr = []
	a = []
	b = []
	try:
		f = open("CID.txt", "r")
		CID = f.readline()
		cur.execute( "SELECT RID,NRENTED FROM RENTED WHERE CID = "+str(CID))
		arr.append(cur.fetchall())
	except:
		messagebox.showerror(title='Error',message="Failed to fetch files from database")

	for i in range(len(arr[0])):
		a.append(arr[0][i][0])
	try:
		for i in range(len(a)):
			cur.execute( "SELECT Name FROM Records WHERE RID = "+str(a[i]))
			b.append(cur.fetchall())
	except:
		messagebox.showerror(title='Error',message="Failed to fetch files from database")


	j = 0
	y = 0.25
	labels = []
	btn = []

	scrollbar = Scrollbar(labelFrame)
	scrollbar.pack( side = RIGHT, fill = Y )

	for i in range(len(b)):
		title = str(b[i][0][0])
		n = str(arr[0][i][1])
		rid = str(a[i])
		labels.append(rid+" \t"+n+"\t "+title)
		mylist = Listbox(labelFrame, yscrollcommand = scrollbar.set,bg = 'black',fg ='white')

		Outputlb = Label(labelFrame, text=labels[i],bg='black',fg='white')
		Outputlb.place(relx=0.07,rely=y)
		y += 0.1
		j += 1

	y = 0.25
	
	for i in range(len(b)):
		btn.append(Button(labelFrame, text='Return', command=lambda c=i: Return(labels[c].split()[0])))
		btn[i].place(relx=0.75,rely=y,relwidth=0.2,relheight=0.1)
		y += 0.1
	
	BackBtn = Button(root,text="Back",bg='#f7f1e3', fg='black', command=root.destroy)
	BackBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
	
	root.mainloop()