# TODO: Fill in the details of the item you plan to buy
order = {
    "Name": "laptop",
    "Brand": "apple",
    "Price": "50,000",
}

# TODO: Print the item details in the following format:
"""
Order:
	Name: item name
	Info: item info
	...
"""

print(order["Name"])
print(order["Brand"])
print(order["Price"])
print(order.items())
for k, v in order.items():
    print(k, v)