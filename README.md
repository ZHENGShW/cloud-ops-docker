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