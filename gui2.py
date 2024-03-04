from pathlib import Path

from tkinter import *

from tkinter import END, Tk, Canvas, Entry, Text, Button, PhotoImage,Spinbox, Toplevel
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
# from obj import products,prices_list

import gui0
#Path(r"E:\Python\Storerp\assets\frame2")

f1=("Arial",15,"bold")
f2=("Arial",10,"bold")
class Page2:
    # global products,prices_list
    # products=['AA Batteries (4-pack)','AAA Batteries (4-pack)','USB-C Charging Cable','Lightning Charging Cable','Wired Headphones','Apple Airpods Headphones','Bose SoundSport Headphones','27in FHD Monitor','27in 4K Gaming Monitor','iPhone','34in Ultrawide Monitor','Google Phone','Flatscreen TV','Macbook Pro Laptop','ThinkPad Laptop','20in Monitor','Vareebadd Phone','LG Washing Machine','LG Dryer']
    # prices_list = {'AA Batteries (4-pack)': 5.99,'AAA Batteries (4-pack)': 6.99,'USB-C Charging Cable': 12.99,'Lightning Charging Cable': 14.99,'Wired Headphones': 24.99,'Apple Airpods Headphones': 149.99,'Bose SoundSport Headphones': 89.99,'27in FHD Monitor': 199.99,'27in 4K Gaming Monitor': 399.99,'iPhone': 699.99,'34in Ultrawide Monitor': 499.99,'Google Phone': 599.99,'Flatscreen TV': 299.99,'Macbook Pro Laptop': 1299.99,'ThinkPad Laptop': 999.99,'20in Monitor': 129.99,'Vareebadd Phone': 499.99,'LG Washing Machine': 799.99,'LG Dryer': 699.99}
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

    def __init__(self,im):
        self.box()
        self.im=im
        self.im.geometry("1350x800+100+0")
        self.im.configure(bg = "#FFFFFF")
        lacn="E:/Python/Storerp/assets/frame2/"


        self.canvas = Canvas(
            self.im,
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
            46.0,
            image=self.image_image_1
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
            1153.0,
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
            text="TIME:",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=lacn+"button_1.png")
        self.button_1 = Button(self.im,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.exit_im,
            relief="flat"
        )
        self.button_1.place(
            x=588.0,
            y=710.0,
            width=173.0,
            height=54.0
        )

        self.image_image_2 = PhotoImage(
            file=lacn+"image_2.png")
        self.image_2 = self.canvas.create_image(
            189.0,
            43.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=lacn+"image_3.png")
        self.image_3 = self.canvas.create_image(
            104.57647705078125,
            229.0,
            image=self.image_image_3
        )

        self.entry_image_1 = PhotoImage(
            file=lacn+"entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            741.0,
            239.5,
            image=self.entry_image_1
        )

        # entry_1 = Text(
        #     bd=0,
        #     bg="#D9D9D9",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # entry_1.place(
        #     x=196.0,
        #     y=116.0,
        #     width=1090.0,
        #     height=245.0
        # )

        self.columns=('prd_id','prd_name','qty','price','total')
        self.scrollbary=Scrollbar(self.im,orient=VERTICAL)
        self.tree=ttk.Treeview(self.canvas,columns=self.columns,show="headings")
        self.style=ttk.Style()
        self.style.configure("Treeview",font=f2,anchor="center")
        self.style.configure("Treeview.Heading",font=f2)
        self.tree.place(
            x=196.0,
            y=116.0,
            width=1090.0,
            height=245.0
        )

        self.tree.configure(yscrollcommand=self.scrollbary.set)
        self.tree.configure(selectmode="extended")
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbary.place(x=1296,y=115,width=14,height=245)

        self.tree.heading('prd_id',text="Product ID")
        self.tree.heading('prd_name',text="Product Name")
        self.tree.heading('qty',text="Quantity")
        self.tree.heading('price',text="Unit Price")
        self.tree.heading('total',text="Total")

        self.image_image_4 = PhotoImage(
            file=lacn+"image_4.png")
        self.image_4 = self.canvas.create_image(
            121.0,
            426.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=lacn+"image_5.png")
        self.image_5 = self.canvas.create_image(
            538.0,
            418.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=lacn+"image_6.png")
        self.image_6 = self.canvas.create_image(
            995.0,
            489.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=lacn+"image_7.png")
        self.image_7 = self.canvas.create_image(
            108.0,
            585.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=lacn+"image_8.png")
        self.image_8 = self.canvas.create_image(
            525.0,
            577.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=lacn+"image_9.png")
        self.image_9 = self.canvas.create_image(
            982.0,
            550.0,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file=lacn+"image_10.png")
        self.image_10 = self.canvas.create_image(
            120.0,
            479.0,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file=lacn+"image_11.png")
        self.image_11 = self.canvas.create_image(
            537.0,
            471.0,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file=lacn+"image_12.png")
        self.image_12 = self.canvas.create_image(
            119.0,
            532.0,
            image=self.image_image_12
        )

        self.image_image_13 = PhotoImage(
            file=lacn+"image_13.png")
        self.image_13 = self.canvas.create_image(
            536.0,
            524.0,
            image=self.image_image_13
        )

        
        # -----------------------------------------------------------------------------------------------------------------------------------------
       
        # self.entry_image_2 = PhotoImage(
        #     file=lacn+"entry_2.png")
        # self.entry_bg_2 = self.canvas.create_image(
        #     273.0,
        #     426.0,
        #     image=self.entry_image_2
        # )
        global ap_lab_prodid,ap_lab_proddesc,ap_lab_unitp,ap_lab_quant,up_lab_prodid,up_lab_proddesc,up_lab_unitp,up_lab_quant,dl_lab_prodid,dl_lab_proddesc
        
        ap_lab_prodid = Entry(self.im,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        ap_lab_prodid.place(
            x=182.0,
            y=408.0,
            width=182.0,
            height=34.0

            # x=182.0,
            # y=567.0,
            # width=182.0,
            # height=34.0
        )

        # self.entry_image_3 = PhotoImage(
        #     file=lacn+"entry_3.png")
        # self.entry_bg_3 = self.canvas.create_image(
        #     690.0,
        #     418.0,
        #     image=self.entry_image_3
        # )
        up_lab_prodid = Entry(self.im,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        up_lab_prodid.place(
            x=599.0,
            y=400.0,
            width=182.0,
            height=34.0
        )

        self.entry_image_4 = PhotoImage(
            file=lacn+"entry_4.png")
        self.entry_bg_4 = self.canvas.create_image(
            1147.0,
            489.0,
            image=self.entry_image_4
        )
        dl_lab_prodid = Entry(self.im,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        dl_lab_prodid.place(
            x=1056.0,
            y=471.0,
            width=182.0,
            height=34.0
        )

        ap_lab_unitp = Entry(self.im,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        ap_lab_unitp.place(
            x=182.0,
            y=514.0,
            width=182.0,
            height=36.0
        )

        # self.canvas.create_rectangle(
        #     182.0,
        #     514.0,
        #     364.0,
        #     550.0,
        #     fill="#D9D9D9",
        #     outline="")

        self.entry_image_5 = PhotoImage(
            file=lacn+"entry_5.png")
        self.entry_bg_5 = self.canvas.create_image(
            690.0,
            524.0,
            image=self.entry_image_5
        )
        up_lab_unitp = Entry(self.im,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        up_lab_unitp.place(
            x=599.0,
            y=506.0,
            width=182.0,
            height=34.0
        )

        self.entry_image_6 = PhotoImage(
            file=lacn+"entry_6.png")
        self.entry_bg_6 = self.canvas.create_image(
            273.0,
            585.0,
            image=self.entry_image_6
        )
        ap_lab_proddesc = Entry(self.im,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            font=f2
        )
        ap_lab_proddesc.place(
            x=182.0,
            y=567.0,
            width=182.0,
            height=34.0
            # x=182.0,
            # y=408.0,
            # width=182.0,
            # height=34.0
        )
        


        up_lab_proddesc = ttk.Combobox(self.im,
            # bd=0,
            # bg="#D9D9D9",
            # fg="#000716",
            # highlightthickness=0
            values=products,font=f2
        )
        up_lab_proddesc.place(
            x=599.0,
            y=559.0,
            width=182.0,
            height=34.0
        )
        up_lab_proddesc.set(' ')
        up_lab_proddesc.bind("<<ComboboxSelected>>", self.update_unit_price_prodid)
        # self.canvas.create_rectangle(
        #     599.0,
        #     559.0,
        #     781.0,
        #     595.0,
        #     fill="#D9D9D9",
        #     outline="")
        

        entry_image_7 = PhotoImage(
            file=lacn+"entry_7.png")
        self.entry_bg_7 = self.canvas.create_image(
            1147.0,
            550.0,
            image=entry_image_7
        )
        dl_lab_proddesc = Entry(self.im,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        dl_lab_proddesc.place(
            x=1056.0,
            y=532.0,
            width=182.0,
            height=34.0
        )

        # entry_image_8 = PhotoImage(
        #     file=lacn+"entry_8.png")
        # self.entry_bg_8 = self.canvas.create_image(
        #     273.0,
        #     479.0,
        #     image=entry_image_8
        # )
        ap_lab_quant = Entry(self.im,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        ap_lab_quant.place(
            x=182.0,
            y=461.0,
            width=182.0,
            height=34.0
        )

        self.entry_image_9 = PhotoImage(
            file=lacn+"entry_9.png")
        self.entry_bg_9 = self.canvas.create_image(
            690.0,
            471.0,
            image=self.entry_image_9
        )
        up_lab_quant = Entry(self.im,
            bd=0,
            bg="#D9D9D9",
            fg="#000716",
            highlightthickness=0
        )
        up_lab_quant.place(
            x=599.0,
            y=453.0,
            width=182.0,
            height=34.0
        )

        self.button_image_2 = PhotoImage(
            file=lacn+"button_2.png")
        self.button_2 = Button(self.im,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.add_product,
            relief="flat"
        )
        self.button_2.place(
            x=109.0,
            y=628.0,
            width=196.0,
            height=48.0
        )

        self.button_image_3 = PhotoImage(
            file=lacn+"button_3.png")
        self.button_3 = Button(self.im,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.update,
            relief="flat"
        )
        self.button_3.place(
            x=501.0,
            y=624.0,
            width=196.0,
            height=48.0
        )

        self.button_image_4 = PhotoImage(
            file=lacn+"button_4.png")
        self.button_4 = Button(self.im,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.delete,
            relief="flat"
        )
        self.button_4.place(
            x=958.0,
            y=624.0,
            width=196.0,
            height=48.0
        )

        self.button_image_5 = PhotoImage(
            file=lacn+"button_5.png")
        self.button_5 = Button(self.im,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.refresh,
            relief="flat"
        )
        self.button_5.place(
            x=1090.0,
            y=377.0,
            width=196.0,
            height=48.0
        )

        self.image_image_14 = PhotoImage(
            file=lacn+"image_14.png")
        self.image_14 = self.canvas.create_image(
            424.0,
            524.0,
            image=self.image_image_14
        )

        self.image_image_15 = PhotoImage(
            file=lacn+"image_15.png")
        self.image_15 = self.canvas.create_image(
            873.0,
            524.0,
            image=self.image_image_15
        )
        im.resizable(False, False)
#--------------------------------------------------------------------------------------------------------------------------------
        self.present_time()
        global con,cursor
        con = connect(
            host="localhost",
            user="root",
            password="anuj1234",
            database="storerp_1"
        )
        # Create a cursor to execute SQL queries
        cursor = con.cursor()
        
        self.box()
        self.view_data()


    def update_unit_price_prodid(self,event):
        selected_product = up_lab_proddesc.get()
        selected_price = prices_list.get(selected_product, 0.0)  # Default to 0.0 if not found
        product_id = products.index(selected_product) + 101 
        up_lab_unitp.delete(0, "end")  # Clear existing content
        up_lab_unitp.insert(0, selected_price)
        up_lab_prodid.delete(0,"end")
        up_lab_prodid.insert(0,product_id)

    def refresh(self):
        self.tree.delete(*self.tree.get_children())
        self.view_data()
    def present_time(self):
        try:
            dt=datetime.now()
            display_time=dt.strftime("%I:%M:%S %p")
            self.canvas.itemconfig(tagOrId=self.TIME,text=display_time)
            self.im.after(200,self.present_time)

            display_date=dt.strftime("%d/%m/%Y")
            self.canvas.itemconfig(tagOrId=self.DATE,text=display_date)
            
        except Exception as e:
            print("Issue",e)


    def view_data(self):
        try:
            sql="select product_id,p_name,quantity,p_price,total from stock_1"
            cursor.execute(sql)
            data=cursor.fetchall()
            # print(data)

            for i, (product_id,p_name,quantity,p_price,total) in enumerate(data, start=1):
                self.tree.insert("","end",values=(product_id,p_name,quantity,p_price,total))
            con.commit()
        
        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)
        


    def exit_im(self):
        win=Toplevel()
        gui0.Page0(win)
        self.im.withdraw()
        win.deiconify()
     # global ap_lab_prodid,ap_lab_proddesc,ap_lab_unitp,ap_lab_quant   
    
    
    def add_product(self):
        try:
            # global id2,id3
            id1=ap_lab_prodid.get()
            id2=ap_lab_proddesc.get()
            id3=ap_lab_unitp.get()
            id4=ap_lab_quant.get()
            
            sql="INSERT INTO stock_1 (product_id, p_name, quantity, p_price) VALUES ('%s', '%s', '%s', '%s');"
            cursor.execute(sql%(id1,id2,id4,id3))
            con.commit()

            # sql="INSERT INTO stock_2 (product_id, p_name,sp_price) VALUES ('%s', '%s','%d');"
            # cursor.execute(sql%(id1,id2,idx))
            # con.commit()

            sql="INSERT INTO stock_2 (product_id, p_name) VALUES ('%s', '%s');"
            cursor.execute(sql%(id1,id2))
            con.commit()

            products.append(id2)
            new_pricelist={'id2':id3}
            prices_list.update(new_pricelist)
            
            showinfo("success","Product Added")
            ap_lab_prodid.delete(0,END)
            ap_lab_proddesc.delete(0,END)
            ap_lab_unitp.delete(0,END)
            ap_lab_quant.delete(0,END)
            ap_lab_prodid.focus()
            self.refresh()
        
        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)

    # def update_lists(self):
    #         products.append(id2)
    #         new_pricelist={'id2':id3}
    #         prices_list.update(new_pricelist)

    def update(self):
        try:
            id11=up_lab_prodid.get()
            id12=up_lab_proddesc.get()
            id13=up_lab_unitp.get()
            id14=up_lab_quant.get()
            
            sql="UPDATE stock_1 SET p_name='%s', quantity='%s', p_price='%s' WHERE product_id='%s';"
            cursor.execute(sql%(id12,id14,id13,id11))
            con.commit()
            new_pricelist={'id12':id13}
            prices_list.update(new_pricelist)
            showinfo("success","Product Updated")
            up_lab_prodid.delete(0,END)
            up_lab_proddesc.delete(0,END)
            up_lab_unitp.delete(0,END)
            up_lab_quant.delete(0,END)
            up_lab_prodid.focus()
            self.refresh()
        
        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)
            
    def delete(self):
        try:
            id21=dl_lab_prodid.get()
            
            sql="delete from stock_1  where product_id='%s';"
            cursor.execute(sql%(id21))
            con.commit()
            showinfo("success","Product Deleted")
            dl_lab_prodid.delete(0,END)
            dl_lab_proddesc.delete(0,END)
            dl_lab_prodid.focus()
            self.refresh()
        
        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)
    

def page():
    im=Tk()
    Page2(im)
    im.mainloop()
if __name__ == '__main__':
    page()