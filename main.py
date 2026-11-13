# Part 1: Create the parent class with family traits 
class FamilyMember:
    def __init__(self, eye_color, height_cm):
        self.eye_color = eye_color
        self.height_cm = height_cm

    def show_traits(self):
        print("Eye Color:", self.eye_color)
        print("Height (cm):", self.height_cm)
            

# Part 2: Create the child class that inherits from the parent class
class Kid(FamilyMember):
    
    # Part 3: Give Kid its own details that inherit from FamilyMember
    def __init__(self, name, eye_color, height_cm, age):
        self.name = name
        self.age = age
        super().__init__(eye_color, height_cm)  
    
    # Part 4: Create a method to show the kid's details too
    def show_traits(self):
        print("Name:", self.name)
        print("Age:", self.age)
        super().show_traits()
        
    # Part 5: Add a brand new method that only Kid has
    def favourite_hobby(self, hobby):
        print(self.name + " loves " + hobby)
    
# Part 6: Create a Kid object with real family trait values
child = Kid("Ziko", "Brown", 10, 140)

# Part 7: Call the overriden method and the new method
child.show_traits()
child.favourite_hobby("painting")

# Part 8: Check whether Kid is really a subc;ass of Family 
print("Is Kid a subclass of FamilyMember?", issubclass(Kid, FamilyMember))
