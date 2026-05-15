# Python OOP - Inheritance & Polymorphism

## 📋 Description du Projet

Construction d'une hiérarchie de formes géométriques pour explorer l'héritage et le polymorphisme en Python.

**Hiérarchie:** BaseGeometry → Rectangle → Square

---

## 🎯 Objectifs d'Apprentissage

- Expliquer comment l'héritage permet la réutilisation de code
- Identifier classes parentes et enfants
- Créer sous-classes étendant le comportement d'une autre classe
- Redéfinir méthodes héritées (override)
- Comprendre le polymorphisme
- Utiliser `isinstance()` et `issubclass()`
- Concevoir hiérarchies d'héritage simples

---

## 📚 Concepts Clés

### Héritage

Mécanisme permettant à une classe de réutiliser attributs et méthodes d'une autre classe. La classe enfant hérite automatiquement du code parent et peut le modifier ou l'étendre.

### Polymorphisme

Capacité pour différents objets de répondre à un même appel de méthode avec des comportements différents selon leur classe.

### Override

Redéfinition d'une méthode héritée dans une classe enfant. Même nom de méthode, implémentation différente.

### Encapsulation

Protection des données internes via attributs privés (`__attribute`).

---

## 🔧 Fonctions Principales

### isinstance(objet, Classe)

Vérifie si un objet est une instance d'une classe. Considère l'héritage.

### issubclass(Enfant, Parent)

Vérifie si une classe hérite d'une autre classe.

### super()

Permet d'appeler les méthodes de la classe parent depuis la classe enfant.

### raise

Lève une exception volontairement pour signaler une erreur.

### type(variable)

Retourne le type exact d'une variable sans considérer l'héritage.

---

## 📖 Classes Implémentées

### BaseGeometry

Classe de base pour toutes les formes géométriques.

**Méthodes:**
- `area()` - Lève Exception (non implémentée, à définir dans sous-classes)
- `integer_validator(name, value)` - Valide qu'une valeur est un entier positif

### Rectangle

Hérite de BaseGeometry. Représente un rectangle avec largeur et hauteur.

**Attributs privés:**
- `__width` - Largeur
- `__height` - Hauteur

**Méthodes:**
- `__init__(width, height)` - Initialise avec validation
- `area()` - Retourne width × height
- `__str__()` - Retourne "[Rectangle] width/height"

### Square

Hérite de Rectangle. Représente un carré (rectangle où largeur = hauteur).

**Attributs privés:**
- `__size` - Taille du côté

**Méthodes:**
- `__init__(size)` - Initialise avec validation, appelle Rectangle.__init__(size, size)
- `area()` - Hérité de Rectangle
- `__str__()` - Retourne "[Square] size/size"

---

## 📁 Structure du Projet
python_oop/inheritance/
├── 0-polymorphism_demo.py    # Démo Animal/Dog/Cat
├── base_geometry.py          # BaseGeometry
├── 1-rectangle.py            # Rectangle basique
├── 2-rectangle.py            # Rectangle complet
├── 1-square.py               # Square basique
└── 2-square.py               # Square complet

---

## 🏗️ Hiérarchie Complète
BaseGeometry
├─ integer_validator()
└─ area() [non implémentée]
│
▼
Rectangle
├─ integer_validator() [hérité]
├─ area() [implémenté: width × height]
└─ str() ["[Rectangle] w/h"]
│
▼
Square
├─ integer_validator() [hérité]
├─ area() [hérité de Rectangle]
└─ str() ["[Square] s/s"]

---

## 🔑 Concepts Techniques

### Name Mangling

Transformation de `self.__attribute` en `self._ClassName__attribute` pour protéger les attributs privés.

### Ordre de Résolution

Python cherche les méthodes d'abord dans la classe de l'objet, puis remonte vers les parents jusqu'à trouver ou lever AttributeError.

### Validation Pattern

Toujours valider les données AVANT de les stocker dans les attributs pour garantir la cohérence de l'état de l'objet.

---

## ✅ Tasks Complétées

- **Task 0:** Introduction Polymorphisme (Animal/Dog/Cat)
- **Task 1:** BaseGeometry (area + integer_validator)
- **Task 2:** Rectangle basique (héritage + validation)
- **Task 3:** Rectangle complet (+ area + __str__)
- **Task 4:** Square basique (héritage Rectangle)
- **Task 5:** Square complet (+ __str__ override)
- **Task 6:** Quiz Final

**Score:** 100% (70/70 pts)

---

## 🎯 Avantages de l'Héritage

**Réutilisation:** Code écrit une fois, utilisé partout  
**Organisation:** Hiérarchie claire reflétant relations logiques  
**Extensibilité:** Ajout de nouvelles formes simplifié  
**Maintenance:** Modifications parent propagées automatiquement  
**Polymorphisme:** Interface commune pour objets différents

---

## 📋 Exigences Techniques

- Python 3.8
- Ubuntu 20.04
- Fichiers exécutables
- Shebang: `#!/usr/bin/env python3`
- Conforme PEP8
- Docstrings obligatoires
- Import via `__import__()` pour classes de base

---

## 🎓 Résumé

**Héritage:** `class Child(Parent):` - Réutilisation du code parent  
**Override:** Même nom de méthode → comportement différent  
**super():** Appel explicite de méthode parent  
**Polymorphisme:** Même interface, implémentations variées  
**Validation:** Contrôle données avant stockage pour cohérence

---

**Projet:** Python OOP - Inheritance & Polymorphism  
**Institution:** Holberton School  
**Status:** ✅ Completed (100%)
