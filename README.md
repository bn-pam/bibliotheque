# bibliotheque

# --------- Guilhem ------------
1. Qu'est ce qui distingue SQlite de la plupart des autres moteurs sql? (postgre, Oracle,mysql):


# --------- Laetitia ------------
2. Quels sont les avantages et les limitations de sqlite
AVANTAGES: 
* faible besoin en mémoire
* sans autre logiciel serveur
* polyvalence, grande compatibilité
* fichiers faciles à sauvegarder et à transporter 
* indépendance par rapport à une structure serveur-client
* faible consommation de ressources
* accès unifié aux données
* disponible sans licence

LIMITATIONS:
* pas de possibilités d'avoir plusieurs comptes utilisateurs
* pas de demande de données à partir du client possible
* pas de possibilité de plusieurs connexions à la fois
* manque cryptage de données intégré
* certains formats (date, ...) ne sont pas pris en charge

ORM Object-Relational Mapping
= programme qui sert d'interface entre une application et une bdd relationnelle pour simuler une bdd orientée objet
> réduit la quantité de code
> couche logicielle supplémentaire

SQLAlchemy
= boîte à outils Python SQL et ORM
vient traduire en fonction de l'engine pour travailler avec n'importe quelle bdd

2. Quel est l'avantage d'utiliser Sqlalchemy par rapport à pymysql, psycopg2 ou sqlite3 ?
pymysql : lib qui permet d'interroger une base mysql
psycopg2 : lib qui permet d'interroger une base PostgreSQL "adaptateur de base de données"
sqlite3 : lib qui permet d'interroger une base sqlite3
> librairies orientées fonctionnelles (plutôt qu'objet)

engine : crée la structure de la bdd (trouve l'adresse et s'y connecte) et gère la connexion physique (connexion de bas niveau)
session : gère le niveau ACID des transactions - modifie les données dans la bdd

Atomicité : toute la transaction réussit ou tout est annulé
Cohérence : l'état final doit être cohérent avec les règles (sinon annulé)
Isolation : pas d'accès aux autres étapes de la transaction
Durabilité : une fois que la transaction est validé, pas de retour en arrière possible