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
import calendar
from utils import f1,f2
from mysql.connector import *
from matplotlib.figure import Figure
import pandas as pd
import warnings
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import gui0
import gui7

warnings.filterwarnings("ignore", category=FutureWarning)


class Page8:
    def __init__(self,pw):
      self.pw=pw
      self.pw.geometry("1073x726+100+0")
      self.pw.configure(bg = "#FFFFFF")
      lacn="E:/Python/Storerp/assets/frame8/"

      self.canvas = Canvas(
          self.pw,
          bg = "#FFFFFF",
          height = 726,
          width = 1073,
          bd = 0,
          highlightthickness = 0,
          relief = "ridge"
      )

      self.canvas.place(x = 0, y = 0)
      self.image_image_1 = PhotoImage(
          file=lacn+"image_1.png")
      self.image_1 = self.canvas.create_image(
          536.0,
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

      entry_image_1 = PhotoImage(
          file=lacn+"entry_1.png")
      self.entry_bg_1 = self.canvas.create_image(
          659.0,
          177.0,
          image=entry_image_1
      )
      self.mnth_path = Entry(self.pw,
          bd=0,
          bg="#D9D9D9",
          fg="#000716",
          highlightthickness=0
      )
      self.mnth_path.place(
          x=377.0,
          y=153.0,
          width=564.0,
          height=46.0
      )

      self.button_image_1 = PhotoImage(
          file=lacn+"button_1.png")
      self.button_1 = Button(self.pw,
          image=self.button_image_1,
          borderwidth=0,
          highlightthickness=0,
          command=self.dwn_month_data,
          relief="flat"
      )
      self.button_1.place(
          x=33.0,
          y=131.0,
          width=311.0,
          height=83.0
      )

      self.button_image_2 = PhotoImage(
          file=lacn+"button_2.png")
      self.button_2 = Button(self.pw,
          image=self.button_image_2,
          borderwidth=0,
          highlightthickness=0,
          command=self.process,
          relief="flat"
      )
      self.button_2.place(
          x=475.0,
          y=351.0,
          width=311.0,
          height=83.0
      )

      self.button_image_3 = PhotoImage(
          file=lacn+"button_3.png")
      self.button_3 = Button(self.pw,
          image=self.button_image_3,
          borderwidth=0,
          highlightthickness=0,
          command=self.add_data,
          relief="flat"
      )
      self.button_3.place(
          x=501.0,
          y=214.0,
          width=274.6748046875,
          height=58.0
      )

    #   self.button_image_4 = PhotoImage(
    #       file=lacn+"button_4.png")
    #   self.button_4 = Button(self.pw,
    #       image=self.button_image_4,
    #       borderwidth=0,
    #       highlightthickness=0,
    #       command=self.copy_path,
    #       relief="flat"
    #   )
    #   self.button_4.place(
    #       x=501.0,
    #       y=522.0,
    #       width=274.6748046875,
    #       height=58.0
    #   )

      self.image_image_3 = PhotoImage(
          file=lacn+"image_3.png")
      self.image_3 = self.canvas.create_image(
          658.0,
          123.0,
          image=self.image_image_3
      )
        
      self.entry_image_2 = PhotoImage(
          file=lacn+"entry_2.png")
      self.entry_bg_2 = self.canvas.create_image(
          667.0,
          309.0,
          image=self.entry_image_2
      )
      self.added_path = Entry(self.pw,
          bd=0,
          bg="#D9D9D9",
          fg="#000716",
          highlightthickness=0
      )
      self.added_path.place(
          x=385.0,
          y=285.0,
          width=564.0,
          height=46.0
      )

      self.image_image_4 = PhotoImage(
          file=lacn+"image_4.png")
      self.image_4 = self.canvas.create_image(
          197.0,
          309.0,
          image=self.image_image_4
      )

      self.entry_image_3 = PhotoImage(
          file=lacn+"entry_3.png")
      self.entry_bg_3 = self.canvas.create_image(
          669.0,
          475.0,
          image=self.entry_image_3
      )
      self.copy = Entry(self.pw,
          bd=0,
          bg="#D9D9D9",
          fg="#000716",
          highlightthickness=0
      )
      self.copy.place(
          x=387.0,
          y=451.0,
          width=564.0,
          height=46.0
      )

      self.image_image_5 = PhotoImage(
          file=lacn+"image_5.png")
      self.image_5 = self.canvas.create_image(
          197.0,
          477.0,
          image=self.image_image_5
      )

      self.button_image_5 = PhotoImage(
          file=lacn+"button_5.png")
      self.button_5 = Button(self.pw,
          image=self.button_image_5,
          borderwidth=0,
          highlightthickness=0,
          command=self.exit,
          relief="flat"
      )
      self.button_5.place(
          x=790.0,
          y=626.0,
          width=183.0,
          height=49.0
      )

      self.button_image_6 = PhotoImage(
          file=lacn+"button_6.png")
      self.button_6 = Button(self.pw,
          image=self.button_image_6,
          borderwidth=0,
          highlightthickness=0,
          command=self.next,
          relief="flat"
      )
      self.button_6.place(
          x=539.0,
          y=626.0,
          width=183.0,
          height=49.0
      )

      self.button_image_7 = PhotoImage(
          file=lacn+"button_7.png")
      self.button_7 = Button(self.pw,
          image=self.button_image_7,
          borderwidth=0,
          highlightthickness=0,
          command=self.skip,
          relief="flat"
      )
      self.button_7.place(
          x=285.0,
          y=626.0,
          width=183.0,
          height=49.0
      )
      self.pw.resizable(False, False)
      
#-----------------------------------------------------
    global con,cursor
    con = connect(
        host="localhost",
        user="root",
        password="anuj1234",
        database="storerp_1"
        
    )

    # Create a cursor to execute SQL queries
    cursor = con.cursor()
    
    def dwn_month_data(self):
        try:
          # Calculate the start and end date for the previous month
          today = datetime.now()
          first_day_of_current_month = today.replace(day=1)
          last_day_of_previous_month = first_day_of_current_month - timedelta(days=1)
          first_day_of_previous_month = last_day_of_previous_month.replace(day=1)

          # SQL query to select data for the previous month only
          sql1 = "SELECT 'Order ID', 'Product','Quantity Ordered', 'Price Each', 'Order Date', 'Purchase Address' UNION SELECT order_id, description, quantity, unit_price, i_date, address INTO OUTFILE 'E:/Python/Storerp/StoreSalesData/PrevMonth/"
          # doc_name = "SalesRecord" + datetime.now().strftime("%Y-%m") + ".csv"

          # Get the name of the previous month
          previous_month_name = calendar.month_name[last_day_of_previous_month.month]

          # Format the document name
          doc_name = "SalesRecord_" + str(last_day_of_previous_month.year) + "_" + previous_month_name + ".csv"

          sql2 = f"' FIELDS TERMINATED BY ',' FROM invoice_2 WHERE i_date >= '{first_day_of_previous_month.strftime('%Y-%m-%d')}' AND i_date <= '{last_day_of_previous_month.strftime('%Y-%m-%d')}'"
          sql = sql1 + doc_name + sql2
          cursor.execute(sql)
          con.commit()
          showinfo("success", "File Downloaded")

          # Update the Entry widget with the file path
          self.mnth_path.delete(0, 'end')  # Clear the Entry widget
          self.mnth_path.insert(0, 'E:/Python/Storerp/StoreSalesData/AllData/' + doc_name)


        except Exception as e:
          print("Issue", e)
          messagebox.showerror("Issue", e)
    

    def process(self):
        try:
            # Find NAN
            path=self.added_path.get()
            all_data=pd.read_csv(path)
            all_data[all_data.isna().any(axis=1)]
            #display(nan_df.head())

            all_data = all_data.dropna(how='all')
            
            # Read the CSV file into a DataFrame
            df = all_data

            # Function to identify repeated column names
            def remove_repeated_columns(df):
                column_counts = df.columns.value_counts()
                repeated_columns = column_counts[column_counts > 1].index
                return df.drop(columns=repeated_columns)

            # Clean the DataFrame by removing repeated column names
            remove_repeated_columns(df)
            
            all_data = all_data[all_data['Order Date'].str[0:2]!='Or']  # Make columns correct type
            all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
            all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])
            all_data['Month'] = all_data['Order Date'].str[0:2]
            all_data['Month'] = all_data['Month'].astype('int32')
            all_data['Month 2'] = pd.to_datetime(all_data['Order Date']).dt.month

            # Save the processed data into a cleaned CSV file
            cleaned_file_path = "E:/Python/Storerp/StoreSalesData/Cleaned/cleaned_file.csv"
            all_data.to_csv(cleaned_file_path, index=False)

            # Show the path in the added_data entry field
            self.copy.delete(0, END)  # Clear any existing text
            self.copy.insert(0,cleaned_file_path )  # Set the file location


            messagebox.showinfo("Success", "Data processed and saved to cleaned CSV file")

        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)

    def add_data(self):
        try:
          # Specify the path to the main CSV file
            all_data_path = r"E:/Python/Storerp/StoreSalesData/AllData/all_data_check.csv"

            all_months_data = pd.DataFrame()
            all_months_data=pd.read_csv(all_data_path)

            # Specify the directory path containing previous month files
            directory_path = "E:/Python/Storerp/StoreSalesData/PrevMonth"

            files = [file for file in os.listdir(directory_path) if not file.startswith('.')] # Ignore hidden files

            # Append data from previous month files to the main DataFrame
            for file in files:
                current_data = pd.read_csv(os.path.join(directory_path, file))
                all_months_data = pd.concat([all_months_data, current_data])

            # Write the updated data to the main CSV file
            all_months_data.to_csv(all_data_path, index=False)

            # Remove the previous month files from the directory

            for file in files:
                os.remove(os.path.join(directory_path, file))

            # Show the path in the added_data entry field
            self.added_path.delete(0, END)  # Clear any existing text
            self.added_path.insert(0, all_data_path)  # Set the file location

            showinfo("Success", "Data appended and file updated")

        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)



    def copy_path(self):
        try:
            text = self.copy.get("1.0", "end-1c")  # Get text from the text field
            self.pw.clipboard_clear()  # Clear the clipboard
            self.pw.clipboard_append(text)  # Copy text to the clipboard
            messagebox.showinfo("Copy", "Text has been copied to the clipboard")
        except Exception as e:
            print("Issue", e)
            messagebox.showerror("Issue", e)



    def exit(self):
        win=Toplevel(self.pw)
        gui0.Page0(win)
        self.pw.withdraw()
        win.deiconify()
    def next(self):
        aw=Toplevel(self.pw)
        gui7.Page7(aw)
        self.pw.withdraw()
        aw.deiconify()
    def skip(self):
        aw=Toplevel(self.pw)
        gui7.Page7(aw)
        self.pw.withdraw()
        aw.deiconify()
        
    
def page():
    pw=Tk()
    Page8(pw)
    pw.mainloop()

if __name__ == '__main__':
    page()