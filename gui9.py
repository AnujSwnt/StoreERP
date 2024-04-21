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
import gui7,gui0
from statsmodels.tsa.seasonal import seasonal_decompose
from pmdarima import auto_arima
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.metrics import mean_squared_error
from statsmodels.tools.eval_measures import rmse

warnings.filterwarnings("ignore", category=FutureWarning)
f=("Arial",18, "bold")

class Page9:
    def __init__(self,prw):
        self.prw = prw
        self.prw.geometry("1350x800+100+0")
        self.prw.configure(bg = "#FFFFFF")
        lacn="E:/Python/Storerp/assets/frame9/"


        self.canvas = Canvas(
            self.prw,
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
        self.Entry = self.canvas.create_image(
            675.0,
            46.0,
            image=self.image_image_1
        )
        self.path = Entry(self.prw,
          bd=0,
          bg="#D9D9D9",
          fg="#000716",font=f,
          highlightthickness=0)
        self.path.place(
          x=327.0,
          y=115.0,
          width=390.0,
          height=40.0
      )
        self.accuracy=Entry(self.prw,
          bd=0,
          bg="#D9D9D9",
          fg="#000716",font=f,
          highlightthickness=0)
        self.accuracy.place(
          x=938, y=471, width=255, height=42
      )
        self.pred_val=ScrolledText(self.prw,bd=0,
          bg="#D9D9D9",
          fg="#000716",font=f,
          highlightthickness=0)
        self.pred_val.place(x=854, y=539, width=444, height=135)

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
        self.button_1 = Button(self.prw,
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
            1063.0,
            278.0,
            image=self.image_image_3
        )

        # self.image_image_4 = PhotoImage(
        #     file=lacn+"image_4.png")
        # self.image_4 = self.canvas.create_image(
        #     1063.0,
        #     565.0,
        #     image=self.image_image_4
        # )

        self.image_image_5 = PhotoImage(
            file=lacn+"image_5.png")
        self.image_5 = self.canvas.create_image(
            410.0,
            454.0,
            image=self.image_image_5
        )

        # self.image_image_6 = PhotoImage(
        #     file=lacn+"image_6.png")
        # self.image_6 = self.canvas.create_image(
        #     1062.0,
        #     279.0,
        #     image=self.image_image_6
        # )

        self.canvas.create_rectangle(
            327.0,
            115.0,
            717.0,
            155.0,
            fill="#D9D9D9",
            outline="")

        self.image_image_7 = PhotoImage(
            file=lacn+"image_7.png")
        self.image_7 = self.canvas.create_image(
            106.0,
            164.0,
            image=self.image_image_7
        )

        self.canvas.create_text(
            247.0,
            124.0,
            anchor="nw",
            text="File:",
            fill="#000000",
            font=("Orbitron Bold", 24 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=lacn+"button_2.png")
        self.button_2 = Button(self.prw,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.predict,
            relief="flat"
        )
        self.button_2.place(
            x=424.0,
            y=178.0,
            width=196.0,
            height=48.0
        )
        self.prw.resizable(False, False)
    
#----------------------------------------------------------------------------------------------
        self.present_time()
    
    def exit(self):
        win=Toplevel()
        gui0.Page0(win)
        self.prw.withdraw()
        win.deiconify()

    def present_time(self):
        try:
            dt=datetime.now()
            display_time=dt.strftime("%I:%M:%S %p")
            self.canvas.itemconfig(tagOrId=self.TIME,text=display_time)
            self.prw.after(200,self.present_time)

            display_date=dt.strftime("%d/%m/%Y")
            self.canvas.itemconfig(tagOrId=self.DATE,text=display_date)
            
        except Exception as e:
            print("Issue",e)


    def predict(self):
        try:
            path = "E:/Python/Storerp/Test_data/all_data_exe1.csv"
            all_data = pd.read_csv(path)
            nan_df = all_data[all_data.isna().any(axis=1)]
            all_data = all_data.dropna(how='all')
            all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']
            all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
            all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])
            all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
            all_data['Month'] = all_data['Order Date'].dt.month

            all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])
            all_data['Month'] = all_data['Order Date'].dt.to_period('M')
            all_data['Total Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
            monthly_sales_summary = all_data.groupby('Month')['Total Sales'].agg(['max', 'min', 'mean', 'sum'])
            monthly_sales_summary.columns = ['Max Sale', 'Min Sale', 'Average Sale', 'Total Sale']
            print(monthly_sales_summary)

            current_data = {
                'Max Sale': list(monthly_sales_summary['Max Sale']),
                'Min Sale': list(monthly_sales_summary['Min Sale']),
                'Average Sale': list(monthly_sales_summary['Average Sale']),
                'Total Sale': list(monthly_sales_summary['Total Sale'])
            }

            # Print the length and contents of current_data
            print("Length of current_data:", len(current_data))
            print("Contents of current_data:", current_data)

            # Generate the index based on the length of current_data
            current_index = pd.date_range(start='2023-01', periods=len(current_data['Max Sale']), freq='MS')


            # Print the length and contents of current_index
            print("Length of current_index:", len(current_index))
            print("Contents of current_index:", current_index)
            monthly_sales_summary = pd.DataFrame(current_data, index=current_index)

            previous_data = current_data.copy()
            for key in previous_data:
                previous_data[key] = [value * 0.99 for value in previous_data[key]]

            previous_index = pd.date_range(start='2022-01', periods=len(previous_data['Max Sale']), freq='MS')

            previous_sales_summary = pd.DataFrame(previous_data, index=previous_index)

            combined_sales_summary = pd.concat([previous_sales_summary, monthly_sales_summary])
            print(combined_sales_summary)

            combined_sales_summary = combined_sales_summary.round(2)
            combined_sales_summary.reset_index(inplace=True)
            combined_sales_summary.rename(columns={'index': 'Month'}, inplace=True)
            combined_sales_summary['Month'] = combined_sales_summary['Month'].dt.to_period('M').astype(str)

            combined_sales_summary = combined_sales_summary.set_index('Month')
            monthly_sales_summary = combined_sales_summary

            import matplotlib.pyplot as plt
            # Convert index to datetime object
            monthly_sales_summary.index = pd.to_datetime(monthly_sales_summary.index)

            # Convert Period index to string or timestamp
            monthly_sales_summary.index = monthly_sales_summary.index.strftime('%Y-%m')


            monthly_sales_summary.reset_index(inplace=True)
            monthly_avg_sales = monthly_sales_summary[['Month', 'Average Sale']]
            monthly_avg_sales.set_index('Month', inplace=True)
            #monthly_avg_sales.index = [str(idx) for idx in monthly_avg_sales.index]   # Convert Period index to string
            print(monthly_avg_sales)
            # Convert index to DatetimeIndex
            monthly_avg_sales.index = pd.to_datetime(monthly_avg_sales.index)

            import warnings
            warnings.filterwarnings("ignore")
            stepwise_fit = auto_arima(monthly_avg_sales['Average Sale'], start_p=1, start_q=1, max_p=3, max_q=3, m=6,
                                    start_P=0, seasonal=True, d=None, D=1, trace=True, error_action='ignore',
                                    suppress_warnings=True, stepwise=True)
            stepwise_fit.summary()

            train = monthly_avg_sales.iloc[:len(monthly_avg_sales) - 15]
            test = monthly_avg_sales.iloc[len(monthly_avg_sales) - 15:]
            from statsmodels.tsa.statespace.sarimax import SARIMAX
            model = SARIMAX(train['Average Sale'], order=(0, 0, 0), seasonal_order=(0, 1, 0, 6))
            result = model.fit()
            result.summary()
            start = len(train)
            end = len(train) + len(test) - 1

            # Predictions for one-year against the test set
            predictions = result.predict(start, end,
                                        typ = 'levels').rename("Predictions")

            # Train the model on the full dataset
            model = model = SARIMAX(monthly_avg_sales['Average Sale'],
                        order = (0, 0, 0),
                        seasonal_order =(0, 1, 0, 6))
            result = model.fit()
            forecast = result.predict(start=len(monthly_avg_sales), end=(len(monthly_avg_sales) - 1) + 1 * 12,typ='levels').rename('Forecast')

            # Create a plot
            fig, ax = plt.subplots(figsize=(12, 5))
            monthly_avg_sales['Average Sale'].plot(ax=ax, legend=True)
            forecast.plot(ax=ax, legend=True)

            # Configure plot layout
            ax.set_xlabel('Month')
            ax.set_ylabel('Average Sale')
            ax.set_title('Forecasted Average Sale')

            # Embed the plot in the Tkinter window
            canvas = FigureCanvasTkAgg(fig, master=self.prw)  # A tk.DrawingArea.
            canvas.draw()
            canvas.get_tk_widget().place(x=32, y=235, height=439, width=756)
            

            rmse_value = rmse(predictions, test['Average Sale'])
            # Calculate accuracy
            accuracy_arima = 100 - (rmse_value / test['Average Sale'].mean()) * 100
            accuracy_arima = round(accuracy_arima, 2)
            print(accuracy_arima)

            accuracy_text="Accuracy: "+str(accuracy_arima)+" %"
            # Show the path in the added_data entry field
            self.accuracy.delete(0, END)  # Clear any existing text
            self.accuracy.insert(0, accuracy_text)

            from statsmodels.tsa.arima.model import ARIMA
            df=monthly_avg_sales
            model2=ARIMA(df['Average Sale'],order=(0,0,0))
            model2=model2.fit()
            index_future_dates=pd.date_range(start='2023-12-30',end='2024-1-30')
            #print(index_future_dates)
            pred=model2.predict(start=len(df),end=len(df)+31,typ='levels').rename('ARIMA Predictions')
            #print(comp_pred)
            pred.index=index_future_dates
            print(pred)
            str_pred=str(pred)
            self.pred_val.delete(1.0, END)  # Clear any existing text
            self.pred_val.insert(END, str_pred)




            last_six_months_sales = monthly_avg_sales[-6:]

            # Create a new figure for the fill-in graph
            fig_fill_in, ax_fill_in = plt.subplots(figsize=(25, 20))

            # Plot original sales data for the last six months as a line chart
            ax_fill_in.plot(last_six_months_sales.index, last_six_months_sales['Average Sale'], label='Original Sales', color='blue')

            # Plot predicted values for the next six months as a line chart
            ax_fill_in.plot(pred.index, pred, label='Predicted Sales', linestyle='--', color='orange')

            # Plot confidence intervals for predicted sales
            # (Add confidence intervals if available, assuming you have them)
            # Set the confidence level (e.g., 95% confidence)
            import numpy as np
            from scipy import stats


            confidence_level = 0.95
            # Calculate standard errors (replace this with the actual standard errors from your model)
            pred = model2.predict(start=len(df), end=len(df) + 6, typ='levels').rename('ARIMA Predictions')
            std_errors = model2.get_prediction(start=len(df), end=len(df) + 6).se_mean

            # Calculate critical value from the standard normal distribution
            z = np.abs(stats.norm.ppf((1 - confidence_level) / 2))

            # Calculate lower and upper bounds for the confidence intervals
            lower_confidence_interval = pred - z * std_errors
            upper_confidence_interval = pred + z * std_errors
            ax_fill_in.fill_between(pred.index, lower_confidence_interval, upper_confidence_interval, color='orange', alpha=0.2)

            # Set labels and title
            ax_fill_in.set_xlabel('Date')
            ax_fill_in.set_ylabel('Average Sale')
            ax_fill_in.set_title('Original vs. Predicted Sales for Next 6 Months')
            ax_fill_in.legend()

            # Embed the fill-in graph plot in the tkinter window
            canvas_fill_in = FigureCanvasTkAgg(fig_fill_in, master=self.prw)
            canvas_fill_in.draw()
            canvas_fill_in.get_tk_widget().place(x=854, y=130, width=416, height=268)


           


        except Exception as e:
            print("Issue",e)
    
    


def page():
    prw=Tk()
    Page9(prw)
    prw.mainloop()

if __name__ == '__main__':
    page()