import json

class Langue:
    def __init__(self, fichier_traduction, langue_code):
        self.traductions = self.charger_traductions(fichier_traduction)
        self.langue_code = langue_code

    def charger_traductions(self, chemin_fichier):
        with open(chemin_fichier, 'r') as file:
            traductions = json.load(file)
        return traductions