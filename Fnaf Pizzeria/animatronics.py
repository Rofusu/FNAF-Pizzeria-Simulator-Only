from matplotlib.style import available

from sprites import images

class Animatronic:
    def __init__(self, name, risk, entertainment, image=None, description="No Description", cost=0, available=True):
        self.name = name
        self.risk = risk
        self.entertainment = entertainment
        self.image = image
        self.description = description
        self.cost = cost
        self.available = available
        self.owned= False

    def __repr__(self):
        return f"Animatronic({self.name})"

        animatronic_list.append(self)


playerCash = 10000

animatronic_list = []
animatronic_dict = {
    "Freddy": Animatronic(
        name="Freddy", risk=6, entertainment=6, cost=2000, image=images["Freddy"]
    ),
    "Bonnie": Animatronic(
        name="Bonnie", risk=4, entertainment=9, cost=5000, image=images["Bonnie"]
    ),
    "Chica": Animatronic(
        name="Chica", risk=3, entertainment=6, cost=2500, image=images["Chica"]
    ),
    "Toy Chica": Animatronic(
        name="Toy Chica", risk=1, entertainment=99, cost=10000, image=images["Toy Chica"], available=False
    )
}

animatronic_order = list(animatronic_dict.keys())