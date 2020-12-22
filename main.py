from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from EmployeeLogin import EmpLogin
from CusLogin import CusLogin
import pymysql

def main():

	#Creates a Window
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
	Canvas1.config(bg="#ff6e40")
	Canvas1.pack(expand=True,fill=BOTH)


	headingtxt = "Are you a Customer \n or an Employee"


	headingFrame = Frame(Canvas1,bg="#FFBB00",bd=5)
	headingFrame.place(relx=0.13,rely=0.1,relwidth=0.75,relheight=0.25)


	headingLabel = Label(headingFrame, text = headingtxt, bg='black', fg='white', font=('Courier',15), anchor=CENTER)
	headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

	CustomerBtn = Button(Canvas1,text="Customer",bg='black', fg='white', command=lambda:[root.destroy(),CusLogin()]) #Destroys window and Calls Customer Login
	CustomerBtn.place(relx=0.24,rely=0.45, relwidth=0.55,relheight=0.2)

	EmployeeBtn = Button(Canvas1,text="Employee",bg='black', fg='white', command=lambda:[root.destroy(),EmpLogin()]) #Destroys window and Calls Employee Login
	EmployeeBtn.place(relx=0.24,rely=0.70, relwidth=0.55,relheight=0.2)

	root.mainloop()

main()