import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
temperature_values = np.array([25, 28, 30, 32, 35, 38, 37, 36, 34, 30, 27, 25])
rainfall_values = np.array([50, 45, 60, 30, 20, 10, 5, 15, 25, 40, 55, 50])

# 1. Line Plot 
plt.figure(figsize=(8, 5))
plt.plot(months, temperature_values, marker='o', linestyle='-', color='red')
plt.title('Monthly Temperature Data - Line Plot')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# 2. Scatter Plot 
plt.figure(figsize=(8, 5))
plt.scatter(months, rainfall_values, color='blue', marker='o')
plt.title('Monthly Rainfall Data - Scatter Plot')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()
