#!/usr/bin/python3

import re

from tables import *
from course import *
from semester import *


def main():
    filename_loc = "../grades.txt"
    semesters = parse(filename_loc)
    # pass in list of semester objects to calculate gpa
    gpa = calculate_gpa(semesters)
    write_file(semesters, gpa)


def test_open(filename):
    # counter = 1
    try:
        file = open(filename, 'r+')
        file = file.readlines()
        return file
    except ValueError as err:
        print(err.args)


def parse(filename):
    semesters = list()

    lines = test_open(filename)
    for i in range(0, len(lines)):
        line = lines[i]
        if line[0] == '-':
            name = line[1:-1]

            courses = list()

            j = i + 1

            while lines[j][0] != '-':
                line = lines[j].split(",")

                # warn user if there is bad formatting for the courses
                if len(line) != 3:
                    print("Invalid course entry for course: " + line[3])
                else:
                    # structure of file input:
                    # 3 B HNRS: FOUND BUSNSS II

                    # create a course object and add it to the list of courses
                    courses.append(Course(line[0], line[1], line[2]))

                if((j + 1) < len(lines)):
                    j += 1
                else:
                    break

            # create a semester object and add it to the list of semesters
            semesters.append(Semester(name, courses))
        else:
            continue

    return semesters


def calculate_gpa(semesters):
    total_hours = 0
    for semester in semesters:
        total_hours += semester.get_total_hours()

    gpa = 0.0

    for semester in semesters:
        gpa += semester.get_gpa() * (semester.get_total_hours() / total_hours)
    return gpa


def filewrite(text):
    name = "text.txt"
    file = open(name, 'w')

    for line in text:
        file.write(line)

    file.close()


def write_file(semesters, gpa):
    name_loc = "../gpa.txt"
    file = open(name_loc, 'w')

    for sem in semesters:
        file.write(sem.to_string())

    file.write("After " + str(len(semesters)) + " semesters, cumulative GPA is: " + str(gpa))
    file.close()

if __name__ == "__main__":
    main()
