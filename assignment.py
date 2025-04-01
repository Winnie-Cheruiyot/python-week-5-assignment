# Base class representing a generic Superhero
class Superhero:
    def __init__(self, name, superpower, alias):
        self.name = name          # Real name of the superhero
        self.superpower = superpower  # Superpower the hero possesses
        self.alias = alias        # Hero's superhero alias

    def introduce(self):
        print(f"Hi, I am {self.name}, also known as {self.alias}. My superpower is {self.superpower}.")

    def fight(self):
        print(f"{self.alias} is fighting evil!")

    def use_power(self):
        print(f"{self.alias} uses {self.superpower} to save the day!")

# Derived class representing a specific Superhero: IronMan
class IronMan(Superhero):
    def __init__(self, name, superpower, alias, suit_type):
        super().__init__(name, superpower, alias)  # Calling the constructor of Superhero class
        self.suit_type = suit_type  # Additional attribute specific to IronMan

    def introduce(self):
        super().introduce()  # Using the parent class's method
        print(f"I am also wearing a {self.suit_type} suit.")

    def fly(self):
        print(f"{self.alias} flies using his advanced IronMan suit!")

# Derived class representing another Superhero: SpiderMan
class SpiderMan(Superhero):
    def __init__(self, name, superpower, alias, web_type):
        super().__init__(name, superpower, alias)
        self.web_type = web_type  # Additional attribute specific to SpiderMan

    def introduce(self):
        super().introduce()  # Using the parent class's method
        print(f"I shoot {self.web_type} webs!")

    def swing(self):
        print(f"{self.alias} swings through the city using webs!")

# Create objects of both superheroes
ironman = IronMan("Lucas Elba", "Genius-level intellect", "Iron Man", "Stark suit")
spiderman = SpiderMan("Stanin Taye", "Spider agility and web-slinging", "speed yoh", "web-based")

# Calling methods to test polymorphism and inheritance
ironman.introduce()  # Demonstrates polymorphism by overriding the 'introduce' method
ironman.fight()
ironman.use_power()
ironman.fly()

print("\n")

spiderman.introduce()  # Demonstrates polymorphism by overriding the 'introduce' method
spiderman.fight()
spiderman.use_power()
spiderman.swing()

