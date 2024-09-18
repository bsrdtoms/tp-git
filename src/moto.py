class Moto:
    def __init__(self, nom, couleur):
        self.couleur = couleur
        self.nom = nom
        self.vitesse = 6464

    def accelere(self, increment):
        if increment > 15:
            increment = 15
        self.vitesse = min(150, self.vitesse + increment)