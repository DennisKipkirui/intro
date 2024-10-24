class Person:
    def __init__(self, name, age, gender):
        # Initialize the attributes for the person
        self.name = name
        self.age = age
        self.gender = gender
    
    def introduce(self):
        # Method to introduce the person
        print(f"Hello, my name is {self.name}. I am {self.age} years old, and I am {self.gender}.")
        
# Example of creating an instance of Person and calling the introduce method
person1 = Person("John Doe", 30, "Male")
person1.introduce()
