import unittest
from src.Livre import Livre
from src.Bibliotheque import Bibliotheque
class TestBibliotheque(unittest.TestCase):
    def setUp(self):
        self.biblio = Bibliotheque()
        self.livre1 = Livre("Python 101", "John Doe", 2020)
        self.livre2 = Livre("Deep Learning", "Jane Smith", 2019)
    
    def test_ajouter_livre(self):
        self.biblio.ajouter_livre(self.livre1)
        self.assertIn(self.livre1, self.biblio.livres)
    
    def test_ajouter_livre_type_error(self):
        with self.assertRaises(TypeError):
            self.biblio.ajouter_livre("Not a Book")
    
    def test_supprimer_livre(self):
        self.biblio.ajouter_livre(self.livre1)
        self.biblio.supprimer_livre("Python 101")
        self.assertNotIn(self.livre1, self.biblio.livres)
    
    def test_supprimer_livre_value_error(self):
        with self.assertRaises(ValueError):
            self.biblio.supprimer_livre("Nonexistent Book")
    
    def test_lister_livres(self):
        self.biblio.ajouter_livre(self.livre1)
        self.biblio.ajouter_livre(self.livre2)
        self.biblio.lister_livres()
    
    def test_sauvegarder_dans_fichier(self):
        self.biblio.ajouter_livre(self.livre1)
        self.biblio.sauvegarder_dans_fichier("test_biblio.txt")
        with open("test_biblio.txt", "r", encoding="utf-8") as f:
            data = f.read()
        self.assertIn("Python 101,John Doe,2020", data)
    
    def test_charger_depuis_fichier(self):
        with open("test_biblio.txt", "w", encoding="utf-8") as f:
            f.write("Deep Learning,Jane Smith,2019\n")
        self.biblio.charger_depuis_fichier("test_biblio.txt")
        self.assertEqual(len(self.biblio.livres), 1)
        self.assertEqual(self.biblio.livres[0].titre, "Deep Learning")

