 # E-Commerce-Data-Analytics

You can clone the project using 
```
git clone https://github.com/Dharshana16/E-cart.git
```

## This project works on python 3.10
## If you want to install virtual environment 
```python
python3 -m venv venv
source venv/bin/activate
```
## To deactivate virtual environement 
```
deactivate
```

## To install the required libraries 
```
pip install -r requirements.txt
```

## Install postgres and setup your database 
### The table schemas are at 
```schemas/```
### To create a table using python you should import the schema in create_db.py and run it.

<img src="assets/screenshot1.png">

### Repeat this for every table you need to create

## In the database.py file change the username password and the dbname

<img src="assets/screenshot2.png">

## Add the dataset file in your database using
```
psql -d [databasename] -U [username] -f [schema.sql]
```

## Start the server using uvicorn
```
uvicorn main:app --reload --log-config logging.conf
```
## Make sure you are in virtual environment.
## You can see the swagger UI at
>http://127.0.0.1:8000/docs

## There are 7 APIs in the repo 

```customer/{id}```
### This provides customer details when given a customer id (cust_1234)

```unique/customer```
### Unique customers in January who came back every month over the entire year in 2011

``` product/details/{product_category}```
### This provides the list of product under the given category

```/maxorder/{first}/{off_set}```
### This provides the customer who had the most purchases from the given offset

```/order/{id}```
### This provides the order details when an order id is given (Ord_123)

```/sales```
### This gives the sales made by each product

```/product ```
### This gives the profit made by each product
