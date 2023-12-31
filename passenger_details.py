from tkinter import *
from tkinter import messagebox
import pymysql

# Add your own database name and password here to reflect in the code

con = pymysql.connect(host="localhost",user="root",password='toor',database='airline_management_system')
cur = con.cursor()

# Enter Table Names here
passengerDetails = "passenger_details" 
    
def View(): 
    
    root = Tk()
    root.title("Airline Management System")
    root.minsize(width=1500,height=750)
    root.geometry("850x700")


    Canvas1 = Canvas(root) 
    Canvas1.config(bg="#12a4d9")
    Canvas1.pack(expand=True,fill=BOTH)
        
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Passenger Details", bg='black', fg='white', font=('Helvetica',30))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)
    y = 0.25
    
    Label(labelFrame, text="%-30s%-40s%-30s%-30s%-40s%-40s%-35s%-30s"%('Passenger Name','Passenger Phone No','Date of Travel','Where From?','Where To?','Flight No','PNR No','Seat No'),bg='black',fg='white').place(relx=0.07,rely=0.1)
    Label(labelFrame, text="----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------",bg='black',fg='white').place(relx=0.05,rely=0.2)
    getpassengerDetails = "select * from "+passengerDetails
    try:
        cur.execute(getpassengerDetails)
        con.commit()
        for i in cur:
            Label(labelFrame, text="%-40s%-40s%-45s%-30s%-40s%-40s%-40s%-80s"%(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]),bg='black',fg='white').place(relx=0.07,rely=y)
            y += 0.1
    except:
        messagebox.showinfo("Failed to fetch Passenger Details from Database")
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4,rely=0.9, relwidth=0.18,relheight=0.08)
    
    root.mainloop()
