import src.Livre as Livre

class Bibliotheque:
    def __init__(self):
        self.livres = []

    def ajouter_livre(self, livre):
        if not isinstance(livre, Livre.Livre):
            raise TypeError("Seul un objet de type Livre peut être ajouté.")
        self.livres.append(livre)
        print(f"Livre ajouté : {livre}")

    def supprimer_livre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                self.livres.remove(livre)
                print(f"Livre supprimé : {livre}")
                return
        raise ValueError(f"Aucun livre trouvé avec le titre : {titre}")

    def lister_livres(self):
        if not self.livres:
            print("La bibliothèque est vide.")
        else:
            for livre in self.livres:
                print(livre)

    def sauvegarder_dans_fichier(self, fichier):
        try:
            with open(fichier, 'w', encoding='utf-8') as fichier:
                for livre in self.livres:
                    fichier.write(f"{livre.titre},{livre.auteur},{livre.annee_publication}\n")
            print(f"Données sauvegardées dans le fichier : {fichier}")
        except Exception as e:
            print(f"Erreur lors de la sauvegarde : {e}")

    def charger_depuis_fichier(self, fichier):
        try:
            with open(fichier, 'r', encoding='utf-8') as fichier:
                self.livres.clear()
                for ligne in fichier:
                    titre,auteur,annee_publication =ligne.strip().split(',')
                    self.ajouter_livre(Livre.Livre(titre, auteur, int(annee_publication)))
            print(f"Données chargées depuis le fichier : {fichier}")
        except FileNotFoundError:
            print(f"Erreur: Il exist oucun fichier avec se nom ")
