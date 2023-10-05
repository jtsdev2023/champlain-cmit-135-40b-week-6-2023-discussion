# main.py
# champlain college online cmit-135-40b week 6 discussion - methods and functions

class HogwartsStudent:
    """An object representing a Hogwarts student"""

    def __init__(self, **kwargs):
        """Input student values to be used by the Hogwarts Sorting Hat"""
        self.student_date_of_birth = kwargs['dob']
        self.student_name_first = kwargs['name_first']
        self.student_values = kwargs['student_values']

    def sorting_hat_sort_students(self):
        ...
