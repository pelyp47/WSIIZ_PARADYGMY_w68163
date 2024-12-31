class Employee:
    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary
        
    #(to co będzie pokazywało się pry print)
    def __str__(self):
        return f"Pracownik: {self.name}, Wiek: {self.age}, Wynagrodzenie: {self.salary:.2f}"


class EmployeesManager:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee: Employee):
        self.employees.append(employee)
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
            print(f"Zaktualizowano wynagrodzenie {name} z {old_salary:.2f} na {new_salary:.2f}.")
        else:
            print(f"Nie znaleziono pracownika o imieniu i nazwisku: {name}.")


class FrontendManager:
    def __init__(self):
        self.manager = EmployeesManager()

    def show_menu(self):
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
        age = int(input("Podaj wiek: "))
        salary = float(input("Podaj wynagrodzenie: "))
        employee = Employee(name, age, salary)
        self.manager.add_employee(employee)

    def remove_employees_by_age_range(self):
        min_age = int(input("Podaj minimalny wiek: "))
        max_age = int(input("Podaj maksymalny wiek: "))
        self.manager.remove_employees_by_age_range(min_age, max_age)

    def update_salary(self):
        name = input("Podaj imię i nazwisko pracownika: ")
        new_salary = float(input("Podaj nowe wynagrodzenie: "))
        self.manager.update_salary_by_name(name, new_salary)


if __name__ == "__main__":
    frontend = FrontendManager()
    frontend.show_menu()
