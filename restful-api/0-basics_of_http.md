# 📘 RESTful API — Fichier de Révision

---

# 1️⃣ HTTP / HTTPS — Bases essentielles

## 🔹 HTTP
- Protocole de communication client → serveur
- Non chiffré
- Les données peuvent être interceptées

## 🔹 HTTPS
- HTTP + TLS (chiffrement)
- Garantit :
  - Confidentialité
  - Intégrité
  - Authentification du serveur

👉 En production : **toujours HTTPS**

---

# 2️⃣ Structure d’une requête HTTP

Une requête contient :

- **Méthode** (GET, POST, PUT, PATCH, DELETE)
- **URL**
- **Headers**
- **Body** (optionnel)

### Exemple

```http
POST /users
Authorization: Bearer <token>
Content-Type: application/json

{
  "email": "test@mail.com",
  "password": "123"
}
```

---

# 3️⃣ Structure d’une réponse HTTP

Une réponse contient :

- **Status Code**
- **Headers**
- **Body (souvent JSON)**

### Exemple

```http
201 Created
Content-Type: application/json

{
  "id": 42,
  "email": "test@mail.com"
}
```

---

# 4️⃣ Principes REST fondamentaux

## 🔹 REST = Ressources + Méthodes HTTP

On manipule des **ressources**, pas des actions.

### Exemples de ressources
- `/users`
- `/places`
- `/reviews`

---

## 🔹 Stateless

- Le serveur ne garde aucune mémoire entre deux requêtes.
- Chaque requête doit contenir :
  - L’authentification
  - Les paramètres nécessaires

👉 Chaque requête est indépendante.

---

## 🔹 Authentification

Va dans les **headers HTTP** :

```http
Authorization: Bearer <token>
```

Jamais dans l’URL.  
Jamais en HTTP non sécurisé.

---

# 5️⃣ Méthodes HTTP

## 🔹 GET
→ Récupérer une ressource

```
GET /users
GET /users/42
```

Réponses possibles :
- 200 OK
- 404 Not Found

---

## 🔹 POST
→ Créer une ressource

```
POST /users
```

Réponses possibles :
- 201 Created
- 400 Bad Request
- 409 Conflict

---

## 🔹 PUT
→ Remplacer entièrement une ressource

```
PUT /users/42
```

Réponses possibles :
- 200 OK
- 404 Not Found

---

## 🔹 PATCH
→ Modifier partiellement une ressource

```
PATCH /users/42
```

Réponses possibles :
- 200 OK
- 400 Bad Request
- 404 Not Found
- 403 Forbidden

---

## 🔹 DELETE
→ Supprimer une ressource

```
DELETE /users/42
```

Réponses possibles :
- 204 No Content
- 404 Not Found
- 403 Forbidden

---

# 6️⃣ Status Codes essentiels

## ✅ Succès

| Code | Signification |
|------|--------------|
| 200 | OK |
| 201 | Created |
| 204 | No Content |

---

## ❌ Erreurs côté client

| Code | Signification |
|------|--------------|
| 400 | Mauvaise requête |
| 401 | Non authentifié |
| 403 | Interdit |
| 404 | Ressource inexistante |
| 409 | Conflit |
| 422 | Validation échouée |

---

## 💥 Erreurs côté serveur

| Code | Signification |
|------|--------------|
| 500 | Erreur interne |

---

# 7️⃣ Mapping Ressources → Méthodes → Status Codes

## USERS

### GET /users
- 200 OK

### GET /users/{id}
- 200 OK
- 404 Not Found

### POST /users
- 201 Created
- 400 Bad Request
- 409 Conflict

### PATCH /users/{id}
- 200 OK
- 400 Bad Request
- 404 Not Found
- 403 Forbidden

### DELETE /users/{id}
- 204 No Content
- 404 Not Found
- 403 Forbidden

---

## PLACES

### GET /places
- 200 OK

### POST /places
- 201 Created
- 400 Bad Request
- 401 Unauthorized

---

## REVIEWS

### POST /places/{id}/reviews
- 201 Created
- 400 Bad Request
- 404 Not Found
- 401 Unauthorized

---

# 8️⃣ Synthèse 

- Comprendre HTTP / HTTPS
- Savoir associer Méthodes HTTP ↔ CRUD
- Savoir choisir le bon status code
- Comprendre le principe REST (ressources)
- Comprendre stateless
- Savoir où placer l’authentification
- Concevoir des endpoints propres

---

# 🎯 Résumé rapide

401 → Pas authentifié  
403 → Authentifié mais interdit  

201 → Création  
200 → Succès classique  
204 → Succès sans contenu  

REST = Ressource + Méthode HTTP  

Stateless = Chaque requête indépendante
