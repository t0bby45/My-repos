class Pet:
    def __init__(self, name, age, species="cat"):
        self.name = name
        self.age = age
        self.species = species
        self.energy = 100
        self.hunger = 0
    
    def eat(self, amount):

        if self.hunger > 0:
            self.hunger -= amount
            if self.hunger < 0:
                self.hunger = 0
            self.energy += amount // 2
            print(f"{self.name} поел(а) и чувствует себя лучше.")
        else:
            print(f"{self.name} не голоден(на)!")
    
    def play(self):

        if self.energy > 20:
            self.energy -= 20
            self.hunger += 15
            print(f"{self.name} играл(а) и теперь немного устал(а).")
        else:
            print(f"{self.name} слишком устал(а) для игры.")
    
    def sleep(self, hours):

        self.energy += hours * 10
        self.hunger += hours * 5
        if self.energy > 100:
            self.energy = 100
        print(f"{self.name} поспал(а) и теперь полон(на) сил.")
    
    def status(self):

        print(f"Имя: {self.name}, Возраст: {self.age}, Вид: {self.species}")
        print(f"Энергия: {self.energy}, Голод: {self.hunger}")
        if self.hunger > 50:
            print(f"{self.name} очень голоден(на)!")
        elif self.energy < 20:
            print(f"{self.name} очень устал(а) и хочет поспать.")
        else:
            print(f"{self.name} чувствует себя хорошо!")


my_pet = Pet(name="Мурка", age=2, species="cat")

# Просмотр состояния питомца
my_pet.status()

# Питомец играет
my_pet.play()
my_pet.play()
my_pet.play()
my_pet.status()

# Питомец ест
my_pet.eat(30)
my_pet.eat(30)
my_pet.eat(30)
my_pet.eat(30)
my_pet.status()

# Питомец спит
my_pet.sleep(3)
my_pet.status()

