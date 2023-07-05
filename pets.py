class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def __repr__(self):
        return f"{self.name}"

    def sleep(self):
        print(f"{self.name} falls asleep.")

    def eat(self):
        print(f"{self.name} hunted down a meal")

    def play(self):
        print(f"{self.name} spent some time playing")

    def noise(self):
        print(f"{self.name} lets out a noise totally appropriate for their species!")



kai = Pet("Kai", 'dog', 'sit', 50, 50)
