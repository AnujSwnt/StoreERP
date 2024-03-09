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
import warnings
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import gui0

warnings.filterwarnings("ignore", category=FutureWarning)

class Page7:
    def __init__(self,aw):
        self.aw=aw
        self.aw.geometry("1350x800+100+0")
        self.aw.configure(bg = "#FFFFFF")
        lacn="E:/Python/Storerp/assets/frame7/"

        self.canvas = Canvas(
            self.aw,
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
        self.button_1 = Button(self.aw,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.exit,
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
            996.0,
            405.0,
            image=self.image_image_3
        )

        # self.image_image_4 = PhotoImage(
        #     file=lacn+"image_4.png")
        # self.image_4 = self.canvas.create_image(
        #     1002.0,
        #     405.0,
        #     image=self.image_image_4
        # )

        self.image_image_5 = PhotoImage(
            file=lacn+"image_5.png")
        self.image_5 = self.canvas.create_image(
            138.0,
            154.0,
            image=self.image_image_5
        )

        self.button_image_2 = PhotoImage(
            file=lacn+"button_2.png")
        self.button_2 = Button(self.aw,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.button2,
            relief="flat"
        )
        self.button_2.place(
            x=41.0,
            y=225.0,
            width=599.0,
            height=93.0
        )

        self.button_image_3 = PhotoImage(
            file=lacn+"button_3.png")
        self.button_3 = Button(self.aw,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.button3,
            relief="flat"
        )
        self.button_3.place(
            x=41.0,
            y=355.0,
            width=599.0,
            height=93.0
        )

        self.button_image_4 = PhotoImage(
            file=lacn+"button_4.png")
        self.button_4 = Button(self.aw,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.button4,
            relief="flat"
        )
        self.button_4.place(
            x=41.0,
            y=485.0,
            width=599.0,
            height=93.0
        )

        self.button_image_5 = PhotoImage(
            file=lacn+"button_5.png")
        self.button_5 = Button(self.aw,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.button5,
            relief="flat"
        )
        self.button_5.place(
            x=41.0,
            y=605.0,
            width=599.0,
            height=93.0
        )
        self.aw.resizable(False, False)
#------------------------------------------------------------------------------------------------------------------------------------------------------
        self.present_time()
    
        
    def button2(self):
        try:
           
            all_data=pd.read_csv("E:/Python/Storerp/Test_data/all_data_exe.csv")
            all_data['Sales'] = all_data['Quantity Ordered'].astype('int') * all_data['Price Each'].astype('float')
            monthly_sales=all_data.groupby(['Month']).sum()

             # Create a new figure
            fig = Figure(figsize=(7, 5.7), facecolor="#917FB3")
            ax = fig.add_subplot(111)

            # Plot the bar chart
            months = range(1, 13)
            ax.bar(months, monthly_sales['Sales'], color="deepskyblue")
            ax.set_xticks(months)
            ax.set_ylabel('Sales in USD ($)')
            ax.set_xlabel('Month number')
            ax.set_title('Sales chart')
            ax.grid(visible=True)

            # Create the Tkinter canvas
            canvas = FigureCanvasTkAgg(fig, master=self.aw)
            canvas.draw()

            # Remove any existing figure on the canvas
            # canvas.get_tk_widget().destroy()
            # Pack the canvas into the Tkinter window
            canvas.get_tk_widget().place(x=690, y=125)
        except Exception as e:
            print("Issue",e)

    def button3(self):
        try:
            all_data=pd.read_csv("E:/Python/Storerp/Test_data/all_data_exe.csv")
            #all_data['Sales'] = all_data['Quantity Ordered'].astype('int') * all_data['Price Each'].astype('float')
            #monthly_sales=all_data.groupby(['Month']).sum()
            all_data['Hour'] = pd.to_datetime(all_data['Order Date']).dt.hour
            all_data['Minute'] = pd.to_datetime(all_data['Order Date']).dt.minute
            all_data['Count'] = 1
            keys = [pair for pair, df in all_data.groupby(['Hour'])]

             # Create a new figure
            fig = Figure(figsize=(7, 5.7), facecolor="#917FB3")
            ax = fig.add_subplot(111)

            ax.plot(keys, all_data.groupby(['Hour']).count()['Count'])
            ax.set_xticks(keys)
            ax.grid()
            ax.set_title('Order Counts per Hour')

            # Create the Tkinter canvas
            canvas = FigureCanvasTkAgg(fig, master=self.aw)
            canvas.draw()
            

            # Pack the canvas into the Tkinter window
            canvas.get_tk_widget().place(x=690, y=125)
        except Exception as e:
            print("Issue",e)
       
    
    def button4(self):
        try:
            all_data = pd.read_csv("E:/Python/Storerp/Test_data/all_data_exe.csv")
            df = all_data[all_data['Order ID'].duplicated(keep=False)].copy()

            df['Grouped'] = df.groupby('Order ID')['Product'].transform(lambda x: ','.join(x))
            df2 = df[['Order ID', 'Grouped']].drop_duplicates()

            from itertools import combinations
            from collections import Counter

            count = Counter()

            for row in df2['Grouped']:
                row_list = row.split(',')
                count.update(Counter(combinations(row_list, 2)))

            # Extract product pairs and their counts
            pairs = [key for key, value in count.most_common(10)]
            values = [value for key, value in count.most_common(10)]

            # Create a new figure
            fig = Figure(figsize=(7, 5.7), facecolor="#917FB3")
            ax = fig.add_subplot(111)

            # Plot the horizontal bar chart with reduced bar width
            bars = ax.barh(range(len(pairs)), values, color='skyblue', height=0.5)
            ax.set_xlabel('Count')
            ax.set_ylabel('Product Pairs')
            ax.set_title('Most Often Sold Together Products')

            # Add y-axis labels at the center of the plot region
            y_center = len(pairs) / 2.0
            ax.set_yticks(range(len(pairs)))
            ax.set_yticklabels(pairs, ha='center', va='center', color='black', fontweight='bold', fontsize=8, x=0.7)
            ax.set_ylim([-0.5, len(pairs) - 0.5])

            # Add a grid
            ax.grid(axis='x', linestyle='--', alpha=0.7)

            # Create the Tkinter canvas
            canvas = FigureCanvasTkAgg(fig, master=self.aw)
            canvas.draw()

            # Pack the canvas into the Tkinter window
            canvas.get_tk_widget().place(x=690, y=125)

        except Exception as e:
            print("Issue", e)

    def button5(self):
        try:
            all_data = pd.read_csv("E:/Python/Storerp/Test_data/all_data_exe.csv")

            product_group = all_data.groupby('Product')
            quantity_ordered = product_group.sum()['Quantity Ordered']
            prices = all_data.groupby('Product').mean()['Price Each']
            keys = [pair for pair, df in product_group]

            # Create a new figure
            fig, ax1 = plt.subplots(figsize=(7, 5.7), facecolor="#917FB3")

            # Bar chart for Quantity Ordered on the first y-axis
            ax1.bar(keys, quantity_ordered, color='g', label='Quantity Sold')
            ax1.set_xlabel('Product Name')
            ax1.set_ylabel('Quantity Sold', color='g')
            fig.autofmt_xdate()

            # Create a second y-axis
            ax2 = ax1.twinx()

            # Line plot for Prices on the second y-axis
            ax2.plot(keys, prices, color='b', label='Price ($)')
            ax2.set_ylabel('Price ($)', color='b')

            # Rotate x-axis labels for better visibility
            ax1.set_xticklabels(keys, rotation='vertical', size=8)

            # Show legend
            ax1.legend(loc='upper left')
            ax2.legend(loc='upper right')

            # Adjust layout to ensure all labels fit
            plt.tight_layout()

            # Create the Tkinter canvas
            canvas = FigureCanvasTkAgg(fig, master=self.aw)
            canvas.draw()

            # Pack the canvas into the Tkinter window
            canvas.get_tk_widget().place(x=680, y=125)

        except Exception as e:
            print("Issue", e)


    def present_time(self):
        try:
            dt=datetime.now()
            display_time=dt.strftime("%I:%M:%S %p")
            self.canvas.itemconfig(tagOrId=self.TIME,text=display_time)
            self.aw.after(200,self.present_time)

            display_date=dt.strftime("%d/%m/%Y")
            self.canvas.itemconfig(tagOrId=self.DATE,text=display_date)
            
        except Exception as e:
            print("Issue",e)

    def exit(self):
        win=Toplevel()
        gui0.Page0(win)
        self.aw.withdraw()
        win.deiconify()

def page():
    aw=Tk()
    Page7(aw)
    aw.mainloop()

if __name__ == '__main__':
    page()