======================================================================
README - Functions, Modules & Execution Flow in Python
======================================================================

INTRODUCTION & CONTEXT
----------------------
À mesure qu’un programme grandit, répéter du code devient inefficace et
source d’erreurs. Les fonctions permettent d’encapsuler un comportement
dans un bloc réutilisable. Les modules permettent d’organiser ces blocs
dans des fichiers séparés et de les réutiliser proprement.

Ce projet introduit les notions suivantes :

- Définition de fonctions et valeurs de retour
- Flux d’exécution à l’intérieur et à l’extérieur d’une fonction
- Différence fondamentale entre print et return
- Comment Python exécute un fichier
- Effets de l’importation d’un fichier sur son exécution
- Réutilisation de fonctions et de variables entre plusieurs fichiers

L’ordre des exercices est intentionnel : on commence par définir des
fonctions, puis on apprend à organiser le code de manière sûre dans
plusieurs fichiers.

----------------------------------------------------------------------
LEARNING OBJECTIVES
--------------------

À la fin de ce projet, vous serez capable de :

1. Définir des fonctions avec paramètres et valeurs de retour.
2. Distinguer clairement print et return.
3. Implémenter de la logique interne avec conditions et boucles.
4. Comprendre comment Python exécute le code de niveau supérieur.
5. Expliquer le rôle de :  if __name__ == "__main__"
6. Importer des fonctions depuis d’autres fichiers.
7. Importer des variables depuis d’autres fichiers.
8. Écrire des scripts qui se comportent correctement lorsqu’ils sont
   exécutés directement ou importés comme modules.

----------------------------------------------------------------------
CONCEPTS CLÉS
-------------

Fonctions
- Encapsulent du code réutilisable.
- return renvoie une valeur exploitable.
- print affiche uniquement pour l’utilisateur.

Modules
- Fichiers Python contenant fonctions et variables.
- Peuvent être importés dans d’autres scripts.

Exécution d’un fichier
- Le code de niveau supérieur est exécuté immédiatement.
- Les fonctions sont seulement définies, pas exécutées.

Importation
- Exécute le code de niveau supérieur du fichier importé.
- Peut provoquer des effets indésirables si non contrôlé.

if __name__ == "__main__"
- Empêche l’exécution automatique lors d’un import.
- Permet d’écrire des tests ou un point d’entrée propre.

----------------------------------------------------------------------
CONCLUSION
----------

Ce projet constitue une base solide pour écrire du code Python propre,
réutilisable et organisé. Il prépare à des pratiques professionnelles :
structuration en modules, séparation logique/exécution, tests internes,
et création de scripts fiables.

======================================================================
