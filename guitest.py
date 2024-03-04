from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage,Spinbox
from tkinter import ttk
from tkinter.messagebox import *
from tkinter.scrolledtext import *
import requests as rq
import re
from tkinter import messagebox
import datetime
from datetime import datetime
import tkinter
import tkinter as tk
from docxtpl import DocxTemplate
from datetime import *
from mysql.connector import *
import gui2   #import products,prices_list
import gui0

#Path(r"E:\Python\Storerp\assets\frame1")
f1=("Arial",15,"bold")
f2=("Arial",10,"bold")

class Page1:
    global con,cursor
    con = connect(
            host="localhost",
            user="root",
            password="anuj1234",
            database="storerp_1"
        )
        # Create a cursor to execute SQL queries
    cursor = con.cursor() 
    
        
    def box(self):
        global products,prices_list
        try:
            sql1="select p_name from stock_1"
            cursor.execute(sql1)
            data=cursor.fetchall()

            products = [row[0] for row in data]

            # for i, (p_name) in enumerate(data, start=1):
            #     self.tree.insert("","end",values=(product_id,p_name,quantity,p_price,total))
            sql2="select p_name,p_price from stock_1"
            cursor.execute(sql2)
            data2=cursor.fetchall()
            prices_list={row[0]: row[1] for row in data2}
            con.commit()
        
        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)

    def __init__(self,ig):
        self.ig = ig
        self.box()
        self.ig.geometry("1350x800+100+0")
        self.ig.configure(bg = "#FFFFFF")
        lacn="E:/Python/Storerp/assets/frame1/"

        self.canvas = Canvas(
            self.ig,
            bg = "#FFFFFF",
            height = 800,
            width = 1350,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=lacn+"image_1.png")
        self.image_1 = self.canvas.create_image(
            675.0,
            49.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=lacn+"image_2.png")
        self.image_2 = self.canvas.create_image(
            189.0,
            45.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=lacn+"image_3.png")
        self.image_3 = self.canvas.create_image(
            75.0,
            180.0,
            image=self.image_image_3
        )

        global lab_fname,lab_lname,lab_gstin,lab_address,lab_phnno,lab_orderid,lab_quan,lab_desc,lab_unitprice
        
        lab_fname = Entry(self.ig,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            highlightthickness=0,
            font=f1
        )
        lab_fname.place(
            x=165.0,
            y=154.0,
            width=186.0,
            height=39.0
        )

        lab_orderid = Entry(self.ig,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            highlightthickness=0,
            font=f1
        )
        lab_orderid.place(
            x=165.0,
            y=242.0,
            width=186.0,
            height=39.0
        )
        
        
        lab_gstin = Entry(self.ig,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            highlightthickness=0,
            font=f1
        )
        lab_gstin.place(
            x=595.0,
            y=151.0,
            width=186.0,
            height=39.0
        )

        lab_address = Entry(self.ig,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            highlightthickness=0,font=f1
        )
        lab_address.place(
            x=1025.0,
            y=151.0,
            width=252.0,
            height=63.0
        )

        # self.entry_image_5 = PhotoImage(
        #     file=lacn+"entry_5.png")
        # self.entry_bg_5 = self.canvas.create_image(
        #     903.0,
        #     171.5,
        #     image=self.entry_image_5
        # )
        lab_phnno = Entry(self.ig,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            highlightthickness=0,font=f1
        )
        lab_phnno.place(
            x=810.0,
            y=151.0,
            width=186.0,
            height=39.0
        )

        self.image_image_4 = PhotoImage(
            file=lacn+"image_4.png")
        self.image_4 = self.canvas.create_image(
            229.0,
            136.0,
            image=self.image_image_4
        )

        lab_quan = Spinbox(self.ig,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            highlightthickness=0,font=f1,
            from_=1,to=1000
        )
        lab_quan.place(
            x=417.0,
            y=244.0,
            width=186.0,
            height=39.0
        )
        # global products,prices_list
        # products=['AA Batteries (4-pack)','AAA Batteries (4-pack)','USB-C Charging Cable','Lightning Charging Cable','Wired Headphones','Apple Airpods Headphones','Bose SoundSport Headphones','27in FHD Monitor','27in 4K Gaming Monitor','iPhone','34in Ultrawide Monitor','Google Phone','Flatscreen TV','Macbook Pro Laptop','ThinkPad Laptop','20in Monitor','Vareebadd Phone','LG Washing Machine','LG Dryer']
        # prices_list = {'AA Batteries (4-pack)': 5.99,'AAA Batteries (4-pack)': 6.99,'USB-C Charging Cable': 12.99,'Lightning Charging Cable': 14.99,'Wired Headphones': 24.99,'Apple Airpods Headphones': 149.99,'Bose SoundSport Headphones': 89.99,'27in FHD Monitor': 199.99,'27in 4K Gaming Monitor': 399.99,'iPhone': 699.99,'34in Ultrawide Monitor': 499.99,'Google Phone': 599.99,'Flatscreen TV': 299.99,'Macbook Pro Laptop': 1299.99,'ThinkPad Laptop': 999.99,'20in Monitor': 129.99,'Vareebadd Phone': 499.99,'LG Washing Machine': 799.99,'LG Dryer': 699.99}
   

        lab_desc = ttk.Combobox(
            self.ig,
            # bd=0,
            # bg="#BFBBBB",
            # fg="#000716",
            # highlightthickness=0,
            font=f1,
            values=products
            
        )
        # lab_desc = ttk.Combobox(self.ig, style="TCombobox", values=self.products, font=f1)
        # self.ig.option_add('*TCombobox*Listbox.background', '#BFBBBB')
        # self.ig.option_add('*TCombobox*Listbox.foreground', '#000716')

        lab_desc.place(
            x=630.0,
            y=244.0,
            width=191.0,
            height=39.0
        )
        lab_desc.set(' ')
        lab_desc.bind("<<ComboboxSelected>>", self.update_unit_price)

        lab_unitprice = Spinbox(self.ig,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            font=f1,
            from_=0.0,to=10000,increment=0.5
        )
        lab_unitprice.place(
            x=836.0,
            y=242.0,
            width=186.0,
            height=39.0
        )
        

        self.image_image_5 = PhotoImage(
            file=lacn+"image_5.png")
        self.image_5 = self.canvas.create_image(
            493.0,
            219.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=lacn+"image_6.png")
        self.image_6 = self.canvas.create_image(
            700.0,
            216.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=lacn+"image_7.png")
        self.image_7 = self.canvas.create_image(
            900.0,
            213.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=lacn+"image_8.png")
        self.image_8 = self.canvas.create_image(
            226.0,
            220.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=lacn+"image_9.png")
        self.image_9 = self.canvas.create_image(
            659.0,
            133.0,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file=lacn+"image_10.png")
        self.image_10 = self.canvas.create_image(
            1089.0,
            133.0,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file=lacn+"image_11.png")
        self.image_11 = self.canvas.create_image(
            874.0,
            133.0,
            image=self.image_image_11
        )

        lab_lname = Entry(self.ig,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            highlightthickness=0,font=f1
        )
        lab_lname.place(
            x=380.0,
            y=154.0,
            width=186.0,
            height=39.0
        )

        self.image_image_12 = PhotoImage(
            file=lacn+"image_12.png")
        self.image_12 = self.canvas.create_image(
            444.0,
            136.0,
            image=self.image_image_12
        )
        
        columns=('qty','desc','price','total')
        global tree
        tree=ttk.Treeview(self.canvas,columns=columns,show="headings")
        self.style=ttk.Style()
        self.style.configure("Treeview",font=f2)
        self.style.configure("Treeview.Heading",font=f2)
        tree.place(
            x=31.0,
            y=310.0,
            width=1251.0,
            height=327.0
        )
        tree.heading('qty',text="Quantity")
        tree.heading('desc',text="Description")
        tree.heading('price',text="Unit Price")
        tree.heading('total',text="Total")



        self.button_image_1 = PhotoImage(
            file=lacn+"button_1.png")
        self.button_1 = Button(self.ig,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.new_invoice,
            relief="flat"
        )
        self.button_1.place(
            x=57.0,
            y=664.0,
            width=308.0,
            height=83.0
        )

        self.button_image_2 = PhotoImage(
            file=lacn+"button_2.png")
        self.button_2 = Button(self.ig,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.gen_invoice,
            relief="flat"
        )
        self.button_2.place(
            x=528.0,
            y=669.0,
            width=308.0,
            height=83.0
        )

        self.button_image_3 = PhotoImage(
            file=lacn+"button_3.png")
        self.button_3 = Button(self.ig,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.add_item,
            relief="flat"
        )
        self.button_3.place(
            x=1055.0,
            y=237.0,
            width=196.0,
            height=48.0
        )

        self.button_image_4 = PhotoImage(
            file=lacn+"button_4.png")
        self.button_4 = Button(self.ig,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.exit_ig,
            relief="flat"
        )
        self.button_4.place(
            x=999.0,
            y=669.0,
            width=308.0,
            height=83.0
        )

        self.canvas.create_text(
            1062.0,
            12.0,
            anchor="nw",
            text="Date: ",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.DATE=self.canvas.create_text(
            1153.0,
            12.0,
            anchor="nw",
            text="12/10/2023",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.TIME=self.canvas.create_text(
            1152.0,
            53.0,
            anchor="nw",
            text="09:30",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.canvas.create_text(
            1055.0,
            51.0,
            anchor="nw",
            text="Time:",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )
        ig.resizable(False, False)
        self.present_time()
        
#---------------------------------------------------FUNCTIONS-------------------------------------------------------------------------------
    


        self.new_id()
        lab_orderid.config(state=DISABLED)
        
    def update_unit_price(self,event):
        selected_product = lab_desc.get()
        selected_price = prices_list.get(selected_product, 0.0)  # Default to 0.0 if not found
        lab_unitprice.delete(0, "end")  # Clear existing content
        lab_unitprice.insert(0, selected_price)
    def new_id(self):
        try:
            global maxval,new_order_id
            sql = "select max(order_id) from invoice_2"
            cursor.execute(sql)
            maxval=cursor.fetchone()[0]
            new_order_id=maxval+1
            lab_orderid.delete(0, "end")  # Clear existing content
            lab_orderid.insert(0, new_order_id)  # Insert new content

        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)

        
    def present_time(self):
        global display_date
        try:
            dt=datetime.now()
            display_time=dt.strftime("%I:%M:%S %p")
            self.canvas.itemconfig(tagOrId=self.TIME,text=display_time)
            self.ig.after(200,self.present_time)

            display_date=dt.strftime("%d/%m/%Y")
            self.canvas.itemconfig(tagOrId=self.DATE,text=display_date)
            
        except Exception as e:
            print("Issue",e)

    def clear_item(self):
        lab_quan.delete(0,tkinter.END)
        lab_quan.insert(0,"1"),
        lab_desc.delete(0,tkinter.END),
        lab_unitprice.delete(0,tkinter.END),
        lab_unitprice.insert(0,"0.0")

    invoice_list=[]
    def add_item(self):
        global qty,desc,price,total_l,invoice_item
        qty=int(lab_quan.get())
        desc=lab_desc.get()
        price=float(lab_unitprice.get())
        total_l=qty*price
        invoice_item=[qty,desc,price,total_l]
        tree.insert('',0,values=invoice_item)
        self.clear_item()
        self.invoice_list.append(invoice_item)

    def new_invoice(self):
        lab_fname.delete(0,tkinter.END)
        lab_lname.delete(0,tkinter.END)
        lab_gstin.delete(0,tkinter.END)
        lab_address.delete(0,tkinter.END)
        lab_phnno.delete(0,tkinter.END)
        lab_orderid.delete(0,tkinter.END)
        self.clear_item()
        tree.delete(*tree.get_children())
        self.invoice_list.clear()
    
    def gen_invoice(self):
        doc=DocxTemplate("Invoice_newtemp.docx")
        name=lab_fname.get()+" "+lab_lname.get()
        gst=lab_gstin.get()
        phone=lab_phnno.get()
        add=lab_address.get()
        ord_id=lab_orderid.get()

        # try:
        #     idate=datetime.now().strftime("%Y%m%d")
        #     sql = "INSERT INTO invoice_2(order_id, name, description, quantity, unit_price, gstin, phoneno, address, total,i_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s)"

        #     for item in self.invoice_list:
        #         row = (ord_id, name, item[1], item[0], item[2], gst, phone, add, item[3],idate)
        #         cursor.execute(sql,row)

        #     con.commit()
        #     showinfo("success", "Data Added")
        # except Exception as e:
        #     print("Issue", e)
        #     messagebox.showerror("Issue", e)
        #     self.clear_item()
        #     tree.delete(*tree.get_children())
        #     self.invoice_list.clear()
        #     return
        
        try:
            q=lab_quan.get()
            n=lab_desc.get()

            if not q.isdigit():
                raise ValueError("Quantity must be a valid integer.")
            sql="update stock_1 set quantity=quantity - %s  where p_name=%s"
            for item in self.invoice_list:
                row = (item[0], item[1])
                cursor.execute(sql,row)
            
            cursor.execute(sql,(int(q),n))
            con.commit()

            messagebox.showinfo("Success", "Quantity updated successfully.")

        except ValueError as ve:
            print("ValueError:", ve)
            messagebox.showerror("Error", str(ve))
            

        except Exception as e:
            print("Issue:", e)
            messagebox.showerror("Issue", str(e))
            return

        # try:
        #     subtotal=sum(item[3] for item in self.invoice_list)
        #     tax=0.09
        #     total=subtotal*(1+tax)
        #     tot=round(total,2)
        #     doc.render({
        #         "name":name,
        #         "gst":gst,
        #         "phone":phone,
        #         "address":add,
        #         "orderid":ord_id,
        #         "invoice_list":self.invoice_list,
        #         "subtotal":subtotal,
        #         "tax":str(tax*100)+"%",
        #         "total":tot 
        #         })
        #     doc_name="Invoice"+" "+name+ datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"
        #     doc.save(doc_name)
        # except Exception as e:
        #     print("Issue", e)
        #     messagebox.showerror("Issue", e)

        # messagebox.showinfo("Successful","Invoice Generation Completed")
        lab_orderid.config(state=NORMAL)
        self.new_id()
        lab_orderid.config(state=DISABLED)
        self.new_invoice()
    
    def exit_ig(self):
        win=Toplevel()
        gui0.Page0(win)
        self.ig.withdraw()
        win.deiconify()



def page():
    ig=Tk()
    Page1(ig)
    ig.mainloop()

if __name__ == '__main__':
    page()