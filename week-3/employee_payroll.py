from abc import ABC, abstractmethod
import uuid


class Employee(ABC):
    def __init__(self, name, department):
        self.name = name
        self.employee_id = uuid.uuid4()
        self.department = department

    @abstractmethod
    def calculate_pay(self):
        pass

    @abstractmethod
    def employment_type(self):
        pass

    def display_info(self):
        emp_pay = self.calculate_pay()
        emp_type = self.employment_type()

        print(f"\n{'=' * 30} Employee Info {'=' * 30}\n")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")
        print(f"Pay: {emp_pay}")
        print(f"Type: {emp_type}")

    def __str__(self):
        return f"Employee(Name: {self.name}, Department: {self.department})"


class FullTimeEmployee(Employee):
    EMPLOYMENT_TYPE = "Full-Time"

    def __init__(self, name, department, annual_salary):
        if annual_salary <= 0:
            raise ValueError("Annual salary must be greater than 0.")
        super().__init__(name, department)
        self.annual_salary = annual_salary

    def calculate_pay(self):
        return round((self.annual_salary / 12), 2)

    def employment_type(self):
        return self.EMPLOYMENT_TYPE


class PartTimeEmployee(Employee):
    EMPLOYMENT_TYPE = "Part-Time"

    def __init__(self, name, department, hourly_rate, hours_worked):
        if hourly_rate <= 0 or hours_worked <= 0:
            raise ValueError(
                "Hourly Rate and Hours Worked must be greater than 0.")
        super().__init__(name, department)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_pay(self):
        return round((self.hourly_rate * self.hours_worked), 2)

    def employment_type(self):
        return self.EMPLOYMENT_TYPE


class ContractEmployee(Employee):
    EMPLOYMENT_TYPE = "Contract"

    def __init__(self, name, department, contract_amount, contract_duration_months):
        if contract_amount <= 0 or contract_duration_months <= 0:
            raise ValueError(
                "Contract Amount and Contract Duration Months must be greater than 0.")
        super().__init__(name, department)
        self.contract_amount = contract_amount
        self.contract_duration_months = contract_duration_months

    def calculate_pay(self):
        return round((self.contract_amount / self.contract_duration_months), 2)

    def employment_type(self):
        return self.EMPLOYMENT_TYPE


class PayrollSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        if not isinstance(employee, Employee):
            raise TypeError(f"{employee} is not of type Employee.")

        for emp in self.employees:
            if emp.employee_id == employee.employee_id:
                raise ValueError(
                    "The employee is already added to the payroll system.")

        self.employees.append(employee)
        print(f"Employee {employee.name} added.")

    def remove_employee(self, employee_id):
        if not self.employees:
            raise ValueError(
                f"The Employee with Employee Id {employee_id} does not exist in the payroll system.")

        for index, emp in enumerate(self.employees):
            if emp.employee_id == employee_id:
                del self.employees[index]
                print(f"Employee {emp.name} removed.")
                break
        else:
            raise ValueError(
                f"The Employee with Employee Id {employee_id} does not exist in the payroll system.")

    def process_payroll(self):
        if not self.employees:
            print("No employee added to the payroll system.")
        else:
            print(f"\n{'=' * 30} Payroll Process {'=' * 30}\n")
            print(f"{'S.No':<4} {'Name':<30} {'Department':<15} Pay")
            for index, employee in enumerate(self.employees, start=1):
                print(
                    f"{index:<4} {employee.name:<30} {employee.department:<15} {employee.calculate_pay():.2f} AED")

    def get_department_report(self, department):
        if not self.employees:
            print("No employee added to the payroll system.")
        else:
            rank = 1
            found = any(emp.department == department for emp in self.employees)

            if not found:
                print(f"No employees found in department {department}")
                return

            print(f"\n{'=' * 30} Department Report ({department}) {'=' * 30}\n")
            print(f"{'S.No':<4} {'Name':<30} Pay")
            for employee in self.employees:
                if (employee.department == department):
                    print(
                        f"{rank:<4} {employee.name:<30} {employee.calculate_pay():.2f} AED")
                    rank += 1

    def total_payroll_cost(self):
        return round(sum(emp.calculate_pay() for emp in self.employees), 2)


def main():
    print("=" * 80)
    print("Employee Instance Test")
    print(f"{'=' * 80}\n")

    try:
        emp = Employee("Kamran Khan", "Chief Executive Officer")
    except TypeError as e:
        print(e)

    # Full-Time Employees
    emp_full_1 = FullTimeEmployee("Faisal", "Engineering", 47459)
    emp_full_2 = FullTimeEmployee("Sana", "Design", 31640)

    # Part-Time Employees
    emp_part_1 = PartTimeEmployee("Bilal", "Technology", 30, 160)
    emp_part_2 = PartTimeEmployee("Mariam", "Marketing", 24, 145)
    emp_part_3 = PartTimeEmployee("Hamza", "Product", 28, 155)

    # Contract Employees
    emp_contract_1 = ContractEmployee("Zainab", "Engineering", 90000, 6)
    emp_contract_2 = ContractEmployee("Usman", "Sales", 140000, 12)
    emp_contract_3 = ContractEmployee("Hira", "Operations", 45000, 3)

    # Payroll System
    payroll = PayrollSystem()

    print(f"\n{'=' * 80}")
    print("Employee Addition Test")
    print(f"{'=' * 80}\n")

    try:
        payroll.add_employee(emp_full_1)
        payroll.add_employee(emp_full_2)
        payroll.add_employee(emp_part_1)
        payroll.add_employee(emp_part_2)
        payroll.add_employee(emp_part_3)
        payroll.add_employee(emp_contract_1)
        payroll.add_employee(emp_contract_2)
        payroll.add_employee(emp_contract_3)
        payroll.add_employee(emp_contract_3)
    except ValueError as e:
        print(e)

    print(f"\n{'=' * 80}")
    print("Process Payroll Test")
    print(f"{'=' * 80}\n")

    payroll.process_payroll()

    print(f"\n{'=' * 80}")
    print("Department Report Test")
    print(f"{'=' * 80}\n")

    payroll.get_department_report("Engineering")

    print(f"\n{'=' * 80}")
    print("Total Payroll Cost Test")
    print(f"{'=' * 80}\n")

    cost = payroll.total_payroll_cost()
    print(f"Total Payroll Cost: {cost:.2f} AED")

    print(f"\n{'=' * 80}")
    print("Non Employee Addition Test")
    print(f"{'=' * 80}\n")

    try:
        payroll.add_employee("Saba")
    except TypeError as e:
        print(e)


if __name__ == "__main__":
    main()
