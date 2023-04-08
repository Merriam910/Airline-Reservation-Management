from tkinter import * #allows usage of facilities of tkinter
root=Tk() #creates an instance of the window
root.title("Login")
root.geometry('500x300')
root.configure(height=400,width=400,background='#509099')
def getvals():
    print("Accepted")
#HEADING
Label(text="User Login",font="arial 15 bold", bg='#509099').grid(row=0,column=2)
#FIELDNAMES and PACKING FIELDS
name=Label(root,text="username", bg='#509099').grid(row=1,column=2)
password=Label(root,text="password" ,bg='#509099').grid(row=2,column=2)
#VARIABLES FOR STORING DATA
namevalue=StringVar
passwordvalue=IntVar
checkvalue=IntVar        #will be either one or zero
#Creating entry fields and packing them
nameentry=Entry(root, textvariable=namevalue).grid(row=1,column=3)#Entry value wil always be in our root file
passwordentry=Entry(root,textvariable=passwordvalue).grid(row=2,column=3)
#Creating checkbox and packing(grid)
chckbtn=Checkbutton(text="Remember me?",bg='#509099',variable=checkvalue).grid(row=5,column=3)
#Creating submit button and packing
Button(text="submit", command=getvals).grid(row=6,column=3)
root.mainloop()