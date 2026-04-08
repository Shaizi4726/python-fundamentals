def show_menu():
    print("\nStudents' Grades Menu:")
    print("1. Add student with list of grades")
    print("2. Remove student by name")
    print("3. Add new grade to an existing student")
    print("4. View all students")
    print("5. View the top performer student")
    print("6. View the lowest performer student")
    print("7. Exit the application\n")


def get_average(grades):
    average = 0 if not grades else (sum(grades) / len(grades))
    return average


def get_student_averages(student_grades):
    return {name: get_average(grades) for name, grades in student_grades.items()}


def main():
    student_grades = {}

    while True:
        show_menu()

        choice = input("What do you want to perform? (1-7): ")

        match choice:
            case '1':
                name = input("Enter the student name: ")

                if name in student_grades:
                    print(f"The student '{name}' already exists.")
                else:
                    while True:
                        grades_string = input(
                            "Enter grades (space-separated): ")
                        try:
                            grades = list(map(int, grades_string.split()))
                            student_grades[name] = grades
                            break
                        except ValueError:
                            print("Enter valid integer grades.")

            case '2':
                name = input("Enter the student name to be removed: ")

                if name in student_grades:
                    student_grades.pop(name)
                    print(f"Student '{name}' removed.")
                else:
                    print(f"Student '{name}' not found.")

            case '3':
                name = input("Enter the student name: ")
                if name in student_grades:
                    while True:
                        try:
                            grade = int(input("Enter the grade to add: "))
                        except ValueError:
                            print("Enter a valid grade.")
                        else:
                            student_grades[name].append(grade)
                            break

                else:
                    print(f"Student '{name}' not found.")

            case '4':
                for name, grades in student_grades.items():
                    average = get_average(grades)
                    match average:
                        case x if x >= 90:
                            letter = 'A'

                        case x if x >= 80:
                            letter = 'B'

                        case x if x >= 70:
                            letter = 'C'

                        case x if x >= 60:
                            letter = 'D'

                        case _:
                            letter = 'F'

                    print(
                        f"{name:<15} Grades: {grades} Avg: {round(average, 2):>6} Grade: {letter}")
            case '5':
                if not student_grades:
                    print("No students available.")
                else:
                    student_averages = get_student_averages(student_grades)
                    name, average = max(student_averages.items(),
                                        key=lambda item: item[1])
                    print("Top performer is:")
                    print(
                        f"Name: {name:<15} Average: {round(average, 2):>6}")

            case '6':
                if not student_grades:
                    print("No students available.")
                else:
                    student_averages = get_student_averages(student_grades)

                    name, average = min(student_averages.items(),
                                        key=lambda item: item[1])

                    print("Bottom performer is:")
                    print(
                        f"Name: {name:<15} Average: {round(average, 2):>6}")
            case '7':
                break
            case _:
                print("Invalid choice. Please enter the number (1-7)")


if __name__ == "__main__":
    main()
