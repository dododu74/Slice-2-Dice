# Slice 2 Dice

## Présentation

Je veux faire un jeu de team building à la façon de *Slice & Dice*. En utilisant Pygame.

![Slice & Dice](Images/Slice_dice.png)

## Fonctionnalités 

Le joueur exécute le fichier python `main.py`. Une magnifique fenêtre s'ouvre alors face a lui. La bibliothèque **Pygame** nous permet d'ouvrir cette fenêtre et d'afficher des rectangles colorées.

## Changelog


### V2 :

* Création de deux modules différents :
    * Affichage qui gère une fonction affiche(scène), qui va afficher les élément de la scène.
    * TAD implémentant différents types de TAD.
* Le TAD utilisé est une pile qui permettra la mise en place de priorité de lors d'affichage d'une scène, plus le calque est en bas dans la pile, plus il sera affiché au premier plan 

![Pile](Images/calques.jpg)

### V1 :

* Le programme est en mesure d'ouvrir une fenêtre et de la fermer
* On code des rectangles qui vont être définis/positionnés par la scène 1, on implémente la class Rectangle et Scène.

## Roadmap, Idées 

* Ajouter une priorité sur les rectangles, définissant leurs ordre d'affichage.
* Utiliser une bibliothèque locale pour l'ensemble des fonctions d'affichages :
    + Permettre l'affichage total d'une scène en fonction des priorités d'affichages des rectangles.
* Création de scènes différentes
* Permettre le changement de scènes (expérimentalement: par appuie d'une touche)

*etc...*
***
