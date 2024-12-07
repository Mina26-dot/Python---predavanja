
from pythonProject.school_diary_py.classes import Classes
from pythonProject.school_diary_py.grades import grades_table, Grades
from pythonProject.school_diary_py.students import Students
from pythonProject.school_diary_py.parents import Parents
from pythonProject.school_diary_py.subjects import subjects_table, Subjects
from pythonProject.school_diary_py.teachers import Teachers


def main():
    students = Students("students")
    parents = Parents("parents")
    classes = Classes("classes")
    subjects = Subjects("subjects")
    grades = Grades("grades")
    teachers = Teachers("teachers")

    # parents.insert_parent("Tanja", "Tanjic", "tanja@gmail.com")
    # classes.insert_class(3, "III/1")
    # students.insert_student("Danica", "Danic", 1, 1)
    # students.get_all_students()
    # students.get_by_id(1)
    # parents.get_by_id(1)
    classes.get_all()

    # Ispisivanje kao JSON
    #classes.delete_by_id(2)

if __name__ == "__main__":
    main()