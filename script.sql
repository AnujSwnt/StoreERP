--drop database if exists storerp_1;
--create database if not exists storerp_1;
--use storerp_1;
--create table if not exists invoice_1(order_id int not null,name varchar(40),description varchar(40),quantity decimal(10,2),unit_price decimal(10,2),total decimal(10,2),gstin varchar(20),phoneno int(10),address varchar(100));
--create table if not exists customer_1(customer_id int auto_increment not null,order_id int auto_increment not null,name varchar(40),gstin varchar(20),phoneno int(10),address varchar(100),primary key(customer_id,order_id));

-- create table if not exists stock_1(product_id int primary key not null,p_name varchar(40),quantity decimal(10,2),p_price decimal(10,2),total decimal(100,3) generated always as (quantity*p_price));
-- create table if not exists stock_2(product_id int primary key not null,p_name varchar(40),quantity decimal(10,2),p_price decimal(10,2),total decimal(100,3) generated always as (quantity*p_price));

--ALTER TABLE invoice_1 ADD COLUMN i_date DATE DEFAULT CURRENT_DATE;
--ALTER TABLE invoice_1 ADD COLUMN i_date VARCHAR(10) CHECK (YourDateColumn LIKE '[0-3][0-9]/[0-1][0-9]/[0-9][0-9][0-9][0-9]');

--create table if not exists invoice_2(order_id int not null,name varchar(40),description varchar(40),quantity decimal(10,2),unit_price decimal(10,2),total decimal(10,2),gstin varchar(20),phoneno int(10),address varchar(100),i_date date);


--global products,prices_list
--products=['AA Batteries (4-pack)','AAA Batteries (4-pack)','USB-C Charging Cable','Lightning Charging Cable','Wired Headphones','Apple Airpods Headphones','Bose SoundSport Headphones','27in FHD Monitor','27in 4K Gaming Monitor','iPhone','34in Ultrawide Monitor','Google Phone','Flatscreen TV','Macbook Pro Laptop','ThinkPad Laptop','20in Monitor','Vareebadd Phone','LG Washing Machine','LG Dryer']
--prices_list = {'AA Batteries (4-pack)': 5.99,'AAA Batteries (4-pack)': 6.99,'USB-C Charging Cable': 12.99,'Lightning Charging Cable': 14.99,'Wired Headphones': 24.99,'Apple Airpods Headphones': 149.99,'Bose SoundSport Headphones': 89.99,'27in FHD Monitor': 199.99,'27in 4K Gaming Monitor': 399.99,'iPhone': 699.99,'34in Ultrawide Monitor': 499.99,'Google Phone': 599.99,'Flatscreen TV': 299.99,'Macbook Pro Laptop': 1299.99,'ThinkPad Laptop': 999.99,'20in Monitor': 129.99,'Vareebadd Phone': 499.99,'LG Washing Machine': 799.99,'LG Dryer': 699.99}
   
--sql="SELECT 'OrderId', 'Description', 'Quantity', 'Unit_Price', 'Total', 'Date', 'Address' UNION SELECT order_id, description, quantity, unit_price, total, i_date, address INTO OUTFILE 'E:/Python/Storerp/StoreSalesData/frst.csv' FIELDS TERMINATED BY ',' FROM invoice_2;"


---write a XGBoost python program to predict sales on given data fields and plot a line chart at end Order ID,	Product	Quantity ,	Price Each	,Order Date,	Purchase Address.



--# Import necessary libraries
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the dataset (assuming you have a CSV file named 'sales_data.csv')
data = pd.read_csv('sales_data.csv')

# Feature engineering: Convert 'Order Date' to datetime and create new features if needed
data['Order Date'] = pd.to_datetime(data['Order Date'])
data['Month'] = data['Order Date'].dt.month
data['Day'] = data['Order Date'].dt.day

# Select features and target variable
features = ['Quantity', 'Price Each', 'Month', 'Day']
target = 'Sales'

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data[features], data[target], test_size=0.2, random_state=42)

# Create XGBoost regressor
xg_reg = xgb.XGBRegressor(objective ='reg:squarederror', colsample_bytree = 0.3, learning_rate = 0.1,
                max_depth = 5, alpha = 10, n_estimators = 100)

# Fit the model
xg_reg.fit(X_train, y_train)

# Predict on the test set
y_pred = xg_reg.predict(X_test)

# Evaluate the model
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(f"Root Mean Squared Error: {rmse}")

# Plotting the predicted vs actual sales
plt.figure(figsize=(10, 6))
plt.plot(y_test.reset_index(drop=True), label='Actual Sales', linestyle='--', marker='o')
plt.plot(pd.Series(y_pred), label='Predicted Sales', linestyle='--', marker='o')
plt.xlabel('Test Samples')
plt.ylabel('Sales')
plt.title('Actual vs Predicted Sales')
plt.legend()
plt.show()


INSERT INTO stock_2 (product_id, p_name) SELECT product_id, p_name FROM stock_1;
