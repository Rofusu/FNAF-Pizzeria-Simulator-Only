animatronic_list = []

class Animatronic:
    def __init__(self, name, risk, entertainment):
        self.name = name
        self.risk = risk
        self.entertainment = entertainment

        animatronic_list.append(self)

freddy = Animatronic("Freddy", 2, 7)
bonnie = Animatronic("Bonnie", 2, 6)
chica = Animatronic("Chica", 2, 6)
