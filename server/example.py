class Student():
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Name: {self.name}"

# john_doe = Student(20, "John Doe")
john_doe = Student(age=20, name="John Doe")

print(john_doe)