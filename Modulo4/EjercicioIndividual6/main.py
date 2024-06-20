import json
import csv
import uuid


def create_csv():
    with open("employees.csv", "w", newline="") as employees_file:
        employee = csv.writer(employees_file)
        employee.writerow(["id_employee", "name", "username", "age", "phone", "password"])


def register_employees():

    employees = []

    id_employee = str(uuid.uuid1())
    name = input("Ingrese nombre del Empleado")
    username = input("Ingrese nombre de usuario del empleado")
    age = input("Ingrese la edad del empleado")
    phone = input("Ingrese el numero de telefono del empleado")
    password = input("Ingrese contraseña del empleado")

    with open("employees.csv", "a", newline="") as employees_file:
        employee = csv.writer(employees_file)
        employee.writerow([id_employee, name, username, age, phone, password])

    employees.append({"id": id_employee, "name": name, "username": username, "age": age, "phone": phone, "password": password})

    with open("employees.json", "w") as employees_file_json:
        json.dump(employees, employees_file_json)

    with open("employees.json", "r") as employees_file_json:
        employees = json.load(employees_file_json)

    for employee in employees:
        print("Informacion telefono y edad emplados")
        print(f"Age: {employee['age']}")
        print(f"Phone: {employee['phone']}")


create_csv()
register_employees()
