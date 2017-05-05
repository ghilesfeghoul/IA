Rapport du projet 
==================

Liste des scripts :

		- Test-hard-with-100000-games : 
			Lancement de 100 000 parties de 2 CPU en mode difficile, avec affichage du nombre de victoires
		- Test-50000-gamePlay-with-different-mode : 
			Lancement de 50 000 parties de 2 CPU avec des modes différents 
			   -> Easy VS Easy
			   -> EASY VS MEDIUM 
			   -> MEDIUM VS HARD
			   -> EASY VS HARD
			   -> MEDIUM VS MEDIUM
			   -> HARD VS HARD
			A la fin du mode Hard VS Hard, on enregistre le réseau de neurone dans un fichier sérialisé
		- AmeliorationParAggregation :
		    Dans ce fichier, on a crée un script qui permet d'améliorer encore notre réseau de neurones en créant une aggrégation entre 2 réseaux de neurones (réseau d'une machine qui commence en premier en mode 'hard' + réseau d'une machine qui commence en premier en mode 'medium')
		- Final-gameplay :
			Jeu final en mode console, on peut entrer notre nom et le mode dans lequel on veut jouer et la partie commence
			Le mode Hard utilise le fichier sérialisé créé avec le script 3
		- Optionnel :
			Lancement de 15 000 parties de 2 CPU en mode difficile, avec affichage des taux d'erreurs
        - Interface_Jeu et Main
            On lance le script Main qui utilise le script Interface_Jeu pour simuler le même scénario que le script 'Final-gameplay' en mode fenêtre graphique pour récupèrer le nom et le mode puis passe au mode console pour continuer à jouer
Question 5

		L'ordinateur fait des erreurs car la version "easy" utilise seulement une fonction
		random pour jouer, le facteur hasard a forcèment joué un rôle dans les résultats.

Question 6

		Avec la version Médium, on ne peut pas parler d'apprentissage, car c'est nous qui avons programmé comment elle joue selon notre algorithme et les situations, donc la machine n'a 
		pas appris d'elle-même afin de s'améliorer.
        
Question 8

		Le but de la méthode de faire jouer l'ordinateur contre lui-même est de faire de l'apprentissage.
		En effet, avec le réseau de neurones, on va privilégier le chemin par lequel il est passé lorsqu'il 
		a gagné. On va donc attribuer des récompenses aux synapses que la machine a emprunté lorsqu'elle a 
		gagné.
		On va donc la faire jouer un grand nombre de fois afin qu'elle puisse apprendre d'elle-même et de devenir 
		de plus en plus forte.

		Dans le cas du script 'Test-hard-with-100000-games', on peut remarquer qu'après les 100 000 parties, 
		la machine 1 remportera beaucoup plus de victoires (environ 90%) que la machine 2, car cette dernière a découvert le "biais", c'est à dire 
		la technique pour gagner. Et vu que c'est elle qui joue en premier, elle gagne la plupart du temps.

        On a exploité ces résultats pour mettre en oeuvre le script d'aggrégation
        
Question 9

		En jouant contre l'ordinateur en mode Hard (et en 2ème joueur), il est impossible de gagner.
		L'ordinateur fera tout pour nous ammener à 13 batons, puis 9, puis 5 pour ensuite que l'on perde.
        L'ordinateur utilise l'un des deux fichier (reseau.nmd qui contient les résultats du fichier Test-hard-with-100000-games' et reseau_ameloreAgregat.nmw qui contient les résultats du script d'aggrégation), ce qui rend la tâche difficile à l'humain pour gagner

Question Optionnelle

		Pour gagner une partie en étant le premier joueur, nous devons faire en sorte de tomber sur les batons restants :
		13, 9 et 5. Si la première machine à chaque tour ne tombe pas sur un de ses chiffres après avoir joué (Multiples de 4 + 1),
		on comptabilise une erreur. A la fin de la partie, on obtient le taux d'erreur en divisant le nombre d'erreurs par le nombre
		de coups au total.
		Pour la deuxième machine, on ne compte pas forcément d'erreur puisqu'elle peut ne pas avoir le choix.

		On remarque bien en lançant le script Optionnel que plus les parties avancent et moins les machines font d'erreurs 
		(puisqu'elles apprennent de leurs parties précédentes).

Solution envisagée

		Le fichier qui contient le script d'aggrégation est une des solutions pour améliorer le réseau de neurones