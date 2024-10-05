---
layout: default
---

<div class="container">
    <!-- Conteneur flex pour l'image et la description -->
    <div class="flex-container">
        <div class="image-container">
            <img src="/img/Photo.jpg" alt="Schéma du Projet Robot">
        </div>
        
        <div class="description-container">
            <h2>Cédric Chanfreau</h2>
            <p>Je suis un étudiant motivé en apprentissage dans le domaine de l'automatisation et de l'ingénierie électrique. Passionné par le développement de logiciels et les systèmes embarqués, je recherche des opportunités pour appliquer et approfondir mes compétences techniques et pratiques.</p>
        </div>
    </div>
    
    <div class="nav-container">
        <a href="./jekyll/update/2024/10/02/my-courses.html" class="nav-link">Courses</a>
        <a href="./jekyll/update/2024/10/02/my-projects.html" class="nav-link">Projects</a>
        <a href="./jekyll/update/2024/10/02/my-cv.html" class="nav-link">CV</a>
    </div>
</div>

<style>
/* Container global */
.container {
    margin-top: 50px;
    text-align: center;
}

/* Flex container pour aligner l'image et la description */
.flex-container {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 40px; /* Espace entre l'image et la description */
    margin-bottom: 30px;
}

/* Image stylée et centrée */
.image-container img {
    border-radius: 50%;
    width: 200px;
    height: 200px;
    object-fit: cover;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
}

/* Style pour la description */
.description-container {
    max-width: 400px;
    text-align: left;
}

.description-container h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

.description-container p {
    font-size: 16px;
    color: #555;
}

/* Conteneur des liens de navigation */
.nav-container {
    display: flex;
    justify-content: center;
    gap: 30px; /* Espacement entre les liens */
    margin-top: 20px;
}

/* Style des liens */
.nav-link {
    font-size: 18px;
    font-weight: bold;
    text-decoration: none;
    color: #007bff;
    padding: 10px 20px;
    border: 2px solid #007bff;
    border-radius: 25px;
    transition: all 0.3s ease;
}

/* Effet au survol des liens */
.nav-link:hover {
    background-color: #007bff;
    color: white;
    box-shadow: 0px 4px 8px rgba(0, 123, 255, 0.2);
}
</style>
