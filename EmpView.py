from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import pymysql

mypass = "admin"
mydatabase="RetroRecords"
myusr = "admin"

con = pymysql.connect(host="localhost",user=myusr,password=mypass,database=mydatabase)
cur = con.cursor()

def openWind(RecordID):

	global RID,Name,rootA

	rootA = Tk()
	rootA.title("Details")
	rootA.minsize(width=400,height=400)
	
	RID = RecordID


	size = [400,400] #Resolution

	sw = rootA.winfo_screenwidth()
	sh = rootA.winfo_screenheight()

	x = int((sw/2) - (size[0]/2))
	y = int((sh/2) - (size[1]/2))

	rootA.geometry(f'{size[0]}x{size[1]}+{x}+{y}')

	Canvas1 = Canvas(rootA) 
	Canvas1.config(bg="red")
	Canvas1.pack(expand=True,fill=BOTH)

	arr = []
	cur.execute( "select * from Records where RID="+RecordID+" AND Stock >=1")
	arr.append(cur.fetchall())
	Stock = arr[0][0][1]
	Name = arr[0][0][2]
	Arist = arr[0][0][3]
	Stock = str(arr[0][0][1])
	Canvas1.focus_set()

	headingFrame1 = Frame(rootA,bg="#FFBB00",bd=5)
	headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
		
	headingLabel = Label(headingFrame1, text="Record #"+RID, bg='black', fg='white', font=('Courier',15))
	headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

	labelFrame = Frame(rootA,bg='black')
	labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

	NameLB = Label(labelFrame,  text="Record Name :\t"+Name,bg='black',fg='white')
	NameLB.place(relx=0.07,rely=0.1)

	AristLB = Label(labelFrame,  text="Composer:\t"+Arist,bg='black',fg='white')
	AristLB.place(relx=0.07,rely=0.3)

	StockLB = Label(labelFrame,  text="Stock:\t\t"+Stock,bg='black',fg='white')
	StockLB.place(relx=0.07,rely=0.5)

	RentBtn = Button(Canvas1,text="Stock",bg='#f7f1e3', fg='black', command=Stock_it)
	RentBtn.place(relx=0.75,rely=0.9, relwidth=0.18,relheight=0.08)

	BackBtn = Button(Canvas1,text="Back",bg='#f7f1e3', fg='black', command=rootA.destroy)
	BackBtn.place(relx=0.15,rely=0.9, relwidth=0.18,relheight=0.08)

	
def Stock_it():
	stock_it = "UPDATE Records SET Stock = Stock WHERE RID = "+RID
	cur.execute(stock_it)
	con.commit()
	root.destroy()
	rootA.destroy()
	openWind(RID)	
	EmpView()


def EmpView(): 

	global root
	
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
		
	headingLabel = Label(headingFrame1, text="View Records", bg='black', fg='white', font=('Courier',15))
	headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
	
	labelFrame = Frame(root,bg='black')
	labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
	
	
	
	Label(labelFrame, text="RID \t\t Title",bg='black',fg='white').place(relx=0.07,rely=0.1)


	Label(labelFrame, text="---------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)

	

	arr = []
	try:
		cur.execute( "select RID,Name from Records WHERE Stock > 0")
		arr.append(cur.fetchall())
	except:
		messagebox.showerror(title='Error',message="Failed to fetch files from database")
	j = 0
	y = 0.25
	labels = []
	btn = []

	scrollbar = Scrollbar(labelFrame)
	scrollbar.pack( side = RIGHT, fill = Y )

	for i in range(len(arr[0])):
		labels.append(str(arr[0][j][0])+'\t\t'+arr[0][j][1])

		mylist = Listbox(labelFrame, yscrollcommand = scrollbar.set,bg = 'black',fg ='white')

		Outputlb = Label(labelFrame, text=labels[i],bg='black',fg='white')
		Outputlb.place(relx=0.07,rely=y)
		y += 0.1
		j += 1

	y = 0.25
	
	if(len(labels)>0):
		for i in range(len(arr[0])):
			btn.append(Button(labelFrame, text='Info', command=lambda c=i: openWind(labels[c].split()[0])))
			btn[i].place(relx=0.9,rely=y,relwidth=0.07,relheight=0.07)
			y += 0.1
	
	BackBtn = Button(root,text="Back",bg='#f7f1e3', fg='black', command=root.destroy)
	BackBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
	
	root.mainloop()

EmpView()