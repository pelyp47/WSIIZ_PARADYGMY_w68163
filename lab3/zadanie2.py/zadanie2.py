import json
import os

class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Pracownik: {self.name}, Wiek: {self.age}, Wynagrodzenie: {self.salary:.2f}"

    def to_dict(self):
        return {
            "name": self.name,
            "age": self.age,
            "salary": self.salary
        }

    @staticmethod
    def from_dict(data):
        return Employee(data["name"], data["age"], data["salary"])


class EmployeesManager:
    def __init__(self, filename="employees.json"):
        current_directory = os.path.dirname(__file__)
        self.filename = os.path.join(current_directory, filename)
        self.employees = self.load_employees()

    def load_employees(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r', encoding='utf-8') as file:
                data = json.load(file)
                return [Employee.from_dict(emp) for emp in data]
        return []

    def save_employees(self):
        with open(self.filename, 'w', encoding='utf-8') as file:
            data = [emp.to_dict() for emp in self.employees]
            json.dump(data, file, ensure_ascii=False, indent=4)

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
        self.save_employees()
        print(f"Dodano pracownika: {employee.name}")

    def display_employees(self):
        if not self.employees:
            print("Brak pracowników do wyświetlenia.")
        else:
            for employee in self.employees:
                print(employee)

    def remove_employees_by_age_range(self, min_age: int, max_age: int):
        initial_count = len(self.employees)
        self.employees = [e for e in self.employees if not (min_age <= e.age <= max_age)]
        removed_count = initial_count - len(self.employees)
        self.save_employees()
        print(f"Usunięto {removed_count} pracowników w wieku od {min_age} do {max_age} lat.")

    def find_employee_by_name(self, name: str):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None

    def update_salary_by_name(self, name: str, new_salary: float):
        employee = self.find_employee_by_name(name)
        if employee:
            old_salary = employee.salary
            employee.salary = new_salary
            self.save_employees()
            print(f"Zaktualizowano wynagrodzenie {name} z {old_salary:.2f} na {new_salary:.2f}.")
        else:
            print(f"Nie znaleziono pracownika o imieniu i nazwisku: {name}.")


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def login(self):
        username = input("Podaj nazwę użytkownika: ")
        password = input("Podaj hasło: ")
        if username == "admin" and password == "admin":
            print("Zalogowano pomyślnie!")
        else:
            print("Nieprawidłowe dane logowania!")
            return False
        return True

    def show_menu(self):
        if not self.login():
            return

        while True:
            print("\n--- System Zarządzania Pracownikami ---")
            print("1. Dodaj nowego pracownika")
            print("2. Wyświetl listę pracowników")
            print("3. Usuń pracowników w określonym przedziale wiekowym")
            print("4. Zaktualizuj wynagrodzenie pracownika")
            print("5. Wyjście")

            choice = input("Wybierz opcję: ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.manager.display_employees()
            elif choice == "3":
                self.remove_employees_by_age_range()
            elif choice == "4":
                self.update_salary()
            elif choice == "5":
                print("Wyjście z programu.")
                break
            else:
                print("Nieprawidłowy wybór. Spróbuj ponownie.")

    def add_employee(self):
        name = input("Podaj imię i nazwisko: ")
        age = self.get_valid_int("Podaj wiek: ")
        salary = self.get_valid_float("Podaj wynagrodzenie: ")
        employee = Employee(name, age, salary)
        self.manager.add_employee(employee)

    def remove_employees_by_age_range(self):
        min_age = self.get_valid_int("Podaj minimalny wiek: ")
        max_age = self.get_valid_int("Podaj maksymalny wiek: ")
        self.manager.remove_employees_by_age_range(min_age, max_age)

    def update_salary(self):
        name = input("Podaj imię i nazwisko pracownika: ")
        new_salary = self.get_valid_float("Podaj nowe wynagrodzenie: ")
        self.manager.update_salary_by_name(name, new_salary)

    def get_valid_int(self, prompt: str):
        while True:
            try:
                value = int(input(prompt))
                return value
            except ValueError:
                print("Wprowadź poprawną liczbę całkowitą.")

    def get_valid_float(self, prompt: str):
        while True:
            try:
                value = float(input(prompt))
                return value
            except ValueError:
                print("Wprowadź poprawną liczbę zmiennoprzecinkową.")


if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.show_menu()