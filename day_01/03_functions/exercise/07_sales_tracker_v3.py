def add(total):
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    total_item_cost = item_cost * item_count
    return total + total_item_cost


def sub(total):
    item_cost = int(input("Enter item cost: "))
    item_count = int(input("Enter item count: "))
    total_item_cost = item_cost * item_count
    return total - total_item_cost
def show(total):
    """TODO: Print total"""
    print(total)

def main():
    total = 0
    running = True
    while running:
        command = input("Provide command: ")
        if command == "add":
            total = add(total)
            print(total)
        if command == "sub":
            total = sub(total)
            print(total)
        elif command=="show":
            show(total)

        elif command == "exit":
            running = False


main()
