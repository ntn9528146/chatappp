from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
# from tkinter.ttk import *
import mysql.connector
import random
from tkinter import messagebox





class Cust_Win:

                
                
        def __init__(self,root):
                self.root=root
                self.root.title("Hotel Management System")
                self.root.geometry("1295x550+230+220")

                #---------------variable---------------------------------
                self.var_ref=StringVar()
                x=random.randint(1000,9999)
                self.var_ref.set(str(x))

                #---------------other all varaible--------------------

                self.var_cust_name=StringVar()

                self.var_mother=StringVar()
        
                self.var_gender=StringVar()
        
                self.var_post=StringVar()
        
                self.var_mobile=StringVar()
        
                self.var_email=StringVar()
        
                self.var_nation=StringVar()
        
                self.var_idproof=StringVar()
        
                self.var_idnumber=StringVar()

                self.var_address=StringVar()

                #---------------function'------------Add function---------
                

        



                ########## title----------------------
                lbl_title=Label(self.root,text="Add Customer Details",font="impack 18 bold", bg="black",fg="gold",relief=RIDGE)
                lbl_title.place(x=0,y=0,width=1295,height=50)
        #-------------- logo---------------------
                img2=Image.open("C:/Users/netni/OneDrive/Desktop/python project/hotel_management_system/image/pexels-photo-96444.jpeg")
                img2=img2.resize((100,40),Image.ANTIALIAS)
                self.photoimg2=ImageTk.PhotoImage(img2)

                lblimg=Label(self.root,bd=3,relief=RIDGE,image=self.photoimg2)
                lblimg.place(x=5,y=2,width=100,height=40)

                #-------label frame--------------------------
                lblframeleft=LabelFrame(self.root,text="Customer Details",bd=2,relief=RIDGE,padx=2,font="impack 12 bold",fg="red")
                lblframeleft.place(x=5,y=50,width=425,height=490)

                # --------labels and Entry-----------------
                lbl_cust_ref=Label(lblframeleft,text="Customer Reference",bd=2,relief=RIDGE,padx=2,font="impack 12 bold",pady=6)
                lbl_cust_ref.grid(row=0,column=0)

                e_ref=ttk.Entry(lblframeleft,width=20,font="impack 11 ",textvariable=self.var_ref,state="readonly")
                e_ref.grid(row=0,column=1)

                #_-------------cust Name-------
                lbl_cust_name=Label(lblframeleft,text="Name",bd=2,relief=RIDGE,padx=2,font="impack 12 bold",pady=6)
                lbl_cust_name.grid(row=1,column=0)

                e_ref=ttk.Entry(lblframeleft,width=20,font="impack 11",textvariable=self.var_cust_name)
                e_ref.grid(row=1,column=1)

        #---------mother name--------------
                lbl_cust_mother_name=Label(lblframeleft,text="Mother Name",bd=2,relief=RIDGE,padx=2,font="impack 12 bold",pady=6)
                lbl_cust_mother_name.grid(row=2,column=0)

                e_ref=ttk.Entry(lblframeleft,width=20,font="impack 11 ",textvariable=self.var_mother)
                e_ref.grid(row=2,column=1)
        #-----------------gender-------------------
                lbl_gender=Label(lblframeleft,text="Gender",bd=2,relief=RIDGE,padx=2,font="impack 12 bold",pady=6)
                lbl_gender.grid(row=3,column=0)

        #         radio_gender=StringVar(lblframeleft,"1")
        #         style=Style(root)
        #         style=Style.configure("TRadiobutton", font="impack 14 bold",fg="red")
        # # dictionary to create store values----------------
        #         values={"Male":"1",
        #                 "Female":"2",
        #                 "Other":"3"
        #         }
        #         #loop is to create multiple Radio button-----------
        #         for (text, value) in values.items():
        #             Radiobutton(lblframeleft,text=text,value=value,variable=radio_gender).pack(side=TOP,ipady=5)

                

                combo_gender=ttk.Combobox(lblframeleft,font="impack 11 ",width=18,state="readonly",textvariable=self.var_gender)
                combo_gender["values"]=("Male","Female","Other")
                combo_gender.current(0)
                combo_gender.grid(row=3,column=1)
        # --------------------gender combobox=------------------------
                # lbl_cust_ref=Label(lblframeleft,text="",bd=2,relief=RIDGE,padx=2,font="impack 12 bold",pady=6)
                # lbl_cust_ref.grid(row=4,column=0)

                # e_ref=ttk.Entry(lblframeleft,width=20,font="impack 14 bold")
                # e_ref.grid(row=0,column=1)
                #----------------------post code------------------
                lbl_postcode=Label(lblframeleft,text="Postcode",bd=2,relief=RIDGE,padx=2,font="impack 12 bold",pady=6)
                lbl_postcode.grid(row=5,column=0)

                e_ref=ttk.Entry(lblframeleft,width=20,font="impack 11",textvariable=self.var_post)
                e_ref.grid(row=5,column=1)
                #------------------mobile number---------------------
                lbl_mobilenumber=Label(lblframeleft,text="Mobile number",bd=2,relief=RIDGE,padx=2,font="impack 12 bold",pady=6)
                lbl_mobilenumber.grid(row=6,column=0)

                e_ref=ttk.Entry(lblframeleft,width=20,font="impack 11",textvariable=self.var_mobile)
                e_ref.grid(row=6,column=1)

                #--------------email___--------------------------------
                lbl_email=Label(lblframeleft,text="Email",bd=2,relief=RIDGE,padx=2,font="impack 12 bold",pady=6)
                lbl_email.grid(row=7,column=0)

                e_ref=ttk.Entry(lblframeleft,width=20,font="impack 11",textvariable=self.var_email)
                e_ref.grid(row=7,column=1)

                #--------------nationality--------------------
                lbl_nationality=Label(lblframeleft,text="Nationality",bd=2,relief=RIDGE,padx=2,font="impack 12 bold",pady=6)
                lbl_nationality.grid(row=8,column=0)

                combo_nation=ttk.Combobox(lblframeleft,width=18,font="impack 11",state="readonly",textvariable=self.var_nation)
                combo_nation["values"]=("INDIAN","USA","ENGLAND","RUSSIA","NEPAL")
                combo_nation.current(0)
                combo_nation.grid(row=8,column=1)

                #-------------------id proof-------------------
                lbl_idproof=Label(lblframeleft,text="Id Proof",bd=2,relief=RIDGE,padx=2,font="impack 12 bold",pady=6)
                lbl_idproof.grid(row=9,column=0)

                combo_id=ttk.Combobox(lblframeleft,font="impack 11",state="readonly",width=18,textvariable=self.var_idproof )
                combo_id["values"]=("AADHAR","PAN CARD","DRIVING LICIENCE","VOTER ID","PASSPORT")
                combo_id.current(0)
                combo_id.grid(row=9,column=1)

                #--------id number------------------------
                lbl_idnumber=Label(lblframeleft,text="Id Number",bd=2,relief=RIDGE,padx=2,font="impack 12 bold",pady=6)
                lbl_idnumber.grid(row=10,column=0)

                e_ref=ttk.Entry(lblframeleft,width=20,font="impack 14 bold",textvariable=self.var_idnumber)
                e_ref.grid(row=10,column=1)
                #---------------Address-------------------------------------
                lbl_address=Label(lblframeleft,text="Address",relief=RIDGE,padx=2,font="impack 12 bold",pady=6)
                lbl_address.grid(row=11,column=0)

                e_ref=ttk.Entry(lblframeleft,width=20,font="impack 14 bold",textvariable=self.var_address)
                e_ref.grid(row=11,column=1)
                #------------btn frame------------
                btn_frame=Frame(lblframeleft,bd=2,relief=RIDGE)
                btn_frame.place(x=0,y=400,width=412,height=40)

        ######## ADD_Button0====================
                add_btn=Button(btn_frame,text="ADD",font="impack 11",fg="white",bg="brown",cursor="hand2",width=10,command=self.add_data)
                add_btn.grid(row=0,column=0,padx=2)

        # save buttton------------------------------------------------
                
                save_btn=Button(btn_frame,text="UPDATE",font="impack 11",fg="white",bg="brown",cursor="hand2",width=10,command=self.update)
                save_btn.grid(row=0,column=1,padx=2)
                # reset button-------------------------
                reset_btn=Button(btn_frame,text="RESET",font="impack 11",fg="white",bg="brown",cursor="hand2",width=10,command=self.reset)
                reset_btn.grid(row=0,column=2,padx=2)

                #------------Delete Button---------------------------------
                delete_btn=Button(btn_frame,text="DELETE",font="impack 11",fg="white",bg="brown",cursor="hand2",width=10,command=self.delete)
                delete_btn.grid(row=0,column=3,padx=2)


                #----LEFT FRAME------------------------------------SEARCH AND VIEW DETAILS-------------------------
                lblframeright=LabelFrame(root,text="Search and View Details",font="impack 14 bold",fg="red",bd=2,padx=2,relief=RIDGE)
                lblframeright.place(x=440,y=50,width=835,height=490)

                #----------search By Frame-----------------------------------------------------
                lbl_searchby=Label(lblframeright,text="Search By",font="impack 12 bold",fg="white",bg="red")
                lbl_searchby.grid(row=0,column=0)
                self.search_var=StringVar()


                combo_searchby=ttk.Combobox(lblframeright,font="impack 11",width=18,state="readonly",textvariable=self.search_var)
                combo_searchby["values"]=("Mobile number","Reference Number")
                combo_searchby.grid(row=0,column=1,padx=2)

                #----search Entry---------------
                self.txt_search=StringVar()
                search_entry=ttk.Entry(lblframeright,font="impack 11",width=18,textvariable=self.txt_search)
                search_entry.grid(row=0,column=2,padx=2)
                #--------------search and show all button-------------
                search_btn=Button(lblframeright,text="SEARCH",font="impack 11 bold",fg="white",bg="brown",cursor="hand2",width=10,command=self.search_by)
                search_btn.grid(row=0,column=3,padx=2)

                showall_btn=Button(lblframeright,text="Show All",font="impack 11 bold",fg="white",bg="brown",cursor="hand2",width=10,command=self.fetch_data)
                showall_btn.grid(row=0,column=4,padx=2)

                #---------show Data Table--------------------------------------
                details_table=Frame(lblframeright,bd=2,relief=RIDGE)
                details_table.place(x=0,y=50,width=825,height=350)

                #-------Scroll Bar---------------------------------

                scroll_x=ttk.Scrollbar(details_table,orient="horizontal")
                scroll_y=ttk.Scrollbar(details_table,orient="vertical")

                self.cust_details_table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post","mobile","email","nation","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
                scroll_x.pack(side=BOTTOM,fill=X)
                scroll_y.pack(side=RIGHT,fill=Y)
                scroll_x.config(command=self.cust_details_table.xview)
                scroll_y.config(command=self.cust_details_table.yview)

                self.cust_details_table.heading("ref",text="Reference Number")
                self.cust_details_table.heading("name",text="Name")
                self.cust_details_table.heading("mother",text="Mother Name")
                self.cust_details_table.heading("gender",text="Gender")
                self.cust_details_table.heading("post",text="Postcode")
                self.cust_details_table.heading("mobile",text="Mobile Number")
                self.cust_details_table.heading("email",text="Email ID")
                self.cust_details_table.heading("nation",text="Nationality")
                self.cust_details_table.heading("idproof",text="ID Proof")
                self.cust_details_table.heading("idnumber",text="ID Number")
                self.cust_details_table.heading("address",text="Address Number")

                self.cust_details_table["show"]="headings"

                self.cust_details_table.column("ref",width=100)
                self.cust_details_table.column("name",width=100)
                self.cust_details_table.column("mother",width=100)
                self.cust_details_table.column("gender",width=100)
                self.cust_details_table.column("post",width=100)
                self.cust_details_table.column("mobile",width=100)
                self.cust_details_table.column("email",width=100)
                self.cust_details_table.column("nation",width=100)
                self.cust_details_table.column("idproof",width=100)
                self.cust_details_table.column("idnumber",width=100)
                self.cust_details_table.column("address",width=100)
                



                self.cust_details_table.pack(fill=BOTH,expand=1)
                self.cust_details_table.bind("<ButtonRelease-1>",self.cursor_value)
                self.fetch_data()


        def add_data(self):
                if self.var_mobile.get()=="" or self.var_mother=="":
                        messagebox.showerror("Error","Please Fill all required fields")
                else:
                        try:
                                con=mysql.connector.connect(host="localhost",username="root",password="1234",database="hotel_management")
                                my_cursor=con.cursor()
                                my_cursor.execute("INSERT INTO hotel_customer values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                        self.var_ref.get(),
                                        self.var_cust_name.get(),
                                        self.var_mother.get(),
                                        self.var_gender.get(),
                                        self.var_post.get(),
                                        self.var_mobile.get(),
                                        self.var_email.get(),
                                        self.var_nation.get(),
                                        self.var_idproof.get(),
                                        self.var_idnumber.get(),
                                        self.var_address.get()

                                        ))
                                con.commit()
                                self.fetch_data()
                                con.close()
                                messagebox.showinfo("Success",f"Customer has been added",parent=self.root)
                        except Exception as es:
                                messagebox.showerror("Warning",f"something went wrong:{str(es)}",parent=self.root)
                        
        def fetch_data(self):
                con=mysql.connector.connect(host="localhost",username="root",password="1234",database="hotel_management")
                my_cursor=con.cursor()
                my_cursor.execute("SELECT * FROM hotel_customer")
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.cust_details_table.delete(*self.cust_details_table.get_children())
                        for i in rows:
                                self.cust_details_table.insert("",END,values=i)
                        con.commit()
                con.close()


        def cursor_value(self,event=""):
                cursor_row=self.cust_details_table.focus()
                content=self.cust_details_table.item(cursor_row)
                row=content["values"]


                self.var_ref.set(row[0]),
                self.var_cust_name.set(row[1]),
                self.var_mother.set(row[2]),
                self.var_gender.set(row[3]),
                self.var_post.set(row[4]),
                self.var_mobile.set(row[5]),
                self.var_email.set(row[6]),
                self.var_nation.set(row[7]),
                self.var_idproof.set(row[8]),
                self.var_idnumber.set(row[9]),
                self.var_address.set(row[10])

        def update(self):
                if self.var_mobile.get()=="":
                        messagebox.showerror("Error","Please Enter Mobile Number",parent=self.root)
                else:
                        con=mysql.connector.connect(host="localhost",username="root",password="1234",database="hotel_management")
                        my_cursor=con.cursor()
                        my_cursor.execute("UPDATE hotel_customer SET name=%s,mother=%s,gender=%s,postcode=%s,mobile=%s,email=%s,nationality=%s,idproof=%s,idnumber=%s,address=%s WHERE ref=%s",(
                                
                                        self.var_cust_name.get(),
                                        self.var_mother.get(),
                                        self.var_gender.get(),
                                        self.var_post.get(),
                                        self.var_mobile.get(),
                                        self.var_email.get(),
                                        self.var_nation.get(),
                                        self.var_idproof.get(),
                                        self.var_idnumber.get(),
                                        self.var_address.get(),
                                        self.var_ref.get()

                        ))
                        con.commit()
                        self.fetch_data()
                        con.close()
                        messagebox.showinfo("Update","Customer details has been updated Successfully")
                
        def delete(self):

                delete=messagebox.askyesno("Hotel Management System","Do you want delete this customer",parent=self.root)
                if delete>0:
                        
                        con=mysql.connector.connect(host="localhost",username="root",password="1234",database="hotel_management")
                        my_cursor=con.cursor()
                        query="delete from hotel_customer WHERE ref=%s"
                        value=(self.var_ref.get(),)
                        my_cursor.execute(query,value)
                else:
                        if not delete:
                                return
                con.commit()
                self.fetch_data()
                con.close()

        def reset(self):
                reset=messagebox.askyesno("Hotel Mana system","Do you want to reset",parent=self.root)
                if reset>0:

                        #self.var_ref.set(""),
                        self.var_cust_name.set(""),
                        self.var_mother.set(""),
                        #self.var_gender.set(""),
                        self.var_post.set(""),
                        self.var_mobile.set(""),
                        self.var_email.set(""),
                        #self.var_nation.set(""),
                        #self.var_idproof.set(""),
                        self.var_idnumber.set(""),
                        self.var_address.set("")
                        x=random.randint(1000,9999)
                        self.var_ref.set(str(x))
                else:
                        if not reset:
                                return
                        self.fetch_data()

        def search_by(self):
                con=mysql.connector.connect(host="localhost",username="root",password="1234",database="hotel_management")
                my_cursor=con.cursor()
                my_cursor.execute("SELECT * FROM hotel_customer WHERE ref LIKE %s OR mobile LIKE %s",('%'+str(self.search_var.get())+'%','%' +str(self.txt_search.get())+'%'))
                # my_cursor.execute("SELECT * FROM hotel_customer WHERE ref LIKE ? OR mobile LIKE ?",'%'+str(self.search_var.get())+'%','%' +str(self.txt_search.get())+'%')
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                        self.cust_details_table.delete(*self.cust_details_table.get_children())
                        for i in rows:
                                self.cust_details_table.insert("",END,values=i)
                        con.commit()
                con.close()
                                







                
                                



if __name__=="__main__":
        root=Tk()
        obj=Cust_Win(root)
        root.mainloop()
