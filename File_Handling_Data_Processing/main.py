import csv


def read_employees():
    employees = []

    try:
        with open("employees.csv", "r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                employees.append(row)

    except FileNotFoundError:
        print("Error: employees.csv file not found")

    except PermissionError:
        print("Error: Permission denied")

    return employees


def display_employees(employees):

    print("\n========== EMPLOYEE RECORDS ==========")

    if len(employees) == 0:
        print("No Records Found")
        return

    for emp in employees:

        print(f"ID         : {emp['ID']}")
        print(f"Name       : {emp['Name']}")
        print(f"Department : {emp['Department']}")
        print(f"Salary     : {emp['Salary']}")
        print("-" * 40)


def filter_it_employees(employees):

    print("\n========== IT EMPLOYEES ==========")

    found = False

    for emp in employees:

        if emp["Department"].strip().upper() == "IT":

            print(
                f"{emp['Name']} - ₹{emp['Salary']}"
            )

            found = True

    if not found:
        print("No IT Employees Found")


def sort_by_salary(employees):

    print("\n========== SORTED BY SALARY ==========")

    sorted_employees = sorted(
        employees,
        key=lambda x: int(x["Salary"]),
        reverse=True
    )

    for emp in sorted_employees:

        print(
            f"{emp['Name']} - ₹{emp['Salary']}"
        )


def generate_report(employees):

    total_salary = 0

    for emp in employees:
        total_salary += int(emp["Salary"])

    average_salary = total_salary / len(employees)

    with open("report.txt", "w") as file:

        file.write("EMPLOYEE REPORT\n")
        file.write("========================\n")
        file.write(
            f"Total Employees : {len(employees)}\n"
        )
        file.write(
            f"Total Salary : {total_salary}\n"
        )
        file.write(
            f"Average Salary : {average_salary}\n"
        )

    print("\nReport Generated Successfully")
    print("report.txt created")


employees = read_employees()

while True:

    print("\n========== FILE HANDLING SYSTEM ==========")
    print("1. Display Employees")
    print("2. Filter IT Employees")
    print("3. Sort By Salary")
    print("4. Generate Report")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        display_employees(employees)

    elif choice == "2":

        filter_it_employees(employees)

    elif choice == "3":

        sort_by_salary(employees)

    elif choice == "4":

        generate_report(employees)

    elif choice == "5":

        print("Thank You")
        break

    else:

        print("Invalid Choice")
