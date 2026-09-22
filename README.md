# Django Starter Template

Starter Django réutilisable pour lancer rapidement de nouveaux projets web avec une configuration séparée pour le développement et la production, Tailwind CSS, HTMX et une structure d'application simple.

## Stack

- Python `3.14+`
- Django `6.1+`
- SQLite en développement
- Tailwind CSS avec `django-tailwind`
- HTMX avec `django-htmx`
- Authentification extensible avec `django-allauth`
- Gestion des variables d'environnement avec `python-dotenv`
- Gestion de base de données avec `dj-database-url`
- Gestion des dépendances Python avec `uv`

## Démarrage rapide

### 1. Installer les dépendances

Installer [uv](https://docs.astral.sh/uv/) si nécessaire, puis lancer :

```bash
uv sync
```

Les dépendances de développement peuvent être installées avec :

```bash
uv sync --dev
```

### 2. Configurer l'environnement

Créer un fichier `.env` à la racine du projet :

```env
DJANGO_SECRET_KEY=remplacer-par-une-cle-secrete
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
DJANGO_CSRF_TRUSTED_ORIGINS=http://localhost,http://127.0.0.1
DJANGO_SECURE_SSL_REDIRECT=false
```

Ne jamais versionner `.env`. Le fichier est déjà exclu par `.gitignore`.

### 3. Préparer la base de données

```bash
uv run python manage.py migrate
```

Créer un compte administrateur si nécessaire :

```bash
uv run python manage.py createsuperuser
```

### 4. Lancer le projet

Démarrer Django :

```bash
uv run python manage.py runserver
```

L'application est disponible à l'adresse `http://127.0.0.1:8000/`.

Pour compiler et surveiller Tailwind dans un second terminal :

```bash
uv run python manage.py tailwind start
```

Le fichier `Procfile.tailwind` permet aussi de lancer les processus `django` et `tailwind` avec un outil compatible Procfile.

## Structure

```text
config/
├── settings/
│   ├── base.py      # Configuration commune
│   ├── dev.py       # Développement local
│   └── prod.py      # Production
├── asgi.py
├── urls.py
└── wsgi.py

core/
├── templates/core/  # Pages de l'application principale
├── models.py
├── urls.py
└── views.py

theme/
├── static_src/      # Sources Tailwind
└── static/          # Assets générés

templates/           # Templates partagés, dont base.html
```

## Configuration Django

Les commandes `manage.py` utilisent `config.settings.dev` par défaut. Les serveurs WSGI et ASGI utilisent `config.settings.prod` par défaut.

Pour sélectionner explicitement un environnement :

```bash
DJANGO_SETTINGS_MODULE=config.settings.dev uv run python manage.py check
DJANGO_SETTINGS_MODULE=config.settings.prod uv run python manage.py check --deploy
```

En production, renseigner au minimum :

```env
DJANGO_SECRET_KEY=une-cle-secrete-unique
DJANGO_ALLOWED_HOSTS=example.com,www.example.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://example.com,https://www.example.com
DJANGO_SECURE_SSL_REDIRECT=true
```

La configuration de production active les cookies sécurisés, la redirection HTTPS et la prise en charge du proxy SSL.

## Commandes utiles

```bash
# Vérifier la configuration de développement
uv run python manage.py check --settings=config.settings.dev

# Vérifier la configuration de production
uv run python manage.py check --deploy --settings=config.settings.prod

# Appliquer les migrations
uv run python manage.py migrate

# Créer une migration
uv run python manage.py makemigrations

# Collecter les fichiers statiques
uv run python manage.py collectstatic --noinput --settings=config.settings.prod

# Lancer les tests
uv run python manage.py test

# Vérifier le formatage et la qualité Python
uv run ruff check .
```

## Ajouter une application

Créer l'application :

```bash
uv run python manage.py startapp blog
```

Puis :

1. Ajouter `blog` dans `INSTALLED_APPS`.
2. Ajouter les URLs de l'application dans `config/urls.py`.
3. Créer les templates dans `blog/templates/blog/`.
4. Créer et appliquer les migrations.

## Avant un déploiement

- Remplacer `DJANGO_SECRET_KEY` par une valeur secrète unique.
- Définir les domaines réels dans `DJANGO_ALLOWED_HOSTS`.
- Définir les origines HTTPS dans `DJANGO_CSRF_TRUSTED_ORIGINS`.
- Activer `DJANGO_SECURE_SSL_REDIRECT`.
- Configurer une base de données de production au lieu de SQLite si nécessaire.
- Lancer `check --deploy`.
- Lancer `collectstatic`.
- Utiliser `config.wsgi:application` avec un serveur WSGI ou `config.asgi:application` avec un serveur ASGI.

## Licence

Ce starter est destiné à servir de base à vos projets. Ajoutez la licence adaptée à votre projet avant sa distribution.
