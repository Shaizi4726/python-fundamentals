import uuid


class Address:
    def __init__(self, street, city, country):
        self.street = street
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"


class Course:
    def __init__(self, course_name, course_code, credits):
        self.course_name = course_name
        self.course_code = course_code
        self.credits = credits

    def __str__(self):
        return f"{self.course_code}: {self.course_name} ({self.credits} credits)"


class Student:
    def __init__(self, name, address):
        if not isinstance(address, Address):
            raise ValueError(
                f"Addres must be an instance of Address.")
        self.name = name
        self.id = uuid.uuid4()
        self.address = address
        self.courses = []

    def enroll(self, course):
        if not isinstance(course, Course):
            raise ValueError(f"Course must be an instance of Course.")
        if any(c.course_code == course.course_code for c in self.courses):
            raise ValueError("Course already enrolled.")

        self.courses.append(course)

    def drop(self, course_code):
        for index, course in enumerate(self.courses):
            if course.course_code == course_code:
                del self.courses[index]
                break
        else:
            raise ValueError(
                f"Course {course_code} not in the enrolled courses.")

    def get_courses(self):
        return self.courses.copy()

    def __str__(self):
        return f"Name: {self.name}, Id: {self.id}, Address: {self.address}, Number of courses: {len(self.courses)}"


class GraduateStudent(Student):
    def __init__(self, name, address, thesis_topic):
        super().__init__(name, address)
        self.thesis_topic = thesis_topic

    def enroll(self, course):
        if len(self.courses) == 3:
            raise ValueError(
                "You cannot exceed the limit of maximum 3 courses at a time.")

        super().enroll(course)

    def __str__(self):
        return f"{super().__str__()}, Thesis Topic: {self.thesis_topic}"


def main():
    try:
        student = Student("Ali", Address(
            "Street 4", "Dubai", "United Arab Emirates"))

        student.enroll(Course("Computer Science", "CS50", 50))
        student.enroll(Course("Applied Physics", "AP30", 80))
        student.enroll(Course("Calculus", "C14", 76))
        student.enroll(Course("Analytical Geometery", "AG09", 69))
        print(student)
        student.drop("C1")
    except ValueError as e:
        print(e)

    try:
        grad_student = GraduateStudent("Shahzad", Address(
            "Street 5", "Dubai", "United Arab Emirates"), "Telecommunications")
        grad_student.enroll(Course("Computer Science", "CS50", 50))
        grad_student.enroll(Course("Object Oriented Programming", "OOP30", 80))
        grad_student.enroll(Course("Calculus", "C14", 76))
        grad_student.drop("C14")
        grad_student.enroll(Course("Analytical Geometery", "AG09", 69))
        grad_student_courses = grad_student.get_courses()

        print("Courses")
        for index, course in enumerate(grad_student_courses, start=1):
            print(f"{index}. {course}")
        grad_student.enroll(
            Course("Data Structures & Algorithms", "DSA101", 99))
    except ValueError as e:
        print(e)

    print(grad_student)


if __name__ == "__main__":
    main()
