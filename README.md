# DA-Python-P11
Plateforme de réservation de places pour des compétitions pour l'entreprise GÜDLFT.

# GÜDLFT

GÜDLFT est mon onzième projet en Python dans le cadre de ma formation de Développeur d'Application Python via la plateforme de formation OpenClassrooms. <br>
Contexte: L'entreprise GÜDLFT est une société qui a créé une plateforme numérique pour coordonner les compétitions de force en Amérique du Nord et en Australie.
GÜDLFT a commencé par organiser des compétitions pour les clubs locaux, a gagné en popularité et accueille désormais exclusivement des compétitions pour les entreprise de vêtements de fitness de marque. Peu après avoir célébré son cinquième anniversaire, la société s'est retrouvée critiquée sur les réseaux sociaux par rapports aux moyens utilisés pour le développement de l'application.
GÜDLFT a alors décidée de créer une application plus légère et moins coûteuse.

Je suis alors chargée de corriger les erreurs et bugs présents dans le projet [GitHub Pages](https://github.com/OpenClassrooms-Student-Center/Python_Testing), ainsi que d'implémenter de nouvelles fonctionnalités. Chaque correction / ajout se trouve sur sa propre branche, et est supporté(e) par une suite de tests via Pytest et Locust.

# Initialisation du projet 

## Windows :

`git clone https://github.com/AlexianeBA/Python_Testing` <br>
`python3 -m venv venv`<br>
`source venv/bon/activate`<br>
`pip install -r requirements.txt`

# Utilisation

1. Lancer le serveur Flask:

    `export FLASK_APP=server.py`<br>
    `python3 -m flask run`
2. Accéder au site:<br>
   http://127.0.0.1:5000/

# Tests

* Tous les paquets nécessaries pour lancer les tests sont inclus dans 'requirements.txt'.

## Tests unitaires/intégration
Pytest est utilisé pour réaliser les tests unitaires et d'intégration.
Pour lancer les tests unitaires et d'intégration :
`pytest tests`

Afin de générer un rapport des couvertures des tests, le module Coverage a été installé et utilisé :
`coverage run -m pytest tests`
`coverage html`


## Test de performances

Le test de performance est effectué grace à Locust. Pour lancer le serveur de test :
`locust tests/`

Se rendre sur l'adresse http://localhost:8089 et entrer les options souhaitées, avec pour 'host' l'adresse par défaut du site (http://127.0.0.1:5000/).