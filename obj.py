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

# import gui2

# # class Page01:
# #     def __init__(self,lg):
# #         self.lg=lg
    
    
# #     # global products,prices_list
# #     products=['AA Batteries (4-pack)','AAA Batteries (4-pack)','USB-C Charging Cable','Lightning Charging Cable','Wired Headphones','Apple Airpods Headphones','Bose SoundSport Headphones','27in FHD Monitor','27in 4K Gaming Monitor','iPhone','34in Ultrawide Monitor','Google Phone','Flatscreen TV','Macbook Pro Laptop','ThinkPad Laptop','20in Monitor','Vareebadd Phone','LG Washing Machine','LG Dryer']
# #     prices_list = {'AA Batteries (4-pack)': 5.99,'AAA Batteries (4-pack)': 6.99,'USB-C Charging Cable': 12.99,'Lightning Charging Cable': 14.99,'Wired Headphones': 24.99,'Apple Airpods Headphones': 149.99,'Bose SoundSport Headphones': 89.99,'27in FHD Monitor': 199.99,'27in 4K Gaming Monitor': 399.99,'iPhone': 699.99,'34in Ultrawide Monitor': 499.99,'Google Phone': 599.99,'Flatscreen TV': 299.99,'Macbook Pro Laptop': 1299.99,'ThinkPad Laptop': 999.99,'20in Monitor': 129.99,'Vareebadd Phone': 499.99,'LG Washing Machine': 799.99,'LG Dryer': 699.99}
# #     def update_lists(self):
# #         prod_desc=gui2.Page2.__init__.ap_lab_proddesc.get()
# #         unitpr=gui2.Page2.add_product.id3
# #         self.products.append(prod_desc)
# #         self.new_pricelist={'prod_desc':unitpr}
# #         self.prices_list.update(self.new_pricelist)



# # if __name__ == '__main__':
# #     gui2.page()


# products=['AA Batteries (4-pack)','AAA Batteries (4-pack)','USB-C Charging Cable','Lightning Charging Cable','Wired Headphones','Apple Airpods Headphones','Bose SoundSport Headphones','27in FHD Monitor','27in 4K Gaming Monitor','iPhone','34in Ultrawide Monitor','Google Phone','Flatscreen TV','Macbook Pro Laptop','ThinkPad Laptop','20in Monitor','Vareebadd Phone','LG Washing Machine','LG Dryer']
# prices_list = {'AA Batteries (4-pack)': 5.99,'AAA Batteries (4-pack)': 6.99,'USB-C Charging Cable': 12.99,'Lightning Charging Cable': 14.99,'Wired Headphones': 24.99,'Apple Airpods Headphones': 149.99,'Bose SoundSport Headphones': 89.99,'27in FHD Monitor': 199.99,'27in 4K Gaming Monitor': 399.99,'iPhone': 699.99,'34in Ultrawide Monitor': 499.99,'Google Phone': 599.99,'Flatscreen TV': 299.99,'Macbook Pro Laptop': 1299.99,'ThinkPad Laptop': 999.99,'20in Monitor': 129.99,'Vareebadd Phone': 499.99,'LG Washing Machine': 799.99,'LG Dryer': 699.99}


#-----------------------------------------------------------------------------------------------------------------------------------------

# import matplotlib.pyplot as plt
# import mysql.connector
# from mysql.connector import Error

# # Function to create a connection to MySQL
# def create_connection(host, user, password, database):
#     try:
#         connection = mysql.connector.connect(
#             host=host,
#             user=user,
#             password=password,
#             database=database
#         )
#         if connection.is_connected():
#             print(f"Connected to MySQL database: {database}")
#             return connection
#     except Error as e:
#         print(f"Error: {e}")
#         return None

# # Function to execute an SQL query and fetch results
# def execute_query(connection, query):
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         result = cursor.fetchall()
#         return result
#     except Error as e:
#         print(f"Error executing query: {e}")
#         return None
#     finally:
#         cursor.close()

# # Function to plot a pie chart
# def plot_pie_chart(labels, sizes):
#     plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
#     plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#     plt.title('Distribution of Quantities by Product')
#     plt.show()

# if __name__ == "__main__":
#     # Modify these parameters with your MySQL connection details
#     db_host = "localhost"
#     db_user = "root"
#     db_password = "anuj1234"
#     db_database = "storerp_1"

#     # SQL query to select product names and quantities
#     sql_query = "SELECT p_name,quantity FROM stock_1;"

#     # Create a connection to MySQL
#     connection = create_connection(db_host, db_user, db_password, db_database)

#     if connection:
#         # Execute the query
#         result = execute_query(connection, sql_query)

#         if result:
#             # Extract data from the result
#             product_names = [row[0] for row in result]
#             quantities = [row[1] for row in result]

#             # Plot a pie chart
#             plot_pie_chart(product_names, quantities)

#         # Close the MySQL connection
#         connection.close()


# sql1 = "SELECT 'OrderId', 'Description', 'Quantity', 'Unit_Price', 'Total', 'Date', 'Address' UNION SELECT order_id, description, quantity, unit_price, total, i_date, address INTO OUTFILE 'E:/Python/Storerp/StoreSalesData/"
# doc_name = "SalesRecord" + datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".csv"
# sql2 = "' FIELDS TERMINATED BY ',' FROM invoice_2"
# sql = sql1 + doc_name + sql2
# print(sql)
