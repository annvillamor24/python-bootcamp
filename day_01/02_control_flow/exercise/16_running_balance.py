total = 0
running = True
while running:
    command = input("Provide command: ")

    if command == "add":

        pass  # TODO: Ask for number, add to total, and print
        number=int(input())
        total+=number
        print(total)
    if command == "sub":
        number=int(input())
        total-=number
        print(total)
        pass  # TODO: Ask for number, subtract to total, and print
    elif command == "exit":
        running = False
