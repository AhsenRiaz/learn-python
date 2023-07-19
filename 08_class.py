class Person:
    def __init__(self, name, age):
        # properties
        self.name = name
        self.age = age

    def walk(self):
            print(self.name , " is walking");

    def talk(self):
         print(self.name, " is talking");



John = Person("John", 24);
Bob = Person("Bob", 28);

print(John.name, John.age);
John.walk();

print(Bob.name, Bob.age);
Bob.talk();

