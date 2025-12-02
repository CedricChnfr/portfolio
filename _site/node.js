const express = require('express');
const cors = require('cors');
const axios = require('axios');

const app = express();
app.use(cors());
app.use(express.json());

const SYSTEM_PROMPT = `Tu es un assistant virtuel pour le portfolio de Cédric Chanfreau. 
Voici son profil complet :

FORMATION:
- Diplôme d'Ingénieur INSA Toulouse 2025 - Automatique & Électronique
- Master 2 ENSEEIHT - Réseaux Embarqués et Objets Connectés

EXPÉRIENCE:
- Ingénieur Logiciel Embarqué - Vitesco Technologies (2022-2024)
- Stage International - Vitesco Technologies Roumanie (2024)

COMPÉTENCES TECHNIQUES:
- Langages: C/C++, Python, Java, JavaScript, MATLAB, SQL
- Systèmes embarqués: Microcontrôleurs, IoT, Edge Computing
- IA: Machine Learning, TensorFlow, PyTorch
- Outils: Docker, Git, Jenkins, Eclipse, Keil

PROJETS:
- Application mobile Toulouse Sport (React Native)
- Système IA d'automatisation vidéo
- Projets robotique et IoT

Réponds de manière professionnelle, concise et en français. Si tu ne connais pas une information, dis-le clairement.`;

app.post('/api/chat', async (req, res) => {
    try {
        const { message } = req.body;
        
        const response = await axios.post('http://localhost:11434/api/generate', {
            model: 'llama3.2',
            prompt: `${SYSTEM_PROMPT}\n\nQuestion: ${message}\nRéponse:`,
            stream: false
        });
        
        res.json({ response: response.data.response });
    } catch (error) {
        console.error('Erreur Ollama:', error);
        res.status(500).json({ error: 'Erreur lors de la génération de réponse' });
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => console.log(`API lancée sur port ${PORT}`));