# TODO: Ask the user how many items will be calculated
input_count = (int(input("Enter a number")))
total = 0
for item in range(input_count):
    item_cost = (int(input("item cost")))  # Let the user enter a number
    item_count = (int(input("item count")))  # Let the user enter a number
    item_total = item_cost * item_count
    total+=item_total



# item_cost_1 = int(input("enter a number"))
# item_count_1 = int(input("enter a number"))
#
# item_cost_2 = int(input("enter a number"))
# item_count_2 = int(input("enter a number"))
#
# item_cost_3 = int(input("enter a number"))
# item_count_3 = int(input("enter a number"))
#
# total= item_cost_1 * item_count_1 + item_cost_2 * item_count_2 + (item_cost_3) * (item_count_3)
print(total)