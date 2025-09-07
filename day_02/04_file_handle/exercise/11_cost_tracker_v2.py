def spend(expenses):
    """TODO: Add a new cost in expenses"""
    expense = int(input("Enter expense: "))
    expenses.append(expense)
    print("This is your expense", expense)

    print(f"Total expenses: {sum(expenses)}")


def refund(expenses):
    """TODO: Remove the last cost added (if any)"""
    refund_ = expenses.pop(-1)

def show(expenses):
    """TODO: Print the current list of expenses and total"""
    print(f"Expenses: {expenses}")
    print(f"Total: {sum(expenses)}")

def load(expenses):
    loaded_expenses = []
    with open("expenses.txt","r") as file:
        file_content = file.readlines()
        for line in file_content:
            number = float(line.replace("\n",""))
            loaded_expenses.append(number)
    expenses.extend(loaded_expenses)
            
"""TODO: Save the current list of expenses to a new file"""
def save(expenses):

    with open("test.txt", "w") as file:
        for expense in expenses:
            file.write(str(expense) + "\n")


running = True
current_expenses = []

def main():
    running = True
    current_expenses = []

    while running:
        command = input("Command: ")
        if command == "spend":
            spend(current_expenses)
        if command == "refund":
            refund(current_expenses)
        if command == "show":
            show(current_expenses)
        if command == "save":
            save(current_expenses)
        if command == "load":
            load(current_expenses)
main()
# with open("test.txt","r") as file:
#     file.contents = file.read()
exit()