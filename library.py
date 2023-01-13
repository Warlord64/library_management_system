#from multiprocessing import active_children
from tkinter import*
from tkinter import ttk
import tkinter as tk
import mysql.connector
import tkinter
from tkinter import messagebox
import datetime


class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("library management system")
        self.root.geometry("1366x700+0+0")

#========================var========================


        self.member_var=StringVar()
        self.prn_var=StringVar()
        self.id_var=StringVar()
        self.firstname_var=StringVar()
        self.lastname_var=StringVar()
        self.address1_var=StringVar()
        self.address2_var=StringVar()
        self.postcode_var=StringVar()
        self.mobile_var=StringVar()
        self.bookid_var=StringVar()
        self.booktitle_var=StringVar()
        self.auther_var=StringVar()
        self.dateborrowed_var=StringVar()
        self.datedue_var=StringVar()
        self.daysonbook_var=StringVar()
        self.lateratefine_var=StringVar()
        self.dateoverdue_var=StringVar()
        self.finalprice_var=StringVar()


#label title on top

        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="#343434",fg="white",bd=16,relief=FLAT,font=("Bauhaus 93",25,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,padx=20,pady=3,bg='#343434')
        frame.place(x=0,y=70,width=1366,height=400)

#df left
        DataFrameLeft=LabelFrame(frame,text="LIBRARY MEMBER INFORMATION",bg="#343434",fg="white",bd=10,relief=RIDGE,borderwidth=6,font=("Cascadia Code",15,"bold"))
        DataFrameLeft.place(x=0,y=6,width=850,height=350)


        lblMembr=Label(DataFrameLeft,font=("monospace",12,"bold"),fg="white",
        text="Member Type: ",
        bg="#343434",
        
        padx=2,pady=6)
        lblMembr.grid(row=0,column=0,sticky=W)

        #form combobox
        comMember=ttk.Combobox(DataFrameLeft,textvariable=self.member_var,font=("monospace",13,"bold"),width=27,state="readonly")
        comMember["value"]=("Admin Staff","Student","Lecturer")
        comMember.grid(row=0,column=1)

        #prn no.
        lblPrn_no=Label(DataFrameLeft,text="PRN No: ",bg="#343434",font=("monospace",12,"bold"),fg="white",padx=2,pady=6)
        lblPrn_no.grid(row=1,column=0,sticky=W)
        txtPrn_no=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.prn_var,width=29)
        txtPrn_no.grid(row=1,column=1)

        #id_no
        id_no=Label(DataFrameLeft,text="ID No: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        id_no.grid(row=2,column=0,sticky=W)
        text_id=Entry(DataFrameLeft,textvariable=self.id_var,
        font=("monospace",13,"bold"),width=29)
        text_id.grid(row=2,column=1)
        

        #firstname
        FirstName=Label(DataFrameLeft,text="FirstName: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        FirstName.grid(row=3,column=0,sticky=W)
        FN_text=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.firstname_var,width=29)
        FN_text.grid(row=3,column=1)

        #LastName
        LastName=Label(DataFrameLeft,text="LastName: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        LastName.grid(row=4,column=0,sticky=W)
        LastName_text=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.lastname_var,width=29)
        LastName_text.grid(row=4,column=1)


        #Address1
        Address1=Label(DataFrameLeft,text="Address1: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        Address1.grid(row=5,column=0,sticky=W)
        Address1_text=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.address1_var,width=29)
        Address1_text.grid(row=5,column=1)

        #Address2
        Address2=Label(DataFrameLeft,text="Address2: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        Address2.grid(row=6,column=0,sticky=W)
        Address2_text=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.address2_var,width=29)
        Address2_text.grid(row=6,column=1)

        #Post_Code
        Post_Code=Label(DataFrameLeft,text="Post Code: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        Post_Code.grid(row=7,column=0,sticky=W)
        Post_Txt=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.postcode_var,width=29)
        Post_Txt.grid(row=7,column=1)

        #mob_no
        mob_no=Label(DataFrameLeft,text="Mobile Number: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        mob_no.grid(row=8,column=0,sticky=W)
        mob_no_Txt=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.mobile_var,width=29)
        mob_no_Txt.grid(row=8,column=1)


        #next_row


        #Book_id
        Book_id=Label(DataFrameLeft,text="Book ID: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        Book_id.grid(row=0,column=2,sticky=W)
        Book_id_Txt=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.bookid_var,width=29)
        Book_id_Txt.grid(row=0,column=3)


        #Book_ttl
        Book_ttl=Label(DataFrameLeft,text="Book Title: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        Book_ttl.grid(row=1,column=2,sticky=W)
        Book_ttl_Txt=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.booktitle_var,width=29)
        Book_ttl_Txt.grid(row=1,column=3)


        #Auth_name
        Auth_name=Label(DataFrameLeft,text="Auther Name: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        Auth_name.grid(row=2,column=2,sticky=W)
        Auth_name_Txt=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.auther_var,width=29)
        Auth_name_Txt.grid(row=2,column=3)


        #dt_borrow
        dt_borrow=Label(DataFrameLeft,text="Date Borrowed: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        dt_borrow.grid(row=3,column=2,sticky=W)
        dt_borrow_Txt=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.dateborrowed_var,width=29)
        dt_borrow_Txt.grid(row=3,column=3)

        #dt_due
        dt_due=Label(DataFrameLeft,text="Date Due: ",bg="#343434",font=("monospace",12,"bold"),fg="white",padx=2,pady=6)
        dt_due.grid(row=4,column=2,sticky=W)
        dt_due_Txt=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.datedue_var,width=29)
        dt_due_Txt.grid(row=4,column=3)

        #dobk
        dobk=Label(DataFrameLeft,text="Days on Book: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        dobk.grid(row=5,column=2,sticky=W)
        dobk_Txt=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.daysonbook_var,width=29)
        dobk_Txt.grid(row=5,column=3)

        #lrf
        dobk=Label(DataFrameLeft,text="Late Return Fine: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        dobk.grid(row=6,column=2,sticky=W)
        dobk_Txt=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.lateratefine_var,width=29)
        dobk_Txt.grid(row=6,column=3)


        #dod
        dod=Label(DataFrameLeft,text="Date Over Due: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        dod.grid(row=7,column=2,sticky=W)
        dod_Txt=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.dateoverdue_var,width=29)
        dod_Txt.grid(row=7,column=3)

        #Actual_price
        Actual_price=Label(DataFrameLeft,text="Actual Price: ",bg="#343434",fg="white",font=("monospace",12,"bold"),padx=2,pady=6)
        Actual_price.grid(row=8,column=2,sticky=W)
        Actual_price_Txt=Entry(DataFrameLeft,font=("monospace",13,"bold"),textvariable=self.finalprice_var,width=29)
        Actual_price_Txt.grid(row=8,column=3)


        
        




#dataframe right

        DataFrameRight=LabelFrame(frame,text="Book Details",bg='#343434',fg="white",bd=10,relief=RIDGE,borderwidth=6,font=("Cascadia Code",15,"bold"))
        DataFrameRight.place(x=860,y=7,width=450,height=350)


        self.txtBox=Text(DataFrameRight, font=("monospace",12,"bold"),width=28,height=15.5)
        self.listBox=Listbox(DataFrameRight,font=("monospace",12,"bold"),width=17,height=15)
        #scrollbars
        listScrollbar = Scrollbar(DataFrameRight,orient=HORIZONTAL)
        listScrollbar1 = Scrollbar(DataFrameRight,orient=VERTICAL)
        
        listbooks=['Telephone Book','Learn Python The Hard Way','Python Programming','Math','Python Basics','Into to Machine Learning','Fluent English','Digital Marketing','My Python Buddy','Learn HTML','Calculas 12th','Some Basic Concept of Chemestry','Kabir ke Dohe','mysql','Machine Learning with Python', 'Advance Python', 'Encyclopedia', 'Dictionery', 'Modern Physics']

        def SelectBook(event=""):
            value=str(self.listBox.get(self.listBox.curselection()))
            x=value
            if (x=="Telephone Book"):
                self.bookid_var.set("BKID12344")
                self.booktitle_var.set("Telephone Book")
                self.auther_var.set("company")
                #for date
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.78")
            elif (x=="Learn Python The Hard Way"):
                self.bookid_var.set("BKID12345")
                self.booktitle_var.set("Learn Python The Hard Way")
                self.auther_var.set("author1")
                #for date
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.488")
            elif (x=="Python Programming"):
                self.bookid_var.set("BKID12346")
                self.booktitle_var.set("Python Programming")
                self.auther_var.set("author2")
                #for date
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.299")
            elif (x=="Math"):
                self.bookid_var.set("BKID12347")
                self.booktitle_var.set("Math")
                self.auther_var.set("N.C.E.R.T")
                #for date
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.104")
            elif (x=="Python Basics"):
                self.bookid_var.set("BKID12348")
                self.booktitle_var.set("Math")
                self.auther_var.set("N.C.E.R.T")
                #for date
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.180")
            elif (x=="Into to Machine Learning"):
                self.bookid_var.set("BKID12349")
                self.booktitle_var.set("Into to Machine Learning")
                self.auther_var.set("aDVANCEABC")
                #for date
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1180")
            elif (x=="Fluent English"):
                self.bookid_var.set("BKID12350")
                self.booktitle_var.set("Fluent English")
                self.auther_var.set("ENGNEW")
                #for date
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.699")
            elif (x=="Digital Marketing"):
                self.bookid_var.set("BKID12351")
                self.booktitle_var.set("Digital Marketing")
                self.auther_var.set("CATMSTER")
                #for date
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.3499")
            elif (x=="My Python Buddy"):
                self.bookid_var.set("BKID12352")
                self.booktitle_var.set("My Python Buddy")
                self.auther_var.set("oGGY")
                #for date
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.499")
            elif (x=="Learn HTML"):
                self.bookid_var.set("BKID12353")
                self.booktitle_var.set("Learn HTML")
                self.auther_var.set("JOHN DUCKKET")
                #for date
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=10)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(10)
                self.lateratefine_var.set("Rs.100")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1299")
            elif (x=="Learn HTML"):
                self.bookid_var.set("BKID12353")
                self.booktitle_var.set("Learn HTML")
                self.auther_var.set("JOHN DUCKKET")
                #for date
                d1=datetime.datetime.today()
                d2=datetime.timedelta(days=15)
                d3=d1+d2
                self.dateborrowed_var.set(d1)
                self.datedue_var.set(d3)
                self.daysonbook_var.set(15)
                self.lateratefine_var.set("Rs.50")
                self.dateoverdue_var.set("NO")
                self.finalprice_var.set("Rs.1299")

        self.listBox.bind("<<ListboxSelect>>",SelectBook)
        self.listBox.grid(row=0,column=0)
        self.txtBox.grid(row=0,column=2)
        listScrollbar.config(command=self.listBox.xview)
        listScrollbar.grid(row=2, column=0, sticky=EW)
        listScrollbar1.config(command=self.listBox.yview)
        listScrollbar1.grid(row=0, column=1, sticky=NS)

        for item in listbooks:
            self.listBox.insert(END,item)


        #btnframes
        Framebutton=Frame(self.root,bd=12,#100
        relief=RIDGE,padx=0,bg='#343434')
        Framebutton.place(x=0,y=630,width=1366,height=70)
        #adddata
        btnAddData=Button(Framebutton,
        command=self.add_data,text="Add Data",width=23,font='Bahnschrift',bg='#0178D8',fg='white', borderwidth=3, relief="solid",
        padx=4,pady=7)
        btnAddData.grid(row=0,column=0,padx=0)
        
        #showdata
        btnShow=Button(Framebutton,command=self.showData,text="Show Data",width=23,font='Bahnschrift',bg='#0178D8',fg='white',borderwidth=3, relief="solid",
        padx=4,pady=7)
        btnShow.grid(row=0,column=1,padx=0)
        
        #update
        btnUpdate=Button(Framebutton,text="Update",width=23,
        command=self.update,font='Bahnschrift',bg='#0178D8',fg='white',borderwidth=3, relief="solid",
        padx=4,pady=7)
        btnUpdate.grid(row=0,column=2,padx=0)
        
        #delete
        btnDel=Button(Framebutton,text="Delete",width=23,
        command=self.delete,font='Bahnschrift',bg='#0178D8',fg='white',borderwidth=3, relief="solid",
        padx=4,pady=7)
        btnDel.grid(row=0,column=3,padx=0)
        
        #reset
        btnRst=Button(Framebutton,text="Reset",width=23,
        command=self.reset,font='Bahnschrift',bg='#0178D8',fg='white',borderwidth=3, relief="solid",
        padx=4,pady=7)
        btnRst.grid(row=0,column=4,padx=0)
        
        #exit
        btnExt=Button(Framebutton,text="Exit",width=23,font='Bahnschrift',bg='#0178D8',fg='white',borderwidth=3, relief="solid",
        command=self.iExit,
        padx=4,pady=7)
        btnExt.grid(row=0,column=5,padx=0)

        #FOR SHOWING DATABASES
        FrameDetails=Frame(self.root,bd=12,relief=RIDGE,padx=1,bg='#343434')
        FrameDetails.place(x=0,y=450,width=1366,height=190)

        Table_frame=Frame(FrameDetails,bd=6,relief=RIDGE,bg="#343434")
        Table_frame.place(x=0,y=0,width=1340,height=165)
        #scrollbar_from_google
        xscroll=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        yscroll=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.library_table=ttk.Treeview(Table_frame,column=("membertype","prnno","title","firstname","lastname","adress1","adress2","postid","mobile","bookid","booktitle","auther","dateborrowed","datedue","days","lastreturnfine","dateoverdue","finalprice"),xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM,fill=X)
        yscroll.pack(side=RIGHT,fill=Y)

        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)

        self.library_table.heading("membertype",text="Member Type")
        self.library_table.heading("prnno",text="PRN NO")
        self.library_table.heading("title",text="Title")
        self.library_table.heading("firstname",text="First Name")
        self.library_table.heading("lastname",text="Last Name")
        self.library_table.heading("adress1",text="Adress 1")
        self.library_table.heading("adress2",text="Adress 2")
        self.library_table.heading("postid",text="Post ID")
        self.library_table.heading("mobile",text="Mobile")
        self.library_table.heading("bookid",text="Book ID")
        self.library_table.heading("booktitle",text="Book Title")
        self.library_table.heading("auther",text="Auther Name")
        self.library_table.heading("dateborrowed",text="Date Borrowed")
        self.library_table.heading("datedue",text="Duedate")
        self.library_table.heading("days",text="Days on Book")
        self.library_table.heading("lastreturnfine",text="Last Return Fine")
        self.library_table.heading("dateoverdue",text="Date over Due")
        self.library_table.heading("finalprice",text="Actual Price")
        
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH,expand=1)

        self.library_table.column("membertype",width=100)
        self.library_table.column("prnno",width=100)
        self.library_table.column("title",width=100)
        self.library_table.column("firstname",width=100)
        self.library_table.column("lastname",width=100)
        self.library_table.column("adress1",width=100)
        self.library_table.column("adress2",width=100)
        self.library_table.column("postid",width=100)
        self.library_table.column("mobile",width=100)
        self.library_table.column("bookid",width=100)
        self.library_table.column("booktitle",width=100)
        self.library_table.column("auther",width=100)
        self.library_table.column("dateborrowed",width=100)
        self.library_table.column("datedue",width=100)
        self.library_table.column("days",width=100)
        self.library_table.column("lastreturnfine",width=100)
        self.library_table.column("dateoverdue",width=100)
        self.library_table.column("finalprice",width=100)

        self.fatch_data()
        self.library_table.bind("<ButtonRelease-1>",self.get_cursor)

    def add_data(self):
        conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aryan@123",
        database="new_schem")
        my_cursor=conn.cursor()
        my_cursor.execute("use new_schem")

        
        sql = "INSERT INTO library VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    #    val = ("John", "Highway", "Highway", "Highway", "Highway", "Highway", "Highway", "Highway", "Highway", "Highway", "Highway", "Highway", "Highway", "Highway", "Highway", "Highway", "Highway", "Highway")
        val = (self.member_var.get(),
            self.prn_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.auther_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.lateratefine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get())
        my_cursor.execute(sql,val)

        conn.commit()
        self.fatch_data()
        conn.close()


        messagebox.showinfo("Success","Member Has been inserted succesfully")      

    def update(self):
        conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aryan@123",
        database="new_schem")
        my_cursor=conn.cursor()

        my_cursor.execute("UPDATE library SET Member=%s,ID=%s,FirstName=%s,LastName=%s,Address1=%s,Address2=%s,Postid=%s,Mobile=%s,Bookid=%s,Book_title=%s,Author=%s,Databorrowed=%s,Datedue=%s,Daysonbook=%s,Latereturnfine=%s,Dateoverdue=%s,actualprice=%s WHERE PRN_NO=%s" ,(
            self.member_var.get(),
            self.id_var.get(),
            self.firstname_var.get(),
            self.lastname_var.get(),
            self.address1_var.get(),
            self.address2_var.get(),
            self.postcode_var.get(),
            self.mobile_var.get(),
            self.bookid_var.get(),
            self.booktitle_var.get(),
            self.auther_var.get(),
            self.dateborrowed_var.get(),
            self.datedue_var.get(),
            self.daysonbook_var.get(),
            self.lateratefine_var.get(),
            self.dateoverdue_var.get(),
            self.finalprice_var.get(),
            self.prn_var.get()
    ))
        



        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()


        messagebox.showinfo("Success","Member has been Updated")

    def fatch_data(self):
        conn=mysql.connector.connect(
            host="localhost",
        username="root",
        password="Aryan@123",
        database="new_schem"
        ) 
        my_cursor=conn.cursor()
        my_cursor.execute("select * from library")
        rows=my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()
    

    def get_cursor(self,event=""):
        cursor_row=self.library_table.focus()
        content=self.library_table.item(cursor_row)
        row=content['values']

        self.member_var.set(row[0]),
        self.prn_var.set(row[1]),
        self.id_var.set(row[2]),
        self.firstname_var.set(row[3]),
        self.lastname_var.set(row[4]),
        self.address1_var.set(row[5]),
        self.address2_var.set(row[6]),
        self.postcode_var.set(row[7]),
        self.mobile_var.set(row[8]),
        self.bookid_var.set(row[9]),
        self.booktitle_var.set(row[10]),
        self.auther_var.set(row[11]),
        self.dateborrowed_var.set(row[12]),
        self.datedue_var.set(row[13]),
        self.daysonbook_var.set(row[14]),
        self.lateratefine_var.set(row[15]),
        self.dateoverdue_var.set(row[16]),
        self.finalprice_var.set(row[17])

    def showData(self):
        self.txtBox.insert(END,"Member Type:\t\t"+self.member_var.get()+"\n")
        self.txtBox.insert(END,"PRN NO:\t\t"+self.prn_var.get()+"\n")
        self.txtBox.insert(END,"ID NO:\t\t"+self.id_var.get()+"\n")
        self.txtBox.insert(END,"First Name:\t\t"+self.firstname_var.get()+"\n")
        self.txtBox.insert(END,"Last Name:\t\t"+self.lastname_var.get()+"\n")
        self.txtBox.insert(END,"Address1:\t\t"+self.address1_var.get()+"\n")
        self.txtBox.insert(END,"Address2:\t\t"+self.address2_var.get()+"\n")
        self.txtBox.insert(END,"Post Code:\t\t"+self.postcode_var.get()+"\n")
        self.txtBox.insert(END,"Mobile No:\t\t"+self.mobile_var.get()+"\n")
        self.txtBox.insert(END,"Book ID:\t\t"+self.bookid_var.get()+"\n")
        self.txtBox.insert(END,"Book Title:\t\t"+self.booktitle_var.get()+"\n")
        self.txtBox.insert(END,"Author:\t\t"+self.auther_var.get()+"\n")
        self.txtBox.insert(END,"DateBorrowed:\t\t"+self.dateborrowed_var.get()+"\n")
        self.txtBox.insert(END,"DateDue:\t\t"+self.datedue_var.get()+"\n")
        self.txtBox.insert(END,"DaysOnBook:\t\t"+self.daysonbook_var.get()+"\n")
        self.txtBox.insert(END,"LateRateFine:\t\t"+self.lateratefine_var.get()+"\n")
        self.txtBox.insert(END,"DateOverDue:\t\t"+self.dateoverdue_var.get()+"\n")
        self.txtBox.insert(END,"FinalPrice:\t\t"+self.finalprice_var.get()+"\n")

    def reset(self):
        self.member_var.set("")
        self.prn_var.set("")
        self.id_var.set("")
        self.firstname_var.set("")
        self.lastname_var.set("")
        self.address1_var.set("")
        self.address2_var.set("")
        self.postcode_var.set("")
        self.mobile_var.set("")
        self.bookid_var.set("")
        self.booktitle_var.set("")
        self.auther_var.set("")
        self.dateborrowed_var.set("")
        self.datedue_var.set("")
        self.daysonbook_var.set("")
        self.lateratefine_var.set("")
        self.dateoverdue_var.set("")
        self.finalprice_var.set("")
        self.txtBox.delete("1.0",END)

    def iExit(self):
        iExit=tkinter.messagebox.askyesno("Library Management System","Do you want to exit")
        if iExit>0:
            self.root.destroy()
            return


    def delete(self):
        if self.prn_var.get()=="" or self.id_var.get()=="":
            messagebox.showerror("Error","First Select the Member")
        else:
            conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aryan@123",
        database="new_schem")
        my_cursor=conn.cursor()
        query="DELETE FROM library WHERE PRN_NO=%s"
        value=(self.prn_var.get() ,)
        my_cursor.execute(query, value)

        conn.commit()
        self.fatch_data()
        self.reset()
        conn.close()

        messagebox.showinfo("Success","Member has been Deleted")
    

if __name__=="__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()



