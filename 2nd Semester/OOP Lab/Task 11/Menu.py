
from file_1 import Manager, Worker # type: ignore
from file_2 import append_employee_to_file, show_all_employees, modify_employee_details, remove_employee # type: ignore

def display_menu():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. Show All Employees")
        print("3. Update Employee Details")
        print("4. Remove Employee")
        print("5. Exit")
        user_choice = input("Enter your choice: ")

        if user_choice == '1':
            employee_type = input("Enter the type of employee (Manager/Worker): ").strip().lower()
            name = input("Enter the employee's name: ")
            age = int(input("Enter the employee's age: "))
            salary = float(input("Enter the employee's salary: "))

            if employee_type == "manager":
                department = input("Enter the department name: ")
                manager = Manager(name, age, salary, department)
                append_employee_to_file(manager)
            elif employee_type == "worker":
                hours_worked = int(input("Enter the number of hours worked: "))
                worker = Worker(name, age, salary, hours_worked)
                append_employee_to_file(worker)
            else:
                print("Invalid employee type entered.")

        elif user_choice == '2':
            show_all_employees()

        elif user_choice == '3':
            name_to_update = input("Enter the name of the employee to update: ")
            updated_employee_info = []
            updated_employee_info.append(input("Enter the new name: "))
            updated_employee_info.append(int(input("Enter the new age: ")))
            updated_employee_info.append(float(input("Enter the new salary: ")))
            updated_employee_info.append(input("Enter the new department (or 'N/A' if not applicable): "))
            modify_employee_details(name_to_update, updated_employee_info)

        elif user_choice == '4':
            name_to_delete = input("Enter the name of the employee to delete: ")
            remove_employee(name_to_delete)

        elif user_choice == '5':
            print("Exiting the system...")
            break

        else:
            print("Invalid choice. Please select a valid option.")
display_menu()