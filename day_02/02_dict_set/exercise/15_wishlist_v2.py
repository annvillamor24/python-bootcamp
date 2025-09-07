# TODO: Fill in the details of the items you plan to buy
order = [

    {
        "Name": "laptop",
        "Brand": "apple",
        "Price": "50_000",
    },
    {
        "Name": "Guitar",
        "Brand": "Fender",
        "Price": "30_000",

    }
]




# TODO: Print the item details in the following format (for each order):
"""
Order:
	Name: item name
	Info: item info
	...
"""
for item in order:
    print("item:")
    # print("\tName:", item["Name"])
    # print("\tBrand:", item["Brand"])
    # print("\tPrice:", item["Price"])

    for key, value in item.items():
        print(key,value)