# Python OOP - Classes & Object Model

Projet d'apprentissage de la Programmation Orientée Objet (OOP) en Python.

## 📚 Concepts Appris

- **Classe vs Instance** : Différence entre le moule et l'objet créé
- **Encapsulation** : Protéger les données avec attributs privés (`__attr`)
- **Properties** : Getters et setters avec `@property`
- **Validation** : Vérifier les données avant de les stocker
- **Méthodes spéciales** : `__init__`, `__str__`

## 🟦 Projet Square (Carré)

Classe représentant un carré avec :
- Attribut privé `size` avec validation
- Property pour accéder/modifier `size`
- Méthode `area()` pour calculer l'aire
- Méthode `my_print()` pour afficher le carré avec `#`
- Attribut `position` pour positionner le carré
- Méthode `__str__()` pour la représentation en string

```python
square = Square(5, (2, 1))
print(square.area())  # 25
square.my_print()
# 
#   #####
#   #####
#   #####
#   #####
#   #####
```

## 🟩 Projet Rectangle

Classe représentant un rectangle avec :
- Attributs privés `width` et `height` avec validation
- Properties pour accéder/modifier les dimensions
- Méthode `area()` : largeur × hauteur
- Méthode `perimeter()` : 2 × (largeur + hauteur)

```python
rect = Rectangle(10, 3)
print(rect.area())       # 30
print(rect.perimeter())  # 26
```

## 🔑 Syntaxe Clé

```python
class MyClass:
    def __init__(self, value):
        self.__private_attr = value  # Attribut privé
    
    @property
    def value(self):                 # Getter
        return self.__private_attr
    
    @value.setter
    def value(self, new_value):      # Setter
        if new_value >= 0:
            self.__private_attr = new_value
    
    def my_method(self):             # Méthode
        return self.__private_attr * 2
```

## 📂 Structure
python_oop/
├── classes_and_object_model/
│   ├── 0-square.py    # Classe vide
│   ├── 1-square.py    # Avec size
│   ├── 2-square.py    # Avec validation
│   ├── 3-square.py    # Avec area()
│   ├── 4-square.py    # Avec properties
│   ├── 5-square.py    # Avec my_print()
│   └── 6-square.py    # Avec position et str
└── rectangle/
├── 1-rectangle.py # Rectangle basique
└── 2-rectangle.py # Avec calculs

## ✅ Compétences Acquises

- ✅ Créer des classes et objets
- ✅ Implémenter l'encapsulation
- ✅ Utiliser properties (getters/setters)
- ✅ Valider les données
- ✅ Créer des méthodes d'instance

---

**Holberton School** - Python OOP Module
