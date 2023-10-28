class Carte_visite:
    def __init__(self, nom, Ets, skills, email, telephone,linkedin,recherche):
        self.nom,self.Ets,self.skills,self.email=nom,Ets,skills,email   
        self.telephone,self.linkedin,self.recherche = telephone,linkedin,recherche
    def print_carte(self):
        print("-" * 67)
        print("|" + self.nom.ljust(65) + "|\n|" + self.Ets.ljust(65) + "|\n|" + self.skills.ljust(65) + "|")
        for i in range(2):
            print("|" + " " * 65 + "|")
        print("|" + self.email.ljust(65) + "|\n|" + self.telephone.ljust(65) + "|\n|" + self.recherche.ljust(65) + "|")
        print("-" * 67)
