![Univ Rouen](https://s-media-cache-ak0.pinimg.com/originals/e8/39/3e/e8393e57f4a0e26cab93e22608d40b94.png)
# Apprentissage : Jeu des bâtons
Réseau de neurones simple appliqué au "jeu des bâtons".
## Description
Le but de ce projet est d’apprendre à la machine comment jouer au mieux au "jeu des bâtons".
Il existe en eﬀet une "technique" pour gagner en fonction du nombre de bâtons à jouer et de quel joueur commence la partie.
Nous allons utiliser une méthode de réseau de neurones simple (type [perceptron]) pour que la machine apprenne à jouer et découvre ainsi la "technique".

## Règles du jeu
Sur un plateau sont disposés quinze bâtons (le nombre peur varier mais nous prendrons cette valeur durant tout le projet). Deux joueurs s'affrontent et doivent, chacun leur tour, prendre un, deux ou trois bâtons. Celui qui prend le dernier bâton a perdu.

#### Modes de jeu
Dans notre programme, la machine pourra jouer selon trois modes :
   
    - Easy : 
             Elle joue aléatoirement 1, 2 ou 3 bâtons (dans la limite des règles)
    - Medium : 
             Elle joue aléatoirement sauf à la ﬁn où elle ne commet pas d’erreurs évidentes
    - Hard : 
             Elle joue via son réseau de neurones grâce à l’apprentissage

Le travail a été divisé en trois phases :
    
    - prise en main du code existant, premiers tests de jeu
    - phase d’apprentissage : où on a entrainé le réseau de neurones en jouant un grand nombre de fois
    - phase de tests : on a crée plusieurs scénarii pour observer les comportements de la machine en fonction de plusieurs paramètres et notamment vériﬁer si la machine joue bien parfaitement en mode "hard".

## Auteurs

* [Ghiles FEGHOUL](mailto:ghiles.feghoul@gmail.com)
* [Yacine HOUMOR](mailto:yacine.houmor@gmail.com)

## Références
[perceptron] - perceptron

[Apprentissage_JeuDesBatons] - github

[perceptron]: <https://fr.wikipedia.org/wiki/Perceptron> 
[Apprentissage_JeuDesBatons]: <https://github.com/QuentinBrodier/Apprentissage_JeuDesBatons>