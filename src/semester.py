#!/usr/bin/python3

from tables import *


class Semester(object):
    """A semester represented by an array of Course objects (name, number of hours, and grade).

    Attributes:
        name: The name of the semester as a string.
        courses: An array representing the courses in the given semester.
        semester_gpa: The floating point number representing the gpa of the semester.
    """

    courses = list()

    def __init__(self, name, courses):
        """Return a new Courses object."""
        self.name = name
        self.courses = courses

    def get_name(self):
        return self.name

    def get_courses(self):
        return self.courses

    def get_total_hours(self):
        hours = 0
        courses = [course for course in self.get_courses() if not course.is_pass_no_pass()]
        for course in courses:
            hours += course.get_num_hours()
        return hours

    def get_gpa(self):
        total_hours = self.get_total_hours()
        gpa = 0.0

        courses = [course for course in self.get_courses() if not course.is_pass_no_pass()]
        for course in courses:
            gpa += (course.get_num_hours() / total_hours) * course.get_grade()
        return gpa

    def to_string(self):
        result = ""
        result += self.get_name() + " Semester"
        result += "\n------------------------------------------\n"
        for course in self.get_courses():
            result += course.to_string()
        result += "\n"
        return result
