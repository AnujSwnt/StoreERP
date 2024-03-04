from pathlib import Path


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

import gui1
#Path(r"E:/Python/Storerp/assets/frame4/")

class Page4:
    def __init__(self,cf):
        self.cf = cf
        self.cf.geometry("1350x800+100+0")
        self.cf.configure(bg = "#FFFFFF")
        lacn="E:/Python/Storerp/assets/frame4/"

        self.canvas = Canvas(
            self.cf,
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

        self.button_image_1 = PhotoImage(
            file=lacn+"button_1.png")
        self.button_1 = Button(self.cf,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.exit_cf,
            relief="flat"
        )
        self.button_1.place(
            x=23.0,
            y=697.0,
            width=183.0,
            height=49.0
        )

        self.button_image_2 = PhotoImage(
            file=lacn+"button_2.png")
        self.button_2 = Button(self.cf,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_2_clicked,
            relief="flat"
        )
        self.button_2.place(
            x=612.0,
            y=735.0,
            width=169.0,
            height=42.0
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
            88.0,
            191.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=lacn+"image_4.png")
        self.image_4 = self.canvas.create_image(
            692.0,
            170.0,
            image=self.image_image_4
        )

        self.button_image_3 = PhotoImage(
            file=lacn+"button_3.png")
        self.button_3 = Button(self.cf,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_3_clicked,
            relief="flat"
        )
        self.button_3.place(
            x=235.0,
            y=213.0,
            width=140.0,
            height=54.0
        )

        self.button_image_4 = PhotoImage(
            file=lacn+"button_4.png")
        self.button_4 = Button(self.cf,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_4_clicked,
            relief="flat"
        )
        self.button_4.place(
            x=573.0,
            y=213.0,
            width=140.0,
            height=54.0
        )

        self.image_image_5 = PhotoImage(
            file=lacn+"image_5.png")
        self.image_5 = self.canvas.create_image(
            692.0,
            607.0,
            image=self.image_image_5
        )

        self.button_image_5 = PhotoImage(
            file=lacn+"button_5.png")
        self.button_5 = Button(self.cf,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_5_clicked,
            relief="flat"
        )
        self.button_5.place(
            x=235.0,
            y=650.0,
            width=140.0,
            height=54.0
        )

        self.button_image_6 = PhotoImage(
            file=lacn+"button_6.png")
        self.button_6 = Button(self.cf,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_6_clicked,
            relief="flat"
        )
        self.button_6.place(
            x=573.0,
            y=650.0,
            width=140.0,
            height=54.0
        )

        self.image_image_6 = PhotoImage(
            file=lacn+"image_6.png")
        self.image_6 = self.canvas.create_image(
            692.0,
            455.0,
            image=self.image_image_6
        )

        self.button_image_7 = PhotoImage(
            file=lacn+"button_7.png")
        self.button_7 = Button(self.cf,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_7_clicked,
            relief="flat"
        )
        self.button_7.place(
            x=235.0,
            y=498.0,
            width=140.0,
            height=54.0
        )

        self.button_image_8 = PhotoImage(
            file=lacn+"button_8.png")
        self.button_8 = Button(self.cf,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_8_clicked,
            relief="flat"
        )
        self.button_8.place(
            x=573.0,
            y=498.0,
            width=140.0,
            height=54.0
        )

        self.image_image_7 = PhotoImage(
            file=lacn+"image_7.png")
        self.image_7 = self.canvas.create_image(
            692.0,
            303.0,
            image=self.image_image_7
        )

        self.button_image_9 = PhotoImage(
            file=lacn+"button_9.png")
        self.button_9 = Button(self.cf,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_9_clicked,
            relief="flat"
        )
        self.button_9.place(
            x=235.0,
            y=346.0,
            width=140.0,
            height=54.0
        )

        self.button_image_10 = PhotoImage(
            file=lacn+"button_10.png")
        self.button_10 = Button(self.cf,
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=self.button_10_clicked,
            relief="flat"
        )
        self.button_10.place(
            x=573.0,
            y=346.0,
            width=140.0,
            height=54.0
        )

        self.canvas.create_rectangle(
            983.0,
            211.0,
            1122.0,
            257.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_text(
            1000.0,
            220.0,
            anchor="nw",
            text="YES",
            fill="#000000",
            font=("Orbitron Bold", 32 * -1)
        )

        self.canvas.create_rectangle(
            983.0,
            653.0,
            1122.0,
            699.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_text(
            1000.0,
            662.0,
            anchor="nw",
            text="YES",
            fill="#000000",
            font=("Orbitron Bold", 32 * -1)
        )

        self.canvas.create_rectangle(
            983.0,
            350.0,
            1122.0,
            396.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_text(
            1000.0,
            359.0,
            anchor="nw",
            text="NO",
            fill="#000000",
            font=("Orbitron Bold", 32 * -1)
        )

        self.canvas.create_rectangle(
            983.0,
            502.0,
            1122.0,
            548.0,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_text(
            1000.0,
            512.0,
            anchor="nw",
            text="NO",
            fill="#000000",
            font=("Orbitron Bold", 32 * -1)
        )

        self.image_image_8 = PhotoImage(
            file=lacn+"image_8.png")
        self.image_8 = self.canvas.create_image(
            114.0,
            305.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file=lacn+"image_9.png")
        self.image_9 = self.canvas.create_image(
            101.0,
            407.0,
            image=self.image_image_9
        )

        self.entry_image_1 = PhotoImage(
            file=lacn+"entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            108.0,
            349.5,
            image=self.entry_image_1
        )
        order_id_cf = Entry(self.cf,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            highlightthickness=0
        )
        order_id_cf.place(
            x=38.0,
            y=329.0,
            width=140.0,
            height=39.0
        )

        self.entry_image_2 = PhotoImage(
            file=lacn+"entry_2.png")
        self.entry_bg_2 = self.canvas.create_image(
            108.0,
            447.5,
            image=self.entry_image_2
        )
        cust_id_cf = Entry(self.cf,
            bd=0,
            bg="#BFBBBB",
            fg="#000716",
            highlightthickness=0
        )
        cust_id_cf.place(
            x=38.0,
            y=427.0,
            width=140.0,
            height=39.0
        )

        self.canvas.create_text(
            1057.0,
            10.0,
            anchor="nw",
            text="Date: ",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.DATE=self.canvas.create_text(
            1148.0,
            10.0,
            anchor="nw",
            text="12/10/2023",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.TIME=self.canvas.create_text(
            1148.0,
            51.0,
            anchor="nw",
            text="09:30",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )

        self.canvas.create_text(
            1050.0,
            49.0,
            anchor="nw",
            text="TIME:",
            fill="#000000",
            font=("Hanuman Bold", 32 * -1)
        )
        self.cf.resizable(False, False)
        self.present_time()
    def present_time(self):
        try:
            dt=datetime.now()
            display_time=dt.strftime("%I:%M:%S %p")
            self.canvas.itemconfig(tagOrId=self.TIME,text=display_time)
            self.cf.after(200,self.present_time)

            display_date=dt.strftime("%d/%m/%Y")
            self.canvas.itemconfig(tagOrId=self.DATE,text=display_date)
            
        except Exception as e:
            print("Issue",e)

    
    def exit_cf(self):
        ig=Toplevel()
        gui1.Page1(ig)
        self.cf.withdraw()
        ig.deiconify()

    def button_2_clicked(self):
        print("Button clicked")
    def button_3_clicked(self):
        print("Button clicked")
    def button_4_clicked(self):
        print("Button clicked")
    def button_5_clicked(self):
        print("Button clicked")
    def button_6_clicked(self):
        print("Button clicked")
    def button_7_clicked(self):
        print("Button clicked")
    def button_8_clicked(self):
        print("Button clicked")
    def button_9_clicked(self):
        print("Button clicked")
    def button_10_clicked(self):
        print("Button clicked")
        
def page():
    cf=Tk()
    Page4(cf)
    cf.mainloop()
if __name__ == '__main__':
    page()