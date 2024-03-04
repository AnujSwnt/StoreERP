
from pathlib import Path
from tkinter import *

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Spinbox, Toplevel
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import requests as rq
import re
from tkinter import messagebox
import datetime
from datetime import datetime
import tkinter
from docxtpl import DocxTemplate
from datetime import *
from mysql.connector import *


import gui3

#Path(r"E:/Python/Storerp/assets/frame6/")
class Page6:
    def __init__(self,dr):

        self.dr=dr
        self.dr.geometry("703x781+200+0")
        self.dr.configure(bg = "#FFFFFF")
        lacn="E:/Python/Storerp/assets/frame6/"

        self.canvas = Canvas(
            self.dr,
            bg = "#FFFFFF",
            height = 781,
            width = 703,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=lacn+"image_1.png")
        self.image_1 = self.canvas.create_image(
            351.0,
            46.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=lacn+"image_2.png")
        self.image_2 = self.canvas.create_image(
            224.686767578125,
            43.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=lacn+"image_3.png")
        self.image_3 = self.canvas.create_image(
            101.0,
            246.0,
            image=self.image_image_3
        )

        global order_Id,cust_Id
        self.entry_image_1 = PhotoImage(
            file=lacn+"entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            250.0,
            247.0,
            image=self.entry_image_1
        )
        order_Id = Entry(self.dr,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            highlightthickness=0
        )
        order_Id.place(
            x=159.0,
            y=224.0,
            width=182.0,
            height=44.0
        )

        self.image_image_4 = PhotoImage(
            file=lacn+"image_4.png")
        self.image_4 = self.canvas.create_image(
            427.0,
            240.0,
            image=self.image_image_4
        )

        self.entry_image_2 = PhotoImage(
            file=lacn+"entry_2.png")
        self.entry_bg_2 = self.canvas.create_image(
            580.0,
            244.0,
            image=self.entry_image_2
        )
        cust_Id = Entry(self.dr,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            highlightthickness=0
        )
        cust_Id.place(
            x=489.0,
            y=221.0,
            width=182.0,
            height=44.0
        )

        self.button_image_1 = PhotoImage(
            file=lacn+"button_1.png")
        self.button_1 = Button(self.dr,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.delete_record,
            relief="flat"
        )
        self.button_1.place(
            x=206.0,
            y=619.0,
            width=311.0,
            height=83.0
        )

        self.button_image_2 = PhotoImage(
            file=lacn+"button_2.png")
        self.button_2 = Button(self.dr,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.view,
            relief="flat"
        )
        self.button_2.place(
            x=307.0,
            y=286.0,
            width=133.0,
            height=38.0
        )
        
        self.button_image_3 = PhotoImage(
            file="E:/Python/Storerp/assets/frame4/button_1.png")
        self.button_3 = Button(self.dr,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.exit_dr,
            relief="flat"
        )
        self.button_3.place(
            x=271.0,
            y=713.0,
            width=183.0,
            height=49.0
        )

        # self.entry_image_3 = PhotoImage(
        #     file=lacn+"entry_3.png")
        # self.entry_bg_3 = self.canvas.create_image(
        #     351.5,
        #     473.5,
        #     image=self.entry_image_3
        # )
        # self.entry_3 = Text(
        #     bd=0,
        #     bg="#D9D9D9",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # self.entry_3.place(
        #     x=36.0,
        #     y=349.0,
        #     width=631.0,
        #     height=247.0
        # )

        self.columns=('order_id','prd_name','qty','price','total','date','address')
        self.scrollbary=Scrollbar(self.dr,orient=VERTICAL)
        self.scrollbarx=Scrollbar(self.dr,orient=HORIZONTAL)
        self.tree=ttk.Treeview(self.canvas,columns=self.columns,show="headings")
        self.tree.place(
            x=36.0,
            y=349.0,
            width=631.0,
            height=247.0
        )

        self.tree.configure(yscrollcommand=self.scrollbary.set)
        self.tree.configure(xscrollcommand=self.scrollbarx.set)
        self.tree.configure(selectmode="extended")
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbary.place(x=674,y=349,width=12,height=247)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbarx.place(x=36,y=607,width=631,height=12)

        self.tree.heading('order_id',text="Order ID")
        self.tree.heading('prd_name',text="Product Name")
        self.tree.heading('qty',text="Quantity")
        self.tree.heading('price',text="Price")
        self.tree.heading('total',text="Total")
        self.tree.heading('date',text="Date")
        self.tree.heading('address',text="Address")

        self.tree.column('#0',stretch=NO,minwidth=25,width=143)
        self.tree.column('#1',stretch=NO,minwidth=25,width=143)
        self.tree.column('#2',stretch=NO,minwidth=25,width=174)
        self.tree.column('#3',stretch=NO,minwidth=25,width=143)
        self.tree.column('#4',stretch=NO,minwidth=25,width=143)
        self.tree.column('#5',stretch=NO,minwidth=25,width=143)
        self.tree.column('#6',stretch=NO,minwidth=25,width=143)

        self.image_image_5 = PhotoImage(
            file=lacn+"image_5.png")
        self.image_5 = self.canvas.create_image(
            352.0,
            155.0,
            image=self.image_image_5
        )
        self.dr.resizable(False, False)

#-------------------------------------------------------------------------------------------------------
        
        global con,cursor
        con = connect(
            host="localhost",
            user="root",
            password="anuj1234",
            database="storerp_1"
           
        )

        cursor = con.cursor()
    
    def view(self):
        try:
            self.tree.delete(*self.tree.get_children())
            id1=order_Id.get()
            #id2=cust_id.get()

            sql1="select order_id,description,quantity,unit_price,total,i_date,address from invoice_2 where order_id=%s;"
            cursor.execute(sql1%(id1))
            
            data=cursor.fetchall() 
            

            for i, (order_id,description,quantity,unit_price,total,i_date,address) in enumerate(data, start=1):
                self.tree.insert("","end",values=(order_id,description,quantity,unit_price,total,i_date,address))
            con.commit()
            

        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)
        
    def delete_record(self):
        
        try:
            #id1=order_Id.get()
            #id2=cust_id.get()
            selected_item=self.tree.selection()[0]

            # Extract order_id and description from the tuple
            selected_id = self.tree.item(selected_item, 'values')[0]
            selected_desc = self.tree.item(selected_item, 'values')[1]
            
            sql1="delete from invoice_2 where order_id=%s AND description=%s;"
            cursor.execute(sql1,(selected_id,selected_desc))
            con.commit()
            self.tree.delete(selected_item)
            showinfo("success","Deleted Successfully")
        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)

    def exit_dr(self):
        vs=Toplevel()
        gui3.Page3(vs)
        self.dr.withdraw()
        vs.deiconify()
    
def page():
    dr=Tk()
    Page6(dr)
    dr.mainloop()

if __name__ == '__main__':
    page()

