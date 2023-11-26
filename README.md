Projet Media Player


NB: LE BACKEND FONCTIONNE TRÈS BIEN SUR LES MACHINES DE L'ÉCOLE, MAIS JE N'AI PAS EU L'OCASION (SEMAINE ATHENS) DE TESTER LE FRONT SUR LES MACHINES DE L'ÉCOLE,

MAIS FONCTIONNE SUR MON PC QUI UN MACBOOK (DONC INUX), DONC NORMALEMENT TOUT DEVRAIT BIEN FONCTIONNER.



Description

Ce projet est divisé en deux répertoires principaux : cpp_pj pour le backend du projet et swing pour l'interface graphique.

Backend (cpp_pj)
Le répertoire cpp_pj contient l'ensemble du backend du projet. Voici une vue d'ensemble des classes présentes :

Photos: Représente un objet photo.
Vidéos: Représente un objet vidéo.
Films: Représente un objet film.
Pour exécuter le fackend du projet, suivez ces étapes :

Placez-vous dans le répertoire cpp_pj.
Exécutez la commande make run.
Cela lancera le serveur qui permet de jouer une musique dont le nom ou le chemin est reçu de l'interface graphique.



Interface Graphique (swing)
Le répertoire swing est dédié à l'interface graphique de l'application.

Pour exécuter l'interface graphique, suivez ces étapes :

Placez-vous dans le répertoire swing.
Exécutez la commande make run.
L'interface graphique se connecte automatiquement au serveur backend.
Interface Graphique

L'interface graphique comporte trois boutons :

PLAYVIDEO: Permet de jouer une vidéo  présente dans la base de donnée (lié au serveur manager) .  et il faudra juste séléctionné une vidéo et elle  se jouera avec un message de confirmation affiché en bas.
PLAYPHOTO: Permet de jouer une photo  présente dans la base de données (lié au serveur manager) .  et il faudra juste séléctionné une photo et elle  se jouera avec un message de confirmation affiché en bas.
Browse: Permet de jouer une vidéo ou une photo présente dans le répertoire personnel de l'utilisateur. Cliquez sur ce bouton pour choisir un fichier à afficher ou à jouer. Lorsqu'on sélectionne, le morceau ou la photo est immediatement enrégistré dans la base de données (manager)
Exit: Permet de quitter l'application.






Exécution

-Backend :

cd cpp_pj
make run


-Interface Graphique :

cd swing
make run