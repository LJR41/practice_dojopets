from pets import Pet

class Ninja:
    def __init__(self,first_name,last_name, pet,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = None
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        print(f"{self.first_name} takes {self.pet} on a walk!")

    def feed(self):
        print(f"{self.first_name} gave {self.pet} some {self.pet_food}")

    def bathe(self):
        print(f"{self.first_name} gives {self.pet} a bath.")

    def display_info(self):
        print(f"Name: {self.first_name}{self.last_name} \n Pet: {self.pet} \n Treats: {self.treats} \n Pet Food: {self.pet_food} ")


josh = Ninja("Josh", "Remulla", "Kai", "chicken", "kibble")
josh.pet = Pet("Kai", 'dog', 'sit', 50, 50)
josh.bathe()
josh.pet.noise()