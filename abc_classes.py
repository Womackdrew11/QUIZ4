from abc import ABC, abstractmethod

class Person(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def get_info(self):
        pass

class Student(Person):
    def get_info(self):
        return f"I am a student named {self.name}."

class Teacher(Person):
    def get_info(self):
        return f"I am a teacher named {self.name}."

def main():
    student = Student("Andrew")
    teacher = Teacher("Melissa")

    print(student.get_info())
    print(teacher.get_info())

if __name__ == "__main__":
    main()
