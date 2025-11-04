class Wizard:
    def __init__(self, n, h, p, w):
        self.name = n
        self.age = 11
        self.school = "Hogwarts"
        self.house = h
        self.patronus = p
        self.wand_core = "dragon heartstring"
        self.wand_length = w

    def get_patronus(self):
        return self.patronus

    def personal_info(self):
        print(self.name, "is", self.age, "years old and has a wand with a core of", self.wand_core)

    def school_info(self):
        return self.name + " belongs to the House of " + self.house + " at " + self.school

    def expelliarmus(self, disarm):
        self.wand_length = 0
        print(self.name, "has disarmed", disarm.name)

    def birthday(self):
        self.age += 1
    
harry = Wizard("Harry", "Gryffindor", "Stag", 11)
ron = Wizard("Ron", "Gryffindor", "Jack Russel Terrier", 14)
hermione = Wizard("Hermione", "Gryffindor", "Otter", 15)
draco = Wizard("Draco", "Slytherin", None, 15)
cedric = Wizard("Cedric", "Hufflepuff", "Badger", 12.24)
newt = Wizard("Newt", "Hufflepuff", "Kelpie", 14)
fleur = Wizard("Fleur", "Bellefeuille", "non-corporeal", 9.5)

print("Harry has a patronus of an", harry.get_patronus())
print()
print("Ron has a patronus of an", ron.get_patronus())
print()
print("Hermione has a patronus of an", hermione.get_patronus())
print()
print("Draco has a patronus of an", draco.get_patronus())

print()
harry.personal_info()
print()
ron.personal_info()
print()
hermione.personal_info()
print()
draco.personal_info()
print()
cedric.personal_info()
print()
newt.personal_info()
print()
fleur.personal_info()

print()
print(harry.school_info())
print()
print(ron.school_info())
print()
print(hermione.school_info())
print()
print(draco.school_info())
print()
print(cedric.school_info())
print()
print(newt.school_info())
print()
print(fleur.school_info())

print()
fleur.birthday()
fleur.birthday()
fleur.birthday()
cedric.birthday()
cedric.birthday()
cedric.birthday()
newt.age = 97

draco.expelliarmus(fleur)

print()
harry.personal_info()
print()
ron.personal_info()
print()
hermione.personal_info()
print()
draco.personal_info()
print()
cedric.personal_info()
print()
newt.personal_info()
print()
fleur.personal_info()

print()
print(harry.school_info())
print()
print(ron.school_info())
print()
print(hermione.school_info())
print()
print(draco.school_info())
print()
print(cedric.school_info())
print()
print(newt.school_info())
print()
print(fleur.school_info())

