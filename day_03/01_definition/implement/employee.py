class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created) created with id {self.id}")

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Added work {task} to {self.name}")


employee1 = Employee("Mary", "123")
employee2 = Employee("Ann", "234")
print(employee1.name)

employee1.add_task("Create slides")
print(employee1.tasks)

