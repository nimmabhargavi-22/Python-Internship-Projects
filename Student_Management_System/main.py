import json
import os

FILE_NAME = "students.json"


def load_students():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            print("Student ID Already Exists!")
            return

    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    students.append({
        "id": sid,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    })

    save_students(students)
    print("Student Added Successfully")


def view_students(students):
    if len(students) == 0:
        print("No Records Found")
        return

    print("\n------------------------------------------------")
    print("ID\tNAME\tAGE\tCOURSE\tMARKS")
    print("------------------------------------------------")

    for student in students:
        print(
            f"{student['id']}\t"
            f"{student['name']}\t"
            f"{student['age']}\t"
            f"{student['course']}\t"
            f"{student['marks']}"
        )


def search_student(students):
    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            print("\nStudent Found")
            print("ID :", student["id"])
            print("Name :", student["name"])
            print("Age :", student["age"])
            print("Course :", student["course"])
            print("Marks :", student["marks"])
            return

    print("Student Not Found")


def update_student(students):
    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:

            student["name"] = input("New Name: ")
            student["age"] = int(input("New Age: "))
            student["course"] = input("New Course: ")
            student["marks"] = float(input("New Marks: "))

            save_students(students)

            print("Student Updated Successfully")
            return

    print("Student Not Found")


def delete_student(students):
    sid = input("Enter Student ID: ")

    for student in students:
        if student["id"] == sid:
            students.remove(student)

            save_students(students)

            print("Student Deleted Successfully")
            return

    print("Student Not Found")


students = load_students()

while True:

    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        update_student(students)

    elif choice == "5":
        delete_student(students)

    elif choice == "6":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
        
