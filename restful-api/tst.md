# ✅ HBnB Part 2 — Testing & Validation (Endpoints + Models)

## 🎯 Objectif de la tâche
Cette tâche vise à prouver que l’API est correcte et robuste en combinant :

1) Validation au niveau des modèles (Business Logic Layer)  
2) Tests manuels “black-box” (cURL + Swagger UI)  
3) Tests automatisés (unittest ou pytest)  
4) Rapport de test (cas OK + cas d’échec + observations)

Le but n’est pas seulement “que ça marche”, mais que :
- les codes HTTP soient cohérents (200/201/400/404)
- les formats JSON soient stables
- les erreurs soient propres et prévisibles
- les relations (Place ↔ User/Amenity, Review ↔ User/Place) restent cohérentes

---

# 1) Validation au niveau Business Logic (Models)

## 1.1 Principe
Les validations doivent être **dans les modèles**, pas uniquement dans l’API.
Flask-RESTx valide surtout :
- champs requis présents
- types basiques (string/int/float)

Mais les règles métier (email valide, rating 1..5, lat/long bornés…) appartiennent aux modèles.

## 1.2 Checklist validations attendues

### User
- first_name non vide
- last_name non vide
- email non vide
- email au format valide (regex)
- longueurs max (50) si déjà implémentées
- `.strip()` conseillé pour supprimer espaces inutiles

Erreurs courantes :
- accepter `"   "` comme prénom (doit être considéré vide après strip)
- accepter email sans `@` ou sans domaine

### Amenity
- name non vide
- (optionnel selon implémentation) longueur max 50

### Place
- title non vide
- price float >= 0 (ou > 0 selon l’énoncé, mais attention à la cohérence)
- latitude entre -90 et 90
- longitude entre -180 et 180
- owner doit être un objet User (la conversion owner_id → owner se fait dans la façade)
- amenities doit rester une liste d’objets Amenity une fois convertie dans la façade

### Review
- text non vide
- rating entier entre 1 et 5
- user doit être un objet User existant
- place doit être un objet Place existant

Important :
- La validation “user_id existe” et “place_id existe” se fait dans la façade (car le modèle Review reçoit déjà des objets).
- Le modèle Review valide la cohérence des objets reçus (type User / Place).

---

# 2) Types de tests à réaliser (séparation claire)

## 2.1 Tests manuels “black-box”
Objectif :
- Tester l’API comme un client externe
- Sans toucher au code
- En observant réponses JSON + status codes

Outils :
- cURL
- Swagger UI (Flask-RESTx)

## 2.2 Tests automatisés (unittest/pytest)
Objectif :
- Reproduire les tests sans dépendre d’une action manuelle
- Pouvoir relancer rapidement après modifications
- Couvrir cas OK + erreurs + limites

Outils :
- unittest (standard library)
- ou pytest (si autorisé/présent)

---

# 3) Tests cURL — Plan complet (succès + erreurs)

## 3.1 Préparation
- Lancer le serveur :
  python3 run.py

- Base URL :
  http://127.0.0.1:5000

Important : la persistence est in-memory.
Donc les données disparaissent si le serveur redémarre.

---

## 3.2 USERS — Tests cURL

### A) POST create user (OK)
curl -i -X POST http://127.0.0.1:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"first_name":"John","last_name":"Doe","email":"john.doe@example.com"}'

Attendu :
- 201 Created
- JSON avec id + champs

### B) POST create user (email déjà utilisé)
curl -i -X POST http://127.0.0.1:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"first_name":"John","last_name":"Doe","email":"john.doe@example.com"}'

Attendu :
- 400 Bad Request
- error: Email already registered

### C) POST invalid email
curl -i -X POST http://127.0.0.1:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{"first_name":"John","last_name":"Doe","email":"not-an-email"}'

Attendu :
- 400 Bad Request (si validation modèle gérée + exceptions attrapées)
- error expliquant input invalide

### D) GET list users (OK)
curl -i http://127.0.0.1:5000/api/v1/users/

Attendu :
- 200 OK
- liste JSON

### E) GET user by id (OK)
curl -i http://127.0.0.1:5000/api/v1/users/USER_ID_HERE

Attendu :
- 200 OK

### F) GET user not found
curl -i http://127.0.0.1:5000/api/v1/users/does-not-exist

Attendu :
- 404 Not Found

### G) PUT update user (OK)
curl -i -X PUT http://127.0.0.1:5000/api/v1/users/USER_ID_HERE \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Jane","last_name":"Doe","email":"jane.doe@example.com"}'

Attendu :
- 200 OK
- JSON user mis à jour (ou message selon implémentation)

### H) PUT user not found
curl -i -X PUT http://127.0.0.1:5000/api/v1/users/does-not-exist \
  -H "Content-Type: application/json" \
  -d '{"first_name":"X","last_name":"Y","email":"x@y.com"}'

Attendu :
- 404 Not Found

---

## 3.3 AMENITIES — Tests cURL

### A) POST create amenity (OK)
curl -i -X POST http://127.0.0.1:5000/api/v1/amenities/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Wi-Fi"}'

Attendu :
- 201 Created
- JSON id + name

### B) POST invalid amenity (name vide)
curl -i -X POST http://127.0.0.1:5000/api/v1/amenities/ \
  -H "Content-Type: application/json" \
  -d '{"name":""}'

Attendu :
- 400 Bad Request

### C) GET list amenities
curl -i http://127.0.0.1:5000/api/v1/amenities/

Attendu :
- 200 OK

### D) GET amenity not found
curl -i http://127.0.0.1:5000/api/v1/amenities/does-not-exist

Attendu :
- 404 Not Found

### E) PUT amenity (OK)
curl -i -X PUT http://127.0.0.1:5000/api/v1/amenities/AMENITY_ID_HERE \
  -H "Content-Type: application/json" \
  -d '{"name":"Air Conditioning"}'

Attendu :
- 200 OK

---

## 3.4 PLACES — Tests cURL (relations + bornes)

Pré-requis :
- un USER_ID existe (owner)
- des AMENITY_ID existent

### A) POST create place (OK)
curl -i -X POST http://127.0.0.1:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -d '{
    "title":"Cozy Apartment",
    "description":"A nice place to stay",
    "price":100.0,
    "latitude":37.7749,
    "longitude":-122.4194,
    "owner_id":"USER_ID_HERE",
    "amenities":["AMENITY_ID_1","AMENITY_ID_2"]
  }'

Attendu :
- 201 Created

### B) POST place invalid owner_id
curl -i -X POST http://127.0.0.1:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -d '{
    "title":"Bad Place",
    "description":"x",
    "price":10.0,
    "latitude":0.0,
    "longitude":0.0,
    "owner_id":"does-not-exist",
    "amenities":[]
  }'

Attendu :
- 400 Bad Request

### C) POST place invalid amenity id
curl -i -X POST http://127.0.0.1:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -d '{
    "title":"Bad Place",
    "description":"x",
    "price":10.0,
    "latitude":0.0,
    "longitude":0.0,
    "owner_id":"USER_ID_HERE",
    "amenities":["does-not-exist"]
  }'

Attendu :
- 400 Bad Request

### D) Boundary test latitude > 90
curl -i -X POST http://127.0.0.1:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -d '{
    "title":"Bad Lat",
    "description":"x",
    "price":10.0,
    "latitude":91.0,
    "longitude":0.0,
    "owner_id":"USER_ID_HERE",
    "amenities":[]
  }'

Attendu :
- 400 Bad Request

### E) GET list places (OK)
curl -i http://127.0.0.1:5000/api/v1/places/

Attendu :
- 200 OK
- liste légère (id, title, lat, lon)

### F) GET place detail (OK) – enriched
curl -i http://127.0.0.1:5000/api/v1/places/PLACE_ID_HERE

Attendu :
- 200 OK
- owner nested + amenities nested (+ reviews si ajoutée ensuite)

### G) PUT update place (OK)
curl -i -X PUT http://127.0.0.1:5000/api/v1/places/PLACE_ID_HERE \
  -H "Content-Type: application/json" \
  -d '{
    "title":"Luxury Condo",
    "description":"Updated",
    "price":200.0,
    "latitude":37.7749,
    "longitude":-122.4194,
    "owner_id":"USER_ID_HERE",
    "amenities":["AMENITY_ID_1"]
  }'

Attendu :
- 200 OK

---

## 3.5 REVIEWS — Tests cURL (relations + delete)

Pré-requis :
- USER_ID existe
- PLACE_ID existe

### A) POST create review (OK)
curl -i -X POST http://127.0.0.1:5000/api/v1/reviews/ \
  -H "Content-Type: application/json" \
  -d '{
    "text":"Great place to stay!",
    "rating":5,
    "user_id":"USER_ID_HERE",
    "place_id":"PLACE_ID_HERE"
  }'

Attendu :
- 201 Created
- review id + fields

### B) POST review invalid rating (6)
curl -i -X POST http://127.0.0.1:5000/api/v1/reviews/ \
  -H "Content-Type: application/json" \
  -d '{
    "text":"Bad rating",
    "rating":6,
    "user_id":"USER_ID_HERE",
    "place_id":"PLACE_ID_HERE"
  }'

Attendu :
- 400 Bad Request

### C) POST review invalid place_id
curl -i -X POST http://127.0.0.1:5000/api/v1/reviews/ \
  -H "Content-Type: application/json" \
  -d '{
    "text":"Bad place",
    "rating":5,
    "user_id":"USER_ID_HERE",
    "place_id":"does-not-exist"
  }'

Attendu :
- 400 Bad Request

### D) GET list reviews (OK)
curl -i http://127.0.0.1:5000/api/v1/reviews/

Attendu :
- 200 OK
- liste light (id, text, rating)

### E) GET review by id (OK)
curl -i http://127.0.0.1:5000/api/v1/reviews/REVIEW_ID_HERE

Attendu :
- 200 OK

### F) GET reviews by place (nested route)
curl -i http://127.0.0.1:5000/api/v1/places/PLACE_ID_HERE/reviews

Attendu :
- 200 OK
- liste des reviews du place

### G) DELETE review (OK)
curl -i -X DELETE http://127.0.0.1:5000/api/v1/reviews/REVIEW_ID_HERE

Attendu :
- 200 OK
- message deleted

### H) Vérification cohérence après DELETE
curl -i http://127.0.0.1:5000/api/v1/places/PLACE_ID_HERE/reviews

Attendu :
- la review supprimée ne doit plus apparaître

---

# 4) Guide Swagger UI — Mode d’emploi (tests manuels)

## 4.1 Accès
Ouvrir :
http://127.0.0.1:5000/api/v1/

Si redirection :
- utiliser le slash final /api/v1/

## 4.2 Principe
Swagger UI affiche :
- les namespaces (users, amenities, places, reviews)
- les endpoints disponibles
- les modèles attendus
- la liste des réponses déclarées

Swagger permet d’exécuter une requête réelle via le bouton :
- “Try it out”
- “Execute”

## 4.3 Procédure type de test sur Swagger
1) Ouvrir l’endpoint (ex : POST /users/)
2) Cliquer sur “Try it out”
3) Remplir le body JSON
4) Cliquer “Execute”
5) Observer :
   - Response body
   - Response code
   - Headers

## 4.4 Bon ordre de test conseillé sur Swagger
1) POST /users/ (créer un owner)
2) POST /amenities/ (créer 1 ou 2 amenities)
3) POST /places/ (créer un place avec owner_id + amenities IDs)
4) POST /reviews/ (créer une review avec user_id + place_id)
5) GET /places/<id> (vérifier owner/amenities/reviews)
6) GET /places/<id>/reviews (nested)
7) DELETE /reviews/<id> (vérifier disparition)

## 4.5 Pièges fréquents sur Swagger
- Confondre les IDs : toujours copier-coller depuis la réponse
- Tester GET list avant d’avoir créé des objets (liste vide est OK)
- Oublier qu’un redémarrage serveur vide tout (in-memory)
- Croire que Swagger “valide” la logique métier : Swagger valide seulement la forme du JSON

---

# 5) Tests automatisés (unittest) — Structure recommandée

## 5.1 Organisation de fichiers
Créer un dossier :
tests/

Puis des fichiers :
- tests/test_users.py
- tests/test_amenities.py
- tests/test_places.py
- tests/test_reviews.py

## 5.2 Exemple minimal unittest (User)
Créer `tests/test_users.py` :

```python
import unittest
from app import create_app

class TestUserEndpoints(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_create_user_ok(self):
        resp = self.client.post("/api/v1/users/", json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "jane.doe@example.com"
        })
        self.assertEqual(resp.status_code, 201)
        data = resp.get_json()
        self.assertIn("id", data)
        self.assertEqual(data["email"], "jane.doe@example.com")

    def test_create_user_invalid_email(self):
        resp = self.client.post("/api/v1/users/", json={
            "first_name": "Jane",
            "last_name": "Doe",
            "email": "invalid"
        })
        self.assertEqual(resp.status_code, 400)

if __name__ == "__main__":
    unittest.main()

```
