# Chatbot IA pour Portfolio

Ce chatbot permet aux recruteurs de poser des questions sur votre profil en utilisant Ollama en local.

## 📋 Prérequis

1. **Ollama installé et fonctionnel** (vous l'avez déjà ✅)
2. **Node.js** (version 16 ou supérieure)
3. **Un modèle Ollama** (par défaut : `gemma2:2b`)

## 🚀 Installation

### 1. Installer les dépendances Node.js

```bash
cd /Users/cedric/Documents/INSA/S9/Portfolio/my-portfolio
npm install
```

### 2. Vérifier qu'Ollama fonctionne

```bash
# Démarrer Ollama (si pas déjà fait)
ollama serve

# Dans un autre terminal, vérifier les modèles disponibles
ollama list
```

### 3. Télécharger un modèle (si nécessaire)

```bash
# Modèle léger et rapide (recommandé)
ollama pull gemma2:2b

# OU modèle plus performant (plus lent)
ollama pull llama3.2
```

## 🎯 Utilisation

### Démarrer le serveur chatbot

```bash
npm start
```

Le serveur démarre sur `http://localhost:3001`

### Démarrer Jekyll en parallèle

Dans un autre terminal :

```bash
bundle exec jekyll serve
```

Votre site sera accessible sur `http://localhost:4000`

### Tester le chatbot

1. Ouvrez votre site : `http://localhost:4000`
2. Cliquez sur le bouton flottant en bas à droite 🤖
3. Posez une question !

## 🔧 Configuration

### Changer le modèle Ollama

Éditez `chatbot-server.js` ligne 103 :

```javascript
model: 'gemma2:2b', // Changez ici : 'llama3.2', 'mistral', etc.
```

### Modifier le prompt système

Le prompt contient toutes vos informations. Éditez `chatbot-server.js` à partir de la ligne 12.

Ajoutez des détails sur :
- Vos projets récents
- Vos compétences spécifiques
- Vos expériences professionnelles
- Vos objectifs de carrière

### Personnaliser l'apparence

Éditez `_includes/chatbot.html` pour modifier :
- Les couleurs (variables CSS)
- La position du bouton
- La taille de la fenêtre
- Les animations

## 📝 Exemples de questions pour tester

- "Quelles sont les compétences principales de Cédric ?"
- "Parle-moi de son expérience chez Vitesco Technologies"
- "Quels projets IoT a-t-il réalisés ?"
- "Quels langages de programmation maîtrise-t-il ?"
- "Quel est son parcours académique ?"

## 🐛 Résolution de problèmes

### Le chatbot ne répond pas

1. Vérifiez qu'Ollama est démarré : `ollama serve`
2. Vérifiez que le serveur Node.js fonctionne : `npm start`
3. Testez l'API : `curl http://localhost:3001/api/health`
4. Vérifiez la console du navigateur (F12)

### Erreur "model not found"

```bash
# Téléchargez le modèle manquant
ollama pull gemma2:2b
```

### Port 3001 déjà utilisé

Changez le port dans `chatbot-server.js` ligne 164 :

```javascript
const PORT = process.env.PORT || 3002; // Changez ici
```

Et dans `_includes/chatbot.html` ligne 284 :

```javascript
const API_URL = 'http://localhost:3002/api/chat'; // Changez ici
```

### Erreur CORS en production

Si vous déployez en production, ajoutez votre domaine dans `chatbot-server.js` :

```javascript
app.use(cors({
    origin: 'https://votre-domaine.com'
}));
```

## 🚀 Déploiement en production

### Option 1 : VPS / Serveur dédié

1. Installez Node.js et Ollama sur votre serveur
2. Clonez votre repository
3. Installez les dépendances : `npm install`
4. Utilisez PM2 pour garder le serveur actif :

```bash
npm install -g pm2
pm2 start chatbot-server.js
pm2 save
pm2 startup
```

5. Configurez un reverse proxy Nginx :

```nginx
server {
    listen 80;
    server_name votre-api-domaine.com;
    
    location / {
        proxy_pass http://localhost:3001;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection 'upgrade';
        proxy_set_header Host $host;
        proxy_cache_bypass $http_upgrade;
    }
}
```

6. Mettez à jour l'URL dans `_includes/chatbot.html` :

```javascript
const API_URL = 'https://votre-api-domaine.com/api/chat';
```

### Option 2 : Hébergement cloud

Services compatibles :
- **Railway.app** (facile, gratuit pour commencer)
- **Render.com**
- **DigitalOcean App Platform**
- **Heroku** (nécessite buildpack Ollama custom)

⚠️ **Note** : Ollama nécessite des ressources significatives. Un VPS avec au moins 2GB RAM est recommandé.

## 📚 Structure des fichiers

```
my-portfolio/
├── chatbot-server.js          # Serveur API backend
├── _includes/
│   └── chatbot.html            # Widget frontend
├── _includes/
│   └── footer.html             # Footer modifié pour inclure chatbot
├── package.json                # Dépendances Node.js
└── README-CHATBOT.md          # Cette documentation
```

## 🎨 Personnalisation avancée

### Ajouter des suggestions de questions

Ajoutez ces boutons dans `chatbot.html` après le message de bienvenue :

```javascript
const suggestions = [
    "Quelles sont ses compétences ?",
    "Parle-moi de ses projets",
    "Quelle est son expérience ?"
];

suggestions.forEach(suggestion => {
    const btn = document.createElement('button');
    btn.textContent = suggestion;
    btn.onclick = () => {
        input.value = suggestion;
        sendMessage();
    };
    messagesContainer.appendChild(btn);
});
```

### Ajouter un historique persistant

Utilisez localStorage pour sauvegarder les conversations :

```javascript
// Sauvegarder
localStorage.setItem('chatHistory', JSON.stringify(conversationHistory));

// Charger au démarrage
conversationHistory = JSON.parse(localStorage.getItem('chatHistory') || '[]');
```

## 💡 Conseils

1. **Prompt détaillé** : Plus vous ajoutez d'informations dans le prompt système, meilleures seront les réponses
2. **Modèle adapté** : `gemma2:2b` est rapide mais moins précis. `llama3.2` est plus lent mais plus intelligent
3. **Température** : Ajustez le paramètre `temperature` (0.7 par défaut) pour des réponses plus créatives (↑) ou plus factuelles (↓)
4. **Cache** : Les modèles Ollama gardent en cache les prompts récents pour accélérer les réponses

## 📞 Support

Pour toute question, consultez :
- [Documentation Ollama](https://ollama.ai/docs)
- [Documentation Express](https://expressjs.com/)
- [Documentation Jekyll](https://jekyllrb.com/)

---

Créé avec ❤️ pour améliorer l'expérience des recruteurs sur votre portfolio !
