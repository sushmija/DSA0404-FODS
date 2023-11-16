import pandas as pd
from datetime import datetime


data = {
    'Customer ID': [1, 2, 1, 3, 2, 1, 3, 3],
    'order date': ['2023-01-05', '2023-02-10', '2023-01-15', '2023-03-20', '2023-02-28', '2023-01-20', '2023-04-12', '2023-05-03'],
    'product name': ['Product A', 'Product B', 'Product A', 'Product C', 'Product B', 'Product A', 'Product C', 'Product A'],
    'order quantity': [5, 7, 3, 2, 4, 6, 3, 8]
}


data['order date'] = pd.to_datetime(data['order date'])


order_data = pd.DataFrame(data)


print("Sample Order Data:")
print(order_data)
print("\n")


orders_per_customer = order_data.groupby('Customer ID')['order date'].count()
print("Total number of orders made by each customer:\n", orders_per_customer)
print("\n")


average_order_quantity_per_product = order_data.groupby('product name')['order quantity'].mean()
print("Average order quantity for each product:\n", average_order_quantity_per_product)
print("\n")


earliest_order_date = order_data['order date'].min()
latest_order_date = order_data['order date'].max()
print("Earliest Order Date:", earliest_order_date)
print("Latest Order Date:", latest_order_date)
