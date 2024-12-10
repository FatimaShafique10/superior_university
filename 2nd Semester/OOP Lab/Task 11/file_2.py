# file_operations.py
import csv
from file_1 import Manager, Worker # type: ignore

def append_employee_to_file(employee, file_name="employees.csv"):
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        if isinstance(employee, Manager):
            writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), employee.get_department(), "N/A"])
        elif isinstance(employee, Worker):
            writer.writerow([employee.get_name(), employee.get_age(), employee.get_salary(), "N/A", employee.get_hours_worked()])

def show_all_employees(file_name="employees.csv"):
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        for employee in reader:
            print(employee)

def modify_employee_details(name, updated_info, file_name="employees.csv"):
    all_rows = []
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        all_rows = list(reader)

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in all_rows:
            if row[0] == name:
                writer.writerow(updated_info)
            else:
                writer.writerow(row)

def remove_employee(name, file_name="employees.csv"):
    all_rows = []
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        all_rows = list(reader)

    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in all_rows:
            if row[0] != name:
                writer.writerow(row)
