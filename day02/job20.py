class Person:
    def __init__(self, lastname, firstname):
        self.lastname = lastname
        self.firstname = firstname
        
# "SePresenter()" method
    def SePresenter(self):
        print(f"I am {self.firstname} {self.lastname}")

# "accessor" and a "mutator"
    def get_lastname(self):
        return self.lastname

    def set_lastname(self, new_lastname):
        self.set_lastname = new_lastname

    def get_firstname(self):
        return self.firstname

    def set_firstname(self, new_firstname):
        self.firstname = new_firstname

person_1 = Person("ABBADI", "Ibrahim")
person_2 = Person("Jelbini", "Saad")

person_1.SePresenter()
person_2.SePresenter()

print(f"person_1's lastname : {person_1.get_lastname()}")
print(f"person_1's firstname :: {person_1.get_firstname()}")

person_1.set_lastname("aa")
person_1.set_firstname("Jean-pierre")

print(f"lastname after modif- : {person_1.get_lastname()}")
print(f"firstname after modif: {person_1.get_firstname()}")

