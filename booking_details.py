from tkinter import *
from tkinter import messagebox
import pymysql
def booking():
    Passenger_Name=Name.get()
    Passenger_PhoneNo=PhoneNo.get()
    Passenger_Address=Address.get()
    Passenger_EmailID=EmailID.get()
    Date_of_Birth=DOB.get()
    Date_of_Travel=Travel.get()
    Flight_No=FNo.get()
    Where_From=WFrom.get()
    Where_To=WTo.get()
    PNR_No=PNR.get()
    Seat_No=Seat.get()

    EnterBookingDetails="insert into "+bookingDetails+" values('"+Passenger_Name+"','"+Passenger_PhoneNo+"','"+Passenger_Address+"','"+Passenger_EmailID+"','"+Date_of_Birth+"','"+Date_of_Travel+"','"+Where_From+"','"+Where_To+"','"+Flight_No+"','"+PNR_No+"','"+Seat_No+"')"
    EnterPassengerDetails="insert into "+passengerDetails+" values('"+Passenger_Name+"','"+Passenger_PhoneNo+"','"+Date_of_Travel+"','"+Where_From+"','"+Where_To+"','"+Flight_No+"','"+PNR_No+"','"+Seat_No+"')"
    try:
        cur.execute(EnterBookingDetails)
        con.commit()
        cur.execute(EnterPassengerDetails)
        con.commit()
        messagebox.showinfo("Success", "Flight Booked Successfully")
    except:
        messagebox.showinfo("Error", "Can't add Data into Database")

    print(Passenger_Name)
    print(Passenger_PhoneNo)
    print(Passenger_Address)
    print(Passenger_EmailID)
    print(Date_of_Birth)
    print(Date_of_Travel)
    print(Flight_No)
    print(Where_From)
    print(Where_To)
    print(PNR_No)
    print(Seat_No)

    root.destroy()

def bookingdetails():
    global Name, PhoneNo, Address, EmailID, DOB, Travel, FNo, WFrom, WTo, PNR, Seat, con, cur, bookingDetails, root, Canvas1, passengerDetails

    root=Tk()
    root.title("Airline Management System")
    root.minsize(width=1500,height=750)
    root.geometry("850x700")

    con=pymysql.connect(host="localhost",user="root",password="toor",database="airline_management_system")
    cur=con.cursor()
    
    bookingDetails = "booking_details"
    passengerDetails = "passenger_details"
    
    Canvas1 = Canvas(root)
    
    Canvas1.config(bg="maroon")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root,bg="yellow",bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame1, text="Flight Booking Details", bg='black', fg='white', font=('Helvetica',30))
    headingLabel.place(relx=0,rely=0, relwidth=1, relheight=1)

    lb1=Label(root,text="Passenger Name:",bg="maroon",fg="white", font=("Helvetica", 15))
    lb1.place(relx=0.01,rely=0.30,relheight=0.05, relwidth=0.23)

    Name=Entry(root,width=30,font=("Helvetica",15))
    Name.place(relx=0.3,rely=0.30,relheight=0.04, relwidth=0.30)

    lb2=Label(root,text="Phone No:", bg="maroon",fg="white", font=("Helvetica",15))
    lb2.place(relx=0.01,rely=0.35,relheight=0.05,relwidth=0.23)

    PhoneNo=Entry(root,width=30,font=("Helvetica",15))
    PhoneNo.place(relx=0.3,rely=0.35,relheight=0.04,relwidth=0.30)

    lb3=Label(root,text="Address:", bg="maroon",fg="white",font=("Helvetica",15))
    lb3.place(relx=0.01, rely=0.40,relheight=0.05,relwidth=0.23)

    Address=Entry(root,width=30,font=("Helvetica",15))
    Address.place(relx=0.3, rely=0.40,relheight=0.04,relwidth=0.30)

    lb4=Label(root, text="Email ID:", bg="maroon", fg="white",font=("Helvetica",15))
    lb4.place(relx=0.01, rely=0.45, relheight=0.05,relwidth=0.23)

    EmailID=Entry(root,width=30,font=("Helvetica",15))
    EmailID.place(relx=0.3,rely=0.45, relheight=0.04,relwidth=0.30)

    lb5=Label(root, text="Date of Birth:", bg="maroon", fg="white", font=("Helvetica",15))
    lb5.place(relx=0.01, rely=0.50, relheight=0.05, relwidth=0.23)

    DOB=Entry(root, width=30, font=("Helvetica",15))
    DOB.place(relx=0.3, rely=0.50, relheight=0.04, relwidth=0.30)

    lb6=Label(root, text="Date of Travelling:", bg="maroon", fg="white", font=("Helvetica",15))
    lb6.place(relx=0.01,rely=0.55, relheight=0.05, relwidth=0.23)

    Travel=Entry(root, width=30, font=("Helvetica",15))
    Travel.place(relx=0.3, rely=0.55, relheight=0.04,relwidth=0.30)

    lb7=Label(root, text="Where From?:", bg="maroon", fg="white", font=("Helvetica",15))
    lb7.place(relx=0.01, rely=0.60, relheight=0.05, relwidth=0.23)

    WFrom=Entry(root, width=30, font=("Helvetica",15))
    WFrom.place(relx=0.3, rely=0.60, relheight=0.04, relwidth=0.30)

    lb8=Label(root, text="Where To?:", bg="maroon", fg="white", font=("Helvetica",15))
    lb8.place(relx=0.01, rely=0.65, relheight=0.05, relwidth=0.23)

    WTo=Entry(root, width=30, font=("Helvetica",15))
    WTo.place(relx=0.3, rely=0.65, relheight=0.04, relwidth=0.30)

    lb9=Label(root, text="Flight No:", bg="maroon", fg="white", font=("Helvetica",15))
    lb9.place(relx=0.01, rely=0.70, relheight=0.05, relwidth=0.23)

    FNo=Entry(root, width=30, font=("Helvetica",15))
    FNo.place(relx=0.3, rely=0.70, relheight=0.04, relwidth=0.30)

    lb10=Label(root, text="PNR No:", bg="maroon", fg="white", font=("Helvetica",15))
    lb10.place(relx=0.01, rely=0.75, relheight=0.05, relwidth=0.23)

    PNR=Entry(root, width=30, font=("Helvetica",15))
    PNR.place(relx=0.3, rely=0.75, relheight=0.04, relwidth=0.30)

    lb11=Label(root, text="Seat No:", bg="maroon", fg="white", font=("Helvetica",15))
    lb11.place(relx=0.01, rely=0.80, relheight=0.05, relwidth=0.23)

    Seat=Entry(root, width=30, font=("Helvetica",15))
    Seat.place(relx=0.3, rely=0.80, relheight=0.04, relwidth=0.30)

    btn1=Button(root, text="Submit", bg="maroon", fg="white", font=("Helvetica",20), command=booking)
    btn1.place(relx=0.15, rely=0.85, relheight=0.10, relwidth=0.30)

    btn2=Button(root, text="Quit", bg="maroon", fg="white", font=("Helvetica",20), command=root.destroy)
    btn2.place(relx=0.60, rely=0.85, relheight=0.10, relwidth=0.30)

    root.mainloop()
