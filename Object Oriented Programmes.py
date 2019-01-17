import time


class person:

    # Base class functions
    # constructor method
    def data(self):
        print("++++ BASE CLASS ACCESSED ++++")
        print('Enter the details below')
        name = input("Enter name :  ")
        age = input("Enter age :  ")
        grade = input("Enter Grade :  ")
        print("Student Name= {} \n Age = {} \n Grade = {} \n".format(name, age, grade))
        time.sleep(3)
        return

    # Method call and passing Arguments
    def passing_arguments(self, name, age, grade):
        print("++++ BASE CLASS ARGUMENTS PASSED ++++")
        print("Name= {} \n Age = {} \n Grade = {} \n".format(name, age, grade))
        time.sleep(3)
        return


# Class Inheritance
class teacher(person):
    # Derived class functions
    def data1(self):
        print("++++ DERIVED CLASS ACCESSED ++++")
        print('Enter the details below')
        name = input("Enter name :  ")
        speciality = input("Enter Speciality subject :  ")
        handle = input("Enter handling Grade :  ")
        print("Teacher Name= {} \nspecialized  = {} \n handling Grade = {}".format(name, speciality, handle))
        time.sleep(3)

    # Method call and passing Arguments
    def passing_arguments(self, name, age, grade):
        print("++++ DERIVED CLASS ARGUMENTS PASSED ++++")
        print("Name= {} \n Age = {} \n Grade = {} \n".format(name, age, grade))
        time.sleep(3)
        return


class student(person):

    # Derived class overloading Base class
    def data(self,name, age, grade, mark):
        print("++++ BASE CLASS OVER-RAIDING ++++")
        self.mark = mark
        print("Student Name= {} \n Age = {} \n Grade = {} \n Mark = {}".format(name, age, grade, mark))
        time.sleep(3)
        return


while True:
    print(" Enter the option demo")
    a = int(input(
        '1: Class Construction \n2: Passing Arguments \n3:Class Inheritance \n4:Inheritance with arguments passing '
        '\n5:Overloading Class function\n'))
    if a == 1:
        s1 = person
        print(s1.data(s1))

    elif a == 2:
        s2 = person
        print('Enter the details below')
        name = input("Enter name :  ")
        age = input("Enter age :  ")
        grade = input("Enter Grade :  ")
        s2.passing_arguments(s2, name, age, grade)
    elif a == 3:
        s3 = teacher
        print(s3.data1(0))

    elif a == 4:
        s4 = teacher
        print('Enter the details below')
        name = input("Enter name :  ")
        age = input("Enter age :  ")
        grade = input("Enter Grade :  ")
        print(s4.passing_arguments(s4, name, age, grade))

    else:
        s5 = student
        print('Enter the details below')
        name = input("Enter name :  ")
        age = input("Enter age :  ")
        grade = input("Enter Grade :  ")
        mark = input("Enter Mark:  ")
        print(s5.data(s5,name, age, grade, mark))
