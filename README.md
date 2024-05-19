# Architectures applicatives

Le prototype est accessible dans la branche **prototype**

L'application finale est dans la branche **main**

# Installation des dépendances 
```
pip install -r requirements.txt
```

# Lancement de l'application en console

À la racine du projet : 
```
py App/console.py
```

# Lancement de l'application en console
À la racine du projet :
```
py App/api.py
```

# Lancement de l'application en console
```
# À la racine du projet
py App/api.py
```

## Template de la requête curl à executer
```
# À la racine du projet
curl -X POST http://localhost:5000/check -H "Content-Type: application/json; charset=utf-8" -H "Accept-Language: fr" -d "{\"text\":\"chaine\"}"
```
### Choix de votre language grâce aux headers **Accept-Language**
### Choix de votre chaine de caractère à analyser dans le json avec la clé **text**, ici **chaine**

