import pandas as pd
from pmdarima import auto_arima
from statsmodels.tsa.statespace.sarimax import SARIMAX
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def predict():
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

    # Plot the forecast values

    # #  Create a plot
    # fig, ax = plt.subplots(figsize=(12, 5))
    # monthly_avg_sales['Average Sale'].plot(ax=ax, legend=True)
    # forecast.plot(ax=ax, legend=True)

    # # Fill between plot for forecast
    # ax.fill_between(forecast.index, forecast, color='skyblue', alpha=0.4)

    # # Configure plot layout
    # ax.set_xlabel('Month')
    # ax.set_ylabel('Average Sale')
    # ax.set_title('Forecasted Average Sale')

    # Embed the plot in the Tkinter window
    root = tk.Tk()
    root.geometry("900x700")
    canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    # Run the Tkinter event loop
    root.mainloop()

# Call the predict function
predict()

