import pandas as pd

# Step 2: Load the sales data into a DataFrame
# Assuming your DataFrame is named 'sales_data'
# You can replace this with the actual variable name or read the data from a CSV/Excel file

# Example DataFrame creation (replace this with your actual data)
data = {'Product': ['A', 'B', 'A', 'C', 'B'],
        'Price': [10.0, 15.0, 10.0, 5.0, 15.0],
        'Quantity': [2, 1, 3, 4, 2]}

sales_data = pd.DataFrame(data)

# Step 3: Create a new column 'Total Sales'
sales_data['Total Sales'] = sales_data['Price'] * sales_data['Quantity']

# Step 4: Display or save the updated DataFrame
print("Updated Sales Data:")
print(sales_data)

# If you want to save the updated DataFrame to a new CSV file
# sales_data.to_csv('updated_sales_data.csv', index=False)
