#!/usr/bin/python3
"""
This file contains a class Students
"""


class Student:
    """
    This class represent a Student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        if type(attrs) is list:
            dic = {}
            for i in attrs:
                if i == "first_name":
                    dic[i] = self.first_name
                if i == "last_name":
                    dic[i] = self.last_name
                if i == "age":
                    dic[i] = self.age
        return dic

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
