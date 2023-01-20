class Human:
    # first_name = 'Aziret'
    # last_name = 'Sarylbekov'

    def __init__(self, name, last_name, age=0):
        self.first_name = name
        self.last_name = last_name
        self.age = age

    def greeting(self):
        print(f"Hi my name is {self.first_name}!")


human1 = Human(name='Aziret', last_name='Sarylbekov')
human2 = Human(name='Jandos', last_name='Karagozov', age=35)
human3 = Human(name='Aibike', last_name='Manapova')
print(human1.first_name, "human 1")
print(human3.first_name, "human 3")


human1.greeting()
human2.greeting()

human2.first_name, human1.last_name, human3.greeting()

print('---' * 20)


# Class Birds

class Bird:
    def __init__(self, name, neck, head, body, feathers, beak, wings, type):
        self.name = name
        self.head = head
        self.neck = neck
        self.body = body
        self.feathers = feathers
        self.beak = beak
        self.wings = wings
        self.type = type

    def name_bird(self):
        print(f"Name bird: {self.name}:")

    def status(self):
        print(f"{self.head},\n Neck: {self.neck},\nBody: {self.body}")


bird = Bird(name='Eagle', head='has a head', neck='Short', body='Middle body',
            feathers=True, beak='Spicy', wings='Two', type='Predators')

bird.name_bird()
bird.status()
