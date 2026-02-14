---
layout: default
title:  "Portfolio"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

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

<div class="back-nav">
  <a href="./my-courses-2024-2025.html" data-i18n-html="back_courses_2024_2025">← Back to My Courses 2024-2025</a>
</div>

<div class="lang-fr">

<h1>Portfolio</h1>

<h2>PART A : PRESENTATION GENERALE</h2>

<h3>Presentation</h3>

<p>Le portfolio est un exercice de pratique reflexive essentiel dans la formation d'ingenieur a l'INSA Toulouse. Il s'inscrit dans le cadre de la certification RNCP (Repertoire National des Certifications Professionnelles), qui exige de l'etudiant qu'il soit capable de documenter, analyser et valoriser les competences acquises tout au long de son parcours.</p>

<p>L'objectif de ce portfolio est de constituer une trace structuree et evolutive de mon parcours academique et professionnel. Il ne s'agit pas simplement de lister des cours ou des projets, mais de mener une reflexion approfondie sur les apprentissages realises, les competences developpees et les axes d'amelioration identifies. Cette demarche s'inscrit dans une logique d'amelioration continue et de construction d'une identite professionnelle coherente.</p>

<h3>Structure du portfolio</h3>

<p>Le portfolio est organise en plusieurs sections principales :</p>

<ol>
  <li><strong>Courses</strong> : Descriptions detaillees des cours suivis, incluant le contenu aborde, la duree, et les apprentissages cles.</li>
  <li><strong>Projects</strong> : Vue d'ensemble des projets realises, avec les objectifs, methodologies et resultats.</li>
  <li><strong>CV</strong> : Mon curriculum vitae, presentant mon parcours academique, mes experiences professionnelles, mes competences techniques et mes activites extra-curriculaires.</li>
  <li><strong>About</strong> : Informations sur mon parcours, mes interets et mes aspirations futures.</li>
</ol>

<h3>Objectifs</h3>

<p>Les objectifs de ce portfolio sont de :</p>

<ul>
  <li>Presenter une vue claire et organisee de mon parcours educatif et professionnel.</li>
  <li>Demontrer mon expertise dans differents domaines techniques, notamment l'IoT, les systemes embarques et le developpement logiciel.</li>
  <li>Mettre en valeur ma capacite a appliquer les connaissances theoriques a des situations pratiques a travers des projets et des stages.</li>
  <li>Servir de ressource pour de potentiels employeurs, en mettant en avant mes competences et experiences.</li>
  <li>Refleter sur mon apprentissage et ma progression, en identifiant les domaines a developper davantage.</li>
</ul>

<h2>PART B : EXPERIENCE ET CONTEXTE</h2>

<h3>Environnement technique</h3>

<p>Ce portfolio a ete entierement developpe sous forme de site web statique en utilisant <strong>Jekyll</strong>, un generateur de sites statiques ecrit en Ruby. Le site est heberge sur <strong>GitHub Pages</strong>, ce qui permet un deploiement automatique a chaque push sur la branche principale du depot Git.</p>

<h4>Outils de developpement</h4>

<p>Les principaux outils utilises pour la realisation de ce portfolio sont :</p>

<ul>
  <li><strong>Jekyll</strong> : Generateur de sites statiques utilisant le theme Minima comme base. Jekyll transforme des fichiers Markdown en pages HTML completes.</li>
  <li><strong>GitHub Pages</strong> : Service d'hebergement gratuit de GitHub permettant de servir le site directement depuis le depot.</li>
  <li><strong>Git</strong> : Systeme de controle de version utilise pour suivre l'evolution du code et du contenu du portfolio.</li>
  <li><strong>Visual Studio Code</strong> : Editeur de code utilise pour le developpement, avec des extensions pour Markdown, HTML et CSS.</li>
  <li><strong>Kramdown</strong> : Moteur de rendu Markdown utilise par Jekyll pour convertir le contenu ecrit en Markdown vers du HTML.</li>
</ul>

<h4>Organisation du depot</h4>

<p>Le depot est organise selon la structure standard de Jekyll :</p>
<ul>
  <li><code>_posts/</code> : Contient tous les articles organises par annee scolaire (2022-2023, 2023-2024, 2024-2025) et par categorie (Courses, Personal_Project).</li>
  <li><code>_includes/</code> : Fichiers HTML reutilisables (chatbot, footer).</li>
  <li><code>_config.yml</code> : Configuration globale du site (titre, URL, plugins).</li>
  <li><code>img/</code> et <code>cours-pdf/</code> : Ressources statiques (images, rapports PDF).</li>
  <li><code>assets/</code> : Feuilles de style et scripts.</li>
  <li><code>search.json</code> : Index de recherche pour la fonctionnalite de recherche du site.</li>
</ul>

<h2>PART C : ASPECTS TECHNIQUES</h2>

<h3>1. Framework Jekyll et templating Liquid</h3>

<p>Jekyll repose sur le moteur de templates <strong>Liquid</strong>, developpe par Shopify. Ce systeme permet d'utiliser des variables, des boucles et des conditions dans les fichiers HTML. Par exemple, la page d'accueil utilise des boucles Liquid pour generer dynamiquement la liste des articles :</p>

<pre><code>{% raw %}{% for post in site.posts %}
  &lt;li&gt;&lt;a href="{{ post.url }}"&gt;{{ post.title }}&lt;/a&gt;&lt;/li&gt;
{% endfor %}{% endraw %}</code></pre>

<p>Chaque page du site commence par un bloc <strong>YAML Front Matter</strong> qui definit les metadonnees : le layout utilise, le titre, la date et les categories. Ce mecanisme permet a Jekyll de savoir comment traiter et rendre chaque fichier.</p>

<pre><code>---
layout: default
title: "Portfolio"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---</code></pre>

<p>Le contenu est ensuite redige en <strong>Markdown</strong> (syntaxe Kramdown), ce qui facilite la redaction et la maintenance du contenu sans avoir a manipuler directement du HTML.</p>

<h3>2. Architecture du site</h3>

<p>L'architecture du site repose sur plusieurs concepts cles de Jekyll :</p>

<ul>
  <li><strong>Layouts</strong> : Le layout <code>default</code> fournit la structure HTML de base (en-tete, navigation, pied de page) dans laquelle le contenu de chaque page est injecte.</li>
  <li><strong>Includes</strong> : Les fichiers <code>_includes/</code> permettent de reutiliser des composants HTML. Le site utilise notamment un composant <code>chatbot.html</code> pour l'assistant conversationnel et un <code>footer.html</code> pour le pied de page.</li>
  <li><strong>Posts Collection</strong> : Les articles sont organises dans <code>_posts/</code> avec une convention de nommage <code>YYYY-MM-DD-titre.markdown</code>. Jekyll genere automatiquement les URLs et l'index a partir de cette structure.</li>
</ul>

<h3>3. Design responsive avec CSS</h3>

<p>Chaque page du portfolio integre des styles CSS personnalises pour assurer une presentation coherente et agreable. Les elements stylistiques principaux comprennent :</p>

<ul>
  <li>Une palette de couleurs basee sur le bleu (<code>#007BFF</code> pour les titres, <code>#66B2FF</code> pour les boutons).</li>
  <li>Des boutons stylises avec des transitions et des effets de survol (<code>hover</code>).</li>
  <li>Un texte justifie pour une meilleure lisibilite.</li>
  <li>Un arriere-plan clair (<code>#f4f4f9</code>) pour un contraste optimal.</li>
</ul>

<h3>4. Fonctionnalite de recherche</h3>

<p>Le site integre une fonctionnalite de recherche implementee via un fichier <code>search.json</code> qui indexe l'ensemble des articles. Ce fichier JSON est genere dynamiquement par Jekyll a partir des metadonnees des posts, permettant une recherche cote client rapide et efficace sans necessite de serveur backend.</p>

<h3>5. Integration d'un chatbot</h3>

<p>Un chatbot conversationnel a ete integre au portfolio via le composant <code>_includes/chatbot.html</code>. Cette fonctionnalite enrichit l'experience utilisateur en permettant aux visiteurs d'interagir avec le site de maniere dynamique.</p>

<h3>6. Integration de documents PDF</h3>

<p>Pour les pages de cours, le portfolio utilise des balises <code>&lt;iframe&gt;</code> pour integrer directement les rapports et documents PDF dans les pages. Cela permet aux visiteurs de consulter les documents sans quitter le site, avec un lien de telechargement disponible en complement.</p>

<pre><code>&lt;iframe src="/cours-pdf/document.pdf" width="100%" height="800px"&gt;&lt;/iframe&gt;</code></pre>

<h3>7. Pipeline de deploiement</h3>

<p>Le deploiement du portfolio suit un pipeline simple mais efficace :</p>

<ol>
  <li>Modification du contenu localement (ajout de pages, edition de Markdown).</li>
  <li>Commit et push des modifications sur le depot GitHub.</li>
  <li>GitHub Pages detecte automatiquement les changements et declenche une reconstruction du site via Jekyll.</li>
  <li>Le site mis a jour est servi sur le domaine personnalise <code>cedric.littlenuage.com</code>.</li>
</ol>

<h3>8. Controle de version avec Git</h3>

<p>L'ensemble du portfolio est gere sous <strong>Git</strong>, ce qui permet de :</p>

<ul>
  <li>Suivre l'historique complet des modifications apportees au contenu et au code.</li>
  <li>Revenir a une version anterieure en cas de besoin.</li>
  <li>Travailler sur des fonctionnalites en parallele via des branches.</li>
  <li>Documenter les evolutions du site a travers les messages de commit.</li>
</ul>

<h2>PART D : ANALYSE ET REFLEXION</h2>

<h3>Pratique reflexive</h3>

<p>La creation et la maintenance de ce portfolio constituent un exercice de pratique reflexive a part entiere. Chaque page de cours suit une structure en quatre parties (Presentation generale, Partie descriptive, Partie technique, Partie analytique) qui m'oblige a ne pas simplement decrire ce que j'ai fait, mais aussi a analyser ce que j'ai appris, comment je l'ai appris, et ce que cela signifie pour mon developpement professionnel.</p>

<p>Cette demarche reflexive m'a permis de prendre du recul sur mes apprentissages et de mieux comprendre les liens entre les differents cours et projets de ma formation.</p>

<h3>Documentation des competences</h3>

<p>Le portfolio sert de preuve tangible des competences acquises tout au long de la formation. En documentant systematiquement les aspects techniques de chaque cours, les projets realises et les reflexions personnelles, je constitue un dossier qui peut etre presente dans le cadre de la certification RNCP et qui demontre ma capacite a :</p>

<ul>
  <li>Analyser des problemes techniques complexes.</li>
  <li>Mettre en oeuvre des solutions adaptees.</li>
  <li>Communiquer efficacement sur des sujets techniques.</li>
  <li>Travailler en equipe et gerer des projets.</li>
</ul>

<h3>Identite professionnelle</h3>

<p>Au-dela de la simple documentation, le portfolio contribue a la construction de mon identite professionnelle. En choisissant de le realiser sous forme de site web statique plutot que sous forme de document classique, j'ai demontre des competences en developpement web, en gestion de contenu et en deploiement d'applications, ce qui enrichit mon profil d'ingenieur en IoT et systemes embarques.</p>

<p>Le fait de maintenir un site web public accessible a tous constitue egalement une vitrine professionnelle qui va au-dela du simple CV, en montrant concretement ce que je sais faire et comment je travaille.</p>

<h3>Amelioration continue</h3>

<p>Ce portfolio est un projet vivant, en constante evolution. Chaque semestre, de nouvelles pages sont ajoutees pour les nouveaux cours et projets. Les pages existantes peuvent etre ameliorees et enrichies. Cette demarche d'amelioration continue reflete la philosophie de la formation d'ingenieur : ne jamais cesser d'apprendre et de progresser.</p>

<p>Parmi les ameliorations futures envisagees :</p>
<ul>
  <li>Enrichissement du contenu technique de chaque page de cours.</li>
  <li>Amelioration de l'accessibilite et du design responsive.</li>
  <li>Ajout de nouvelles fonctionnalites interactives.</li>
  <li>Integration de retours d'experience de stages et de projets professionnels.</li>
</ul>

<h3>Auto-evaluation</h3>

<p>La realisation de ce portfolio m'a permis de developper des competences transversales que je n'aurais pas necessairement acquises dans le cadre des cours techniques seuls. La redaction en Markdown, la gestion d'un site web avec Jekyll, l'utilisation de Git pour le versioning, et surtout la pratique reflexive systematique sont autant de competences qui me seront utiles dans ma vie professionnelle.</p>

<p>Ce travail de documentation et de reflexion, bien qu'exigeant en temps, est extremement formateur. Il m'a appris a structurer ma pensee, a prendre du recul sur mes experiences et a valoriser mes competences de maniere professionnelle.</p>

</div>

<div class="lang-en">

<h1>Portfolio</h1>

<h2>PART A: GENERAL PRESENTATION</h2>

<h3>Presentation</h3>

<p>The portfolio is an essential reflective practice exercise in the engineering program at INSA Toulouse. It is part of the RNCP (National Directory of Professional Certifications) certification framework, which requires students to be able to document, analyze, and showcase the skills acquired throughout their academic journey.</p>

<p>The objective of this portfolio is to build a structured and evolving record of my academic and professional path. It is not simply about listing courses or projects, but about conducting an in-depth reflection on the learning achieved, the skills developed, and the areas for improvement identified. This approach is part of a continuous improvement logic and the construction of a coherent professional identity.</p>

<h3>Portfolio Structure</h3>

<p>The portfolio is organized into several main sections:</p>

<ol>
  <li><strong>Courses</strong>: Detailed descriptions of the courses taken, including the content covered, duration, and key learnings.</li>
  <li><strong>Projects</strong>: Overview of completed projects, with objectives, methodologies, and results.</li>
  <li><strong>CV</strong>: My curriculum vitae, presenting my academic background, professional experiences, technical skills, and extracurricular activities.</li>
  <li><strong>About</strong>: Information about my background, interests, and future aspirations.</li>
</ol>

<h3>Objectives</h3>

<p>The objectives of this portfolio are to:</p>

<ul>
  <li>Present a clear and organized view of my educational and professional journey.</li>
  <li>Demonstrate my expertise in various technical fields, including IoT, embedded systems, and software development.</li>
  <li>Highlight my ability to apply theoretical knowledge to practical situations through projects and internships.</li>
  <li>Serve as a resource for potential employers, showcasing my skills and experiences.</li>
  <li>Reflect on my learning and progression, identifying areas for further development.</li>
</ul>

<h2>PART B: EXPERIENCE AND CONTEXT</h2>

<h3>Technical Environment</h3>

<p>This portfolio was entirely developed as a static website using <strong>Jekyll</strong>, a static site generator written in Ruby. The site is hosted on <strong>GitHub Pages</strong>, which allows automatic deployment with each push to the main branch of the Git repository.</p>

<h4>Development Tools</h4>

<p>The main tools used to build this portfolio are:</p>

<ul>
  <li><strong>Jekyll</strong>: Static site generator using the Minima theme as a base. Jekyll transforms Markdown files into complete HTML pages.</li>
  <li><strong>GitHub Pages</strong>: GitHub's free hosting service that serves the site directly from the repository.</li>
  <li><strong>Git</strong>: Version control system used to track the evolution of the portfolio's code and content.</li>
  <li><strong>Visual Studio Code</strong>: Code editor used for development, with extensions for Markdown, HTML, and CSS.</li>
  <li><strong>Kramdown</strong>: Markdown rendering engine used by Jekyll to convert content written in Markdown to HTML.</li>
</ul>

<h4>Repository Organization</h4>

<p>The repository is organized according to the standard Jekyll structure:</p>
<ul>
  <li><code>_posts/</code>: Contains all articles organized by school year (2022-2023, 2023-2024, 2024-2025) and by category (Courses, Personal_Project).</li>
  <li><code>_includes/</code>: Reusable HTML files (chatbot, footer).</li>
  <li><code>_config.yml</code>: Global site configuration (title, URL, plugins).</li>
  <li><code>img/</code> and <code>cours-pdf/</code>: Static resources (images, PDF reports).</li>
  <li><code>assets/</code>: Stylesheets and scripts.</li>
  <li><code>search.json</code>: Search index for the site's search functionality.</li>
</ul>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>1. Jekyll Framework and Liquid Templating</h3>

<p>Jekyll relies on the <strong>Liquid</strong> template engine, developed by Shopify. This system allows the use of variables, loops, and conditions in HTML files. For example, the homepage uses Liquid loops to dynamically generate the list of articles:</p>

<pre><code>{% raw %}{% for post in site.posts %}
  &lt;li&gt;&lt;a href="{{ post.url }}"&gt;{{ post.title }}&lt;/a&gt;&lt;/li&gt;
{% endfor %}{% endraw %}</code></pre>

<p>Each page of the site begins with a <strong>YAML Front Matter</strong> block that defines the metadata: the layout used, the title, the date, and the categories. This mechanism tells Jekyll how to process and render each file.</p>

<pre><code>---
layout: default
title: "Portfolio"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---</code></pre>

<p>The content is then written in <strong>Markdown</strong> (Kramdown syntax), which makes it easy to write and maintain content without having to directly manipulate HTML.</p>

<h3>2. Site Architecture</h3>

<p>The site architecture is based on several key Jekyll concepts:</p>

<ul>
  <li><strong>Layouts</strong>: The <code>default</code> layout provides the base HTML structure (header, navigation, footer) into which each page's content is injected.</li>
  <li><strong>Includes</strong>: The <code>_includes/</code> files allow the reuse of HTML components. The site notably uses a <code>chatbot.html</code> component for the conversational assistant and a <code>footer.html</code> for the footer.</li>
  <li><strong>Posts Collection</strong>: Articles are organized in <code>_posts/</code> with a naming convention of <code>YYYY-MM-DD-title.markdown</code>. Jekyll automatically generates URLs and the index from this structure.</li>
</ul>

<h3>3. Responsive Design with CSS</h3>

<p>Each page of the portfolio includes custom CSS styles to ensure a consistent and pleasant presentation. The main stylistic elements include:</p>

<ul>
  <li>A blue-based color palette (<code>#007BFF</code> for titles, <code>#66B2FF</code> for buttons).</li>
  <li>Styled buttons with transitions and hover effects.</li>
  <li>Justified text for better readability.</li>
  <li>A light background (<code>#f4f4f9</code>) for optimal contrast.</li>
</ul>

<h3>4. Search Functionality</h3>

<p>The site includes a search functionality implemented via a <code>search.json</code> file that indexes all articles. This JSON file is dynamically generated by Jekyll from the posts' metadata, enabling fast and efficient client-side search without the need for a backend server.</p>

<h3>5. Chatbot Integration</h3>

<p>A conversational chatbot has been integrated into the portfolio through the <code>_includes/chatbot.html</code> component. This feature enriches the user experience by allowing visitors to interact with the site dynamically.</p>

<h3>6. PDF Document Integration</h3>

<p>For course pages, the portfolio uses <code>&lt;iframe&gt;</code> tags to directly embed reports and PDF documents within the pages. This allows visitors to view documents without leaving the site, with a download link available as a complement.</p>

<pre><code>&lt;iframe src="/cours-pdf/document.pdf" width="100%" height="800px"&gt;&lt;/iframe&gt;</code></pre>

<h3>7. Deployment Pipeline</h3>

<p>The portfolio deployment follows a simple but effective pipeline:</p>

<ol>
  <li>Modify content locally (add pages, edit Markdown).</li>
  <li>Commit and push changes to the GitHub repository.</li>
  <li>GitHub Pages automatically detects changes and triggers a site rebuild via Jekyll.</li>
  <li>The updated site is served on the custom domain <code>cedric.littlenuage.com</code>.</li>
</ol>

<h3>8. Version Control with Git</h3>

<p>The entire portfolio is managed under <strong>Git</strong>, which allows:</p>

<ul>
  <li>Tracking the complete history of changes made to content and code.</li>
  <li>Reverting to a previous version if needed.</li>
  <li>Working on features in parallel via branches.</li>
  <li>Documenting site evolutions through commit messages.</li>
</ul>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Reflective Practice</h3>

<p>The creation and maintenance of this portfolio constitute a reflective practice exercise in its own right. Each course page follows a four-part structure (General Presentation, Descriptive Part, Technical Part, Analytical Part) that requires me not simply to describe what I did, but also to analyze what I learned, how I learned it, and what it means for my professional development.</p>

<p>This reflective approach has allowed me to step back from my learning and better understand the connections between the different courses and projects in my program.</p>

<h3>Skills Documentation</h3>

<p>The portfolio serves as tangible proof of the skills acquired throughout the program. By systematically documenting the technical aspects of each course, completed projects, and personal reflections, I am building a file that can be presented as part of the RNCP certification and that demonstrates my ability to:</p>

<ul>
  <li>Analyze complex technical problems.</li>
  <li>Implement appropriate solutions.</li>
  <li>Communicate effectively on technical subjects.</li>
  <li>Work in teams and manage projects.</li>
</ul>

<h3>Professional Identity</h3>

<p>Beyond simple documentation, the portfolio contributes to building my professional identity. By choosing to create it as a static website rather than a traditional document, I have demonstrated skills in web development, content management, and application deployment, which enriches my profile as an IoT and embedded systems engineer.</p>

<p>Maintaining a publicly accessible website also serves as a professional showcase that goes beyond a simple CV, concretely showing what I can do and how I work.</p>

<h3>Continuous Improvement</h3>

<p>This portfolio is a living project, constantly evolving. Each semester, new pages are added for new courses and projects. Existing pages can be improved and enriched. This continuous improvement approach reflects the philosophy of engineering education: never stop learning and progressing.</p>

<p>Among the future improvements planned:</p>
<ul>
  <li>Enriching the technical content of each course page.</li>
  <li>Improving accessibility and responsive design.</li>
  <li>Adding new interactive features.</li>
  <li>Integrating feedback from internships and professional projects.</li>
</ul>

<h3>Self-Assessment</h3>

<p>Creating this portfolio has allowed me to develop cross-cutting skills that I would not necessarily have acquired through technical courses alone. Writing in Markdown, managing a website with Jekyll, using Git for versioning, and above all the systematic reflective practice are all skills that will be useful in my professional life.</p>

<p>This documentation and reflection work, although time-demanding, is extremely formative. It taught me to structure my thinking, to step back from my experiences, and to showcase my skills in a professional manner.</p>

</div>
