import random

class Coin:

    def __init__(self, rare=False, clean=True, heads=True, **kwargs):
        self.isRare = rare
        self.isClean = clean
        self.heads = heads

        for key, value in kwargs.items():
            setattr(self, key, value)

        if self.isRare:
            self.value = self.originalValue * 1.25
        else:
            self.value = self.originalValue

        if self.isClean:
            self.color = self.cleanColor
        else:
            self.color = self.rustyColor

    def rust(self):
        self.color = self.rustyColor
        
    def clean(self):
        self.color = self.cleanColor

    def flip(self):
        headsOptions = [True, False]
        choice = random.choice(headsOptions)
        self.heads = choice

    def __del__(self):
        print("Coin Spent!")


class Pound(Coin):

    def __init__(self):
        data = {
            "originalValue": 1.00,
            "cleanColor": "gold",
            "rustyColor": "greenish",
            "numEdges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
            }
        super().__init__(**data)
            
