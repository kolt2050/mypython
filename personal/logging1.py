# -*- coding: utf-8 -*-
import os
from datetime import datetime


class Student(object):
    def __init__(
        self, name, surname, birthdate, gender,
            grade, speciality, coursenumber):

        self.setname(name)
        self.setsurname(surname)
        self.setbirthdate(birthdate)
        self.setgender(gender)
        self.grade = grade
        self.speciality = speciality
        self.coursenumber = coursenumber

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def birthdate(self):
        return self.__birthdate

    @property
    def gender(self):
        return self.__gender

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        self.setgrade(value)

    @property
    def speciality(self):
        return self.__speciality

    @speciality.setter
    def speciality(self, value):
        self.setspeciality(value)

    @property
    def coursenumber(self):
        return self.__coursenumber

    @coursenumber.setter
    def coursenumber(self, value):
        self.setcoursenumber(value)

    def setname(self, value):
        if isinstance(value, str):
            if len(value) <= 25:
                self.__name = value
            else:
                raise ValueError("Name input error")
        else:
            raise ValueError("Name input error")

    def setsurname(self, value):
        if isinstance(value, str):
            if len(value) <= 25:
                self.__surname = value
            else:
                raise ValueError("Surname input error")
        else:
            raise ValueError("Surname input error")

    def setbirthdate(self, value):
        valid = True
        if len(value) != 10:
            valid = False
        else:
            try:
                datetime.strptime(value, '%Y-%m-%d')
            except:
                valid = False
        if valid:
            self.__birthdate = value
        else:
            raise ValueError("Birth date input error")

    def setgender(self, value):
        if (value == 'Male') | (value == 'Female'):
            self.__gender = value
        else:
            raise ValueError("Gender input error")

    def setgrade(self, value):
        if isinstance(value, int):
            if value in range(1, 10):
                self.__grade = value
            else:
                raise ValueError("Grade input error")
        else:
            raise ValueError("Grade input error")

    def setspeciality(self, value):
        if isinstance(value, str):
            if len(value) <= 50:
                self.__speciality = value
            else:
                raise ValueError("Specialty input error")
        else:
            raise ValueError("Specialty input error")

    def setcoursenumber(self, value):
        if isinstance(value, int):
            if value in range(1, 5):
                self.__coursenumber = value
            else:
                raise ValueError("Course number input error")
        else:
            raise ValueError("Course number input error")

    def __str__(self):
        res = (
            "Student:" + '   |  ' + "Birth Date:" + ' | ' + "Gender:" +
            ' | ' + "Grade:" + ' | ' + "Specialty:" + '   |   ' +
            "Course number:\n")
        res += self.name + ' ' + self.surname + ' | ' + self.birthdate + ' | '
        res += self.gender + '  |  ' + str(
            self.grade) + '   |   ' + self.speciality + ' | ' + str(
                self.coursenumber)
        return res

    @staticmethod
    def defSt(string):
        args = string.split(':')
        if args[3] == 'M':
            args[3] = 'Male'
        else:
            args[3] = 'Female'
        args[4] = int(args[4])
        args[6] = int(args[6])
        return Student(
            args[0], args[1], args[2], args[3], args[4], args[5], args[6])


student = Student(
    "Pavel", "Kamyshev", "1987-12-08", "Male", 4, "construction", 3)


print (student)
student = Student.defSt("Dmitry:Sergeev:1996-08-01:M:8:Building:2")
print (student)