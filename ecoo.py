from abc import ABC, abstractmethod

class Organism(ABC):
    def __init__(self, energy):
        self.__energy = energy  # private variable

    @property
    def energy_level(self):
        return self.__energy

    @energy_level.setter
    def energy_level(self, energy):
        if energy < 0:
            self.__energy = 0   # prevent negative energy
        else:
            self.__energy = energy
    
    @abstractmethod
    def sleep(self):
        pass


class Plant(Organism):
    def eat(self):
        print("Plant gained energy from sunlight ")
        self.energy_level += 10

    def sleep(self):
        return "Plant doesnt even sleep, well kinda"
        


class Animal(Organism):
    def move(self):
        print("moved ")
        self.energy_level -= 5

    def eat(self):
        print("Animal Eat")
        self.energy_level +=10
    
    def sleep(self):
        return "Animal is sleeping"

class Herbivore(Animal):
    def eat_plants(self):
        print("Herbivore ate plants ")
        self.energy_level += 15

    

    


class Omnivore(Animal):
    def eat(self):
        print("Omnivore ate food ")
        self.energy_level += 20
        


# ------------------ Testing ------------------

# dog = Animal(100)
# print("Dog Initial energy:", dog.energy_level)

# dog.move()
# print("After moving:", dog.energy_level)
# print("\n")


# cow = Herbivore(80)
# cow.eat_plants()
# print("Cow energy:", cow.energy_level)
# print("\n")


# human = Omnivore(90)
# human.eat()

# print("Human energy:", human.energy_level)
# print("\n")

# human.move()
# print("Human energy now :",human.energy_level)
# print("\n")



# tree = Plant(50)
# tree.photosynthesis()
# print("Tree energy:", tree.energy_level)


tree=Plant(50)

Dog=Animal(100)

human=Omnivore(80)

loop=True
while(loop):
    Choice = int(input("Enter the choice For Next 1 And For Exit 2 :"))

    match Choice:
        case 1:
            print("Dog energy level before: " ,Dog.energy_level)
            Dog.move()
            print("Dog energy level now: " ,Dog.energy_level)

            print("\n")

            print("Dog energy level before: " ,Dog.energy_level)
            Dog.eat()
            print(Dog.sleep())
            print("Dog energy level now: " ,Dog.energy_level)

           
            print("\n")

            print("Humana energy before:",human.energy_level)
            human.move()
            print("Humana energy now:",human.energy_level)

            print("\n")

            print("Humana energy before:",human.energy_level)
            human.eat()
            print(human.sleep())
            print("Humana energy now:",human.energy_level)


            print("\n")
            print("tree energy now:",tree.energy_level)
            tree.eat()
            print(tree.sleep())
            print("tree energy now:",tree.energy_level)



        case 2:
            loop=False
            break
