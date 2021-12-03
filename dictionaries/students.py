# This script aims to display students data


chaine_etudiants = "213615200;BESNIER;JEAN;213565488;DUPOND;MARC"

DATA_NUMBER_FOR_EACH_STUDENT = 3

students_grades = {"Tarik": [11, 12, 13], "Karl": [11, 12, 13]}


def transform_students_string_to_dic(string_to_transform):
    students: list = string_to_transform.split(";")
    return {students[i * DATA_NUMBER_FOR_EACH_STUDENT]: students[i * DATA_NUMBER_FOR_EACH_STUDENT + 1]
            + " " + students[i * DATA_NUMBER_FOR_EACH_STUDENT + 2]
            for i in range(0, len(students) // DATA_NUMBER_FOR_EACH_STUDENT)}


def get_student_average_grade(student_name):
    student_average = sum(students_grades[student_name]) // len(students_grades[student_name])
    return student_average


def get_best_student():
    best_average = max(get_student_average_grade(name) for name in students_grades.keys())
    best_student = {name: best_average
                    for name in students_grades.keys()
                    if get_student_average_grade(name) == best_average}
    return best_student


def main():
    print(transform_students_string_to_dic(chaine_etudiants))

    print(get_best_student())


if __name__ == '__main__':
    main()
