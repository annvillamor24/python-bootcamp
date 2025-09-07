def add(inventory, item):
    """TODO: Add a new item (dict) to the inventory (list[dict])"""
    inventory.append(item)

def remove(inventory, index):
    """TODO: Remove item (dict) in the given index (int) of inventory"""
    inventory.pop(index)

def read(inventory, index):
    """TODO: Return the item (dict) in the given index (int) of inventory"""
    return inventory[index]

def show(inventory):
    """TODO: Print the items and their details line-by-line"""
    for item in inventory:
        print(f"Name: {item['Name']}, Brand: {item['Brand']}, Price: {item['Price']}")

def main():
    running = True
    inventory = []

    while running:
        command = input("Command: ")
        if command == "add":
            name = input("Name: ")
            brand = input("Brand: ")
            price = input("Price: ")

            item = {'Name': name, 'Brand': brand, 'Price': price}
            add(inventory, item)


            # TODO: Use add command"""
            pass
        elif command == "remove":
            #  TODO: Use remove command"""
            index = input("Index: ")
            remove(inventory, int(index))
            pass
        elif command == "read":
            # TODO: Use read command"""
            index = input("Index: ")
            print(read(inventory, int(index)))
            pass
        elif command == "show":
            # TODO: Use show command"""
            show(inventory)

            pass
        elif command == "exit":
            running = False


main()
