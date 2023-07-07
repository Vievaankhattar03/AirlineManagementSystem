from tkinter import *
import pymysql
from tkinter import messagebox
from booking_details import *
from flight_details import *
from passenger_details import *
from flight_cancellation import *
con=pymysql.connect(database='airline_management_system',password='toor',user='root',host='localhost')
cur=con.connect()
root=Tk()
root.config(background='#6237A0')
root.title("Airline Management System")
root.minsize(width=1500, height=750)
root.geometry("850x700")

same=True
n=0.25

headingFrame1=Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.28,rely=0.1,relwidth=0.45,relheight=0.16)

headingLabel=Label(headingFrame1, text="Airline Management \n System",bg='black', fg='white',font=('Helvetica',30))
headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

btn1 = Button(root,text="Book a Ticket",bg='#F5B301', fg='white',font=('Helvetica',12),command=bookingdetails)
btn1.place(relx=0.28,rely=0.4, relwidth=0.45,relheight=0.1)
    
btn2 = Button(root,text="Cancel Booking",bg='black', fg='white',font=('Helvetica',12),command=cancelf)
btn2.place(relx=0.28,rely=0.5, relwidth=0.45,relheight=0.1)
    
btn3 = Button(root,text="View Flight Details",bg='#F5B301', fg='white',font=('Helvetica',12),command=details)
btn3.place(relx=0.28,rely=0.6, relwidth=0.45,relheight=0.1)
    
btn4 = Button(root,text="Passenger Details",bg='black', fg='white',font=('Helvetica',12),command=View)
btn4.place(relx=0.28,rely=0.7, relwidth=0.45,relheight=0.1)

root.mainloop()
