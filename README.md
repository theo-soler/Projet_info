# Livrable : 
Script python permettant d’extraire automatiquement et consolider le jeu de données de cours de matières premières stratégiques (acier, bois, pétrole, cuivre, aluminium et polymères) pour le groupe Modulaire ainsi qu’une analyse des corrélations avec les prix d’achats aux fournisseurs.

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
-	[x] Steel (Coils & Beams)
-	[x]	Copper
-	[ ]	Wood
-	[ ] … 

Les sites utilisés sont :
- Boursorama : 
    - taux de change dollar - euros : https://www.boursorama.com/bourse/devises/cours/historique/3fUSD_EURfromSymbol=USD&toSymbol=EUR&fromLabel=dollar&toLabel=euro
    - cuivre : https://www.boursorama.com/bourse/indices/cours/7xCAUSD15M/
    - aluminium alloy : https://www.boursorama.com/bourse/indices/cours/historique/7xAAUSD15M
- Le site de la banque de St Louis pour le brent : https://fred.stlouisfed.org/series/DCOILBRENTEU#
- le site du conseil national routier pour le fuel en France : www.cnr.fr/espaces/13/indicateurs/43?noContext=1
- Pour l'acier, les valeurs proviennent du site MEPS (https://portal.mepsinternational.com/?logout=true) mais n'ayant pas de login, on a utilisé des extracts fournis


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

- [x] Finalisation du tableau de données et export au format csv

## Phase 4 :
- [x] Structuration de l'architecture du repo (github) :

    - Readme.md (document des réalisations)
    - Script (récuperation des données dans init et analyse dans main) :
        - init.py
        - main.py
    - Result (resultat de l'analyse)
    - Data (extracts fournis)
    - Data_extraite (données extraites par web_scrapping)

- [x] Etude de corrélations avec les prix d'achats aux fournisseurs (fenêtres, panneaux, toits)

- [x] Etablissement de la licence (GNU general public licence version 3)

choix technique :

- Utilisation de la méthode ccf (librairie statsmodels) pour l'étude des corrélations croisées
