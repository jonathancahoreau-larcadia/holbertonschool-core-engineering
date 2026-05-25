======================================================================
README - Python File I/O Essentials
======================================================================

INTRODUCTION & CONTEXT
----------------------
Travailler avec l’entrée et la sortie est un pilier de la programmation.
C’est ce qui permet à un programme de dialoguer avec le monde extérieur :
lire des données, écrire des résultats, conserver des informations après
l’exécution.

En Python, cela passe principalement par la manipulation de fichiers :
ouvrir, lire, écrire, ajouter du contenu… mais aussi gérer correctement
les ressources pour éviter les fuites, les corruptions ou les pertes de
données.

Ce projet initie l’étudiant aux mécanismes d’I/O en Python, en mettant
l’accent sur :

- l’ouverture et la fermeture des fichiers
- la lecture complète ou ligne par ligne
- l’écriture et l’ajout de texte
- la gestion du curseur dans un fichier
- l’importance du contexte `with` pour sécuriser les opérations

Ces notions sont indispensables dans des applications réelles : traitement
de données, stockage de résultats, communication entre systèmes, APIs,
pipelines, etc.

Les débutants sous‑estiment souvent les pièges liés :
- aux encodages,
- aux fichiers manquants,
- à la mauvaise gestion des ressources.

Ces aspects doivent être abordés avec rigueur pour éviter des bugs
subtils ou des pertes de données.

----------------------------------------------------------------------
RESOURCES
---------

À lire ou regarder :

- 7.2. Reading and Writing Files
- 8.7. Predefined Clean-up Actions
- *Dive Into Python 3* : Chapter 11. Files
  (jusqu’à “11.4 Binary Files” inclus — chapitre commençant page 263)
- *Learn to Program 8 : Reading / Writing Files*

----------------------------------------------------------------------
LEARNING OBJECTIVES
-------------------

À la fin de ce projet, vous saurez :

1. Ouvrir un fichier en Python.
2. Écrire du texte dans un fichier.
3. Lire l’intégralité du contenu d’un fichier.
4. Lire un fichier ligne par ligne.
5. Déplacer le curseur dans un fichier (`seek`, `tell`).
6. Garantir la fermeture d’un fichier après utilisation.
7. Comprendre et utiliser correctement l’instruction `with`.

----------------------------------------------------------------------
CONCLUSION
----------

La maîtrise des opérations d’entrée/sortie est un prérequis essentiel
pour évoluer vers des sujets plus avancés : bases de données, APIs,
traitement de données, automatisation, et bien plus encore.

Ce projet pose les fondations d’une manipulation fiable, propre et
professionnelle des fichiers en Python.

======================================================================
