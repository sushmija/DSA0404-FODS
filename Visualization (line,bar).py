import matplotlib.pyplot as plt
import numpy as np

# Sample data (replace this with your actual monthly sales data)
months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
sales_values = np.array([10000, 12000, 8000, 15000, 11000])

# a. Line Plot
plt.figure(figsize=(8, 5))
plt.plot(months, sales_values, marker='o', linestyle='-')
plt.title('Monthly Sales Data - Line Plot')
plt.xlabel('Month')
plt.ylabel('Sales Value')
plt.grid(True)
plt.show()

# b. Bar Plot
plt.figure(figsize=(8, 5))
plt.bar(months, sales_values, color='blue')
plt.title('Monthly Sales Data - Bar Plot')
plt.xlabel('Month')
plt.ylabel('Sales Value')
plt.grid(axis='y')
plt.show()
