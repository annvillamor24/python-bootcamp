# Ask the user for an input
user_input = input("Enter number: ")

# TODO: Remove extra spaces
# TODO: Remove commas
clean = user_input.strip()
clean = clean.replace("", "")
words = clean.split()
clean = "".join(words)
print(clean)

# TODO: If user enters a valid number
user_input = int(user_input)
print(user_input + 1)

# TODO: Else
print("Please enter a valid number!")
