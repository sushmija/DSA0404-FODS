import numpy as np
item_prices=np.array([120.5,250.75,90.00])
item_quantities = np.array([2, 3, 4])
discount_rate = 10  
tax_rate = 8      
subtotal = np.sum(item_prices * item_quantities)
discount_amount = (subtotal * discount_rate / 100)
discounted_subtotal = subtotal - discount_amount
tax_amount = (discounted_subtotal * tax_rate / 100)
total_cost = discounted_subtotal + tax_amount
print("Total cost for the customer: Rs.", total_cost)
