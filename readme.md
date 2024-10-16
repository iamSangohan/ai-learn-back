# Guide pour Exécuter le Script de Chargement des Données

Ce guide vous explique comment installer les dépendances nécessaires et exécuter le script Python pour charger les données dans la base de données.

## Prérequis

- Python 3 doit être installé sur votre machine. Vous pouvez vérifier la version installée avec la commande suivante :

    ```bash
    python3 --version
    ```

- Assurez-vous également que `pip` (le gestionnaire de paquets pour Python) est installé. Vous pouvez vérifier avec :

    ```bash
    pip --version
    ```

## Étapes pour Exécuter le Script

1. **Installer la bibliothèque `pandas`**

   `pandas` est une bibliothèque nécessaire pour manipuler les données dans le script. Installez-la en exécutant la commande suivante :

    ```bash
    pip install pandas
    ```

2. **Exécuter le Script**

   Une fois `pandas` installé, vous pouvez exécuter le script `load.py` pour charger les données. Utilisez la commande suivante :

    ```bash
    python3 load.py
    ```

   Assurez-vous d'être dans le même répertoire que le fichier `load.py` lorsque vous lancez cette commande.

## Remarques

- Si vous rencontrez des problèmes avec l'installation de `pandas`, vérifiez que `pip` est correctement configuré et que vous avez accès à Internet.
- Si le script ne fonctionne pas avec `python3`, essayez d'utiliser `python` à la place, selon la configuration de votre système :

    ```bash
    python load.py
    ```

## Aide Supplémentaire

Si vous avez des questions ou des problèmes, veuillez consulter la documentation officielle de `pandas` ou vérifier la version de Python installée sur votre machine.

- [Documentation de Pandas](https://pandas.pydata.org/)
- [Documentation de Python](https://docs.python.org/3/)

