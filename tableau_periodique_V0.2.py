import tkinter as tk
from tkinter import ttk

# Liste des éléments chimiques (numéro atomique, symbole, nom, masse atomique, catégorie)
elements = [
    (1, "H", "Hydrogène", 1.008, "Non-métal"),
    (2, "He", "Hélium", 4.0026, "Gaz noble"),
    (3, "Li", "Lithium", 6.94, "Métal alcalin"),
    (4, "Be", "Béryllium", 9.0122, "Métal alcalino-terreux"),
    (5, "B", "Bore", 10.81, "Métalloïde"),
    (6, "C", "Carbone", 12.011, "Non-métal"),
    (7, "N", "Azote", 14.007, "Non-métal"),
    (8, "O", "Oxygène", 15.999, "Non-métal"),
    (9, "F", "Fluor", 18.998, "Halogène"),
    (10, "Ne", "Néon", 20.180, "Gaz noble"),
    (11, "Na", "Sodium", 22.990, "Métal alcalin"),
    (12, "Mg", "Magnésium", 24.305, "Métal alcalino-terreux"),
    (13, "Al", "Aluminium", 26.982, "Métaux de post-transition"),
    (14, "Si", "Silicium", 28.086, "Métalloïde"),
    (15, "P", "Phosphore", 30.974, "Non-métal"),
    (16, "S", "Soufre", 32.065, "Non-métal"),
    (17, "Cl", "Chlore", 35.453, "Halogène"),
    (18, "Ar", "Argon", 39.948, "Gaz noble"),
    (19, "K", "Potassium", 39.098, "Métal alcalin"),
    (20, "Ca", "Calcium", 40.078, "Métal alcalino-terreux"),
    (21, "Sc", "Scandium", 44.956, "Métaux de transition"),
    (22, "Ti", "Titane", 47.867, "Métaux de transition"),
    (23, "V", "Vanadium", 50.942, "Métaux de transition"),
    (24, "Cr", "Chrome", 51.996, "Métaux de transition"),
    (25, "Mn", "Manganèse", 54.938, "Métaux de transition"),
    (26, "Fe", "Fer", 55.845, "Métaux de transition"),
    (27, "Co", "Cobalt", 58.933, "Métaux de transition"),
    (28, "Ni", "Nickel", 58.693, "Métaux de transition"),
    (29, "Cu", "Cuivre", 63.546, "Métaux de transition"),
    (30, "Zn", "Zinc", 65.380, "Métaux de transition"),
    (31, "Ga", "Gallium", 69.723, "Métaux de post-transition"),
    (32, "Ge", "Germanium", 72.630, "Métalloïde"),
    # Ajoutez d'autres éléments ici
]

# Catégories et leurs couleurs correspondantes
category_colors = {
    "Non-métal": "#F0E68C",  # Khaki
    "Gaz noble": "#FFD700",  # Gold
    "Métal alcalin": "#FFB6C1",  # Light Pink
    "Métal alcalino-terreux": "#87CEFA",  # Light Sky Blue
    "Métalloïde": "#98FB98",  # Pale Green
    "Halogène": "#FFA07A",  # Light Salmon
    "Métaux de post-transition": "#68C178",  # Medium Sea Green
    "Métaux de transition": "#A97FC6",  # Medium Orchid
}

class PeriodicTableApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tableau Périodique des Éléments")
        self.create_widgets()

    def create_widgets(self):
        """Créer les widgets de l'interface graphique."""
        # Création de la grille pour le tableau
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        for element in elements:
            atomic_number, symbol, name, atomic_mass, category = element
            color = category_colors.get(category, "#FFFFFF")  # Blanc par défaut

            # Créer un bouton pour chaque élément
            btn = tk.Button(
                frame,
                text=f"{symbol}\n{atomic_number}",
                bg=color,
                width=6,
                height=3,
                font=("Arial", 10),
                command=lambda e=element: self.show_element_details(e)
            )

            # Position dans la grille (simplifiée pour la démo)
            row = (atomic_number - 1) // 18  # 18 colonnes pour correspondre au tableau périodique
            col = (atomic_number - 1) % 18
            btn.grid(row=row, column=col, padx=2, pady=2)

        # Créer une zone d'affichage des détails
        self.details_label = ttk.Label(
            self.root,
            text="Sélectionnez un élément pour voir les détails.",
            anchor="center",
            background="white",
            relief="solid",
            padding=10,
            font=("Arial", 12)
        )
        self.details_label.pack(fill="x", padx=10, pady=10)

    def show_element_details(self, element):
        """Afficher les détails d'un élément dans la zone de détails."""
        atomic_number, symbol, name, atomic_mass, category = element
        details = (
            f"Nom : {name}\n"
            f"Symbole : {symbol}\n"
            f"Numéro atomique : {atomic_number}\n"
            f"Masse atomique : {atomic_mass}\n"
            f"Catégorie : {category}"
        )
        self.details_label.config(text=details)

if __name__ == "__main__":
    root = tk.Tk()
    app = PeriodicTableApp(root)
    root.mainloop()