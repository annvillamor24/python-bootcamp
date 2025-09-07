items = ["rice", "noodles", "toyo", "spam", "coffee"]
item_to_find = "spam"

for item in items:
    # TODO: If item equals the item_to_find, print and exit loop
    print(item)
    if item_to_find==item:
        break
if item_to_find in items:
    print(item)
#note

#try to find
if item_to_find in items:
    print("Item found")
else:
    print('Item not found')