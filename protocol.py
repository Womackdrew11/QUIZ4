from typing import Protocol

class Person(Protocol):
    def get_info(self) -> str:
        pass

class Student:
    def __init__(self, name: str):
        self.name = name
    
    def get_info(self) -> str:
        return f"I am a student named {self.name}."

class Teacher:
    def __init__(self, name: str):
        self.name = name
    
    def get_info(self) -> str:
        return f"I am a teacher named {self.name}."

def main():
    person = Student("Andrew")
    teacher = Teacher("Melissa")

    people = [person, teacher]

    for individual in people:
        print(individual.get_info())

if __name__ == "__main__":
    main()
