======================================================================
REAL-TIME COMMUNICATION WITH WEBSOCKETS
======================================================================

INTRODUCTION
------------
Le modèle traditionnel HTTP fonctionne en requête–réponse : le client envoie
une requête, le serveur répond, puis la connexion se termine. Ce modèle est
insuffisant pour les applications nécessitant des mises à jour continues :
    - systèmes de chat,
    - tableaux de bord en temps réel,
    - outils collaboratifs,
    - jeux en ligne,
    - notifications instantanées.

Les WebSockets résolvent ce problème en établissant une connexion persistante
entre le client et le serveur. Une fois ouverte, cette connexion permet un
échange bidirectionnel continu, sans réouverture de session.

Ce projet vous apprend à construire un système de communication en temps réel
basé sur WebSockets en Python.

----------------------------------------------------------------------
CONTEXT
-------
Vous allez implémenter progressivement :

    - un serveur WebSocket,
    - des clients capables de communiquer avec ce serveur,
    - un échange de messages entre plusieurs participants,
    - un routage et une validation basique des messages,
    - une intégration avec un client web.

Chaque étape dépend du comportement construit précédemment.

----------------------------------------------------------------------
LEARNING OBJECTIVES
-------------------
À la fin de ce projet, vous devez être capable de :

Implement a WebSocket server using asynchronous programming
    Utiliser async / await et la librairie websockets.

Handle multiple concurrent client connections
    Gérer plusieurs connexions simultanées sans bloquer le serveur.

Send and receive messages in real time
    Échanger des données instantanément via une connexion persistante.

Implement different message exchange patterns
    Diffusion, messages privés, broadcast, etc.

Enforce a defined message format when required
    Respecter strictement les formats imposés pour l’évaluation.

----------------------------------------------------------------------
RESOURCES
---------
Intro Videos (à regarder avant de commencer) :
    Be a Better Dev – API REST (HTTP) vs WebSockets (7 min)
    FreeCodeCamp – A Beginner's Guide to WebSockets (30 min)

Documentation :
    websockets documentation
    Python asyncio documentation
    MDN WebSockets API

----------------------------------------------------------------------
GENERAL REQUIREMENTS
--------------------
Environment used for correction :
    - Ubuntu 20.04
    - Python 3.x

You must use :
    - the websockets library
    - asynchronous programming (async / await)

Your implementation must :
    - behave exactly as specified
    - handle continuous communication correctly
    - support multiple concurrent connections when required

Unless explicitly stated, do not :
    - introduce additional frameworks
    - modify the communication protocol
    - add features beyond the requirements

----------------------------------------------------------------------
IMPORTANT NOTES
---------------
- La communication est persistante : les connexions restent ouvertes.
- Plusieurs clients peuvent interagir simultanément.
- Les formats de messages doivent être respectés à la lettre.
- Toute déviation du comportement attendu peut entraîner un échec
  lors de l’évaluation.

----------------------------------------------------------------------
FINAL REMARKS
-------------
Ce projet vous apprend à :
    - construire un système de communication en temps réel,
    - comprendre les connexions persistantes,
    - gérer des clients concurrents,
    - structurer un protocole simple mais fiable,
    - utiliser asyncio et websockets de manière professionnelle.

La précision du comportement est essentielle. Les WebSockets sont puissants,
mais sensibles aux erreurs de logique. Ce projet vous donnera une base solide
pour créer des applications interactives modernes.

======================================================================
