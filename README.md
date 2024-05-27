# bibliotheque

# --------- Guilhem ------------

### _1. Qu'est ce qui distingue SQlite de la plupart des autres moteurs sql? (postgre, Oracle,mysql):_

* Système BDD relationnel **très léger** et facile à installer.
* **Pas besoin de mise en place d'un serveur**. Donné stocké dans un fichier indépendant de la plateforme.
* **Exetuction rapide** (car sur la même machine. pas de serveur, pas de latence réseau). 
* Moteur de BDD le plus utilisé au monde (firefox, skype...). Très populaire sur les système embarqué (mobile) 

### _2. Quels sont les avantages et les limitations de sqlite:_
**AVANTAGES:** 
* Installation sur les systèmes embarqués
* stable et fiable : existe depuis l'an 2000
* Batterie de test (code et script)
* Excécution des tests rapides
* Faible consommation en ressource

**LIMITES:** 
* Acces en écriture et lecture conflictuel car un seul accès au fichier "BDD".
* Peu de typage (classes de stockage)
* Durabilité des données. Si on perd le fichier BDD, on perde notre base. 
 
**Les commandes SQL qui ne fonctionne pas sur SQLite:** 
* ALTER TABLE
* FOR EACH ROW triggers
* Writing to VIEW
* GRANT and REVOKE