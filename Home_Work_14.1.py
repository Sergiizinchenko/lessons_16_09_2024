class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.gender},{self.age},{self.first_name},{self.last_name}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{self.gender},{self.age},{self.first_name},{self.last_name},{self.record_book}"


class Group:

    def __init__(self, number):

        self.number = number
        self.group = set()

    def add_student(self, student):

        if len(self.group) >= 10:
            raise Exception("Cannot add more than 10 students to the group.")
        self.group.add(student)

    def delete_student(self, last_name):

        self.group = [student for student in self.group if student.last_name != last_name]

    def find_student(self, last_name):

        for student in self.group:

            if student.last_name == last_name:
                return student

            # print(last_name)

        return None

    def __str__(self):

        all_students = '\n'.join(str(student) for student in self.group)
        print(len(self.group))

        return f'Number: {self.number}\n{all_students}'


class InvalidStudentCountException(Exception):
    "Raised when the number of students is not equal to 10"

    pass


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)

print(str(gr.find_student('Taylor11')))

# print()

# print (str(gr.find_student('Jobs')))

assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student
gr.delete_student('Taylor')  # No error!
number = 10

try:

    student_count = len(gr.group)

    if student_count != 10:
        raise InvalidStudentCountException(f"Student count is {student_count}, but it should be 10.")
    else:
        print("The number of students is correct.")

except InvalidStudentCountException as e:
    print(f"Exception occurred: {e}")