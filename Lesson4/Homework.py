name = "Main Menu"
commands = {
    1: "create",
    2: "manage",
    0: "end"
}


students = []
teachers = []
homeroom_teachers = []


class Student:
    def __init__(self, firstname, lastname, classname):
        self.firstname = firstname
        self.lastname = lastname
        self.classname = classname

class Teacher:
    def __init__(self, firstname, lastname, subject, classes):
        self.firstname = firstname
        self.lastname = lastname
        self.subject = subject
        self.classes = classes

class HomeroomTeacher:
    def __init__(self, firstname, lastname, classname):
        self.firstname = firstname
        self.lastname = lastname
        self.classname = classname


def main ():
    while True:
        print("\n--- Main Menu ---")
        for number, label in commands.items():
            print(f"{number}: {label}")

        try:
            choice = int(input("> "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            create_user()
        elif choice == 2:
            manage()
        elif choice == 0:
            print("Exiting program...")
            break
        else:
            print("Invalid input!")


def create_user():
    create_menu = {
        1: "student",
        2: "teacher",
        3: "homeroom teacher",
        0: "end"
    }

    while True:
        print("\n--- Create User---")
        for k, v in create_menu.items():
            print(f"{k}: {v}")

        try:
            choice = int(input(">"))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            print("Create student")
            firstname = input("Enter first name:")
            lastname = input("Enter last name:")
            classname = input("Enter class name:")
            students.append(Student(firstname, lastname, classname))
            print("Student created!")

        elif choice == 2:
            print("Create teacher")
            firstname = input("Enter first name:")
            lastname = input("Enter last name:")
            subject = input("Enter subject:")


            classes = []
            print("Enter classes (empty line to stop):")
            while True:
                c = input("> ")
                if c == "":
                    break
                classes.append(c)
            teachers.append(Teacher(firstname, lastname, subject, classes))
            print("Teacher created!")



        elif choice == 3:
            print("Create Homeroom Teacher")
            firstname = input("Enter first name:")
            lastname = input("Enter last name:")
            classname = input("Enter class name:")

            homeroom_teachers.append(HomeroomTeacher(firstname, lastname, classname))
            print("Homeroom Teacher created!")

        elif choice == 0:
            break
        else:
            print("Invalid input!")

def manage():
    manage_menu = {
        1: "class",
        2: "student",
        3: "teacher",
        4: "homeroom teacher",
        0: "end"
    }

    while True:
        print("\n---Manage---")
        for k, v in manage_menu.items():
            print(f"{k}: {v}")

        try:
            choice = int(input("> "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            manage_class()
        elif choice == 2:
            manage_student(students)
        elif choice == 3:
            manage_teacher(teachers)
        elif choice == 4:
            manage_homeroom_teacher(homeroom_teachers)
        elif choice == 0:
            break
        else:
            print("Invalid input!")

def manage_class():
    classname = input("Enter class name: ")

    class_students = [s for s in students if s.classname == classname]

    print(f"\nStudents in class {classname}:")
    if class_students:
        for s in class_students:
            print(f"- {s.firstname} {s.lastname}")
    else:
        print("No students found in this class.")


    class_ht = [ht for ht in homeroom_teachers if ht.classname == classname]

    print("\nHomeroom teacher:")
    if class_ht:
        for ht in class_ht:
            print(f"- {ht.firstname} {ht.lastname}")
    else:
        print("No homeroom teacher found.")


def manage_student(student):
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")

    student_list = [s for s in students if s.firstname == firstname and s.lastname == lastname]

    try:
        student = student_list[0]
        print(f"\n{student.firstname} {student.lastname} attends class {student.classname}")
    except IndexError:
        print("Student not found")

    class_teachers = [t for t in teachers if student.classname in t.classes]

    print("\nTeachers:")
    if class_teachers:
        for t in class_teachers:
            print(f"{t.firstname} {t.lastname} - {t.subject}")
    else:
        print("No teachers found for this student.")

def manage_teacher(teachers):
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")

    teacher_list = [t for t in teachers if t.firstname == firstname and t.lastname == lastname]

    try:
        teacher = teacher_list[0]
        print(f"\n{teacher.firstname} {teacher.lastname} teaches classes:")
        for cls in teacher.classes:
            print(f"- {cls}")
    except IndexError:
        print("Teacher not found.")

def manage_homeroom_teacher(homeroom_teachers):
    firstname = input("Enter first name: ")
    lastname = input("Enter last name: ")

    ht_list = [ht for ht in homeroom_teachers if ht.firstname == firstname and ht.lastname == lastname]

    try:
        ht = ht_list[0]
        class_students = [s for s in students if s.classname == ht.classname]
        print(f"\nHomeroom Teacher {ht.firstname} {ht.lastname} leads class {ht.classname} with students:")

        if class_students:
            for s in class_students:
                print(f"- {s.firstname} {s.lastname}")
        else:
            print("No students found in this class.")
    except IndexError:
            print("Homeroom teacher not found.")


def start_program():
    print("Welcome to the School Database!")
    input("Press Enter to continue...")
    main()

start_program()




