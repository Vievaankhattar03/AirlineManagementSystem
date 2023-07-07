from tkinter import *
from tkinter import messagebox
import pymysql

con = pymysql.connect(host="localhost",user="root",password='toor',database='airline_management_system')
cur = con.cursor()

passengerDetails="passenger_details"
bookingDetails="booking_details"
cancellationDetails="flight_cancellation"

def cancelflight():
    
    PNR_No = PNR.get()
    EnterPassengerDetails = "delete from "+passengerDetails+" where (PNR_No = '"+PNR_No+"')"
    EnterBookingDetails = "delete from "+bookingDetails+" where (PNR_No = '"+PNR_No+"')"
    EnterCancellationDetails = "insert into "+cancellationDetails+" values('"+PNR_No+"')"
    
    try:
        cur.execute(EnterPassengerDetails)
        con.commit()
        cur.execute(EnterBookingDetails)
        con.commit()
        cur.execute(EnterCancellationDetails)
        con.commit()
        messagebox.showinfo('Success',"Flight Cancelled Successfully")
    except:
        messagebox.showinfo("Please check PNR NO")
    

    print(PNR_No)

    PNR.delete(0, END)
    root.destroy()
    
def cancelf():
    global PNR, Name, PhoneNo, Address, EmailID, DOB, Travel, FNo, WFrom, WTo, Seat, con, cur, root, Canvas1, passengerDetails, bookingDetails, cancellationDetails

    root = Tk()
    root.title("Airline Management System")
    root.minsize(width=1000,height=700)
    root.geometry("1000x500")

    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="#006B38")
    Canvas1.pack(expand=True,fill=BOTH)
        
    headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)
        
    headingLabel = Label(headingFrame1, text="Flight Cancellation", bg='black', fg='white', font=('Helvetica',30))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)
    
    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)   
        
    # Book ID to Delete
    lb2 = Label(labelFrame,text="PNR NO : ", bg='black', fg='white',font=('Helvetica',10))
    lb2.place(relx=0.05,rely=0.2)
        
    PNR = Entry(labelFrame)
    PNR.place(relx=0.3,rely=0.2, relwidth=0.62)
    
    #Submit Button
    SubmitBtn = Button(root,text="SUBMIT",bg='#d1ccc0', fg='black',font=('Helvetica',12),command=cancelflight)
    SubmitBtn.place(relx=0.28,rely=0.9, relwidth=0.10,relheight=0.08)
    
    quitBtn = Button(root,text="Quit",bg='#f7f1e3', fg='black',font=('Helvetica',12), command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9, relwidth=0.10,relheight=0.08)
    
    root.mainloop()
