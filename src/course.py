#!/usr/bin/python3

from helper import *
from tables import *


class Course(object):
    """A course represented by the attributes below.

    Attributes:
        name: The name of the course as a string.
        num_hours: An integer representing the number of hours of the course.
        grade: The letter grade from the class, represented as A to F (+/-)
    """

    def __init__(self, num_hours, grade, name):
        """Return a new Courses object."""
        self.name = name
        self.num_hours = int(num_hours)
        self.grade = grade
        self.pass_no_pass = False
        if self.grade.lower() == 'p' or self.grade.lower() == 'f':
            self.pass_no_pass = True

    def get_name(self):
        return self.name

    def get_num_hours(self):
        return self.num_hours

    def get_grade(self):
        return get_from_table(self.grade, gpa_table)

    def is_pass_no_pass(self):
        return self.pass_no_pass == True

    def to_string(self):
        name = self.get_name()[:-1] if self.get_name()[-1:] == '\n' else self.get_name()
        result = "Course name:\t\t" + name
        result += "\nNumber of hours:\t" + str(self.get_num_hours())
        result += "\nCourse Grade:\t\t" + self.grade + "\n\n"
        return result
