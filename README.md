# Simulation du Jeu de la Vie

Ce projet implémente le Jeu de la Vie de Conway, un automate cellulaire conçu par le mathématicien britannique John Horton Conway. La simulation est effectuée sur une grille bidimensionnelle de cellules, chacune pouvant être dans l'un des deux états possibles : vivant ou mort. L'évolution du système est déterminée par un ensemble de règles qui dictent comment l'état de chaque cellule change au fil du temps en fonction des états de ses cellules voisines.

## Règles du Jeu de la Vie

Les règles du Jeu de la Vie sont les suivantes :
1. Toute cellule vivante avec moins de deux voisins vivants meurt, comme par sous-population.
2. Toute cellule vivante avec deux ou trois voisins vivants vit jusqu'à la génération suivante.
3. Toute cellule vivante avec plus de trois voisins vivants meurt, comme par surpopulation.
4. Toute cellule morte avec exactement trois voisins vivants devient une cellule vivante, comme par reproduction.

## Description

### main.py

Ce fichier est le point d'entrée du projet. Il lit le fichier de configuration, obtient la graine initiale, crée l'objet Jeu de la Vie et lance la simulation.


### game_of_life.py

Ce module contient la classe `GameOfLife`, qui représente la simulation du Jeu de la Vie de Conway. La classe fournit plusieurs méthodes pour manipuler la grille du jeu et effectuer la simulation.

#### Méthodes de la classe `GameOfLife` :

- `__init__(self, initial_grid: List[List[bool]])` : Le constructeur de la classe initialise le jeu avec une grille initiale donnée.
  
- `evolve(self)` : Cette méthode fait évoluer la grille du jeu d'une génération à l'autre en appliquant les règles du Jeu de la Vie de Conway. Elle met à jour la grille interne du jeu en fonction de l'état actuel de chaque cellule et de ses voisins.
  
- `count_live_neighbors(self, i: int, j: int) -> int` : Cette méthode compte le nombre de voisins vivants d'une cellule donnée dans la grille. Elle parcourt les cellules adjacentes à la cellule spécifiée et compte le nombre de cellules vivantes.
  
- `display_grid(self)` : Cette méthode affiche la grille du jeu dans la console. Elle utilise des symboles `[o]` pour représenter les cellules vivantes et `[ ]` pour représenter les cellules mortes.

- `write_game_states_to_file(output_document: str)` : Cette méthode écrit les états successifs du jeu dans un fichier de sortie spécifié. Elle enregistre chaque génération du jeu dans le fichier avec un numéro de génération correspondant.

#### Attributs de la classe `GameOfLife` :

- `grid` : La grille du jeu représentant l'état actuel des cellules.
  
- `GRID_HEIGHT` et `GRID_WIDTH` : Les dimensions de la grille du jeu.
  
- `states` : Une liste qui enregistre les états successifs du jeu à chaque génération.
  
- `states_count` : Un compteur qui maintient le nombre total de générations simulées jusqu'à présent.

La classe `GameOfLife` fournit une interface pour manipuler et simuler le Jeu de la Vie de Conway. Elle encapsule la logique du jeu et permet de le simuler de manière itérative.

### unit_tests.py

Ce fichier contient les tests unitaires pour les fonctionnalités de la classe `GameOfLife` et les fonctions utilitaires associées.

#### Tests de la classe `GameOfLife` :

- `test_evolve()` : Ce test vérifie si la méthode `evolve()` de la classe `GameOfLife` fonctionne correctement en simulant une évolution d'une génération dans la grille et en vérifiant si l'état de la grille est conforme aux règles du Jeu de la Vie.

- `test_count_live_neighbors()` : Ce test vérifie si la méthode `count_live_neighbors()` de la classe `GameOfLife` compte correctement le nombre de voisins vivants d'une cellule donnée dans la grille. Il teste la fonctionnalité en vérifiant le nombre de voisins vivants pour une cellule spécifique dans différentes configurations de la grille.

#### Tests des fonctions utilitaires :

- `test_read_configuration()` : Ce test vérifie si la fonction `read_configuration()` peut lire correctement les paramètres de configuration à partir d'un fichier de configuration donné. Il teste si les paramètres sont extraits correctement et si les types de données des paramètres sont conformes aux attentes.

- `test_get_initial_seed_custom()` : Ce test vérifie si la fonction `get_initial_seed()` peut récupérer correctement un seed personnalisé à partir de la configuration donnée. Il teste la fonctionnalité en fournissant une configuration avec un seed personnalisé et vérifie si le seed récupéré est conforme aux attentes.

- `test_get_initial_seed_known()` : Ce test vérifie si la fonction `get_initial_seed()` peut récupérer correctement un seed connu à partir de la configuration donnée. Il teste la fonctionnalité en fournissant une configuration avec un seed connu prédéfini et vérifie si le seed récupéré est conforme aux attentes.

Ces tests garantissent que les fonctionnalités de la classe `GameOfLife` et des fonctions utilitaires associées fonctionnent correctement et produisent les résultats attendus dans différentes situations.

### initial_seeds.py

Ce module comprend des motifs de graine initiale prédéfinis pour la simulation du Jeu de la Vie, tels que des planeurs, des clignotants et des oscillateurs.

### config.txt

Le fichier de configuration spécifie les paramètres de la simulation, tels que le nombre de générations, le nom de la graine initiale, le temps d'oscillation et le nom du document de sortie.

## Utilisation

1. Modifiez le fichier `config.txt` pour ajuster les paramètres de la simulation si nécessaire.
2. Exécutez le script `main.py` pour démarrer la simulation.
3. Appuyez sur Entrée pour démarrer la simulation ou sur Ctrl+C pour l'arrêter.
4. La simulation se déroulera pendant le nombre de générations spécifié, affichant l'état de chaque génération et enregistrant l'état final dans le document de sortie.



## Licence

