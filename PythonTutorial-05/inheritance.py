from class_method import Employee

class Engineer(Employee):
    def __init__(self, name, phone):
        super().__init__(name, phone)
        self.title = "Engineer"

    def display_self(self):
        print("#################################")
        print(f"Employee sequence: {self.seq}")
        print(f"name:  {self.name}, phone: {self.phone}, title: engineer")

eng1 = Engineer("Emma", "+886912425817")
eng2 = Engineer("Lily", "+886904318920")
eng1.display_self()
eng2.display_self()
Employee.display_count()