from src.Bibliotheque import Bibliotheque
from src.Livre import Livre
import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style
from ttkbootstrap.constants import *

# Initialize the library
biblio = Bibliotheque()

# Functions
def ajouter_livre():
    titre = entry_titre.get().strip()
    auteur = entry_auteur.get().strip()
    annee = entry_annee.get().strip()

    if not titre or not auteur or not annee:
        messagebox.showerror("Erreur", "Tous les champs doivent être remplis.")
        return

    try:
        annee = int(annee)
        nouveau_livre = Livre(titre, auteur, annee)
        biblio.ajouter_livre(nouveau_livre)
        reset_fields()
        lister_livres()
    except ValueError:
        messagebox.showerror("Erreur", "L'année de publication doit être un nombre.")

def supprimer_livre():
    selected = listbox_livres.curselection()
    if not selected:
        messagebox.showerror("Erreur", "Veuillez sélectionner un livre à supprimer.")
        return

    titre = listbox_livres.get(selected[0]).split(" - ")[0]  # Extract title
    biblio.supprimer_livre(titre)
    messagebox.showinfo("Succès", "Livre supprimé avec succès !")
    lister_livres()

def lister_livres():
    listbox_livres.delete(0, tk.END)
    for livre in biblio.livres:
        listbox_livres.insert(tk.END, f"{livre.titre} - {livre.auteur} ({livre.annee_publication})")

def sauvegarder():
    fichier = entry_fichier.get().strip()
    if not fichier:
        messagebox.showerror("Erreur", "Veuillez entrer un nom de fichier.")
        return

    try:
        biblio.sauvegarder_dans_fichier(fichier)
        messagebox.showinfo("Succès", "Données sauvegardées.")
        entry_fichier.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de sauvegarder : {e}")

def charger():
    fichier = entry_fichier.get().strip()
    if not fichier:
        messagebox.showerror("Erreur", "Veuillez entrer un nom de fichier.")
        return

    try:
        biblio.charger_depuis_fichier(fichier)
        entry_fichier.delete(0, tk.END)
        lister_livres()
    except Exception as e:
        messagebox.showerror("Erreur", f"Impossible de charger : {e}")

def reset_fields():
    entry_titre.delete(0, tk.END)
    entry_auteur.delete(0, tk.END)
    entry_annee.delete(0, tk.END)

# Setup UI
root = tk.Tk()
root.title("Gestion de Bibliothèque")
root.geometry("600x500")
style = Style(theme="superhero")  # Choose from ttkbootstrap themes

# Frames
frame_form = tk.Frame(root, bg="#222222", padx=10, pady=10)
frame_form.pack(fill="x", padx=10, pady=5)

frame_buttons = tk.Frame(root, bg="#222222", padx=10, pady=5)
frame_buttons.pack(fill="x", padx=10)

frame_list = tk.Frame(root, bg="#F8F9FA", padx=10, pady=5)
frame_list.pack(fill="both", expand=True, padx=10, pady=5)

frame_files = tk.Frame(root, bg="#222222", padx=10, pady=5)
frame_files.pack(fill="x", padx=10, pady=5)

# Book Form
tk.Label(frame_form, text="Titre", bg="#222222", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_titre = tk.Entry(frame_form, width=30)
entry_titre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Auteur", bg="#222222", fg="white").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_auteur = tk.Entry(frame_form, width=30)
entry_auteur.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_form, text="Année", bg="#222222", fg="white").grid(row=2, column=0, padx=5, pady=5, sticky="w")
entry_annee = tk.Entry(frame_form, width=30)
entry_annee.grid(row=2, column=1, padx=5, pady=5)

# Add Book Button
tk.Button(frame_buttons, text="Ajouter Livre", command=ajouter_livre, bg="#0D6EFD", fg="white").pack(padx=10, pady=10)

# Book List
tk.Label(frame_list, text="Liste des livres :", font=("Arial", 12, "bold"), bg="#F8F9FA").pack(anchor="w", padx=5, pady=5)
listbox_livres = tk.Listbox(frame_list, width=60, height=10)
listbox_livres.pack(padx=5, pady=5, fill="both", expand=True)

# Delete Book Button (Now under the listbox)
tk.Button(frame_list, text="Supprimer Livre", command=supprimer_livre, bg="#DC3545", fg="white").pack(pady=10)

# File Management
tk.Label(frame_files, text="Nom de fichier", bg="#222222", fg="white").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_fichier = tk.Entry(frame_files, width=30)
entry_fichier.grid(row=0, column=1, padx=5, pady=5)

tk.Button(frame_files, text="Sauvegarder", command=sauvegarder, bg="#198754", fg="white").grid(row=0, column=2, padx=10, pady=5)
tk.Button(frame_files, text="Charger", command=charger, bg="#FFC107", fg="black").grid(row=0, column=3, padx=10, pady=5)

# Run App
root.mainloop()
