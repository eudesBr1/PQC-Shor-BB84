Projet de Cybersécurité Post-Quantique : Shor et BB84
Ce dépôt contient mon travail sur l'étude de la menace quantique (algorithme de Shor) et une solution de distribution de clés par la physique (protocole BB84). Ce projet s'inscrit dans un benchmark global réalisé par notre groupe pour comparer les solutions de sécurité actuelles et futures.

1. Objectifs du projet
L'idée était de simuler deux aspects fondamentaux :

La menace : Montrer comment l'algorithme de Shor rend obsolète le chiffrement RSA en factorisant les nombres premiers beaucoup plus rapidement qu'un ordinateur classique.

La défense : Simuler le protocole BB84 pour prouver que toute tentative d'interception par un espion (Eve) est détectable physiquement par une augmentation du taux d'erreur (QBER).

2. Structure du dépôt
/src : Contient les scripts Python pour les benchmarks et les simulations de circuits.

/results : Contient les données brutes (CSV) et les graphiques générés (PNG).

/docs : Contient ma fiche de synthèse d'une page pour la présentation orale.

3. Résultats obtenus
Les simulations ont permis de mettre en évidence deux points clés :

Shor : Le temps de calcul classique pour RSA croît de manière exponentielle avec la taille de la clé, alors que pour Shor, cette croissance est polynomiale. Cela confirme que doubler la taille des clés RSA ne suffira pas face à un ordinateur quantique.

BB84 : Le benchmark montre que sans espion, le taux d'erreur est de 0%. Avec une interception, le taux d'erreur moyen monte à environ 25%, ce qui permet une détection immédiate de l'intrusion.

4. Installation et utilisation
Pour reproduire les résultats et générer les graphiques, il faut installer les dépendances suivantes :

Bash

pip install pandas matplotlib qiskit qiskit-aer numpy
Ensuite, lancez les scripts de benchmark :

Bash

python src/shor_bench.py
python src/bb84_bench.py
Les fichiers de résultats seront automatiquement créés dans le dossier /results.