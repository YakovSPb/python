class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy):
        self.set_data(name, age, isHappy)

        self.get_data()

    def set_data(self, name = None, age = None, isHappy = None):
        self.name = name
        self.age = age
        self.isHappy = isHappy
    
    
    def get_data(self):
        print(self.name, 'age', self.age, "Happy" if self.isHappy else "Not happy")


cat1 = Cat('Barsik', 3, True)
cat1.set_data("John", 2)

cat2 = Cat("Жопен", 2, False)

