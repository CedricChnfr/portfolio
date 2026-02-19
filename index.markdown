---
layout: default
---

<style>
/* Forcer la page d'accueil à prendre toute la largeur */
.page-content {
    padding: 0 !important;
}

.page-content .wrapper {
    max-width: 100% !important;
    padding: 0 !important;
}

/* Hero Section Moderne */
.hero-section {
    min-height: 75vh;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    margin: 0;
    padding: 80px 20px;
    position: relative;
    overflow: hidden;
    width: 100vw;
    margin-left: calc(-50vw + 50%);
}

.hero-background {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: 
        radial-gradient(circle at 20% 50%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 80%, rgba(255, 255, 255, 0.1) 0%, transparent 50%);
    animation: moveBackground 20s ease-in-out infinite;
}

@keyframes moveBackground {
    0%, 100% { transform: translateY(0) scale(1); }
    50% { transform: translateY(-20px) scale(1.1); }
}

.hero-content {
    display: flex;
    align-items: center;
    gap: 70px;
    max-width: 1200px;
    margin: 0 auto;
    position: relative;
    z-index: 1;
}

.profile-image-wrapper {
    position: relative;
    flex-shrink: 0;
}

.profile-image {
    width: 300px;
    height: 300px;
    border-radius: 50%;
    object-fit: cover;
    border: 6px solid rgba(255, 255, 255, 0.4);
    box-shadow: 0 25px 70px rgba(0, 0, 0, 0.35);
    animation: float 6s ease-in-out infinite;
    position: relative;
    z-index: 2;
}

@keyframes float {
    0%, 100% { transform: translateY(0px) rotate(0deg); }
    50% { transform: translateY(-25px) rotate(2deg); }
}

.image-ring, .image-ring-2 {
    position: absolute;
    border-radius: 50%;
    border: 3px solid rgba(255, 255, 255, 0.3);
}

.image-ring {
    top: -15px;
    left: -15px;
    right: -15px;
    bottom: -15px;
    animation: pulse 3s ease-in-out infinite;
}

.image-ring-2 {
    top: -30px;
    left: -30px;
    right: -30px;
    bottom: -30px;
    animation: pulse 3s ease-in-out infinite 1.5s;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); opacity: 0.5; }
    50% { transform: scale(1.08); opacity: 0.8; }
}

.hero-text {
    color: white;
    flex: 1;
}

.hero-title {
    font-size: 4em;
    font-weight: 900;
    margin: 0 0 15px 0;
    background: linear-gradient(to right, #fff, #f0f0f0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: slideInRight 1s ease-out;
    letter-spacing: -2px;
}

.hero-subtitle {
    font-size: 1.6em;
    margin: 0 0 25px 0;
    opacity: 0.95;
    font-weight: 400;
    animation: slideInRight 1s ease-out 0.2s both;
}

.hero-description {
    font-size: 1.25em;
    line-height: 1.7;
    margin: 0 0 40px 0;
    opacity: 0.95;
    animation: slideInRight 1s ease-out 0.4s both;
    max-width: 600px;
}

@keyframes slideInRight {
    from {
        opacity: 0;
        transform: translateX(60px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.hero-stats {
    display: flex;
    gap: 50px;
    margin-top: 40px;
    animation: slideInRight 1s ease-out 0.6s both;
}

.stat-item {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 15px 25px;
    background: rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    border-radius: 15px;
    transition: all 0.3s ease;
}

.stat-item:hover {
    background: rgba(255, 255, 255, 0.25);
    transform: translateY(-5px);
}

.stat-number {
    font-size: 3em;
    font-weight: 800;
    line-height: 1;
}

.stat-label {
    font-size: 0.95em;
    opacity: 0.9;
    margin-top: 8px;
}

/* Navigation Cards Améliorées */
.navigation-cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 35px;
    margin: 80px auto;
    max-width: 1200px;
    padding: 0 20px;
}

.nav-card {
    background: white;
    border-radius: 25px;
    text-decoration: none;
    color: #333;
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.1);
    transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    position: relative;
    overflow: hidden;
    min-height: 280px;
    display: flex;
    flex-direction: column;
}

.card-background {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, #667eea, #764ba2);
    opacity: 0;
    transition: opacity 0.5s ease;
}

.nav-card:hover .card-background {
    opacity: 1;
}

.card-content {
    position: relative;
    z-index: 1;
    padding: 35px 25px;
    flex: 1;
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    gap: 15px;
    transition: all 0.5s ease;
}

.nav-card:hover .card-content {
    color: white;
}

.nav-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 6px;
    background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
    transform: scaleX(0);
    transition: transform 0.5s ease;
}

.nav-card:hover::before {
    transform: scaleX(1);
}

.nav-card:hover {
    transform: translateY(-15px) scale(1.02);
    box-shadow: 0 25px 60px rgba(102, 126, 234, 0.3);
}

.card-icon {
    font-size: 2.5em;
    margin: 0;
    flex-shrink: 0;
    animation: bounce 2s ease infinite;
    transition: all 0.3s ease;
}

.nav-card:hover .card-icon {
    transform: scale(1.2) rotate(5deg);
    animation: none;
}

@keyframes bounce {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-12px); }
}

.card-text-content {
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 8px;
    width: 100%;
}

.nav-card h3 {
    font-size: 1.3em;
    margin: 0;
    color: #2d3748;
    font-weight: 800;
    transition: color 0.5s ease;
}

.nav-card:hover h3 {
    color: white;
}

.nav-card p {
    color: #718096;
    line-height: 1.5;
    margin: 0;
    font-size: 0.9em;
    transition: color 0.5s ease;
}

.nav-card:hover p {
    color: rgba(255, 255, 255, 0.95);
}

.card-arrow {
    font-size: 1.5em;
    color: #667eea;
    font-weight: bold;
    transition: all 0.4s ease;
    display: inline-block;
    flex-shrink: 0;
    align-self: flex-start;
}

.nav-card:hover .card-arrow {
    color: white;
    transform: translateX(15px);
}

.stacked-cards {
    display: flex;
    flex-direction: column;
    gap: 20px;
}

.nav-card-small {
    min-height: 120px;
    flex: 1;
}

.nav-card-small .card-content {
    padding: 20px 22px;
    gap: 8px;
}

.nav-card-small .card-icon {
    font-size: 1.8em;
}

.nav-card-small h3 {
    font-size: 1.1em;
}

.nav-card-small p {
    font-size: 0.8em;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.pro-card .card-background {
    background: linear-gradient(135deg, #f7971e, #ffd200);
}

.pro-card:hover .card-arrow {
    color: white;
}

/* Experience Section */
.experience-section {
    max-width: 1200px;
    margin: 80px auto 60px auto;
    padding: 80px 40px;
    background: white;
    border-radius: 40px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.08);
}

.experience-hidden {
    display: none !important;
    opacity: 0;
    max-height: 0;
    overflow: hidden;
    transition: all 0.5s ease;
}

.experience-hidden.show {
    display: flex !important;
    opacity: 1;
    max-height: 1000px;
    animation: fadeInLeft 0.8s ease-out both;
}

.show-more-btn {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    margin: 30px auto 0 auto;
    padding: 15px 35px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    border: none;
    border-radius: 50px;
    font-size: 1.1em;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
}

.show-more-btn:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 30px rgba(102, 126, 234, 0.4);
    background: linear-gradient(135deg, #764ba2, #667eea);
}

.show-more-btn .arrow {
    transition: transform 0.3s ease;
}

.show-more-btn.expanded .arrow {
    transform: rotate(180deg);
}

/* Formation Section */
.formation-section {
    max-width: 1200px;
    margin: 60px auto 80px auto;
    padding: 80px 40px;
    background: linear-gradient(135deg, #fff5f5 0%, #ffffff 100%);
    border-radius: 40px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.08);
}

.formation-timeline {
    display: flex;
    flex-direction: column;
    gap: 40px;
    margin-top: 40px;
}

.formation-item {
    display: flex;
    gap: 30px;
    padding: 35px;
    background: white;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.06);
    transition: all 0.4s ease;
    animation: fadeInLeft 0.8s ease-out var(--delay) both;
    border-left: 5px solid transparent;
}

.formation-item:hover {
    transform: translateX(10px);
    box-shadow: 0 12px 35px rgba(240, 147, 251, 0.15);
    border-left-color: #f093fb;
}

.formation-icon {
    font-size: 3em;
    flex-shrink: 0;
    width: 80px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #f093fb, #764ba2);
    border-radius: 50%;
    box-shadow: 0 8px 20px rgba(240, 147, 251, 0.3);
}

.formation-content {
    flex: 1;
}

.formation-content h3 {
    font-size: 1.6em;
    color: #2d3748;
    margin: 0 0 8px 0;
    font-weight: 700;
}

.formation-content h4 {
    font-size: 1.1em;
    color: #f093fb;
    margin: 0 0 15px 0;
    font-weight: 600;
}

.formation-content p {
    color: #4a5568;
    line-height: 1.7;
    margin: 0 0 20px 0;
    font-size: 1.05em;
}

.formation-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.formation-tags .tag {
    background: linear-gradient(135deg, rgba(240, 147, 251, 0.1), rgba(118, 75, 162, 0.1));
    color: #f093fb;
    border: 1px solid rgba(240, 147, 251, 0.2);
}

.formation-tags .tag:hover {
    background: linear-gradient(135deg, #f093fb, #764ba2);
    color: white;
}

.experience-timeline {
    display: flex;
    flex-direction: column;
    gap: 40px;
    margin-top: 40px;
}

.experience-item {
    display: flex;
    gap: 30px;
    padding: 35px;
    background: linear-gradient(135deg, #f8f9fa 0%, #ffffff 100%);
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.06);
    transition: all 0.4s ease;
    animation: fadeInLeft 0.8s ease-out var(--delay) both;
    border-left: 5px solid transparent;
}

.experience-item:hover {
    transform: translateX(10px);
    box-shadow: 0 12px 35px rgba(102, 126, 234, 0.15);
    border-left-color: #667eea;
}

@keyframes fadeInLeft {
    from {
        opacity: 0;
        transform: translateX(-40px);
    }
    to {
        opacity: 1;
        transform: translateX(0);
    }
}

.experience-icon {
    font-size: 3em;
    flex-shrink: 0;
    width: 80px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border-radius: 50%;
    box-shadow: 0 8px 20px rgba(102, 126, 234, 0.3);
}

.experience-content {
    flex: 1;
}

.experience-content h3 {
    font-size: 1.6em;
    color: #2d3748;
    margin: 0 0 8px 0;
    font-weight: 700;
}

.experience-content h4 {
    font-size: 1.1em;
    color: #667eea;
    margin: 0 0 15px 0;
    font-weight: 600;
}

.experience-content p {
    color: #4a5568;
    line-height: 1.7;
    margin: 0 0 20px 0;
    font-size: 1.05em;
}

.experience-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
}

.tag {
    display: inline-block;
    padding: 8px 16px;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
    color: #667eea;
    border-radius: 20px;
    font-size: 0.9em;
    font-weight: 600;
    border: 1px solid rgba(102, 126, 234, 0.2);
    transition: all 0.3s ease;
}

.tag:hover {
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

/* Skills Section Moderne */
.skills-section {
    max-width: 1200px;
    margin: 100px auto 80px auto;
    padding: 80px 40px;
    background: linear-gradient(135deg, #f5f7fa 0%, #e3e7ed 100%);
    border-radius: 40px;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
}

.section-title {
    text-align: center;
    font-size: 3em;
    margin-bottom: 60px;
    color: #2d3748;
    position: relative;
    padding-bottom: 25px;
    font-weight: 800;
}

.section-title::after {
    content: '';
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translateX(-50%);
    width: 120px;
    height: 5px;
    background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
    border-radius: 3px;
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
}

@media (min-width: 1200px) {
    .skills-grid {
        grid-template-columns: repeat(3, 1fr);
    }
}

.skill-card {
    background: white;
    padding: 40px 30px;
    border-radius: 20px;
    text-align: center;
    transition: all 0.4s ease;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.08);
    animation: fadeInUp 0.6s ease-out var(--delay) both;
}

.skill-card:hover {
    transform: translateY(-10px) scale(1.03);
    box-shadow: 0 15px 45px rgba(0, 0, 0, 0.15);
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(30px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.skill-icon {
    font-size: 3.5em;
    margin-bottom: 20px;
}

.skill-card h4 {
    font-size: 1.4em;
    margin: 20px 0 15px 0;
    color: #2d3748;
    font-weight: 700;
}

.skill-card p {
    color: #718096;
    line-height: 1.6;
    margin: 0 0 20px 0;
    font-size: 1.05em;
}

.skill-bar {
    width: 100%;
    height: 8px;
    background: #e2e8f0;
    border-radius: 10px;
    overflow: hidden;
    margin-top: 15px;
}

.skill-progress {
    height: 100%;
    background: linear-gradient(90deg, #667eea, #764ba2);
    border-radius: 10px;
    animation: fillBar 2s ease-out 1s both;
}

@keyframes fillBar {
    from { width: 0 !important; }
}

/* Search Bar Styles */
.search-container {
    position: fixed;
    top: 80px;
    right: 40px;
    z-index: 1000;
}

.search-button {
    width: 50px;
    height: 50px;
    border-radius: 50%;
    background: linear-gradient(135deg, #667eea, #764ba2);
    border: none;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4);
    transition: all 0.3s ease;
}

.search-button:hover {
    transform: scale(1.1);
    box-shadow: 0 12px 30px rgba(102, 126, 234, 0.6);
}

.search-button svg {
    width: 24px;
    height: 24px;
    fill: white;
}

.search-modal {
    display: none;
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: rgba(0, 0, 0, 0.8);
    z-index: 2000;
    align-items: center;
    justify-content: center;
    backdrop-filter: blur(5px);
}

.search-modal.active {
    display: flex;
}

.search-box {
    background: white;
    border-radius: 20px;
    padding: 40px;
    max-width: 700px;
    width: 90%;
    max-height: 80vh;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
}

.search-input-wrapper {
    position: relative;
    margin-bottom: 30px;
}

.search-input {
    width: 100%;
    padding: 18px 50px 18px 20px;
    font-size: 1.1em;
    border: 2px solid #e2e8f0;
    border-radius: 12px;
    outline: none;
    transition: all 0.3s ease;
}

.search-input:focus {
    border-color: #667eea;
    box-shadow: 0 0 0 4px rgba(102, 126, 234, 0.1);
}

.search-clear {
    position: absolute;
    right: 15px;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    font-size: 1.5em;
    color: #a0aec0;
    cursor: pointer;
    display: none;
}

.search-clear.visible {
    display: block;
}

.search-results {
    overflow-y: auto;
    flex: 1;
}

.search-result-item {
    padding: 20px;
    border-bottom: 1px solid #e2e8f0;
    cursor: pointer;
    transition: all 0.3s ease;
    border-radius: 10px;
    margin-bottom: 10px;
}

.search-result-item:hover {
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
    transform: translateX(5px);
}

.search-result-title {
    font-size: 1.3em;
    font-weight: 700;
    color: #2d3748;
    margin-bottom: 8px;
}

.search-result-excerpt {
    color: #718096;
    line-height: 1.6;
    font-size: 0.95em;
}

.search-result-highlight {
    background: #fef3c7;
    padding: 2px 4px;
    border-radius: 3px;
    font-weight: 600;
}

.search-no-results {
    text-align: center;
    padding: 60px 20px;
    color: #718096;
}

.search-no-results-icon {
    font-size: 4em;
    margin-bottom: 20px;
    opacity: 0.3;
}

.search-close {
    position: absolute;
    top: 20px;
    right: 20px;
    background: none;
    border: none;
    font-size: 2em;
    color: #a0aec0;
    cursor: pointer;
    line-height: 1;
    transition: all 0.3s ease;
}

.search-close:hover {
    color: #667eea;
    transform: rotate(90deg);
}

/* Responsive Design */
/* Tablettes */
@media (max-width: 1024px) and (min-width: 768px) {
    .navigation-cards {
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 25px;
    }
}

/* Mobile */
@media (max-width: 900px) {
    .hero-content {
        flex-direction: column;
        text-align: center;
        gap: 40px;
    }
    
    .hero-title {
        font-size: 3em;
    }
    
    .hero-subtitle {
        font-size: 1.3em;
    }
    
    .hero-description {
        max-width: 100%;
    }
    
    .hero-stats {
        justify-content: center;
        flex-wrap: wrap;
        gap: 25px;
    }
    
    .profile-image {
        width: 220px;
        height: 220px;
    }
    
    .navigation-cards {
        grid-template-columns: 1fr !important;
        gap: 20px;
        margin: 40px auto;
    }
    
    .nav-card {
        min-height: 200px;
    }
    
    .experience-section {
        padding: 60px 20px;
        margin: 60px 20px;
    }
    
    .experience-item {
        flex-direction: column;
        text-align: center;
        padding: 25px;
    }
    
    .experience-item:hover {
        transform: translateY(-5px);
    }
    
    .experience-icon {
        margin: 0 auto;
    }
    
    .formation-section {
        padding: 60px 20px;
        margin: 60px 20px;
    }
    
    .formation-item {
        flex-direction: column;
        text-align: center;
        padding: 25px;
    }
    
    .formation-item:hover {
        transform: translateY(-5px);
    }
    
    .formation-icon {
        margin: 0 auto;
    }
    
    .skills-section {
        padding: 60px 20px;
        margin: 60px 20px;
    }

    .stacked-cards {
        gap: 20px;
    }
}

@media (max-width: 600px) {
    .hero-title {
        font-size: 2.2em;
    }
    
    .hero-section {
        min-height: 60vh;
        padding: 60px 15px;
    }
    
    .stat-item {
        padding: 10px 15px;
    }
    
    .stat-number {
        font-size: 2.2em;
    }
}
</style>

<!-- Search Button -->
<div class="search-container">
    <button class="search-button" onclick="openSearch()" title="Search">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
            <path d="M15.5 14h-.79l-.28-.27C15.41 12.59 16 11.11 16 9.5 16 5.91 13.09 3 9.5 3S3 5.91 3 9.5 5.91 16 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/>
        </svg>
    </button>
</div>

<!-- Search Modal -->
<div class="search-modal" id="searchModal" onclick="closeSearchOnOutsideClick(event)">
    <div class="search-box" onclick="event.stopPropagation()">
        <button class="search-close" onclick="closeSearch()">&times;</button>
        <div class="search-input-wrapper">
            <input
                type="text"
                class="search-input"
                id="searchInput"
                placeholder="Search courses, projects, topics..."
                data-i18n-placeholder="search-placeholder"
                autocomplete="off"
            >
            <button class="search-clear" id="searchClear" onclick="clearSearch()">&times;</button>
        </div>
        <div class="search-results" id="searchResults">
            <div class="search-no-results">
                <div class="search-no-results-icon">🔍</div>
                <p data-i18n="search-default-message">Start typing to search through all courses and content...</p>
            </div>
        </div>
    </div>
</div>

<script>
let searchData = [];

// Load search data (cache-bust to avoid stale URLs)
fetch('{{ "/search.json" | relative_url }}?v={{ site.time | date: "%s" }}')
    .then(response => {
        if (!response.ok) {
            throw new Error('Search data not found');
        }
        return response.json();
    })
    .then(data => {
        searchData = data;
    })
    .catch(() => {});

function openSearch() {
    document.getElementById('searchModal').classList.add('active');
    document.getElementById('searchInput').focus();
}

function closeSearch() {
    document.getElementById('searchModal').classList.remove('active');
    clearSearch();
}

function closeSearchOnOutsideClick(event) {
    if (event.target === document.getElementById('searchModal')) {
        closeSearch();
    }
}

function clearSearch() {
    const input = document.getElementById('searchInput');
    input.value = '';
    document.getElementById('searchClear').classList.remove('visible');
    var defaultMsg = window.i18n ? window.i18n.t('search-default-message') : 'Start typing to search through all courses and content...';
    document.getElementById('searchResults').innerHTML = `
        <div class="search-no-results">
            <div class="search-no-results-icon">🔍</div>
            <p>${defaultMsg}</p>
        </div>
    `;
}

// Search functionality
document.getElementById('searchInput').addEventListener('input', function(e) {
    const query = e.target.value.trim().toLowerCase();
    const clearBtn = document.getElementById('searchClear');
    
    if (query.length > 0) {
        clearBtn.classList.add('visible');
    } else {
        clearBtn.classList.remove('visible');
        clearSearch();
        return;
    }
    
    if (query.length < 2) return;
    
    const results = searchData.filter(item => {
        return item.title.toLowerCase().includes(query) || 
               item.content.toLowerCase().includes(query);
    });
    
    displayResults(results, query);
});

function displayResults(results, query) {
    const resultsContainer = document.getElementById('searchResults');
    
    if (results.length === 0) {
        var noResultsMsg = window.i18n ? window.i18n.t('search-no-results') : 'No results found for';
        resultsContainer.innerHTML = `
            <div class="search-no-results">
                <div class="search-no-results-icon">😕</div>
                <p>${noResultsMsg} "<strong>${escapeHtml(query)}</strong>"</p>
            </div>
        `;
        return;
    }
    
    resultsContainer.innerHTML = results.map(result => {
        const excerpt = getExcerpt(result.content, query);
        const highlightedTitle = highlightText(result.title, query);
        const highlightedExcerpt = highlightText(excerpt, query);
        
        return `
            <div class="search-result-item" onclick="window.location.href='${result.url}'">
                <div class="search-result-title">${highlightedTitle}</div>
                <div class="search-result-excerpt">${highlightedExcerpt}</div>
            </div>
        `;
    }).join('');
}

function getExcerpt(content, query) {
    const lowerContent = content.toLowerCase();
    const lowerQuery = query.toLowerCase();
    const index = lowerContent.indexOf(lowerQuery);
    
    if (index === -1) {
        return content.substring(0, 200) + '...';
    }
    
    const start = Math.max(0, index - 100);
    const end = Math.min(content.length, index + query.length + 100);
    const excerpt = content.substring(start, end);
    
    return (start > 0 ? '...' : '') + excerpt + (end < content.length ? '...' : '');
}

function highlightText(text, query) {
    const regex = new RegExp(`(${escapeRegex(query)})`, 'gi');
    return escapeHtml(text).replace(regex, '<span class="search-result-highlight">$1</span>');
}

function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

function escapeRegex(string) {
    return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
}

// Close on Escape key
document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && document.getElementById('searchModal').classList.contains('active')) {
        closeSearch();
    }
});
</script>

<div class="hero-section">
    <div class="hero-background"></div>
    <div class="hero-content">
        <div class="profile-image-wrapper">
            <div class="image-ring"></div>
            <div class="image-ring-2"></div>
            <img src="/img/Photo.jpg" alt="Cédric Chanfreau" class="profile-image">
        </div>
        
        <div class="hero-text">
            <h1 class="hero-title">Cédric Chanfreau</h1>
            <p class="hero-subtitle" data-i18n="hero-subtitle">Ingénieur Diplômé INSA Toulouse • Automatique & Électronique</p>
            <p class="hero-description" data-i18n="hero-description">
                            Diplômé 2025 d'un Diplôme d'Ingénieur INSA Toulouse et d'un Master 2 ENSEEIHT,
                            spécialisé en développement logiciel et systèmes embarqués.
                            Passionné par la réalisation de projets innovants, je suis actuellement ouvert aux opportunités professionnelles.
                        </p>
                        
            <div class="hero-stats">
                <div class="stat-item">
                    <span class="stat-number">5</span>
                    <span class="stat-label" data-i18n="stat-label-studies">Ans d'études ingénieur</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">25+</span>
                    <span class="stat-label" data-i18n="stat-label-projects">Projets techniques</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">3</span>
                    <span class="stat-label" data-i18n="stat-label-alternance">Ans d'alternance</span>
                </div>
            </div>
        </div>
    </div>
</div>

<div class="navigation-cards">
    <a href="./my-courses-2024-2025.html" class="nav-card courses-card">
        <div class="card-background"></div>
        <div class="card-content">
            <div class="card-icon">📚</div>
            <h3 data-i18n="nav-courses-title">Mes Cours</h3>
            <p data-i18n="nav-courses-desc">Découvrez mon parcours académique complet et les compétences techniques acquises</p>
            <span class="card-arrow">→</span>
        </div>
    </a>
    
    <div class="stacked-cards">
        <a href="./my-projects.html" class="nav-card projects-card nav-card-small">
            <div class="card-background"></div>
            <div class="card-content">
                <div class="card-icon">🎓</div>
                <h3 data-i18n="nav-projects-title">Projets Académiques</h3>
                <p data-i18n="nav-projects-desc">Explorez mes réalisations techniques et projets d'études</p>
                <span class="card-arrow">→</span>
            </div>
        </a>
        <a href="./my-pro-projects.html" class="nav-card pro-card nav-card-small">
            <div class="card-background"></div>
            <div class="card-content">
                <div class="card-icon">💼</div>
                <h3 data-i18n="nav-pro-projects-title">Projets Professionnels</h3>
                <p data-i18n="nav-pro-projects-desc">Mini-projets réalisés lors de mes alternances en entreprise</p>
                <span class="card-arrow">→</span>
            </div>
        </a>
    </div>
    
    <a href="./my-perso-projects.html" class="nav-card perso-card">
        <div class="card-background"></div>
        <div class="card-content">
            <div class="card-icon">💡</div>
            <h3 data-i18n="nav-perso-title">Projets Personnels</h3>
            <p data-i18n="nav-perso-desc">Découvrez mes créations personnelles et expérimentations</p>
            <span class="card-arrow">→</span>
        </div>
    </a>
    
    <a href="./my-cv.html" class="nav-card cv-card">
        <div class="card-background"></div>
        <div class="card-content">
            <div class="card-icon">📄</div>
            <h3 data-i18n="nav-cv-title">Mon CV</h3>
            <p data-i18n="nav-cv-desc">Consultez mon parcours professionnel et mes compétences</p>
            <span class="card-arrow">→</span>
        </div>
    </a>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; max-width: 1400px; margin: 80px auto; padding: 0 20px;">
    <div class="experience-section" style="margin: 0;">
        <h2 class="section-title" data-i18n="experience-title">Parcours Professionnel</h2>
        <div class="experience-timeline">
            <div class="experience-item" style="--delay: 0s">
                <div class="experience-icon">🔒</div>
                <div class="experience-content">
                    <h3 data-i18n="exp1-title">Ingénieur Logiciel Embarqué - Cybersécurité</h3>
                    <h4><a href="https://www.schaeffler.fr/fr/" target="_blank" style="color: #667eea; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#764ba2'" onmouseout="this.style.color='#667eea'">Schaeffler</a> • Oct. 2024 - Sept. 2025</h4>
                    <p data-i18n="exp1-desc">Développement du Secure Logger, un composant logiciel embarqué générique pour l'enregistrement et la gestion des événements de sécurité dans les calculateurs automobiles (ECUs). Revue de code et développement de logiciels critiques.</p>
                    <div class="experience-tags">
                        <span class="tag">Cybersécurité</span>
                        <span class="tag">C/C++</span>
                        <span class="tag">ECU</span>
                        <span class="tag">Automotive</span>
                    </div>
                </div>
            </div>
            
            <div class="experience-item" style="--delay: 0.15s">
                <div class="experience-icon">🌍</div>
                <div class="experience-content">
                    <h3 data-i18n="exp2-title">Stage Mobilité Internationale Ingénierie</h3>
                    <h4><a href="https://www.vitesco-technologies.com/fr-fr" target="_blank" style="color: #667eea; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#764ba2'" onmouseout="this.style.color='#667eea'">Vitesco Technologies</a> • Juil. - Sept. 2024 • Iasi, Roumanie</h4>
                    <p data-i18n="exp2-desc">Étude et implémentation de solutions pour la gestion de la mémoire Flash sur un nouveau microcontrôleur. Test et validation des fonctionnalités pour garantir la fiabilité et la performance de la nouvelle plateforme.</p>
                    <div class="experience-tags">
                        <span class="tag">Microcontrôleurs</span>
                        <span class="tag">Flash Memory</span>
                        <span class="tag">Jenkins</span>
                        <span class="tag">Testing</span>
                    </div>
                </div>
            </div>
            
            <div class="experience-item" style="--delay: 0.3s">
                <div class="experience-icon">🚀</div>
                <div class="experience-content">
                    <h3 data-i18n="exp3-title">Ingénieur Logiciel Embarqué</h3>
                    <h4><a href="https://www.vitesco-technologies.com/fr-fr" target="_blank" style="color: #667eea; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#764ba2'" onmouseout="this.style.color='#667eea'">Vitesco Technologies</a> • Sept. 2022 - Sept. 2024</h4>
                    <p data-i18n="exp3-desc">Développement de solutions génériques embarquées pour la reprogrammation des ECUs. Création d'environnements d'automatisation des tests avec Python et Jenkins. Correction de code conforme aux standards MISRA et CERT pour garantir la sécurité et la qualité.</p>
                    <div class="experience-tags">
                        <span class="tag">C/C++</span>
                        <span class="tag">Python</span>
                        <span class="tag">Jenkins</span>
                        <span class="tag">MISRA/CERT</span>
                    </div>
                </div>
            </div>
            
            <div class="experience-item experience-hidden" style="--delay: 0.45s">
                <div class="experience-icon">⚙️</div>
                <div class="experience-content">
                    <h3 data-i18n="exp4-title">Technicien Méthodes Électroniques</h3>
                    <h4><a href="https://www.siemens.com/fr/fr.html" target="_blank" style="color: #667eea; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#764ba2'" onmouseout="this.style.color='#667eea'">Siemens</a> • Avr. - Juil. 2022 • Stage</h4>
                    <p data-i18n="exp4-desc">Analyse complète du système de rack frein VAL208NG. Réalisation de tests fonctionnels sur les cartes électroniques pour garantir des performances optimales. Développement d'un banc de tests pour la carte entrées-sorties, assurant des évaluations complètes.</p>
                    <div class="experience-tags">
                        <span class="tag">Tests Électroniques</span>
                        <span class="tag">Cartes PCB</span>
                        <span class="tag">Banc de Tests</span>
                        <span class="tag">VAL208NG</span>
                    </div>
                </div>
            </div>
        </div>
        
        <button class="show-more-btn" onclick="toggleExperiences()" id="experienceToggle">
            <span id="experienceToggleText" data-i18n="show-more">Voir plus</span>
            <span class="arrow">▼</span>
        </button>
    </div>

    <div class="formation-section" style="margin: 0;">
        <h2 class="section-title" data-i18n="formation-title">Formation</h2>
        <div class="formation-timeline">
            <div class="formation-item" style="--delay: 0s">
                <div class="formation-icon">🎓</div>
                <div class="formation-content">
                    <h3><a href="https://formations.enseeiht.fr/enseeiht/fr/index/master-lmd-XB/master-reseaux-embarques-et-objets-connectes-M3XKUK0T.html" target="_blank" style="color: #2d3748; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#667eea'" onmouseout="this.style.color='#2d3748'" data-i18n="formation1-title">Master 2 Réseaux Embarqués et Objets Connectés (REOC)</a></h3>
                    <h4>ENSEEIHT • Sept. 2024 - Sept. 2025</h4>
                    <p data-i18n="formation1-desc">Formation spécialisée en systèmes embarqués et objets connectés avec un focus sur l'intégration des technologies de communication, le traitement des données et l'interconnexion des dispositifs. Développement de compétences avancées en IoT, protocoles de communication et sécurité des réseaux.</p>
                    <div class="formation-tags">
                        <span class="tag">IoT</span>
                        <span class="tag">QoS</span>
                        <span class="tag">Réseaux Embarqués</span>
                        <span class="tag">Communication</span>
                    </div>
                </div>
            </div>
            
            <div class="formation-item" style="--delay: 0.2s">
                <div class="formation-icon">🏛️</div>
                <div class="formation-content">
                    <h3><a href="https://www.insa-toulouse.fr/formation/ingenieur-specialite-automatique-electronique/" target="_blank" style="color: #2d3748; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#667eea'" onmouseout="this.style.color='#2d3748'" data-i18n="formation2-title">Diplôme d'Ingénieur - Automatique Électronique</a></h3>
                    <h4>INSA Toulouse • Sept. 2022 - Sept. 2025</h4>
                    <p data-i18n="formation2-desc">Formation d'ingénieur experts en technologies intelligentes pour les systèmes connectés. Compétences en conception de dispositifs intelligents (microcontrôleurs, IA embarquée, capteurs), sécurité des systèmes, réseaux de capteurs sans fil, 5G, architectures middleware et cloud/edge computing.</p>
                    <div class="formation-tags">
                        <span class="tag">Systèmes Embarqués</span>
                        <span class="tag">IA Embarquée</span>
                        <span class="tag">5G</span>
                        <span class="tag">Edge Computing</span>
                        <span class="tag">SOA</span>
                    </div>
                </div>
            </div>
            
            <div class="formation-item" style="--delay: 0.4s">
                <div class="formation-icon">🔌</div>
                <div class="formation-content">
                    <h3><a href="https://iut.univ-tlse3.fr/" target="_blank" style="color: #2d3748; text-decoration: none; transition: color 0.3s;" onmouseover="this.style.color='#667eea'" onmouseout="this.style.color='#2d3748'" data-i18n="formation3-title">DUT GEII - Génie Électrique et Informatique Industrielle</a></h3>
                    <h4>IUT Paul Sabatier - Toulouse, Auch, Castres • 2020 - 2022</h4>
                    <p data-i18n="formation3-desc">Formation technique approfondie en génie électrique et électronique. Acquisition de compétences pratiques en électronique, automatisme, informatique industrielle et systèmes embarqués. Projets concrets en électronique de puissance, traitement du signal et automatique.</p>
                    <div class="formation-tags">
                        <span class="tag">Électronique</span>
                        <span class="tag">Automatisme</span>
                        <span class="tag">Informatique Industrielle</span>
                        <span class="tag">Électrotechnique</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
@media (max-width: 1200px) {
    div[style*="grid-template-columns: 1fr 1fr"] {
        grid-template-columns: 1fr !important;
    }
}
</style>

<div class="skills-section">
    <h2 class="section-title" data-i18n="skills-title">Domaines d'Expertise</h2>
    <div class="skills-grid">
        <div class="skill-card" style="--delay: 0s">
            <div class="skill-icon">💻</div>
            <h4 data-i18n="skill-dev">Développement Logiciel</h4>
            <p>C/C++, Python, Java, JavaScript, MATLAB, SQL</p>
            <div class="skill-bar">
                <div class="skill-progress" style="width: 92%"></div>
            </div>
        </div>
        <div class="skill-card" style="--delay: 0.1s">
            <div class="skill-icon">🤖</div>
            <h4 data-i18n="skill-ai">Intelligence Artificielle</h4>
            <p>Machine Learning, Deep Learning, TensorFlow, PyTorch</p>
            <div class="skill-bar">
                <div class="skill-progress" style="width: 85%"></div>
            </div>
        </div>
        <div class="skill-card" style="--delay: 0.2s">
            <div class="skill-icon">🌐</div>
            <h4 data-i18n="skill-iot">IoT & Edge Computing</h4>
            <p>5G, LoRa, MQTT, Cloud Computing, Architectures distribuées</p>
            <div class="skill-bar">
                <div class="skill-progress" style="width: 88%"></div>
            </div>
        </div>
        <div class="skill-card" style="--delay: 0.3s">
            <div class="skill-icon">🔧</div>
            <h4 data-i18n="skill-embedded">Systèmes Embarqués</h4>
            <p>STM32, Arduino, VHDL, PCB Design, Temps Réel</p>
            <div class="skill-bar">
                <div class="skill-progress" style="width: 87%"></div>
            </div>
        </div>
        <div class="skill-card" style="--delay: 0.4s">
            <div class="skill-icon">🔐</div>
            <h4 data-i18n="skill-cyber">Cybersécurité Embarquée</h4>
            <p>Sécurité ECU, AUTOSAR, Secure Logger, Standards ISO 21434</p>
            <div class="skill-bar">
                <div class="skill-progress" style="width: 82%"></div>
            </div>
        </div>
        <div class="skill-card" style="--delay: 0.5s">
            <div class="skill-icon">⚡</div>
            <h4 data-i18n="skill-control">Automatique & Contrôle</h4>
            <p>Systèmes linéaires/non-linéaires, Robotique, Modélisation</p>
            <div class="skill-bar">
                <div class="skill-progress" style="width: 90%"></div>
            </div>
        </div>
    </div>
</div>

<script>
function toggleExperiences() {
    const hiddenItems = document.querySelectorAll('.experience-hidden');
    const button = document.getElementById('experienceToggle');
    const buttonText = document.getElementById('experienceToggleText');
    const isExpanded = button.classList.contains('expanded');

    if (isExpanded) {
        hiddenItems.forEach(item => {
            item.classList.remove('show');
        });
        button.classList.remove('expanded');
        buttonText.textContent = window.i18n ? window.i18n.t('show-more') : 'Voir plus';
    } else {
        hiddenItems.forEach(item => {
            item.classList.add('show');
        });
        button.classList.add('expanded');
        buttonText.textContent = window.i18n ? window.i18n.t('show-less') : 'Voir moins';
    }
}

// Update button text when language changes
document.addEventListener('langChanged', function() {
    var button = document.getElementById('experienceToggle');
    var buttonText = document.getElementById('experienceToggleText');
    if (button && buttonText && window.i18n) {
        var isExpanded = button.classList.contains('expanded');
        buttonText.textContent = isExpanded ? window.i18n.t('show-less') : window.i18n.t('show-more');
    }
});
</script>

