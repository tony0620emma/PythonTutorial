
class Employee:
    """Base class for employees"""

    employee_count = 0
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        Employee.employee_count += 1
        self.seq = Employee.employee_count

    def work(self, start, hours):
        print(f"{self.name} starts to work at {start} for {hours}")

    # This can make the method call-able without instances
    @classmethod
    def display_count(self):
        print(f"We currently have {self.employee_count} employees")

    def display_self(self):
        print("=================================")
        print(f"Employee sequence: {self.seq}")
        print(f"name:  {self.name}, phone: {self.phone}")

Employee.display_count()
employee1 = Employee("Tony", "+886912425817")
employee2 = Employee("Adam", "+886904318920")
employee1.display_self()
employee2.display_self()
Employee.display_count()
