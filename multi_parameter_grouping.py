"""
Sample Algorithm to group students based on multiple parameters.
- group students into a specified number of groups
- as much as possible, ensure even distribution based on gender, grade, specialization, and nationality
"""

import operator
from itertools import groupby


class Student:
    def __init__(self, name, grade, gender, specialisation, foreigner=0):
        self.name = name
        self.grade = grade
        self.gender = gender
        self.foreigner = foreigner
        self.specialisation = specialisation

    def __repr__(self):
        return repr((self.gender, self.grade, self.foreigner, self.specialisation, self.name))


students = [
    Student("sam", 4, "male", "Nurse", 1),
    Student("David", 1, "male", "Eng", 0),
    Student("Tunde", 1, "female", "Nurse", 0),
    Student("Ayomide", 1, "male", "med(surg)", 1),
    Student("Tutu", 2, "male", "med(lab)", 0),
    Student("Tope", 4, "female", "med(surg)", 0),
    Student("Daudu", 3, "male", "med(surg)", 1),
    Student("Tonto", 4, "male", "Eng", 0),
    Student("Mariam", 2, "female", "Law", 1),
    Student("Sunday", 3, "male", "med(lab)", 0),
    Student("Mary", 2, "female", "med(lab)", 0),
    Student("Ayo", 3, "female", "Eng", 1),
    Student("Wahid", 4, "female", "med(surg)", 0),
    Student("Saburu", 3, "male", "med(surg)", 1),
    Student("Tayo", 4, "male", "Eng", 0),
    Student("Muyiwa", 2, "female", "Law", 1),
    Student("Ope", 3, "male", "med(lab)", 0),
    Student("Tina", 2, "female", "med(lab)", 0),
    Student("Tomiwa", 3, "female", "Eng", 1),
]

NUMBER_OF_GROUPS = 3
groups = [[] for i in range(NUMBER_OF_GROUPS)]
counter = 0

reverse = False


def reverse_sort():
    global reverse
    reverse = not reverse
    return reverse


gender_attr = operator.attrgetter("gender")
grade_attr = operator.attrgetter("grade")
natinal_attr = operator.attrgetter("foreigner")
spe_attr = operator.attrgetter("specialisation")


grouped_students = []
# Group by national
for national_key, national_vals in groupby(sorted(students, key=natinal_attr), natinal_attr):
    grouped_students.append(
        [
            [
                list(grade_vals)
                # Group by grade
                for grade_key, grade_vals in groupby(sorted(gender_vals, key=grade_attr), grade_attr)
            ]
            # Group by gender
            for gender_key, gender_vals in groupby(sorted(national_vals, key=gender_attr), gender_attr)
        ]
    )

for gender_group in grouped_students:
    for national_group in gender_group:
        for specialisation_group in national_group:
            for student in sorted(specialisation_group, key=spe_attr, reverse=reverse_sort()):
                groups[counter].append(student)
                counter = (counter + 1) % NUMBER_OF_GROUPS


def print_group(student_groups):
    for i in range(len(student_groups)):
        print("Group {0}:".format(i + 1))
        for member in student_groups[i]:
            print(member)


print_group(groups)
