---
layout: default
title:  "Portfolio"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---



[← Back to My Courses 2024-2025](./my-courses-2024-2025.html)

# Portfolio

## PART A : PRESENTATION GENERALE

### Presentation

Le portfolio est un exercice de pratique reflexive essentiel dans la formation d'ingenieur a l'INSA Toulouse. Il s'inscrit dans le cadre de la certification RNCP (Repertoire National des Certifications Professionnelles), qui exige de l'etudiant qu'il soit capable de documenter, analyser et valoriser les competences acquises tout au long de son parcours.

L'objectif de ce portfolio est de constituer une trace structuree et evolutive de mon parcours academique et professionnel. Il ne s'agit pas simplement de lister des cours ou des projets, mais de mener une reflexion approfondie sur les apprentissages realises, les competences developpees et les axes d'amelioration identifies. Cette demarche s'inscrit dans une logique d'amelioration continue et de construction d'une identite professionnelle coherente.

### Structure du portfolio

Le portfolio est organise en plusieurs sections principales :

1. **Courses** : Descriptions detaillees des cours suivis, incluant le contenu aborde, la duree, et les apprentissages cles.
2. **Projects** : Vue d'ensemble des projets realises, avec les objectifs, methodologies et resultats.
3. **CV** : Mon curriculum vitae, presentant mon parcours academique, mes experiences professionnelles, mes competences techniques et mes activites extra-curriculaires.
4. **About** : Informations sur mon parcours, mes interets et mes aspirations futures.

### Objectifs

Les objectifs de ce portfolio sont de :

- Presenter une vue claire et organisee de mon parcours educatif et professionnel.
- Demontrer mon expertise dans differents domaines techniques, notamment l'IoT, les systemes embarques et le developpement logiciel.
- Mettre en valeur ma capacite a appliquer les connaissances theoriques a des situations pratiques a travers des projets et des stages.
- Servir de ressource pour de potentiels employeurs, en mettant en avant mes competences et experiences.
- Refleter sur mon apprentissage et ma progression, en identifiant les domaines a developper davantage.

## PART B : EXPERIENCE ET CONTEXTE

### Environnement technique

Ce portfolio a ete entierement developpe sous forme de site web statique en utilisant **Jekyll**, un generateur de sites statiques ecrit en Ruby. Le site est heberge sur **GitHub Pages**, ce qui permet un deploiement automatique a chaque push sur la branche principale du depot Git.

#### Outils de developpement

Les principaux outils utilises pour la realisation de ce portfolio sont :

- **Jekyll** : Generateur de sites statiques utilisant le theme Minima comme base. Jekyll transforme des fichiers Markdown en pages HTML completes.
- **GitHub Pages** : Service d'hebergement gratuit de GitHub permettant de servir le site directement depuis le depot.
- **Git** : Systeme de controle de version utilise pour suivre l'evolution du code et du contenu du portfolio.
- **Visual Studio Code** : Editeur de code utilise pour le developpement, avec des extensions pour Markdown, HTML et CSS.
- **Kramdown** : Moteur de rendu Markdown utilise par Jekyll pour convertir le contenu ecrit en Markdown vers du HTML.

#### Organisation du depot

Le depot est organise selon la structure standard de Jekyll :
- `_posts/` : Contient tous les articles organises par annee scolaire (2022-2023, 2023-2024, 2024-2025) et par categorie (Courses, Personal_Project).
- `_includes/` : Fichiers HTML reutilisables (chatbot, footer).
- `_config.yml` : Configuration globale du site (titre, URL, plugins).
- `img/` et `cours-pdf/` : Ressources statiques (images, rapports PDF).
- `assets/` : Feuilles de style et scripts.
- `search.json` : Index de recherche pour la fonctionnalite de recherche du site.

## PART C : ASPECTS TECHNIQUES

### 1. Framework Jekyll et templating Liquid

Jekyll repose sur le moteur de templates **Liquid**, developpe par Shopify. Ce systeme permet d'utiliser des variables, des boucles et des conditions dans les fichiers HTML. Par exemple, la page d'accueil utilise des boucles Liquid pour generer dynamiquement la liste des articles :

```liquid
{% raw %}{% for post in site.posts %}
  <li><a href="{{ post.url }}">{{ post.title }}</a></li>
{% endfor %}{% endraw %}
```

Chaque page du site commence par un bloc **YAML Front Matter** qui definit les metadonnees : le layout utilise, le titre, la date et les categories. Ce mecanisme permet a Jekyll de savoir comment traiter et rendre chaque fichier.

```yaml
---
layout: default
title: "Portfolio"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---
```

Le contenu est ensuite redige en **Markdown** (syntaxe Kramdown), ce qui facilite la redaction et la maintenance du contenu sans avoir a manipuler directement du HTML.

### 2. Architecture du site

L'architecture du site repose sur plusieurs concepts cles de Jekyll :

- **Layouts** : Le layout `default` fournit la structure HTML de base (en-tete, navigation, pied de page) dans laquelle le contenu de chaque page est injecte.
- **Includes** : Les fichiers `_includes/` permettent de reutiliser des composants HTML. Le site utilise notamment un composant `chatbot.html` pour l'assistant conversationnel et un `footer.html` pour le pied de page.
- **Posts Collection** : Les articles sont organises dans `_posts/` avec une convention de nommage `YYYY-MM-DD-titre.markdown`. Jekyll genere automatiquement les URLs et l'index a partir de cette structure.

### 3. Design responsive avec CSS

Chaque page du portfolio integre des styles CSS personnalises pour assurer une presentation coherente et agreable. Les elements stylistiques principaux comprennent :

- Une palette de couleurs basee sur le bleu (`#007BFF` pour les titres, `#66B2FF` pour les boutons).
- Des boutons stylises avec des transitions et des effets de survol (`hover`).
- Un texte justifie pour une meilleure lisibilite.
- Un arriere-plan clair (`#f4f4f9`) pour un contraste optimal.

### 4. Fonctionnalite de recherche

Le site integre une fonctionnalite de recherche implementee via un fichier `search.json` qui indexe l'ensemble des articles. Ce fichier JSON est genere dynamiquement par Jekyll a partir des metadonnees des posts, permettant une recherche cote client rapide et efficace sans necessite de serveur backend.

### 5. Integration d'un chatbot

Un chatbot conversationnel a ete integre au portfolio via le composant `_includes/chatbot.html`. Cette fonctionnalite enrichit l'experience utilisateur en permettant aux visiteurs d'interagir avec le site de maniere dynamique.

### 6. Integration de documents PDF

Pour les pages de cours, le portfolio utilise des balises `<iframe>` pour integrer directement les rapports et documents PDF dans les pages. Cela permet aux visiteurs de consulter les documents sans quitter le site, avec un lien de telechargement disponible en complement.

```html
<iframe src="/cours-pdf/document.pdf" width="100%" height="800px"></iframe>
```

### 7. Pipeline de deploiement

Le deploiement du portfolio suit un pipeline simple mais efficace :

1. Modification du contenu localement (ajout de pages, edition de Markdown).
2. Commit et push des modifications sur le depot GitHub.
3. GitHub Pages detecte automatiquement les changements et declenche une reconstruction du site via Jekyll.
4. Le site mis a jour est servi sur le domaine personnalise `cedric.littlenuage.com`.

### 8. Controle de version avec Git

L'ensemble du portfolio est gere sous **Git**, ce qui permet de :

- Suivre l'historique complet des modifications apportees au contenu et au code.
- Revenir a une version anterieure en cas de besoin.
- Travailler sur des fonctionnalites en parallele via des branches.
- Documenter les evolutions du site a travers les messages de commit.

## PART D : ANALYSE ET REFLEXION

### Pratique reflexive

La creation et la maintenance de ce portfolio constituent un exercice de pratique reflexive a part entiere. Chaque page de cours suit une structure en quatre parties (Presentation generale, Partie descriptive, Partie technique, Partie analytique) qui m'oblige a ne pas simplement decrire ce que j'ai fait, mais aussi a analyser ce que j'ai appris, comment je l'ai appris, et ce que cela signifie pour mon developpement professionnel.

Cette demarche reflexive m'a permis de prendre du recul sur mes apprentissages et de mieux comprendre les liens entre les differents cours et projets de ma formation.

### Documentation des competences

Le portfolio sert de preuve tangible des competences acquises tout au long de la formation. En documentant systematiquement les aspects techniques de chaque cours, les projets realises et les reflexions personnelles, je constitue un dossier qui peut etre presente dans le cadre de la certification RNCP et qui demontre ma capacite a :

- Analyser des problemes techniques complexes.
- Mettre en oeuvre des solutions adaptees.
- Communiquer efficacement sur des sujets techniques.
- Travailler en equipe et gerer des projets.

### Identite professionnelle

Au-dela de la simple documentation, le portfolio contribue a la construction de mon identite professionnelle. En choisissant de le realiser sous forme de site web statique plutot que sous forme de document classique, j'ai demontre des competences en developpement web, en gestion de contenu et en deploiement d'applications, ce qui enrichit mon profil d'ingenieur en IoT et systemes embarques.

Le fait de maintenir un site web public accessible a tous constitue egalement une vitrine professionnelle qui va au-dela du simple CV, en montrant concretement ce que je sais faire et comment je travaille.

### Amelioration continue

Ce portfolio est un projet vivant, en constante evolution. Chaque semestre, de nouvelles pages sont ajoutees pour les nouveaux cours et projets. Les pages existantes peuvent etre ameliorees et enrichies. Cette demarche d'amelioration continue reflete la philosophie de la formation d'ingenieur : ne jamais cesser d'apprendre et de progresser.

Parmi les ameliorations futures envisagees :
- Enrichissement du contenu technique de chaque page de cours.
- Amelioration de l'accessibilite et du design responsive.
- Ajout de nouvelles fonctionnalites interactives.
- Integration de retours d'experience de stages et de projets professionnels.

### Auto-evaluation

La realisation de ce portfolio m'a permis de developper des competences transversales que je n'aurais pas necessairement acquises dans le cadre des cours techniques seuls. La redaction en Markdown, la gestion d'un site web avec Jekyll, l'utilisation de Git pour le versioning, et surtout la pratique reflexive systematique sont autant de competences qui me seront utiles dans ma vie professionnelle.

Ce travail de documentation et de reflexion, bien qu'exigeant en temps, est extremement formateur. Il m'a appris a structurer ma pensee, a prendre du recul sur mes experiences et a valoriser mes competences de maniere professionnelle.

<style>
    body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f9;
        color: #333;
        line-height: 1.6;
    }
    h2, h3, h4 {
        color: #007BFF;
    }
    footer {
        display: flex;
        justify-content: space-around;
        margin-top: 20px;
    }
    .footer-section {
        flex: 1;
        text-align: center;
    }
    .styled-button {
        display: inline-block;
        width: 100px;
        margin: 10px;
        padding: 15px 30px;
        font-size: 16px;
        color: white;
        background-color: #66B2FF;
        text-decoration: none;
        border-radius: 25px;
        transition: background-color 0.3s, transform 0.3s;
    }
    .styled-button:hover {
        background-color: #3399FF;
        transform: scale(1.05);
    }
    p {
        text-align: justify;
    }
</style>
