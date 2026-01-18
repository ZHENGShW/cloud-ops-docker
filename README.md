# Tp docker

## Exercice 1 : Manipulation de base des conteneurs
La commande 'docker --version' a été exécutée avec succès, et la version est : Docker version 29.1.3, build f52814d
Télécharger de l'image 'hello-world' et lancer du conteneur avec succès
Lister les images par utiliser de 'docker images'.
Lister les conteneurs par utiliser de 'docker ps -a' pour visualiser les ID des conteneurs précédents.
Supprimer des conteneurs et des images de test.

## Exercice 2 : Création d'un serveur web avec Docker
Téléchargerr de l'image officielle 'nginx'.
Lancer du conteneur en arrière-plan avec mappage de port : 'docker run -d -p 8080:80 --name mon_nginx nginx'.
Accès réussi à la page d'accueil Nginx via 'http://localhost:8080', et la page affiche 'Welcome to nginx!'.
Après le test, arrêter du conteneur par 'docker stop' et supprimer par 'docker rm'

## Exercice 3 : Déploiement d'une application Python Flask
Créer 2 fichier : 
---- app.py : : Code source de l'application web
---- Dockerfile : Instructions de construction de l'image.
Lancer la commande 'docker build -t mon-app-flask .' pour construire l'image, et la commande 'docker run -d -p 5000:5000 --name container_flask mon-app-flask' pour le lancement du conteneur.
Le résultat est que l'application est accessible sur 'http://localhost:5000' et affiche le message "Hello, World!".

## Exercice 4 : Utilisation de docker compose 
Créer 3 fichiers : 
---- docker-compose.yml : Orchestration des services my-web-app et mongo_service
---- app.py : >Code modifié pour se connecter à mongodb://mongo_service:27017/
---- Dockerfile : Ajout de la dépendance pymongo.
Lancer la commande docker compose up --build : Construction et lancement simultané des conteneurs
Les résultats sont que L'application est accessible sur 'http://localhost:5000' et La page affiche "Succès : Flask s'a connecté à la MongoDB!", confirmant la connexion à la base de données