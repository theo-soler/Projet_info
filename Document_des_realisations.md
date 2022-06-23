# Livrable : 
Script python permettant d’extraire automatiquement et consolider le jeu de données de cours de matières premières stratégiques (acier, bois, pétrole, cuivre, aluminium, matières plastiques et polymères) pour le groupe Algeco ainsi qu’une analyse des corrélations avec les prix d’achats aux fournisseurs.

# Prélude :

Pour créer l'environnement conda, nommé `projet_info_06_2022`:

    conda env create -f environment.yml

**Structure du jeu de données :**

|Matières premières| Mois (Date)| Pays|Cours (Prix & devise)|Taux de change|Prix (€)|Taux de variation|
| :-------------   | :--------: | :-: | :-----------------: | :----------: | :----: | :-------------: |
| Acier            |            |     |                     |              |        |                 |
| Bois             |            |     |                     |              |        |                 |
| Pétrole          |            |     |                     |              |        |                 |
| Cuivre           |            |     |                     |              |        |                 |
| Aluminium        |            |     |                     |              |        |                 |
| ...              |            |     |                     |              |        |                 |

Remarques : 
-	Indiquer les sources (ex : LME, …)
-	Documenter le script 
-	Nice to have : Dashboard power BI pour la visualisation des données

# Avancement du projet :
## Phase 1 :
Sources de données fiables pour l’acquisition du cours de matières premières suivantes :
-	[x]	Aluminium
-	[x]	Oil (Brent)
-	[x] 	Steel (Coils & Beams)
-	[x]	Copper
-	[ ]	Wood
-	[ ] … 

En se basant sur les aspects suivants : 
Fourni le cours de la matière considérée sur le marché européen, sur une période d’au moins 2 ans avec une actualisation mensuelle.

## Phase 2 :
- [x] Script python permettant une acquisition automatique du cours sur les sources précédemment identifiées 

Choix techniques :
-	Utilisation de la librairie Beautiful Soup (web scraping)
-	Stockage des données acquis au format .csv

## Phase 3 : 
- [x] Consolidation du jeu de données sous le format suivant :

| Date     | Cours    | Variable        |
| :-------------: | :-------------: | :--------:    |
| Janvier 2019       |        ...     |      Aluminium         |
| ...      |        ...     |     ...        |
| Mai 2022       |        ...     |      Aluminium         |
| Janvier 2019       |        ...     |      Copper         |
| ...      |        ...     |     ...        |
| Mai 2022       |        ...     |      Copper         |
| ...      |        ...     |     ...        |

