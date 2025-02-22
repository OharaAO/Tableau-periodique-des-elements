import tkinter as tk
from tkinter import ttk
from tkinter import Toplevel, Label

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
    (33, "As", "Arsenic", 74.922, "Métalloïde"),
    (34, "Se", "Sélénium", 78.971, "Non-métal"),
    (35, "Br", "Brome", 79.904, "Halogène"),
    (36, "Kr", "Krypton", 83.798, "Gaz noble"),
    (37, "Rb", "Rubidium", 85.468, "Métal alcalin"),
    (38, "Sr", "Strontium", 87.62, "Métal alcalino-terreux"),
    (39, "Y", "Yttrium", 88.906, "Métaux de transition"),
    (40, "Zr", "Zirconium", 91.224, "Métaux de transition"),
    (41, "Nb", "Niobium", 92.906, "Métaux de transition"),
    (42, "Mo", "Molybdène", 95.95, "Métaux de transition"),
    (43, "Tc", "Technétium", 98, "Métaux de transition"),
    (44, "Ru", "Ruthénium", 101.07, "Métaux de transition"),
    (45, "Rh", "Rhodium", 102.91, "Métaux de transition"),
    (46, "Pd", "Palladium", 106.42, "Métaux de transition"),
    (47, "Ag", "Argent", 107.87, "Métaux de transition"),
    (48, "Cd", "Cadmium", 112.41, "Métaux de transition"),
    (49, "In", "Indium", 114.82, "Métaux de post-transition"),
    (50, "Sn", "Étain", 118.71, "Métaux de post-transition"),
    (51, "Sb", "Antimoine", 121.76, "Métalloïde"),
    (52, "Te", "Tellure", 127.60, "Métalloïde"),
    (53, "I", "Iode", 126.90, "Halogène"),
    (54, "Xe", "Xénon", 131.29, "Gaz noble"),
    (55, "Cs", "Césium", 132.91, "Métal alcalin"),
    (56, "Ba", "Baryum", 137.33, "Métal alcalino-terreux"),
    (57, "La", "Lanthane", 138.91, "Lanthanides"),
    (58, "Ce", "Cérium", 140.12, "Lanthanides"),
    (59, "Pr", "Praséodyme", 140.91, "Lanthanides"),
    (60, "Nd", "Néodyme", 144.24, "Lanthanides"),
    (61, "Pm", "Prométhium", 145, "Lanthanides"),
    (62, "Sm", "Samarium", 150.36, "Lanthanides"),
    (63, "Eu", "Europium", 151.96, "Lanthanides"),
    (64, "Gd", "Gadolinium", 157.25, "Lanthanides"),
    (65, "Tb", "Terbium", 158.93, "Lanthanides"),
    (66, "Dy", "Dysprosium", 162.50, "Lanthanides"),
    (67, "Ho", "Holmium", 164.93, "Lanthanides"),
    (68, "Er", "Erbium", 167.26, "Lanthanides"),
    (69, "Tm", "Thulium", 168.93, "Lanthanides"),
    (70, "Yb", "Ytterbium", 173.05, "Lanthanides"),
    (71, "Lu", "Lutécium", 174.97, "Lanthanides"),
    (72, "Hf", "Hafnium", 178.49, "Métaux de transition"),
    (73, "Ta", "Tantale", 180.95, "Métaux de transition"),
    (74, "W", "Tungstène", 183.84, "Métaux de transition"),
    (75, "Re", "Rhénium", 186.21, "Métaux de transition"),
    (76, "Os", "Osmium", 190.23, "Métaux de transition"),
    (77, "Ir", "Iridium", 192.22, "Métaux de transition"),
    (78, "Pt", "Platine", 195.08, "Métaux de transition"),
    (79, "Au", "Or", 196.97, "Métaux de transition"),
    (80, "Hg", "Mercure", 200.59, "Métaux de transition"),
    (81, "Tl", "Thallium", 204.38, "Métaux de post-transition"),
    (82, "Pb", "Plomb", 207.2, "Métaux de post-transition"),
    (83, "Bi", "Bismuth", 208.98, "Métaux de post-transition"),
    (84, "Po", "Polonium", 209, "Métalloïde"),
    (85, "At", "Astate", 210, "Halogène"),
    (86, "Rn", "Radon", 222, "Gaz noble"),
    (87, "Fr", "Francium", 223, "Métal alcalin"),
    (88, "Ra", "Radium", 226, "Métal alcalino-terreux"),
    (89, "Ac", "Actinium", 227, "Actinides"),
    (90, "Th", "Thorium", 232.04, "Actinides"),
    (91, "Pa", "Protactinium", 231.04, "Actinides"),
    (92, "U", "Uranium", 238.03, "Actinides"),
    (93, "Np", "Neptunium", 237, "Actinides"),
    (94, "Pu", "Plutonium", 244, "Actinides"),
    (95, "Am", "Américium", 243, "Actinides"),
    (96, "Cm", "Curium", 247, "Actinides"),
    (97, "Bk", "Berkélium", 247, "Actinides"),
    (98, "Cf", "Californium", 251, "Actinides"),
    (99, "Es", "Einsteinium", 252, "Actinides"),
    (100, "Fm", "Fermium", 257, "Actinides"),
    (101, "Md", "Mendélévium", 258, "Actinides"),
    (102, "No", "Nobélium", 259, "Actinides"),
    (103, "Lr", "Lawrencium", 262, "Actinides"),
    (104, "Rf", "Rutherfordium", 267, "Métaux de transition"),
    (105, "Db", "Dubnium", 270, "Métaux de transition"),
    (106, "Sg", "Seaborgium", 271, "Métaux de transition"),
    (107, "Bh", "Bohrium", 270, "Métaux de transition"),
    (108, "Hs", "Hassium", 277, "Métaux de transition"),
    (109, "Mt", "Meitnérium", 276, "Métaux de transition"),
    (110, "Ds", "Darmstadtium", 281, "Métaux de transition"),
    (111, "Rg", "Roentgenium", 282, "Métaux de transition"),
    (112, "Cn", "Copernicium", 285, "Métaux de transition"),
    (113, "Nh", "Nihonium", 286, "Métaux de post-transition"),
    (114, "Fl", "Flerovium", 289, "Métaux de post-transition"),
    (115, "Mc", "Moscovium", 290, "Métaux de post-transition"),
    (116, "Lv", "Livermorium", 293, "Métaux de post-transition"),
    (117, "Ts", "Tennessine", 294, "Halogène"),
    (118, "Og", "Oganesson", 294, "Gaz noble"),
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
    "Lanthanides": "#FFC0CB",  # Pink
    "Actinides": "#FF69B4",  # Hot Pink
}

# Layout of the periodic table
periodic_table_layout = [
    [1, None, None, None, None, None, None, None, None, None, None, None, None, None, None,None,None, 2],
    [3, 4, None,None,None,None,None,None,None,None,None,None,5, 6, 7, 8, 9, 10],
    [11, 12, None,None,None,None,None,None,None,None,None,None, 13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
    [37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54],
    [55, 56, 57, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86],
    [87, 88, 89, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71],
    [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]
]

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

        # Create a dictionary to map atomic numbers to element details
        element_dict = {element[0]: element for element in elements}

        # Iterate through the periodic table layout
        for row_idx, row in enumerate(periodic_table_layout):
            for col_idx, atomic_number in enumerate(row):
                if atomic_number is not None:
                    element = element_dict.get(atomic_number)
                    if element:
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

                        # Ajouter un tooltip pour chaque bouton
                        Tooltip(btn, f"Nom : {name}\nMasse atomique : {atomic_mass}")

                        # Position dans la grille
                        btn.grid(row=row_idx, column=col_idx, padx=2, pady=2)

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
        atomic_number, symbol, name, atomic_mass, category = element
        # Exemple de données supplémentaires
        electron_config = "1s² 2s² 2p⁶"  # À remplacer par les vraies données
        discovery_year = 1800  # À remplacer par les vraies données

        details = (
            f"Nom : {name}\n"
            f"Symbole : {symbol}\n"
            f"Numéro atomique : {atomic_number}\n"
            f"Masse atomique : {atomic_mass}\n"
            f"Catégorie : {category}\n"
            f"Configuration électronique : {electron_config}\n"
            f"Année de découverte : {discovery_year}"
        )
        self.details_label.config(text=details)


class Tooltip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")
        label = Label(self.tooltip, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None


if __name__ == "__main__":
    root = tk.Tk()
    app = PeriodicTableApp(root)
    root.mainloop()