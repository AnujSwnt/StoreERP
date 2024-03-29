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


import gui0
import gui5
import gui6

#Path(r"E:/Python/Storerp/assets/frame3/")
class Page3:
    def __init__(self,vs):
        self.vs = vs
        self.vs.geometry("1350x800+100+0")
        self.vs.configure(bg = "#FFFFFF")
        lacn="E:/Python/Storerp/assets/frame3/"

        self.canvas = Canvas(
            self.vs,
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
            1165.0,
            45.0,
            anchor="nw",
            text="09:30",
            fill="#000000",
            font=("Orbitron Bold", 24 * -1)
        )

        self.canvas.create_text(
            1087.0,
            7.0,
            anchor="nw",
            text="Date: ",
            fill="#000000",
            font=("Orbitron Bold", 24 * -1)
        )

        self.canvas.create_text(
            1170.0,
            7.0,
            anchor="nw",
            text="2/10/2023",
            fill="#000000",
            font=("Orbitron Bold", 24 * -1)
        )

        self.canvas.create_text(
            1087.0,
            48.0,
            anchor="nw",
            text="TIME:",
            fill="#000000",
            font=("Orbitron Bold", 24 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=lacn+"button_1.png")
        self.button_1 = Button(self.vs,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.exit_vs,
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
            675.0,
            46.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            1122.0,
            7.0,
            anchor="nw",
            text=" ",
            fill="#000000",
            font=("Orbitron Bold", 24 * -1)
        )

        self.image_image_4 = PhotoImage(
            file=lacn+"image_4.png")
        self.image_4 = self.canvas.create_image(
            189.0,
            43.0,
            image=self.image_image_4
        )

        # self.entry_image_1 = PhotoImage(
        #     file=lacn+"entry_1.png")
        # self.entry_bg_1 = self.canvas.create_image(
        #     742.0,
        #     285.5,
        #     image=self.entry_image_1
        # )

        # entry_1 = Text(
        #     bd=0,
        #     bg="#D9D9D9",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # entry_1.place(
        #     x=196.0,
        #     y=116.0,
        #     width=1092.0,
        #     height=337.0
        # )

        self.columns=('order_id','prd_name','qty','price','total','date','address')
        self.scrollbary=Scrollbar(self.vs,orient=VERTICAL)
        self.tree=ttk.Treeview(self.canvas,columns=self.columns,show="headings")
        self.tree.place(
            x=196.0,
            y=116.0,
            width=1098.0,
            height=330.0
        )

        self.tree.configure(yscrollcommand=self.scrollbary.set)
        self.tree.configure(selectmode="extended")
        self.scrollbary.configure(command=self.tree.yview)
        self.scrollbary.place(x=1298,y=116,width=14,height=330)

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
        # self.tree.column('#7',stretch=NO,minwidth=25,width=145)


        self.image_image_5 = PhotoImage(
            file=lacn+"image_5.png")
        self.image_5 = self.canvas.create_image(
            100.0,
            188.0,
            image=self.image_image_5
        )

        self.button_image_2 = PhotoImage(
            file=lacn+"button_2.png")
        self.button_2 = Button(self.vs,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.dwnld_csv,
            relief="flat"
        )
        self.button_2.place(
            x=1015.0,
            y=516.0,
            width=267.0,
            height=57.0
        )

        # self.image_image_6 = PhotoImage(
        #     file=lacn+"image_6.png")
        # self.image_6 = self.canvas.create_image(
        #     294.0,
        #     510.0,
        #     image=self.image_image_6
        # )

        # self.image_image_7 = PhotoImage(
        #     file=lacn+"image_7.png")
        # self.image_7 = self.canvas.create_image(
        #     519.0,
        #     508.0,
        #     image=self.image_image_7
        # )

        # self.image_image_8 = PhotoImage(
        #     file=lacn+"image_8.png")
        # self.image_8 = self.canvas.create_image(
        #     765.0,
        #     508.0,
        #     image=self.image_image_8
        # )

        self.image_image_9 = PhotoImage(
            file=lacn+"image_9.png")
        self.image_9 = self.canvas.create_image(
            81.0,
            372.0,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file=lacn+"image_10.png")
        self.image_10 = self.canvas.create_image(
            92.0,
            336.0,
            image=self.image_image_10
        )
        
        global order_Id,cust_id
        self.entry_image_2 = PhotoImage(
            file=lacn+"entry_2.png")
        self.entry_bg_2 = self.canvas.create_image(
            99.0,
            410.5,
            image=self.entry_image_2
        )
        order_Id = Entry(self.vs,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            highlightthickness=0
        )
        order_Id.place(
            x=29.0,
            y=390.0,
            width=140.0,
            height=39.0
        )

        # self.image_image_11 = PhotoImage(
        #     file=lacn+"image_11.png")
        # self.image_11 = self.canvas.create_image(
        #     94.0,
        #     449.0,
        #     image=self.image_image_11
        # )

        # self.entry_image_3 = PhotoImage(
        #     file=lacn+"entry_3.png")
        # self.entry_bg_3 = self.canvas.create_image(
        #     99.0,
        #     487.5,
        #     image=self.entry_image_3
        # )
        # cust_id = Entry(self.vs,
        #     bd=0,
        #     bg="#BFBBBB",
        #     fg="#000716",
        #     highlightthickness=0
        # )
        # cust_id.place(
        #     x=29.0,
        #     y=467.0,
        #     width=140.0,
        #     height=39.0
        # )

        self.button_image_3 = PhotoImage(
            file=lacn+"button_3.png")
        self.button_3 = Button(self.vs,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.find_vs,
            relief="flat"
        )
        self.button_3.place(
            x=31.0,
            y=522.0,
            width=125.0,
            height=50.0
        )

        self.button_image_4 = PhotoImage(
            file=lacn+"button_4.png")
        self.button_4 = Button(self.vs,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.update_record_vs,
            relief="flat"
        )
        self.button_4.place(
            x=313.0,
            y=595.0,
            width=308.0,
            height=83.0
        )

        self.button_image_5 = PhotoImage(
            file=lacn+"button_5.png")
        self.button_5 = Button(self.vs,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.delete_record_vs,
            relief="flat"
        )
        self.button_5.place(
            x=717.0,
            y=595.0,
            width=311.0,
            height=83.0
        )

        self.canvas.create_text(
            1068.0,
            9.0,
            anchor="nw",
            text="Date: ",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.DATE=self.canvas.create_text(
            1159.0,
            9.0,
            anchor="nw",
            text="12/10/2023",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.TIME=self.canvas.create_text(
            1159.0,
            50.0,
            anchor="nw",
            text="09:30",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.canvas.create_text(
            1061.0,
            48.0,
            anchor="nw",
            text="TIME:",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.button_image_6 = PhotoImage(
            file=lacn+"button_6.png")
        self.button_6 = Button(self.vs,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.view_vs,
            relief="flat"
        )
        self.button_6.place(
            x=1144.0,
            y=465.0,
            width=144.0,
            height=38.0
        )
        self.vs.resizable(False, False)
#------------------------------------------------------------------------------------------------------------------------------------------
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
        self.view_vs()
        
    def present_time(self):
        try:
            dt=datetime.now()
            display_time=dt.strftime("%I:%M:%S %p")
            self.canvas.itemconfig(tagOrId=self.TIME,text=display_time)
            self.vs.after(200,self.present_time)

            display_date=dt.strftime("%d/%m/%Y")
            self.canvas.itemconfig(tagOrId=self.DATE,text=display_date)
            
        except Exception as e:
            print("Issue",e)


    def exit_vs(self):
        win=Toplevel()
        gui0.Page0(win)
        self.vs.withdraw()
        win.deiconify()
    

    def view_vs(self):
        try:
            self.tree.delete(*self.tree.get_children())
            sql="select order_id,description,quantity,unit_price,total,i_date,address from invoice_2"
            cursor.execute(sql)
            data=cursor.fetchall()
            

            for i, (order_id,description,quantity,unit_price,total,i_date,address) in enumerate(data, start=1):
                self.tree.insert("","end",values=(order_id,description,quantity,unit_price,total,i_date,address))
            con.commit()
        
        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)
    
    def dwnld_csv(self):
        try:
            
            sql1 = "SELECT 'OrderId','Name','Description', 'Quantity', 'Unit_Price', 'Total', 'GSTIN','Phoneno','Date' UNION SELECT order_id, name,description, quantity, unit_price, total,gstin,phoneno, i_date  INTO OUTFILE 'E:/Python/Storerp/StoreSalesData/"
            doc_name = "SalesRecord" + datetime.now().strftime("%Y-%m-%d-%H-%M-%S") + ".csv"
            sql2 = "' FIELDS TERMINATED BY ',' FROM invoice_2"
            sql = sql1 + doc_name + sql2
            cursor.execute(sql)
            con.commit()
            showinfo("success", "File Downloaded")

        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)

    def find_vs(self):
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
        


    def update_record_vs(self):
        ur=Toplevel()
        gui5.Page5(ur)
        self.vs.withdraw()
        ur.deiconify()

    def delete_record_vs(self):
        dr=Toplevel()
        gui6.Page6(dr)
        self.vs.withdraw()
        dr.deiconify()
    
        
def page():
    vs=Tk()
    Page3(vs)
    vs.mainloop()


if __name__ == '__main__':
    page()