# Создайте класс Employee, который инкапсулирующем следующие данные:

# Приватные поля __name, __position, __salary.
# Методы set_name, set_position и set_salary для изменения значений
# этих полей (например, при повышении сотрудника).
# Ограничьте прямой доступ к __salary, добавив проверку,
# чтобы зарплату можно было изменить только через метод, например,
# при повышении. Запрещается устанавливать зарплату ниже текущего значения.

# Метод get_employee_info, который возвращает информацию о сотруднике в
# виде строки.
class Employee:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def set_name(self, new_name):
        self.__name = new_name

    def set_position(self, new_position):
        self.__position = new_position

    def set_salary(self, new_salary, new_position):
        if self.__position == new_position:
            return f"Невозможно повысить зп, без повышения в должности"
        elif self.__salary >= new_salary:
            return f"Невозможно установить зп меньше текущей"
        else:
            self.__salary = new_salary
            self.set_position(new_position)
            return f"Зарплата повышена: {new_salary}"

    def get_employee_info(self):
        return f"name: {self.__name}, position: {self.__position}, salary: {self.__salary}"


if __name__ == "__main__":
    employee = Employee("Alex", "QA", 100_000)
    print(employee.get_employee_info())
    # employee.set_name("Victor")
    # employee.set_position("QA_Lead")
    print(employee.set_salary(600_000, "QA_lead"))
    print(employee.get_employee_info())
