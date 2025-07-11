# Projet Atelier Redis

## Objectif
Découvrir Redis : installation, réplication master/slave, et intégration dans une appli Flask avec cache.

## Structure
- Redis master + slave via Docker
- Application Flask (cache-aside)
- Données expirables après 60 sec
- Réplication automatique des données

## Lancement rapide

### 1. Lancer Redis avec Docker
```bash
docker-compose up -d
```

### 2. Lancer l'application Flask
```bash
pip install flask redis
python app.py
```

### 3. Tester dans le navigateur
- http://127.0.0.1:5000/data/test
  - 1er appel : lent (`"source": "slow-db"`)
  - 2e appel : rapide (`"source": "cache"`)

### 4. Vérifier la réplication
```bash
docker exec -it redis-master redis-cli set hello "world"
docker exec -it redis-slave redis-cli get hello
```

### 5. Vérifier l'expiration
```bash
docker exec -it redis-master redis-cli ttl test
```
