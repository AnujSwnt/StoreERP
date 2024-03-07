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
from tkinter import Entry, END


import gui3
f1=("Arial",15,"bold")
f2=("Arial",10,"bold")
#Path(r"E:/Python/Storerp/assets/frame5/")
class Page5:
    global con,cursor
    con = connect(
            host="localhost",
            user="root",
            password="anuj1234",
            database="storerp_1"
           
        )
    cursor = con.cursor()
    
        
    def box(self):
        global products,prices_list
        try:
            sql="select p_name from stock_1"
            cursor.execute(sql)
            data=cursor.fetchall()

            products = [row[0] for row in data]

            # for i, (p_name) in enumerate(data, start=1):
            #     self.tree.insert("","end",values=(product_id,p_name,quantity,p_price,total))
            sql2="select p_name,s_price from stock_1"
            cursor.execute(sql2)
            data2=cursor.fetchall()
            prices_list={row[0]: row[1] for row in data2}
            con.commit()
        
        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)

    def __init__(self,ur):
        self.ur = ur
        self.box()
        self.ur.geometry("1127x781+200+0")
        self.ur.configure(bg = "#FFFFFF")
        lacn="E:/Python/Storerp/assets/frame5/"

        self.canvas = Canvas(
            self.ur,
            bg = "#FFFFFF",
            height = 781,
            width = 1127,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=lacn+"image_1.png")
        self.image_1 = self.canvas.create_image(
            563.0,
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
            339.0,
            155.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=lacn+"image_4.png")
        self.image_4 = self.canvas.create_image(
            81.0,
            235.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=lacn+"image_5.png")
        self.image_5 = self.canvas.create_image(
            857.0,
            155.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=lacn+"image_6.png")
        self.image_6 = self.canvas.create_image(
            578.0,
            153.0,
            image=self.image_image_6
        )

        global Name,Orderid,Gstlab,Address,Date,Phnno

        self.entry_image_1 = PhotoImage(
            file=lacn+"entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            456.5,
            155.5,
            image=self.entry_image_1
        )
        Orderid = Entry(self.ur,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            font=f1,
            highlightthickness=0
        )
        Orderid.place(
            x=390.0,
            y=139.0,
            width=133.0,
            height=31.0
        )

        Orderid.bind("<Return>", lambda event: self.view())

        self.entry_image_2 = PhotoImage(
            file=lacn+"entry_2.png")
        self.entry_bg_2 = self.canvas.create_image(
            707.5,
            155.5,
            image=self.entry_image_2
        )
        Name = Entry(self.ur,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",font=f1,
            highlightthickness=0
        )
        Name.place(
            x=620.0,
            y=139.0,
            width=175.0,
            height=31.0
        )

        Name.bind("<Return>", lambda event: self.up_name())

        self.entry_image_3 = PhotoImage(
            file=lacn+"entry_3.png")
        self.entry_bg_3 = self.canvas.create_image(
            982.5,
            157.5,
            image=self.entry_image_3
        )
        Gstlab = Entry(self.ur,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",font=f1,
            highlightthickness=0
        )
        Gstlab.place(
            x=894.0,
            y=141.0,
            width=177.0,
            height=31.0
        )

        Gstlab.bind("<Return>", lambda event: self.up_gst())

        self.entry_image_4 = PhotoImage(
            file=lacn+"entry_4.png")
        self.entry_bg_4 = self.canvas.create_image(
            216.0,
            235.5,
            image=self.entry_image_4
        )
        Phnno = Entry(self.ur,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",font=f1,
            highlightthickness=0
        )
        Phnno.place(
            x=136.0,
            y=219.0,
            width=160.0,
            height=31.0
        )

        Phnno.bind("<Return>", lambda event: self.up_phn())

        self.image_image_7 = PhotoImage(
            file=lacn+"image_7.png")
        self.image_7 = self.canvas.create_image(
            733.0,
            218.0,
            image=self.image_image_7
        )

        self.entry_image_5 = PhotoImage(
            file=lacn+"entry_5.png")
        self.entry_bg_5 = self.canvas.create_image(
            872.0,
            218.5,
            image=self.entry_image_5
        )
        Date = Entry(self.ur,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",font=f1,
            highlightthickness=0
        )
        Date.place(
            x=800.0,
            y=202.0,
            width=144.0,
            height=31.0
        )

        Date.bind("<Return>", lambda event: self.up_date())

        self.image_image_8 = PhotoImage(
            file=lacn+"image_8.png")
        self.image_8 = self.canvas.create_image(
            373.0,
            219.0,
            image=self.image_image_8
        )

        self.entry_image_6 = PhotoImage(
            file=lacn+"entry_6.png")
        self.entry_bg_6 = self.canvas.create_image(
            534.5,
            223.5,
            image=self.entry_image_6
        )
        Address = Entry(self.ur,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",font=f1,
            highlightthickness=0
        )
        Address.place(
            x=424.0,
            y=199.0,
            width=221.0,
            height=47.0
        )

        Address.bind("<Return>", lambda event: self.up_addrs())

        self.image_image_9 = PhotoImage(
            file=lacn+"image_9.png")
        self.image_9 = self.canvas.create_image(
            147.0,
            156.0,
            image=self.image_image_9
        )

        self.columns=('order_id','prd_name','qty','price','total','date','name','gstin','phoneno','address')
        self.scrollbary=Scrollbar(self.ur,orient=VERTICAL)
        self.scrollbarx=Scrollbar(self.ur,orient=HORIZONTAL)
        self.tree=ttk.Treeview(self.canvas,columns=self.columns,show="headings")
        self.style=ttk.Style()
        self.style.configure("Treeview",font=f2)
        self.style.configure("Treeview.Heading",font=f2)
        self.tree.place(
            x=36.0,
            y=270.0,
            width=1040.0,
            height=188.0
        )

        self.tree.configure(yscrollcommand=self.scrollbary.set)
        self.tree.configure(xscrollcommand=self.scrollbarx.set)
        self.tree.configure(selectmode="extended")
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbary.place(x=1082,y=270,width=12,height=188)
        self.scrollbarx.configure(command=self.tree.xview)
        self.scrollbarx.place(x=36,y=469,width=1040,height=12)

        self.tree.heading('order_id',text="Order ID")
        self.tree.heading('prd_name',text="Product Name")
        self.tree.heading('qty',text="Quantity")
        self.tree.heading('price',text="Price")
        self.tree.heading('total',text="Total")
        self.tree.heading('date',text="Date")
        self.tree.heading('name',text="Name")
        self.tree.heading('gstin',text="GSTIN")
        self.tree.heading('phoneno',text="PhoneNo")
        self.tree.heading('address',text="Address")

        self.tree.column('#0',stretch=NO,minwidth=25,width=143)
        self.tree.column('#1',stretch=NO,minwidth=25,width=143)
        self.tree.column('#2',stretch=NO,minwidth=25,width=174)
        self.tree.column('#3',stretch=NO,minwidth=25,width=143)
        self.tree.column('#4',stretch=NO,minwidth=25,width=143)
        self.tree.column('#5',stretch=NO,minwidth=25,width=143)
        self.tree.column('#6',stretch=NO,minwidth=25,width=143)
        self.tree.column('#7',stretch=NO,minwidth=25,width=143)
        self.tree.column('#8',stretch=NO,minwidth=25,width=143)
        self.tree.column('#9',stretch=NO,minwidth=25,width=143)

        global Quantity_lab,Desc_lab,Unitprice
        self.entry_image_8 = PhotoImage(
            file=lacn+"entry_8.png")
        self.entry_bg_8 = self.canvas.create_image(
            139.0,
            601.5,
            image=self.entry_image_8
        )
        Quantity_lab = Spinbox(self.ur,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",font=f1,
            highlightthickness=0,from_=1,to=1000
        )
        Quantity_lab.place(
            x=46.0,
            y=581.0,
            width=186.0,
            height=39.0
        )

        self.entry_image_9 = PhotoImage(
            file=lacn+"entry_9.png")
        self.entry_bg_9 = self.canvas.create_image(
            347.0,
            601.5,
            image=self.entry_image_9
        )
        Desc_lab = ttk.Combobox(self.ur,font=f1,
            # bd=0,
            # bg="#BFBBBB",
            # fg="#000716",
            #highlightthickness=0,
            values=products
        )
        Desc_lab.place(
            x=254.0,
            y=581.0,
            width=186.0,
            height=39.0
        )
        Desc_lab.set(' ')
        Desc_lab.bind("<<ComboboxSelected>>", self.update_unit_price)

        self.entry_image_10 = PhotoImage(
            file=lacn+"entry_10.png")
        self.entry_bg_10 = self.canvas.create_image(
            556.0,
            601.5,
            image=self.entry_image_10
        )
        Unitprice = Entry(self.ur,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",font=f1,
            highlightthickness=0
        )
        Unitprice.place(
            x=463.0,
            y=581.0,
            width=186.0,
            height=39.0
        )

        self.image_image_10 = PhotoImage(
            file=lacn+"image_10.png")
        self.image_10 = self.canvas.create_image(
            329.0,
            560.0,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file=lacn+"image_11.png")
        self.image_11 = self.canvas.create_image(
            125.0,
            560.0,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file=lacn+"image_12.png")
        self.image_12 = self.canvas.create_image(
            529.0,
            557.0,
            image=self.image_image_12
        )

        self.button_image_1 = PhotoImage(
            file=lacn+"button_1.png")
        self.button_1 = Button(self.ur,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.up_item,
            relief="flat"
        )
        self.button_1.place(
            x=676.0,
            y=574.0,
            width=196.0,
            height=48.0
        )

        self.button_image_2 = PhotoImage(
            file=lacn+"button_2.png")
        self.button_2 = Button(self.ur,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.clear_rec,
            relief="flat"
        )
        self.button_2.place(
            x=492.0,
            y=491.0,
            width=212.414794921875,
            height=48.0
        )

        self.button_image_3 = PhotoImage(
            file=lacn+"button_3.png")
        self.button_3 = Button(self.ur,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.view,
            relief="flat"
        )
        self.button_3.place(
            x=970.0,
            y=199.0,
            width=133.0,
            height=38.0
        )

        self.button_image_4 = PhotoImage(
            file=lacn+"button_4.png")
        self.button_4 = Button(self.ur,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_4_clicked,
            relief="flat"
        )
        self.button_4.place(
            x=473.0,
            y=660.0,
            width=308.0,
            height=83.0
        )

        self.button_image_5 = PhotoImage(
            file="E:/Python/Storerp/assets/frame4/button_1.png")
        self.button_5 = Button(self.ur,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.exit_ur,
            relief="flat"
        )
        self.button_5.place(
            x=857.0,
            y=676.0,
            width=183.0,
            height=49.0
        )
        self.ur.resizable(False, False)

#-----------------------------------------------------------------------------------------------------------------


    def update_unit_price(self,event):
        selected_product = Desc_lab.get()
        selected_price = prices_list.get(selected_product, 0.0)  # Default to 0.0 if not found
        Unitprice.delete(0, "end")  # Clear existing content
        Unitprice.insert(0, selected_price)
    
    
    def view(self):
        try:
            self.tree.delete(*self.tree.get_children())
            id1 = Orderid.get()
            print(id1)
            # Fetch main data for the treeview
            sql1 = "select order_id,description,quantity,unit_price,total,i_date,name,gstin,phoneno,address from invoice_2 where order_id=%s;"
            cursor.execute(sql1, (id1,))
            data = cursor.fetchall()

            for i, (order_id, description, quantity, unit_price, total, i_date,name,gstin,phoneno, address) in enumerate(data, start=1):
                self.tree.insert("", "end", values=(order_id, description, quantity, unit_price, total, i_date,name,gstin,phoneno, address))
        except Exception as e:
            print("Issue in 1", e)
            messagebox.showerror("Issue in 1", e)

    def up_name(self):
        try:
            n1=Name.get()
            selected_item=self.tree.selection()[0]
            current_values = self.tree.item(selected_item, 'values')
            current_values = current_values[:6] + (n1,) + current_values[7:]
            self.tree.item(selected_item, values=current_values)
            #showinfo("success","Name updated successfully")
            print("Name updated successfully")
        except Exception as e:
            print("Error updating Name:", e)

    def up_addrs(self):
        try:
            n1=Address.get()
            selected_item=self.tree.selection()[0]
            current_values = self.tree.item(selected_item, 'values')
            current_values = current_values[:9] + (n1,) + current_values[10:]
            self.tree.item(selected_item, values=current_values)
            #showinfo("success","Address updated successfully")
            #print("Name updated successfully")
        except Exception as e:
            print("Error updating Name:", e)

    def up_phn(self):
        try:
            n1=Phnno.get()
            selected_item=self.tree.selection()[0]
            current_values = self.tree.item(selected_item, 'values')
            current_values = current_values[:8] + (n1,) + current_values[9:]
            self.tree.item(selected_item, values=current_values)
            #showinfo("success","Address updated successfully")
            #print("Name updated successfully")
        except Exception as e:
            print("Error updating Name:", e)
    
    def up_date(self):
        try:
            n1=Date.get()
            selected_item=self.tree.selection()[0]
            current_values = self.tree.item(selected_item, 'values')
            current_values = current_values[:5] + (n1,) + current_values[6:]
            self.tree.item(selected_item, values=current_values)
            #showinfo("success","Address updated successfully")
            #print("Name updated successfully")
            
        except Exception as e:
            print("Error updating Name:", e)
    
    def up_gst(self):
        try:
            n1=Gstlab.get()
            selected_item=self.tree.selection()[0]
            current_values = self.tree.item(selected_item, 'values')
            current_values = current_values[:7] + (n1,) + current_values[8:]
            self.tree.item(selected_item, values=current_values)
            #showinfo("success","Address updated successfully")
            #print("Name updated successfully")
        except Exception as e:
            print("Error updating Name:", e)

    def up_item(self):
        try:
            n1 = Desc_lab.get()
            n2 = Quantity_lab.get()
            n3 = Unitprice.get()

            # Calculate the total
            total = float(n2) * float(n3)

            selected_item = self.tree.selection()[0]
            current_values = self.tree.item(selected_item, 'values')

            # Update the 'Description', 'Quantity', 'Unit Price', and 'Total' columns
            current_values = (current_values[0], n1, n2, n3, total) + current_values[5:]
            self.tree.item(selected_item, values=current_values)

            # Optionally, you can update the corresponding database record here if needed

            print("Fields updated successfully")
        except Exception as e:
            print("Error updating fields:", e)


    def clear_rec(self):
        try:
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
  

    def button_4_clicked(self):
        print("Button 4 clicked")

    def exit_ur(self):
        vs=Toplevel()
        gui3.Page3(vs)
        self.ur.withdraw()
        vs.deiconify()
        
def page():
    ur=Tk()
    Page5(ur)
    ur.mainloop()
if __name__ == '__main__':
    page()
