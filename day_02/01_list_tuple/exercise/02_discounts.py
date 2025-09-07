prices = [10_000, 20, 3_000, 3, 2, 1_000]

# TODO: Change the first, third, and last values to half the price
indices=[0,2,-1]
for index in indices:
    prices[index]=prices[index]/2
# Show the changed list
print(prices)
