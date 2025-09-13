# def spend(expenses):
#     """TODO: Add a new cost in expenses"""
#     expense = int(input("Enter expense: "))
#     expenses.append(expense)
#     print("This is your expense")
#     print(f"Total expenses: {expense}")
#     print(expense)
#
# def refund(expenses):
#     """TODO: Remove the last cost added (if any)"""
#     refund_ = expenses.pop(-1)
#
#
# def show(expenses):
#     """TODO: Print the current list of expenses and total"""
#     print(f"Expenses: {expenses}")
#     print(f"Total: {sum(expenses)}")
#
# def main():
#     running = True
#     current_expenses = []
#
#     while running:
#         command = input("Command: ")
#         if command == "spend":
#             spend(current_expenses)
#         elif command == "refund":
#             refund(current_expenses)
#         elif command == "show":
#             show(current_expenses)
#         elif command == "exit":
#             running = False
#
# main()
class CostTracker:
   def __init__(self):
        self.expenses = []

   def spend(self, ):
       """TODO: Add a new cost in expenses"""
       expense = int(input("Enter expense: "))
       self.expenses.append(expense)
       print("This is your expense")
       print(f"Total expenses: {expense}")
       print(expense)

   def refund(self):
       """TODO: Remove the last cost added (if any)"""
       refund_ = self.expenses.pop(-1)

   def show(self):
       """TODO: Print the current list of expenses and total"""
       print(f"Expenses: {self.expenses}")
       print(f"Total: {sum(self.expenses)}")

   def mainloop(self):
       running = True

       while running:
           command = input("Command: ")
           if command == "spend":
               self.spend()
           elif command == "refund":
               self.spend()
           elif command == "show":
               self.spend()
           elif command == "exit":
               running = False

costtracker = CostTracker()
costtracker.mainloop()