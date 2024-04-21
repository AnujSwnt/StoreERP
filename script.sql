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


--LOAD DATA INFILE 'E:/Python/Storerp/StoreSalesData/SalesRecord2024-01-23-12-15-43.csv'
INTO TABLE invoice_2
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(order_id, description, quantity, unit_price, total, i_date, address)
SET name = NULL, gstin = NULL, phoneno = NULL;


LOAD DATA INFILE 'E:/Python/Storerp/StoreSalesData/EntryData.csv' INTO table invoice_2 FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' (order_id,name,description, quantity, unit_price, total, gstin,phoneno,address,i_date);
