class Employee:
    """Class representation for employee data"""

    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.tasks = []
        print(f"Employee {self.name} created with ID {self.id}")

    def add_work(self, task):
        print(f"Added work {task} to {self.name}")
        return self.tasks.append(task)

class recuiter(Employee):
    def recruit(self, task):
        print(f"Recruited {task} to {self.name}")

employee1 = recuiter(name='John', id=1)
employee1.recruit('Task 1')
print(employee1.tasks)

class Developer(Employee):
    def code(self, task):
        print(f"Developer code {task} to {self.name}")

class Manager(Employee):
    def manage(self, task):
        print(f"Manager {task} to {self.name}")
