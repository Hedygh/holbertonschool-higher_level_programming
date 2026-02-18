# 📘 RESTful API — Révision curl

---

# 1️⃣ Qu’est-ce que curl ?

`curl` (Client URL) est un outil en ligne de commande permettant d’envoyer des requêtes HTTP/HTTPS (et autres protocoles).

Il sert à :
- Tester une API
- Debugger un serveur
- Simuler un client REST
- Inspecter les réponses HTTP

---

# 2️⃣ Vérifier l'installation (Mac)

Sur macOS, curl est déjà installé.

```bash
curl --version
```

Expected output :
- Version de curl
- Protocoles supportés (http, https, ftp…)
- Support SSL/TLS

---

# 3️⃣ Requête GET (par défaut)

```bash
curl https://jsonplaceholder.typicode.com/posts
```

✔ Méthode par défaut : **GET**  
✔ Affiche le body de la réponse  
✔ Retourne du JSON

---

# 4️⃣ Voir les headers uniquement

```bash
curl -I https://jsonplaceholder.typicode.com/posts
```

`-I` → envoie une requête HEAD

Affiche :
- Status code
- Headers
- Pas de body

Utile pour :
- Vérifier le code HTTP
- Voir Content-Type
- Vérifier cache-control

---

# 5️⃣ Voir headers + body

```bash
curl -i https://jsonplaceholder.typicode.com/posts/1
```

`-i` → inclut les headers dans la sortie

---

# 6️⃣ Faire une requête POST

## Version simple (form data)

```bash
curl -X POST -d "title=foo&body=bar&userId=1" \
https://jsonplaceholder.typicode.com/posts
```

- `-X POST` → spécifie la méthode
- `-d` → envoie des données dans le body

---

## Version REST propre (JSON)

```bash
curl -X POST https://jsonplaceholder.typicode.com/posts \
-H "Content-Type: application/json" \
-d '{"title":"foo","body":"bar","userId":1}'
```

- `-H` → ajoute un header
- `Content-Type: application/json`
- `-d` → envoie du JSON

Expected response :
```json
{
  "title": "foo",
  "body": "bar",
  "userId": 1,
  "id": 101
}
```

(JSONPlaceholder simule la création)

---

# 7️⃣ Ajouter un header (ex: Auth)

```bash
curl -H "Authorization: Bearer <token>" \
https://api.example.com/users
```

Les headers servent à envoyer :
- Authentification
- Content-Type
- Accept
- etc.

---

# 8️⃣ Lire uniquement le status code

```bash
curl -o /dev/null -s -w "%{http_code}\n" \
https://jsonplaceholder.typicode.com/posts
```

Utile pour :
- Scripts
- Tests automatiques

---

# 9️⃣ Formatter le JSON avec jq

Installer jq (Mac) :

```bash
brew install jq
```

Utilisation :

```bash
curl https://jsonplaceholder.typicode.com/posts | jq
```

Permet d’avoir un JSON lisible.

---

# 🔟 Récap des options importantes

| Option | Rôle |
|--------|------|
| -X | Spécifie la méthode HTTP |
| -d | Envoie des données dans le body |
| -H | Ajoute un header |
| -I | Affiche seulement les headers |
| -i | Affiche headers + body |
| -o | Redirige la sortie vers un fichier |
| -s | Mode silencieux |
| -w | Affiche une valeur formatée (ex: status code) |

---

# 🎯 Ce que je dois savoir expliquer

- GET est la méthode par défaut
- `-X` permet de changer la méthode
- `-d` envoie des données (POST, PUT, PATCH)
- `-H` ajoute des headers (ex: Authorization)
- `-I` envoie une requête HEAD
- JSONPlaceholder ne sauvegarde rien (simulation)

---

# 🔥 Lien avec mon projet HBnB

Quand mon API Flask tournera en local :

```bash
curl http://localhost:5000/users
curl -X POST http://localhost:5000/users \
-H "Content-Type: application/json" \
-d '{"email":"test@mail.com"}'
```

curl me permet de tester mon API sans Postman.

---

# 🧠 Résumé ultra rapide

GET → par défaut  
-I → headers seulement  
-i → headers + body  
-X → changer méthode  
-d → envoyer données  
-H → ajouter header  
