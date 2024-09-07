class Person:
    def greet(self, name):
        print(f"Hello ${name}")

    def greet(self, name, city):
        print(f"hello ${name} from {city}")


p = Person()

p.greet("shri")
p.greet("shri", "satara")
