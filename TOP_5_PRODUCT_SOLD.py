import pandas as pd


data = {
    'Product': ['Product A', 'Product B', 'Product C', 'Product A', 'Product B', 'Product D', 'Product A', 'Product C', 'Product B', 'Product E']
}
sales_data = pd.DataFrame(data)


top_5_products = sales_data['Product'].value_counts().head(5)
print("Top 5 products sold the most in the past month:")
print(top_5_products)
