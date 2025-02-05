import src.Bibliotheque as Bibliotheque
import src.Livre as Livre

def main_loop():
    biblio = Bibliotheque.Bibliotheque()

    while True:
        print("\nMenu :")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Lister les livres")
        print("4. Sauvegarder dans un fichier")
        print("5. Charger depuis un fichier")
        print("6. Quitter")

        choix = input("Choisissez une option : ")

        if choix == "1":
            titre = input("Titre du livre : ")
            auteur = input("Auteur du livre : ")
            annee_publication = input("Année de publication : ")
            try:
                biblio.ajouter_livre(Livre.Livre(titre, auteur, int(annee_publication)))
            except ValueError as e:
                print(f"Erreur : {e}")
        elif choix == "2":
            titre = input("Titre du livre à supprimer : ")
            try:
                biblio.supprimer_livre(titre)
            except ValueError as e:
                print(f"Erreur : {e}")

        elif choix == "3":
            biblio.lister_livres()

        elif choix == "4":
            chemin_fichier = input("Chemin du fichier pour la sauvegarde : ")
            biblio.sauvegarder_dans_fichier(chemin_fichier)

        elif choix == "5":
            chemin_fichier = input("Chemin du fichier à charger : ")
            try:
                biblio.charger_depuis_fichier(chemin_fichier)
            except FileNotFoundError as e:
                print(f"Erreur : {e}")

        elif choix == "6":
            print("Au revoir !")
            break

        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main_loop()
