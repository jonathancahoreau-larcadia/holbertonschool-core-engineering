======================================================================
README - Python Execution Modes, pip & Virtual Environments
======================================================================

INTRODUCTION & CONTEXTE
-----------------------
Python peut exécuter du code de deux manières principales :

1. Interactivement via l’interpréteur (REPL), où chaque expression est
   évaluée immédiatement.
2. En exécutant un fichier script, où le code est lu séquentiellement
   sans affichage automatique.

Comprendre ces deux modes est essentiel pour un usage professionnel :
- installation d’outils Python,
- influence de l’environnement d’exécution,
- gestion des dépendances,
- isolation via environnements virtuels.

Ce projet vise à construire une compréhension claire du fonctionnement
réel de Python dans un workflow de développement.

----------------------------------------------------------------------
OBJECTIFS PEDAGOGIQUES
-----------------------

A la fin de ce projet, vous serez capable de :

1. Comprendre l’évaluation des expressions et instructions
   - Différencier expression et instruction.
   - Prédire quand le REPL affiche automatiquement un résultat.

2. Distinguer mode interactif et mode script
   - Expliquer pourquoi un script n’affiche rien sans print().
   - Créer un script Python portable et exécutable.

3. Installer et utiliser des outils avec pip
   - Installer un outil via pip.
   - Comprendre les implications d’une installation globale.

4. Comprendre les conflits liés aux installations globales
   - Conflits de versions.
   - Dépendances incompatibles.
   - Manque de reproductibilité.

5. Utiliser un environnement virtuel (venv)
   - Créer et activer un environnement virtuel.
   - Installer des outils localement dans un projet.
   - Démontrer l’isolation des dépendances.

----------------------------------------------------------------------
CONCEPTS CLES
-------------

Mode interactif (REPL)
- Affiche automatiquement les valeurs des expressions.
- Idéal pour tester rapidement du code.

Mode script
- Exécution séquentielle.
- Nécessite print() pour produire une sortie.
- Utilisé pour des programmes reproductibles.

pip et gestion des outils
- pip install <package> installe un outil Python.
- Installation globale = risque de casser d’autres projets.

Environnements virtuels (venv)
- Créent un espace isolé pour un projet.
- Permettent d’utiliser des versions spécifiques de bibliothèques.
- Garantissent la reproductibilité.

----------------------------------------------------------------------
COMPETENCES ACQUISES
--------------------

- Compréhension du fonctionnement interne de l’interpréteur Python.
- Ecriture de scripts exécutables et portables.
- Maîtrise de pip pour installer des outils.
- Compréhension des risques liés aux installations globales.
- Utilisation correcte de venv pour isoler les dépendances.

----------------------------------------------------------------------
CONCLUSION
----------

Ce projet constitue une base essentielle pour tout développeur Python
souhaitant travailler proprement, éviter les conflits de dépendances
et comprendre les mécanismes fondamentaux de l’exécution du code.

Il prépare également à des workflows professionnels plus avancés :
packaging, tests, CI/CD, conteneurisation, etc.

======================================================================
