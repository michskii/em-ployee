class Dog:
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # Instance variables
        self.name = name
        self.breed = breed

    def display_details(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Species: {Dog.species}")


# Create instances of Dog
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")

# Display details of the dogs
dog1.display_details()
dog2.display_details()