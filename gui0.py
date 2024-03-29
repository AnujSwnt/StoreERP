from pathlib import Path
from tkinter import *
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
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
import time
from utils import f1,f2
from mysql.connector import *
from matplotlib.figure import Figure
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from decimal import Decimal


import gui1 
import gui2 
import gui3
import gui8


class Page0:
    def __init__(self,window):
        self.window=window
    
        self.window.geometry("1350x800+100+0")
        self.window.configure(bg = "#FFFFFF")
        lacn="E:/Python/Storerp/assets/frame0/"
        

        self.canvas = Canvas(
            self.window,
            bg = "#FFFFFF",
            height = 800,
            width = 1350,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        
        self.image_image_1 = PhotoImage(file=lacn+"image_1.png")
        self.image_1 = self.canvas.create_image(
            102.0,
            400.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=lacn+"image_2.png")
        self.image_2 = self.canvas.create_image(
            675.0,
            46.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            1082.0,
            9.0,
            anchor="nw",
            text="Date: ",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.DATE=self.canvas.create_text(
            1173.0,
            9.0,
            anchor="nw",
            text="12/10/2023",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.TIME=self.canvas.create_text(
            1166.0,
            50.0,
            anchor="nw",
            text="09:30",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.canvas.create_text(
            1075.0,
            48.0,
            anchor="nw",
            text="Time:",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.image_image_3 = PhotoImage(file=lacn+"image_3.png")
        self.image_3 = self.canvas.create_image(
            1157.0,
            422.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(file=lacn+"image_4.png")
        self.image_4 = self.canvas.create_image(
            595.0,
            459.0,
            image=self.image_image_4
        )

        self.canvas.create_rectangle(
            224.0,
            124.0,
            577.0,
            244.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            980.0,
            124.0,
            1333.0,
            244.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            602.0,
            124.0,
            955.0,
            244.0,
            fill="#D9D9D9",
            outline="")

        self.image_image_5 = PhotoImage(file=lacn+"image_5.png")
        self.image_5 = self.canvas.create_image(
            778.0,
            184.0,
            image=self.image_image_5
        )

        self.expn=self.canvas.create_text(
            785.0,
            180.0,
            anchor="nw",
            text="2000002",
            fill="#000000",
            font=("Hanuman Bold", 20 * -1)
        )

        self.button_image_1 = PhotoImage(file=lacn + "button_1.png")
        self.button_1 = Button(self.window,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            anchor="nw",
            command=self.exit,
            relief="flat"
        )
        self.button_1.place(
            x=523.0,
            y=700.0,
            width=442.0,
            height=71.0
        )

        self.image_image_6 = PhotoImage(file=lacn+"image_6.png")
        self.image_6 = self.canvas.create_image(
            1156.0,
            184.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(file=lacn+"image_7.png")
        self.image_7 = self.canvas.create_image(
            403.0,
            184.0,
            image=self.image_image_7
        )

        self.pft=self.canvas.create_text(
            1168.0,
            180.0,
            anchor="nw",
            text="2000003",
            fill="#000000",
            font=("Hanuman Bold", 20 * -1)
        )

        self.t_sale=self.canvas.create_text(
            415.0,
            180.0,
            anchor="nw",
            text="2000001",
            fill="#000000",
            font=("Hanuman Bold", 20 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=lacn+"/button_2.png")
        self.button_2 = Button(self.window,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            anchor="nw",
            command=self.anl,
            relief="flat"
        )
        self.button_2.place(
            x=21.0,
            y=505.0,
            width=163.0,
            height=122.0
        )

        self.button_image_3 = PhotoImage(
            file=lacn+"/button_3.png")
        self.button_3 = Button(self.window,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            anchor="nw",
            command=self.vs,
            relief="flat"
        )
        self.button_3.place(
            x=21.0,
            y=371.0,
            width=163.0,
            height=122.0
        )

        self.button_image_4 = PhotoImage(
            file=lacn+"/button_4.png")
        self.button_4 = Button(self.window,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            anchor="nw",
            command=self.mi,
            relief="flat"
        )
        self.button_4.place(
            x=21.0,
            y=237.0,
            width=163.0,
            height=122.0
        )

        self.button_image_5 = PhotoImage(
            file=lacn+"/button_5.png")
        self.button_5 = Button(self.window,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            anchor="nw",
            command=self.ig,
            relief="flat"
        )
        self.button_5.place(
            x=21.0,
            y=103.0,
            width=163.0,
            height=122.0
        )

        self.button_image_6 = PhotoImage(
            file=lacn+"/button_6.png")
        self.button_6 = Button(self.window,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            anchor="nw",
            command=self.prd,
            relief="flat"
        )
        self.button_6.place(
            x=21.0,
            y=649.0,
            width=163.0,
            height=122.0
        )

        

        self.image_image_8 = PhotoImage(
            file=lacn+"/image_8.png")
        self.image_8 = self.canvas.create_image(
            189.0,
            43.0,
            image=self.image_image_8
        )

        # self.image_image_9 = PhotoImage(
        #     file=lacn+"/image_9.png")
        # self.image_9 = self.canvas.create_image(
        #     590.0,
        #     468.0,
        #     image=self.image_image_9
        # )

        # self.image_image_10 = PhotoImage(
        #     file=lacn+"/image_10.png")
        # self.image_10 = self.canvas.create_image(
        #     1166.0,
        #     422.0,
        #     image=self.image_image_10
        # )
        self.window.resizable(False, False)
#------------------------------------------------------------------------------------------------------------

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
        self.stock_pie_chart()
        self.sales_chart()
        self.total_sale()
        self.total_expn()
        self.total_pft()
        self.button_7 = Button(self.window,
            text="View Pie Chart",
            borderwidth=0,
            highlightthickness=0,
            anchor="nw",
            command=self.view_pie,
            relief="flat"
        )
        self.button_7.place(
            x=865.0,
            y=620.0,
            width=80.0,
            height=22.0
        )

    def total_sale(self):
        try:
            sql="select sum(total) from invoice_2"
            cursor.execute(sql)
            data=cursor.fetchall()
            # print(data)
            con.commit()
            self.canvas.itemconfig(tagOrId=self.t_sale,text=data)
        
        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)
    def total_expn(self):
        try:
            
            sql="select sum(total) from stock_1"
            cursor.execute(sql)
            expnd=cursor.fetchall()
            # print(data)
            con.commit()
            self.canvas.itemconfig(tagOrId=self.expn,text=expnd)
        
        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)
            
    def total_pft(self):
        try:
            # Fetch the total profit from stock_2
            sql = "select sum(total) from stock_2"
            cursor.execute(sql)
            sp_result = cursor.fetchone()
            total_profit = Decimal(sp_result[0]) if sp_result and sp_result[0] is not None else Decimal(0)

            # Fetch the total expenditure from stock_1
            sql1 = "select sum(total) from stock_1"
            cursor.execute(sql1)
            expnd_result = cursor.fetchone()
            total_expenditure = Decimal(expnd_result[0]) if expnd_result and expnd_result[0] is not None else Decimal(0)

            # Calculate the profit
            profit = total_profit - total_expenditure

            # Update the canvas item with the calculated profit
            self.canvas.itemconfig(tagOrId=self.pft, text=profit)

            con.commit()

        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)

    def present_time(self):
        try:
            dt=datetime.now()
            display_time=dt.strftime("%I:%M:%S %p")
            self.canvas.itemconfig(tagOrId=self.TIME,text=display_time)
            self.window.after(200,self.present_time)

            display_date=dt.strftime("%d/%m/%Y")
            self.canvas.itemconfig(tagOrId=self.DATE,text=display_date)
            
        except Exception as e:
            print("Issue",e)
        
    def stock_pie_chart(self):
        try:
            sql="select p_name,quantity from stock_1"
            cursor.execute(sql)
            data=cursor.fetchall()
            pname=[]
            quan=[]
            for d in data:
                pname.append(d[0])
                quan.append(d[1])
            fig_1=Figure(figsize=(7,3.5),facecolor="#D9D9D9")
            ax_1=fig_1.add_subplot()

            # ax_1.pie(quan,labels=pname,autopct='%1.1f%%', startangle=140)
            # # plt.show()
            # ax_1.axis('equal')
            # ax_1.set_title("STOCK IN INVENTORY")
            # ax_1.tick_params(labelsize=5)
            # # fig_1.autofmt_xdate()
            ax_1.set_facecolor("#917FB3")
            ax_1.bar(pname, quan, color='deepskyblue')  # Use bar chart instead of pie chart
            ax_1.set_title("STOCK IN INVENTORY")
            ax_1.set_xlabel("Product Name")
            ax_1.set_ylabel("Quantity")
            fig_1.autofmt_xdate()
            ax_1.tick_params(labelrotation=45, labelsize=8)
            ax_1.grid(visible=True)

            canvas=FigureCanvasTkAgg(figure=fig_1,master=self.window)
            canvas.draw()
            canvas.get_tk_widget().place(x=236,y=270)
                
        except Exception as e:
            con.rollback()
            showerror("Issue",e)

    def view_pie(self):
        try:
            sql="select p_name,quantity from stock_1"
            cursor.execute(sql)
            data=cursor.fetchall()
            pname=[]
            quan=[]
            for d in data:
                pname.append(d[0])
                quan.append(d[1])
            # plt.pie(quan, labels=pname, autopct='%1.1f%%', startangle=140)
            # plt.axis('equal') #pie is drawn in circle
            # plt.title('Distribution of Quantities by Product')
            quan_float = [float(q) for q in quan]
            fig, ax = plt.subplots()
            # wedges, texts, autotexts = ax.pie(quan, labels=pname, autopct=lambda p: '{:.0f} ({:.f}%)'.format(p * sum(quan) / 100, p),startangle=140, textprops=dict(color="w"))
            wedges, texts, autotexts = ax.pie(quan_float, labels=pname, autopct=lambda p: '{:.0f} ({:.1f}%)'.format(p * sum(quan_float) / 100, p),startangle=140, textprops=dict(color="w"))
            ax.axis('equal') 
            ax.set_title('Distribution of Quantities by Product')

            # Add a legend
            ax.legend(wedges, pname, title="Product Names", loc="center left", bbox_to_anchor=(0.8, 0, 0.5, 1))

            plt.show()
        except Exception as e:
            con.rollback()
            showerror("Issue",e)

    
    def sales_chart(self):
        try:
            sql=" select i_date,sum(total) as total_sum from invoice_2 group by i_date order by i_date desc limit 4"
            cursor.execute(sql)
            data=cursor.fetchall()
            date=[]
            sale=[]
            for d in data:
                date.append(d[0])
                sale.append(d[1])
            fig_2 = Figure(figsize=(3, 2.5), facecolor="#917FB3")
            ax_2 = fig_2.add_subplot()
            ax_2.set_facecolor("#917FB3")
            ax_2.fill_between(x=date, y1=sale, alpha=0.7)
            ax_2.tick_params(labelsize=7, colors="black")
            fig_2.autofmt_xdate()
            ax_2.set_title("Sales chart")
            ax_2.plot(date, sale, color="deepskyblue")
            ax_2.grid(visible=True)

            canvas = FigureCanvasTkAgg(figure=fig_2, master=self.window)
            canvas.draw()
            canvas.get_tk_widget().place(x=1010, y=296)

        except Exception as e:
            con.rollback()
            showerror("Issue",e)

    def exit(self):
        print("Button1 exit clicked")
    
    def vs(self):
        vs=Toplevel(self.window)
        gui3.Page3(vs)
        self.window.withdraw()
        vs.deiconify()

    def mi(self):
        mi=Toplevel(self.window)
        gui2.Page2(mi)
        self.window.withdraw()
        mi.deiconify()

    def ig(self):
        ig=Toplevel(self.window)
        gui1.Page1(ig)
        self.window.withdraw()
        ig.deiconify()

    def anl(self):
        pw=Toplevel(self.window)
        gui8.Page8(pw)
        self.window.withdraw()
        pw.deiconify()

    def prd(self):
        print("Button1 perd clicked")

def page():
    window=Tk()
    Page0(window)
    window.mainloop()

if __name__ == '__main__':
    page()

