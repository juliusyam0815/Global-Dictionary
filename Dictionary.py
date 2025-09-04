import csv

# ===== Global Dictionary to Store Students =====
students = {}  # { student_id: { "info": (id, name), "age": int, "grades": [list] } }


# ===== Helper Functions =====
def calculate_average(grades):
    # Lambda function to calculate average
    return (lambda g: sum(g) / len(g) if g else 0)(grades)


def display_tuple_operations(sid, name):
    student_tuple = (sid, name)
    print("Tuple:", student_tuple)
    print("Length:", len(student_tuple))
    print("Max element:", max(student_tuple))
    print("Min element:", min(student_tuple))


# ===== CRUD Operations =====
def add_student(sid, name, age, grades):
    if sid in students:
        print("Student already exists.")
        return
    students[sid] = {"info": (sid, name), "age": age, "grades": grades}
    print("✅ Student added successfully.")
    display_tuple_operations(sid, name)


def update_student(sid):
    if sid not in students:
        print("Student not found.")
        return
    name = input("Enter new name: ")
    age = int(input("Enter new age: "))
    grades = input("Enter new grades (space separated): ").split()
    grades = [int(g) for g in grades]
    students[sid] = {"info": (sid, name), "age": age, "grades": grades}
    print("✅ Student updated.")


def delete_student(sid):
    if sid in students:
        del students[sid]
        print("✅ Student deleted.")
    else:
        print("Student not found.")


def display_students():
    if not students:
        print("⚠ No students available.")
        return

    print("\n===== All Students =====")
    for sid, data in students.items():
        name = data["info"][1]
        age = data["age"]
        grades = data["grades"]

        print(f"ID: {sid}, Name: {name}, Age: {age}, Grades: {grades}")
        print("Grades (looped):", end=" ")
        for g in grades:  # Nested loop example
            print(g, end=" ")
        print("\nAverage:", calculate_average(grades))
    print("=========================\n")

    # Dictionary methods demo
    print("All Keys:", students.keys())
    print("All Values:", students.values())
    print("All Items:", students.items())


# ===== File Handling =====
def save_to_file(filename="students.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        for sid, data in students.items():
            row = [sid, data["info"][1], data["age"]] + data["grades"]
            writer.writerow(row)
    print("✅ Data saved to file.")


def load_from_file(filename="students.csv"):
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            for row in reader:
                sid = row[0]
                name = row[1]
                age = int(row[2])
                grades = [int(g) for g in row[3:]]
                students[sid] = {"info": (sid, name), "age": age, "grades": grades}
        print("✅ Data loaded from file.")
    except FileNotFoundError:
        print("⚠ No file found. Starting fresh.")


# ===== Scope Demonstration =====
global_message = "Global Variable Example"


def scope_demo():
    local_message = "Local Variable Example"
    print("Inside function:", local_message)
    print("Accessing global:", global_message)


# ===== Main Menu =====
def main():
    load_from_file()  # Load at program start

    while True:
        print("""
===== Student Information System =====
1. Add Student
2. Display Students
3. Update Student
4. Delete Student
5. Save to File
6. Load from File
7. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            grades = input("Enter grades separated by space: ").split()
            grades = [int(g) for g in grades]
            add_student(sid, name, age, grades)

        elif choice == "2":
            display_students()

        elif choice == "3":
            sid = input("Enter Student ID to update: ")
            update_student(sid)

        elif choice == "4":
            sid = input("Enter Student ID to delete: ")
            delete_student(sid)

        elif choice == "5":
            save_to_file()

        elif choice == "6":
            load_from_file()

        elif choice == "7":
            print("👋 Exiting program... Goodbye!")
            break  # break demo

        else:
            print("⚠ Invalid choice, try again.")
            continue  # continue demo


# ===== Run Program =====
if __name__ == "__main__":
    main()
