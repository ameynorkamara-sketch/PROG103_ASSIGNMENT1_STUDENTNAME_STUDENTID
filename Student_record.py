# ============================================================
# PROG103 - Principles of Structured Programming
# Assignment 1: Student Record Management System (SRMS)
# SDG Alignment: SDG 4 - Quality Education
# ============================================================

# Constant for pass mark
PASS_MARK = 50

# Global list to store student records
students = []


# -------------------------------------------------------
# FUNCTION 1: Add a new student record
# -------------------------------------------------------
def add_student():
    print("\n--- Add New Student ---")
    name = input("Enter student name: ").strip()
    student_id = input("Enter student ID: ").strip()

    # Validate that scores are numbers
    scores = []
    subjects = ["Math", "English", "Science", "ICT", "Social Studies"]
    for subject in subjects:
        while True:
            try:
                score = float(input(f"Enter score for {subject} (0-100): "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("  Score must be between 0 and 100. Try again.")
            except ValueError:
                print("  Invalid input. Please enter a number.")

    # Create a student dictionary
    student = {
        "name": name,
        "id": student_id,
        "scores": scores,
        "subjects": subjects
    }

    students.append(student)
    print(f"\n✓ Student '{name}' added successfully!")


# -------------------------------------------------------
# FUNCTION 2: Calculate average and grade
# -------------------------------------------------------
def calculate_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# -------------------------------------------------------
# FUNCTION 3: Display all student records
# -------------------------------------------------------
def display_all_students():
    print("\n--- All Student Records ---")
    if len(students) == 0:
        print("No student records found.")
        return

    print(f"{'No.':<5} {'Name':<20} {'ID':<12} {'Average':<10} {'Grade':<8} {'Status'}")
    print("-" * 65)

    for i, student in enumerate(students):
        average = sum(student["scores"]) / len(student["scores"])
        grade = calculate_grade(average)
        status = "PASS" if average >= PASS_MARK else "FAIL"
        print(f"{i + 1:<5} {student['name']:<20} {student['id']:<12} {average:<10.2f} {grade:<8} {status}")


# -------------------------------------------------------
# FUNCTION 4: View a single student's full report
# -------------------------------------------------------
def view_student_report():
    print("\n--- View Student Report ---")
    if len(students) == 0:
        print("No student records found.")
        return

    student_id = input("Enter student ID to search: ").strip()
    found = False

    for student in students:
        if student["id"] == student_id:
            found = True
            average = sum(student["scores"]) / len(student["scores"])
            grade = calculate_grade(average)
            status = "PASS" if average >= PASS_MARK else "FAIL"

            print("\n" + "=" * 40)
            print(f"  STUDENT REPORT")
            print("=" * 40)
            print(f"  Name     : {student['name']}")
            print(f"  ID       : {student['id']}")
            print("-" * 40)
            print(f"  {'Subject':<20} {'Score'}")
            print("-" * 40)

            for j in range(len(student["subjects"])):
                subject = student["subjects"][j]
                score = student["scores"][j]
                sub_status = "Pass" if score >= PASS_MARK else "Fail"
                print(f"  {subject:<20} {score:.1f}  ({sub_status})")

            print("-" * 40)
            print(f"  Average  : {average:.2f}")
            print(f"  Grade    : {grade}")
            print(f"  Status   : {status}")
            print("=" * 40)
            break

    if not found:
        print(f"No student found with ID '{student_id}'.")


# -------------------------------------------------------
# FUNCTION 5: Delete a student record
# -------------------------------------------------------
def delete_student():
    print("\n--- Delete Student Record ---")
    if len(students) == 0:
        print("No student records found.")
        return

    student_id = input("Enter student ID to delete: ").strip()
    for i, student in enumerate(students):
        if student["id"] == student_id:
            confirm = input(f"Are you sure you want to delete '{student['name']}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                students.pop(i)
                print("✓ Record deleted successfully.")
            else:
                print("Deletion cancelled.")
            return

    print(f"No student found with ID '{student_id}'.")


# -------------------------------------------------------
# FUNCTION 6: Display class summary statistics
# -------------------------------------------------------
def class_summary():
    print("\n--- Class Summary ---")
    if len(students) == 0:
        print("No student records found.")
        return

    total_students = len(students)
    passing = 0
    failing = 0
    all_averages = []

    for student in students:
        average = sum(student["scores"]) / len(student["scores"])
        all_averages.append(average)
        if average >= PASS_MARK:
            passing += 1
        else:
            failing += 1

    class_average = sum(all_averages) / len(all_averages)
    highest = max(all_averages)
    lowest = min(all_averages)

    print(f"\n  Total Students  : {total_students}")
    print(f"  Passing         : {passing}")
    print(f"  Failing         : {failing}")
    print(f"  Class Average   : {class_average:.2f}")
    print(f"  Highest Average : {highest:.2f}")
    print(f"  Lowest Average  : {lowest:.2f}")


# -------------------------------------------------------
# MAIN MENU - Entry point of the program
# -------------------------------------------------------
def main():
    print("=" * 50)
    print("  STUDENT RESULT MANAGEMENT TERMINAL SYSTEM")
    print("  PROG103 | Limkokwing University - SL")
    print("  SDG 4: Quality Education")
    print("=" * 50)

    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add Student Record")
        print("2. View All Students")
        print("3. View Student Report")
        print("4. Delete Student Record")
        print("5. Class Summary")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all_students()
        elif choice == "3":
            view_student_report()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            class_summary()
        elif choice == "6":
            print("\nThank you for using SRMS. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")


# Run the program
main()