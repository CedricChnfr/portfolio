---
layout: default
title:  "Conception Orientée Objet UML"
date:   2024-10-02 09:03:00 +0200
---

<style>
.back-nav {
    background: #f4f4f4;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px;
}

.section-title {
    color: #2a7ae2;
    border-bottom: 2px solid #2a7ae2;
    padding-bottom: 5px;
    margin-top: 30px;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
}

th {
    background-color: #2a7ae2;
    color: white;
    padding: 10px;
    text-align: left;
}

td {
    border: 1px solid #ddd;
    padding: 10px;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

.code-block {
    background: #f4f4f4;
    border-left: 4px solid #2a7ae2;
    padding: 15px;
    margin: 15px 0;
    font-family: 'Courier New', monospace;
}
</style>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>

<div class="lang-fr">

<h1>Conception Orientee Objet UML - Semestre 7</h1>

<p><strong>Annee Universitaire</strong> : 2023-2024<br/>
<strong>Semestre</strong> : 7<br/>
<strong>Credits</strong> : 2.5 ECTS<br/>
<strong>Specialite</strong> : Genie Logiciel et Methodologie</p>

<hr/>

<h2>PART A - Presentation Generale du Module</h2>

<h3 class="section-title">Vue d'ensemble</h3>

<p>Ce cours enseigne la conception orientee objet et le langage UML (Unified Modeling Language) pour analyser, concevoir et documenter des systemes logiciels complexes. Il fournit une methodologie structuree pour passer de l'analyse des besoins a une architecture logicielle robuste avant l'implementation.</p>

<p><strong>Objectifs pedagogiques</strong> :</p>
<ul>
<li>Maitriser les diagrammes UML structurels et comportementaux</li>
<li>Appliquer les principes de conception objet (SOLID)</li>
<li>Utiliser les design patterns classiques (GoF)</li>
<li>Concevoir des architectures logicielles maintenables</li>
<li>Documenter efficacement un projet logiciel</li>
</ul>

<h3 class="section-title">Position dans le cursus</h3>

<p>Ce module complete :</p>
<ul>
<li><strong>Programmation Orientee Objets C++ (S7)</strong> : concepts POO en pratique</li>
<li><strong>Programmation Orientee Objets Java (S7)</strong> : implementation des designs</li>
<li><strong>Langage C (S5)</strong> : transition vers la POO</li>
</ul>

<p>Il prepare a :</p>
<ul>
<li><strong>Projets de genie logiciel</strong> : architectures complexes</li>
<li><strong>Travail en equipe</strong> : communication via UML</li>
<li><strong>Ingenierie logicielle industrielle</strong> : documentation standardisee</li>
<li><strong>Maintenance et evolution</strong> : code structure et extensible</li>
</ul>

<hr/>

<h2>PART B - Experience Personnelle et Contexte d'Apprentissage</h2>

<h3 class="section-title">Organisation et ressources</h3>

<p>Le module etait structure en plusieurs volets :</p>

<p><strong>Cours magistraux (12h)</strong> :</p>
<ul>
<li>Introduction a UML et a la conception objet</li>
<li>Diagrammes structurels (classes, objets, composants, deploiement)</li>
<li>Diagrammes comportementaux (sequence, activite, etats)</li>
<li>Principes SOLID et bonnes pratiques</li>
<li>Design patterns du Gang of Four</li>
</ul>

<p><strong>Travaux diriges (12h)</strong> :</p>
<ul>
<li>Exercices de modelisation sur cas d'etude</li>
<li>Correction et discussion des TD</li>
<li>Ressource disponible : Correction_TD.txt avec lien Notion detaille</li>
<li>Analyse de problemes reels (bibliotheque, e-commerce, systeme embarque)</li>
</ul>

<p><strong>Projet de conception (16h)</strong> :</p>
<p>Realisation complete d'un systeme avec :</p>
<ul>
<li>Analyse des besoins (cas d'utilisation)</li>
<li>Modelisation structurelle (diagrammes de classes)</li>
<li>Modelisation comportementale (sequence, etats)</li>
<li>Prototypage en Java ou C++</li>
<li>Documentation UML complete</li>
</ul>

<p><strong>Ressources pedagogiques</strong> :</p>
<ul>
<li>Cours_ConceptionArchitectures.pdf (support de cours)</li>
<li>Notes partagees Notion (correction des TD)</li>
<li>Outils : Enterprise Architect, StarUML, PlantUML</li>
<li>Livres de reference : "Design Patterns" (GoF), "UML 2" (Pascal Roques)</li>
</ul>

<h3 class="section-title">Methodologie d'apprentissage</h3>

<p><strong>Phase 1 : Analyse des besoins</strong> :</p>
<p>Identifier les acteurs, definir les cas d'utilisation, specifier les exigences fonctionnelles et non-fonctionnelles.</p>

<p><strong>Phase 2 : Modelisation structurelle</strong> :</p>
<p>Creer les diagrammes de classes (entites, relations, multiplicites), definir les interfaces et l'architecture en couches.</p>

<p><strong>Phase 3 : Modelisation comportementale</strong> :</p>
<p>Decrire les interactions (diagrammes de sequence), les workflows (diagrammes d'activite), les etats (machines a etats).</p>

<p><strong>Phase 4 : Application des patterns</strong> :</p>
<p>Identifier les problemes recurrents et appliquer les patterns appropries (Factory, Observer, Strategy, etc.).</p>

<p><strong>Phase 5 : Implementation</strong> :</p>
<p>Generer le code squelette depuis les diagrammes, implementer la logique metier, maintenir la coherence UML/code.</p>

<h3 class="section-title">Difficultes rencontrees</h3>

<p><strong>Niveau d'abstraction</strong> :</p>
<p>Trouver le bon equilibre entre detail et abstraction. Trop detaille rend les diagrammes illisibles, trop abstrait les rend inutiles.</p>

<p><strong>Multiplicite des diagrammes</strong> :</p>
<p>UML propose 14 types de diagrammes. Savoir lesquels utiliser selon le contexte n'est pas immediat.</p>

<p><strong>Maintien de la coherence</strong> :</p>
<p>Garder les diagrammes synchronises avec le code lors des evolutions demande de la rigueur et du temps.</p>

<p><strong>Over-engineering</strong> :</p>
<p>Tendance a vouloir appliquer trop de patterns ou creer des architectures trop complexes pour le probleme donne.</p>

<hr/>

<h2>PART C - Aspects Techniques Detailles</h2>

<h3 class="section-title">1. Introduction a UML</h3>

<p><strong>UML = Unified Modeling Language</strong></p>

<p>Langage de modelisation graphique standardise (ISO/IEC 19505) pour visualiser, specifier, construire et documenter des systemes logiciels.</p>

<p><strong>Historique</strong> :</p>
<ul>
<li>Annees 1990 : fusion des methodes Booch, OMT, OOSE</li>
<li>Version 1.0 en 1997</li>
<li>Version 2.5 actuelle (2015)</li>
</ul>

<p><strong>Les 14 diagrammes UML</strong> :</p>

<table>
<tr><th>Categorie</th><th>Diagrammes</th></tr>
<tr><td>Structurels</td><td>Classes, Objets, Composants, Deploiement, Packages, Structure composite, Profil</td></tr>
<tr><td>Comportementaux</td><td>Cas d'utilisation, Activite, Etats-transitions, Sequence, Communication, Timing, Vue d'ensemble interaction</td></tr>
</table>

<p><strong>En pratique</strong> : On utilise principalement 5-6 diagrammes (classes, sequence, activite, etats, cas d'utilisation, composants).</p>

<h3 class="section-title">2. Diagramme de cas d'utilisation</h3>

<p><strong>Objectif</strong> : Decrire les fonctionnalites du systeme du point de vue utilisateur.</p>

<p><strong>Elements</strong> :</p>
<ul>
<li><strong>Acteur</strong> : Utilisateur ou systeme externe</li>
<li><strong>Cas d'utilisation</strong> : Fonctionnalite offerte</li>
<li><strong>Relations</strong> : include (inclusion obligatoire), extend (extension conditionnelle), generalisation</li>
</ul>

<p><strong>Exemple : Systeme de bibliotheque</strong></p>

<p>Acteurs :</p>
<ul>
<li>Lecteur (emprunter livre, consulter catalogue)</li>
<li>Bibliothecaire (enregistrer retour, gerer amendes)</li>
<li>Administrateur (ajouter livre, gerer utilisateurs)</li>
</ul>

<p>Relations :</p>
<ul>
<li>"Emprunter livre" include "Verifier disponibilite"</li>
<li>"Rechercher livre" extend "Filtrer par auteur"</li>
</ul>

<p><strong>Notation</strong> :</p>
<ul>
<li>Acteur : bonhomme stylise</li>
<li>Cas d'utilisation : ellipse avec nom</li>
<li>Relations : fleches avec stereotypes</li>
</ul>

<h3 class="section-title">3. Diagramme de classes</h3>

<p><strong>Objectif</strong> : Decrire la structure statique du systeme (classes, attributs, methodes, relations).</p>

<p><strong>Classe</strong> :</p>

<p>Une classe contient trois compartiments :</p>
<ul>
<li>Nom de la classe</li>
<li>Attributs (visibilite nom : type)</li>
<li>Methodes (visibilite nom(parametres) : type_retour)</li>
</ul>

<p><strong>Visibilites</strong> :</p>
<ul>
<li>+ public (accessible partout)</li>
<li>- private (accessible seulement dans la classe)</li>
<li># protected (accessible dans la classe et ses sous-classes)</li>
<li>~ package (accessible dans le package)</li>
</ul>

<p><strong>Exemple</strong> :</p>
<pre><code>Livre
--------------
- isbn : String
- titre : String
- auteur : String
- disponible : Boolean
--------------
+ emprunter() : Boolean
+ retourner() : void
+ estDisponible() : Boolean</code></pre>

<p><strong>Relations entre classes</strong> :</p>

<table>
<tr><th>Relation</th><th>Symbole</th><th>Signification</th><th>Exemple</th></tr>
<tr><td>Association</td><td>ligne simple</td><td>Les classes se connaissent</td><td>Lecteur --- Livre</td></tr>
<tr><td>Agregation</td><td>losange vide</td><td>"A des" (partie peut exister seule)</td><td>Bibliotheque --- Livre</td></tr>
<tr><td>Composition</td><td>losange plein</td><td>"Compose de" (partie liee au tout)</td><td>Voiture --- Moteur</td></tr>
<tr><td>Heritage</td><td>fleche triangle vide</td><td>"Est un"</td><td>LivreNumerique ---|&gt; Livre</td></tr>
<tr><td>Realisation</td><td>fleche triangle pointillee</td><td>Implemente interface</td><td>ClasseConcrete ..|&gt; Interface</td></tr>
<tr><td>Dependance</td><td>fleche pointillee</td><td>Utilise temporairement</td><td>Client ...&gt; Service</td></tr>
</table>

<p><strong>Multiplicites</strong> :</p>
<ul>
<li>1 : exactement un</li>
<li>0..1 : zero ou un</li>
<li>* : zero ou plusieurs</li>
<li>1..* : un ou plusieurs</li>
<li>2..5 : entre 2 et 5</li>
</ul>

<p><strong>Exemple complet</strong> :</p>
<p>Bibliotheque (1) --- (0..*) Livre<br/>
Lecteur (1) --- (0..5) Emprunt<br/>
Emprunt (*) --- (1) Livre</p>
<p>Un lecteur peut avoir au maximum 5 emprunts simultanes.</p>

<h3 class="section-title">4. Diagramme d'objets</h3>

<p><strong>Objectif</strong> : Montrer des instances concretes a un instant donne (snapshot).</p>

<p><strong>Difference avec diagramme de classes</strong> :</p>
<ul>
<li>Classes : structure generale</li>
<li>Objets : instances particulieres avec valeurs</li>
</ul>

<p><strong>Exemple</strong> :</p>
<pre><code>livre1 : Livre
- isbn = "978-2-1234"
- titre = "Design Patterns"
- disponible = false

lecteur1 : Lecteur
- nom = "Dupont"
- numeroCarte = "12345"

emprunt1 : Emprunt
- dateEmprunt = "2024-11-15"
- dateRetourPrevue = "2024-12-15"</code></pre>

<p><strong>Utilite</strong> : Valider le diagramme de classes avec des exemples concrets, illustrer des configurations complexes.</p>

<h3 class="section-title">5. Diagramme de sequence</h3>

<p><strong>Objectif</strong> : Montrer les interactions entre objets dans le temps (ordre chronologique des messages).</p>

<p><strong>Elements</strong> :</p>
<ul>
<li><strong>Lignes de vie</strong> : lignes verticales representant les objets</li>
<li><strong>Messages</strong> : fleches horizontales entre lignes de vie</li>
<li><strong>Activation</strong> : rectangle sur ligne de vie (objet actif)</li>
<li><strong>Fragments</strong> : alt (alternative), loop (boucle), opt (optionnel), par (parallele)</li>
</ul>

<p><strong>Types de messages</strong> :</p>
<ul>
<li>Synchrone : fleche pleine (appelant attend la reponse)</li>
<li>Asynchrone : fleche ouverte (appelant continue sans attendre)</li>
<li>Retour : fleche pointillee</li>
</ul>

<p><strong>Exemple : Emprunter un livre</strong></p>

<pre><code>Lecteur -> Bibliotheque : emprunterLivre(isbn)
Bibliotheque -> Catalogue : rechercherLivre(isbn)
Catalogue -> Bibliotheque : livre
alt livre disponible
    Bibliotheque -> Emprunt : creerEmprunt(lecteur, livre)
    Emprunt -> Livre : marquerEmprunte()
    Bibliotheque -> Lecteur : confirmationEmprunt
else livre indisponible
    Bibliotheque -> Lecteur : messageErreur
end</code></pre>

<p><strong>Fragments utiles</strong> :</p>
<ul>
<li><strong>alt</strong> : if/else (branches alternatives)</li>
<li><strong>loop</strong> : boucle (condition et iteration)</li>
<li><strong>opt</strong> : optionnel (execute si condition vraie)</li>
<li><strong>par</strong> : parallele (execution simultanee)</li>
<li><strong>ref</strong> : reference a un autre diagramme</li>
</ul>

<h3 class="section-title">6. Diagramme d'activite</h3>

<p><strong>Objectif</strong> : Modeliser les workflows, processus metier, algorithmes (similaire a un organigramme ameliore).</p>

<p><strong>Elements</strong> :</p>
<ul>
<li><strong>Noeud initial</strong> : cercle noir plein</li>
<li><strong>Noeud final</strong> : cercle noir avec cercle autour</li>
<li><strong>Activite</strong> : rectangle arrondi</li>
<li><strong>Decision</strong> : losange (condition)</li>
<li><strong>Fork/Join</strong> : barre horizontale (parallelisme)</li>
<li><strong>Swimlanes</strong> : partitions par acteur/systeme</li>
</ul>

<p><strong>Exemple : Processus d'emprunt</strong></p>

<pre><code>[Debut]
|
Lecteur presente carte
|
&lt;Carte valide?&gt;
  Non -> Refuser emprunt -> [Fin]
  Oui |
Scanner code-barres livre
|
&lt;Livre disponible?&gt;
  Non -> Proposer reservation -> [Fin]
  Oui |
Enregistrer emprunt
|
Imprimer ticket
|
[Fin]</code></pre>

<p><strong>Parallelisme avec fork/join</strong> :</p>
<p>Fork (barre horizontale) :<br/>
-> Activite A<br/>
-> Activite B (en parallele)</p>
<p>Join : synchronisation (attendre que A et B soient terminees)</p>

<h3 class="section-title">7. Diagramme d'etats-transitions</h3>

<p><strong>Objectif</strong> : Modeliser le cycle de vie d'un objet (etats possibles et transitions).</p>

<p><strong>Elements</strong> :</p>
<ul>
<li><strong>Etat</strong> : rectangle arrondi</li>
<li><strong>Transition</strong> : fleche avec evenement declencheur</li>
<li><strong>Etat initial</strong> : cercle noir</li>
<li><strong>Etat final</strong> : cercle noir avec cercle</li>
<li><strong>Actions</strong> : entry/ (a l'entree), do/ (pendant), exit/ (a la sortie)</li>
</ul>

<p><strong>Exemple : Etats d'un livre</strong></p>

<pre><code>[Initial]
|
Disponible
  entry/ afficherDisponible()

Disponible --[emprunter]--> Emprunte
  entry/ enregistrerEmprunt()
  do/ decrementerDisponibilites()

Emprunte --[retourner]--> Disponible
  exit/ libererExemplaire()

Emprunte --[depasser delai]--> EnRetard
  entry/ calculerAmende()

EnRetard --[retourner + payer amende]--> Disponible

Disponible --[retirer du catalogue]--> [Final]</code></pre>

<p><strong>Etats composites</strong> :</p>
<p>Un etat peut contenir des sous-etats (hierarchie).</p>

<p><strong>Etats concurrents</strong> :</p>
<p>Plusieurs etats actifs simultanement (separes par ligne pointillee).</p>

<h3 class="section-title">8. Diagrammes de composants et deploiement</h3>

<p><strong>Diagramme de composants</strong> :</p>

<p>Montre l'organisation logicielle en modules/bibliotheques avec leurs dependances.</p>

<p>Composants typiques :</p>
<ul>
<li>Interface Utilisateur (UI)</li>
<li>Logique metier (Business Logic)</li>
<li>Acces aux donnees (DAO)</li>
<li>Bibliotheques externes</li>
</ul>

<p>Relations :</p>
<ul>
<li>Dependances entre composants</li>
<li>Interfaces fournies (cercle) et requises (demi-cercle)</li>
</ul>

<p><strong>Diagramme de deploiement</strong> :</p>

<p>Montre l'architecture physique (serveurs, reseaux, artefacts deployes).</p>

<p>Elements :</p>
<ul>
<li><strong>Noeuds</strong> : materiel (serveur, PC, mobile)</li>
<li><strong>Artefacts</strong> : fichiers deployes (JAR, EXE, WAR)</li>
<li><strong>Communications</strong> : protocoles (HTTP, TCP, etc.)</li>
</ul>

<p>Exemple :</p>
<pre><code>Serveur Web
  - Apache Tomcat
  - Application.war

Base de donnees
  - MySQL Server
  - Schema bibliotheque

Poste client
  - Navigateur Web
  - Interface HTML/CSS/JS</code></pre>

<h3 class="section-title">9. Principes de conception SOLID</h3>

<p>Ensemble de 5 principes pour creer du code maintenable et extensible.</p>

<p><strong>S - Single Responsibility Principle (SRP)</strong> :</p>
<p>Une classe doit avoir une seule raison de changer (une seule responsabilite).</p>

<p>Mauvais :</p>
<pre><code>class Livre
  + sauvegarderDansBaseDeDonnees()  // responsabilite persistance
  + envoyerEmailNotification()       // responsabilite notification</code></pre>

<p>Bon :</p>
<pre><code>class Livre
  // seulement logique metier livre

class LivreRepository
  + sauvegarder(livre)

class NotificationService
  + envoyerEmail(destinataire, message)</code></pre>

<p><strong>O - Open/Closed Principle (OCP)</strong> :</p>
<p>Les classes doivent etre ouvertes a l'extension, fermees a la modification.</p>
<p>Utiliser l'heritage, la composition, ou les interfaces pour etendre sans modifier le code existant.</p>

<p><strong>L - Liskov Substitution Principle (LSP)</strong> :</p>
<p>Les objets d'une classe derivee doivent pouvoir remplacer les objets de la classe de base sans alterer le comportement.</p>

<p><strong>I - Interface Segregation Principle (ISP)</strong> :</p>
<p>Mieux vaut plusieurs interfaces specifiques qu'une interface generale.</p>

<p>Mauvais :</p>
<pre><code>interface DocumentActions
  + imprimer()
  + scanner()
  + faxer()</code></pre>

<p>Une imprimante simple doit implementer scanner() et faxer() meme si elle ne les supporte pas.</p>

<p>Bon :</p>
<pre><code>interface Imprimable
  + imprimer()

interface Scannable
  + scanner()

class ImprimanteSimple implements Imprimable
class ImprimanteMultifonction implements Imprimable, Scannable</code></pre>

<p><strong>D - Dependency Inversion Principle (DIP)</strong> :</p>
<p>Dependre des abstractions (interfaces), pas des implementations concretes.</p>

<p>Mauvais :</p>
<pre><code>class Bibliotheque
  private MySQLDatabase db  // dependance concrete</code></pre>

<p>Bon :</p>
<pre><code>interface Database
  + sauvegarder(data)
  + charger(id)

class Bibliotheque
  private Database db  // dependance abstraite

class MySQLDatabase implements Database
class MongoDBDatabase implements Database</code></pre>

<p>Permet de changer facilement de base de donnees sans modifier Bibliotheque.</p>

<h3 class="section-title">10. Design Patterns (Patrons de conception)</h3>

<p>Solutions eprouvees a des problemes recurrents de conception.</p>

<p><strong>Patterns creationnels</strong> : gestion de la creation d'objets</p>

<p><strong>Singleton</strong> :</p>
<p>Garantir une seule instance d'une classe.</p>

<pre><code>class ConfigurationManager
  private static instance : ConfigurationManager

  private ConfigurationManager()  // constructeur prive

  public static getInstance() : ConfigurationManager
    if instance == null
      instance = new ConfigurationManager()
    return instance</code></pre>

<p>Utilisation : gestionnaires uniques (configuration, logging, pool de connexions).</p>

<p><strong>Factory Method</strong> :</p>
<p>Deleguer la creation d'objets aux sous-classes.</p>

<pre><code>abstract class DocumentFactory
  abstract creerDocument() : Document

class PDFFactory extends DocumentFactory
  creerDocument() : Document
    return new PDFDocument()

class WordFactory extends DocumentFactory
  creerDocument() : Document
    return new WordDocument()</code></pre>

<p><strong>Abstract Factory</strong> :</p>
<p>Creer des familles d'objets lies sans specifier leurs classes concretes.</p>

<p><strong>Patterns structurels</strong> : organisation des classes et objets</p>

<p><strong>Adapter</strong> :</p>
<p>Convertir l'interface d'une classe en une autre interface attendue.</p>

<pre><code>interface LecteurMultimedia
  + lire(fichier)

class LecteurMP3
  + jouerMP3(fichier)

class AdapterMP3 implements LecteurMultimedia
  private lecteurMP3 : LecteurMP3

  lire(fichier)
    lecteurMP3.jouerMP3(fichier)</code></pre>

<p><strong>Decorator</strong> :</p>
<p>Ajouter dynamiquement des responsabilites a un objet.</p>

<pre><code>interface Cafe
  + cout() : double

class CafeSimple implements Cafe
  cout() : double
    return 2.0

class AvecLait implements Cafe
  private cafe : Cafe

  cout() : double
    return cafe.cout() + 0.5

class AvecSucre implements Cafe
  private cafe : Cafe

  cout() : double
    return cafe.cout() + 0.2</code></pre>

<p>Usage :</p>
<pre><code>Cafe monCafe = new AvecLait(new AvecSucre(new CafeSimple()))
// cout = 2.0 + 0.2 + 0.5 = 2.7</code></pre>

<p><strong>Composite</strong> :</p>
<p>Composer des objets en structures arborescentes (traiter uniformement objets individuels et compositions).</p>

<p><strong>Patterns comportementaux</strong> : interactions entre objets</p>

<p><strong>Observer</strong> :</p>
<p>Notifier automatiquement des objets lors d'un changement d'etat.</p>

<pre><code>interface Observer
  + update(sujet)

class Sujet
  private observateurs : List&lt;Observer&gt;

  + attacher(observateur)
    observateurs.add(observateur)

  + notifier()
    for each observateur in observateurs
      observateur.update(this)

class AffichageTemperature implements Observer
  update(sujet)
    temperature = sujet.getTemperature()
    afficher(temperature)</code></pre>

<p>Utilisation : interfaces graphiques (MVC), systemes evenementiels.</p>

<p><strong>Strategy</strong> :</p>
<p>Encapsuler des algorithmes interchangeables.</p>

<pre><code>interface StrategieCalculAmende
  + calculer(joursRetard) : double

class AmendeStandard implements StrategieCalculAmende
  calculer(joursRetard) : double
    return joursRetard * 0.5

class AmendeEtudiant implements StrategieCalculAmende
  calculer(joursRetard) : double
    return joursRetard * 0.2

class GestionnaireEmprunt
  private strategie : StrategieCalculAmende

  definirStrategie(strategie)
    this.strategie = strategie

  calculerAmende(joursRetard)
    return strategie.calculer(joursRetard)</code></pre>

<p><strong>Command</strong> :</p>
<p>Encapsuler une requete comme un objet.</p>
<p>Permet : annulation (undo), file d'attente de commandes, journalisation.</p>

<p><strong>State</strong> :</p>
<p>Modifier le comportement d'un objet selon son etat interne.</p>

<p><strong>Template Method</strong> :</p>
<p>Definir le squelette d'un algorithme, les sous-classes redefinissent certaines etapes.</p>

<h3 class="section-title">11. De UML au code</h3>

<p><strong>Forward Engineering</strong> : generer du code depuis les diagrammes UML.</p>

<p>Outils :</p>
<ul>
<li>Enterprise Architect (generation Java, C++, C#, Python)</li>
<li>StarUML (generation code basique)</li>
<li>PlantUML + scripts custom</li>
</ul>

<p>Exemple : diagramme de classes -> classes Java avec attributs et signatures de methodes (squelettes).</p>

<p><strong>Reverse Engineering</strong> : generer des diagrammes UML depuis le code existant.</p>

<p>Utile pour :</p>
<ul>
<li>Documenter du legacy code</li>
<li>Analyser une base de code inconnue</li>
<li>Maintenir coherence code/documentation</li>
</ul>

<p><strong>Round-trip Engineering</strong> : synchronisation bidirectionnelle code / UML.</p>

<p>Modifications du code refletees dans les diagrammes et vice-versa.</p>

<p>En pratique : difficile a maintenir, necessite discipline et outillage adapte.</p>

<h3 class="section-title">12. Outils de modelisation</h3>

<table>
<tr><th>Outil</th><th>Type</th><th>Avantages</th><th>Inconvenients</th></tr>
<tr><td>Enterprise Architect</td><td>Commercial</td><td>Complet, generation code, collaboration</td><td>Couteux, interface complexe</td></tr>
<tr><td>StarUML</td><td>Open-source/Commercial</td><td>Interface intuitive, legerete</td><td>Fonctionnalites limitees version gratuite</td></tr>
<tr><td>PlantUML</td><td>Open-source</td><td>Textuel, integration CI/CD, versioning</td><td>Courbe apprentissage syntaxe</td></tr>
<tr><td>Lucidchart</td><td>Web</td><td>Collaboratif, facile</td><td>Limite version gratuite</td></tr>
<tr><td>draw.io</td><td>Web/Open</td><td>Gratuit, simple</td><td>Pas specialise UML</td></tr>
<tr><td>Visual Paradigm</td><td>Commercial</td><td>Puissant, formation incluse</td><td>Couteux</td></tr>
</table>

<p><strong>Recommandation personnelle</strong> :</p>
<ul>
<li>Projets personnels : PlantUML (versionnable avec Git)</li>
<li>Entreprise : Enterprise Architect ou Visual Paradigm</li>
<li>Collaboration rapide : Lucidchart ou Miro</li>
</ul>

<hr/>

<h2>PART D - Analyse Reflexive et Perspectives</h2>

<h3 class="section-title">Competences acquises</h3>

<p><strong>Modelisation et abstraction</strong> :</p>
<p>Capacite a analyser un probleme complexe et a le decomposer en entites, relations et comportements modelisables.</p>

<p><strong>Communication technique</strong> :</p>
<p>UML fournit un langage universel pour communiquer des architectures entre developpeurs, chefs de projet, et clients.</p>

<p><strong>Anticipation et planification</strong> :</p>
<p>Concevoir avant d'implementer permet d'identifier les problemes d'architecture tot, reduisant les couts de refactoring.</p>

<p><strong>Qualite logicielle</strong> :</p>
<p>Application des principes SOLID et patterns produit du code plus maintenable, testable et extensible.</p>

<h3 class="section-title">Projet realise : Systeme de gestion de bibliotheque</h3>

<p><strong>Contexte</strong> :</p>
<p>Conception complete d'un systeme de bibliotheque multimedia (livres, DVDs, periodiques) avec gestion des emprunts, reservations, amendes, et utilisateurs.</p>

<p><strong>Livrables</strong> :</p>
<ul>
<li>Diagramme de cas d'utilisation (12 cas, 4 acteurs)</li>
<li>Diagramme de classes complet (35+ classes)</li>
<li>Diagrammes de sequence (emprunter, retourner, reserver, payer amende)</li>
<li>Diagrammes d'etats (cycle de vie livre, emprunt)</li>
<li>Diagramme d'activite (processus d'emprunt complet)</li>
<li>Prototype Java avec patterns appliques</li>
</ul>

<p><strong>Patterns utilises</strong> :</p>
<ul>
<li><strong>Singleton</strong> : BibliothequeManager (instance unique)</li>
<li><strong>Factory</strong> : DocumentFactory pour creer Livre, DVD, Periodique</li>
<li><strong>Observer</strong> : notification disponibilite pour reservations</li>
<li><strong>Strategy</strong> : calcul amendes selon type utilisateur (standard, etudiant, enseignant)</li>
<li><strong>State</strong> : gestion etats emprunt (en cours, en retard, termine)</li>
</ul>

<p><strong>Resultats</strong> :</p>
<p>Architecture claire et extensible. Ajout de nouveaux types de documents ou nouvelles regles d'amende facile grace aux patterns. Code bien structure avec separation des responsabilites.</p>

<h3 class="section-title">Points cles a retenir</h3>

<p><strong>1. UML = outil, pas objectif</strong> :</p>
<p>L'objectif est une bonne conception, pas de beaux diagrammes. Utiliser UML de maniere pragmatique.</p>

<p><strong>2. Tous les diagrammes ne sont pas necessaires</strong> :</p>
<p>Identifier ceux qui apportent de la valeur selon le contexte (classes et sequence souvent suffisants).</p>

<p><strong>3. SOLID avant patterns</strong> :</p>
<p>Comprendre et appliquer SOLID est plus important que connaitre tous les patterns.</p>

<p><strong>4. Patterns = solutions, pas recettes magiques</strong> :</p>
<p>Ne pas forcer l'utilisation d'un pattern. L'appliquer seulement si le probleme correspond.</p>

<p><strong>5. Documentation vivante</strong> :</p>
<p>La documentation doit evoluer avec le code, sinon elle devient obsolete et trompeuse.</p>

<h3 class="section-title">Retour d'experience</h3>

<p><strong>Courbe d'apprentissage</strong> :</p>
<p>UML semblait complexe initialement (14 diagrammes, notations specifiques). Avec la pratique, on identifie rapidement les 5-6 diagrammes essentiels.</p>

<p><strong>Lien avec la POO</strong> :</p>
<p>Ce cours a renforce ma comprehension de la POO au-dela de la syntaxe. Concepts comme l'encapsulation, l'abstraction, le polymorphisme deviennent concrets.</p>

<p><strong>Application en projets</strong> :</p>
<p>Utiliser UML sur des projets reels (meme simplifies) a prouve son utilite. Gain de temps et moins de bugs grace a la reflexion en amont.</p>

<p><strong>Collaboration facilitee</strong> :</p>
<p>Travailler en equipe avec UML comme langage commun a grandement ameliore la communication et reduit les malentendus.</p>

<h3 class="section-title">Applications pratiques</h3>

<p><strong>Developpement logiciel</strong> :</p>
<ul>
<li>Applications d'entreprise (ERP, CRM)</li>
<li>Systemes embarques (modelisation etats et sequences critiques)</li>
<li>Applications web (architecture MVC/MVVM)</li>
</ul>

<p><strong>Refactoring</strong> :</p>
<p>Reverse engineering de code legacy, identification des problemes (couplage fort, responsabilites mixtes), puis refactoring guide par SOLID.</p>

<p><strong>Documentation</strong> :</p>
<p>Generer automatiquement documentation technique a partir des diagrammes UML. Integration dans wikis d'entreprise.</p>

<p><strong>Communication client</strong> :</p>
<p>Diagrammes de cas d'utilisation et d'activite comprehensibles par non-developpeurs pour valider les besoins.</p>

<h3 class="section-title">Limites et critiques</h3>

<p><strong>UML lourd et verbeux</strong> :</p>
<p>Creer et maintenir tous les diagrammes prend du temps. Approche agile prefere "UML leger" (quelques diagrammes cles).</p>

<p><strong>Decalage documentation/code</strong> :</p>
<p>Sans discipline ou outils de synchronisation, les diagrammes deviennent rapidement obsoletes.</p>

<p><strong>Over-engineering</strong> :</p>
<p>Risque de creer des architectures trop complexes, avec trop de patterns, pour des problemes simples.</p>

<p><strong>Alternatives modernes</strong> :</p>
<ul>
<li><strong>C4 Model</strong> : documentation architecturale pragmatique (Context, Containers, Components, Code)</li>
<li><strong>Architecture Decision Records (ADR)</strong> : documenter les decisions plutot que les diagrammes</li>
<li><strong>Living Documentation</strong> : tests et code comme documentation</li>
</ul>

<h3 class="section-title">Evolutions et perspectives</h3>

<p><strong>Domain-Driven Design (DDD)</strong> :</p>
<p>Approche centree sur le domaine metier. Utilise UML mais ajoute concepts (Entities, Value Objects, Aggregates, Repositories).</p>

<p><strong>SysML</strong> :</p>
<p>Extension UML pour ingenierie systeme (pas seulement logiciel). Utilise en aeronautique, automobile, defense.</p>

<p><strong>Outils modernes</strong> :</p>
<ul>
<li>Generation automatique de diagrammes depuis le code (Doxygen, Javadoc UML)</li>
<li>Documentation as Code (PlantUML en Markdown, versioning Git)</li>
<li>Collaboration temps reel (Miro, Lucidchart, Figma pour UML)</li>
</ul>

<p><strong>Intelligence Artificielle</strong> :</p>
<p>IA generatrice de diagrammes UML depuis descriptions textuelles, detection automatique de violations SOLID, suggestions de patterns.</p>

<h3 class="section-title">Conseils pour reussir</h3>

<p><strong>1. Pratiquer sur projets concrets</strong> :</p>
<p>Modeliser des systemes reels (e-commerce, reseau social, jeu) plutot que des exercices abstraits.</p>

<p><strong>2. Commencer simple</strong> :</p>
<p>Debuter avec diagrammes de classes et sequence. Ajouter d'autres types selon les besoins.</p>

<p><strong>3. Valider avec du code</strong> :</p>
<p>Implementer les designs pour verifier leur coherence et faisabilite.</p>

<p><strong>4. Etudier du code open-source</strong> :</p>
<p>Analyser l'architecture de projets populaires (Spring Framework, Apache Commons) pour voir SOLID et patterns en pratique.</p>

<p><strong>5. Iterer</strong> :</p>
<p>La conception n'est jamais parfaite du premier coup. Reviser et ameliorer au fur et a mesure.</p>

<h3 class="section-title">Conclusion</h3>

<p>Ce module fournit une methodologie essentielle pour concevoir des systemes logiciels robustes et maintenables. Au-dela de la syntaxe UML, ce sont les principes de conception objet (SOLID) et les patterns qui constituent l'apport majeur.</p>

<p><strong>Competences transferables</strong> :</p>
<ul>
<li>Pensee architecturale et abstraite</li>
<li>Conception avant implementation</li>
<li>Communication technique efficace</li>
<li>Code de qualite professionnelle</li>
</ul>

<p><strong>Pertinence professionnelle</strong> :</p>
<p>En entreprise, la conception et documentation sont attendues, surtout pour projets critiques ou reglementes. Savoir modeliser et justifier ses choix d'architecture est un atout majeur.</p>

<p><strong>Message principal</strong> :</p>
<p>UML est un outil parmi d'autres. L'essentiel est de developper une demarche de conception structuree, applicable quel que soit le formalisme. Les principes SOLID et patterns sont universels et transcendent les langages et outils.</p>

<p><strong>Recommandations</strong> :</p>
<ul>
<li>Utiliser UML de maniere pragmatique (eviter dogmatisme)</li>
<li>Privilegier les diagrammes qui apportent de la valeur</li>
<li>Maintenir documentation a jour (automatisation si possible)</li>
<li>Continuer a apprendre patterns avances et architectures (microservices, event-driven)</li>
<li>Explorer DDD pour approfondir modelisation metier</li>
</ul>

<p><strong>Liens avec les autres cours</strong> :</p>
<ul>
<li><a href="./poo-cpp.html">Programmation Orientee Objets C++ - S7</a> : implementation des concepts</li>
<li><a href="./poo-java.html">Programmation Orientee Objets Java - S7</a> : application pratique</li>
<li><a href="./graphes-programmation-lineaire.html">Graphes et Programmation Lineaire - S8</a> : modelisation problemes</li>
</ul>

<hr/>

<h2><span class="lang-fr">Documents de Cours</span><span class="lang-en">Course Documents</span></h2>

<style>
    .pdf-container {
        margin: 40px 0;
        padding: 20px;
        background: #f9f9f9;
        border-radius: 8px;
    }
    .pdf-viewer {
        display: flex;
        flex-wrap: wrap;
        gap: 20px;
    }
    .pdf-item {
        flex: 1;
        min-width: 400px;
        background: white;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .pdf-item h4 {
        color: #2a7ae2;
        margin-top: 0;
    }
</style>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4><span class="lang-fr">Cours Conception et Architectures</span><span class="lang-en">Design and Architecture Course</span></h4>
      <p><span class="lang-fr">Cours complet UML : diagrammes de classes, sequences, cas d'utilisation, patterns de conception et principes SOLID.</span><span class="lang-en">Complete UML course: class diagrams, sequence diagrams, use cases, design patterns and SOLID principles.</span></p>
      <embed src="/cours-pdf/S7/Conception-UML/cours-conception.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Conception-UML/cours-conception.pdf" target="_blank"><span class="lang-fr">Telecharger</span><span class="lang-en">Download</span></a></p>
    </div>
    <div class="pdf-item">
      <h4><span class="lang-fr">Sujet TD</span><span class="lang-en">Tutorial Subject</span></h4>
      <p><span class="lang-fr">Travaux diriges sur la conception orientee objet : modelisation de systemes embarques et architectures logicielles.</span><span class="lang-en">Tutorials on object-oriented design: modeling of embedded systems and software architectures.</span></p>
      <embed src="/cours-pdf/S7/Conception-UML/td-sujet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Conception-UML/td-sujet.pdf" target="_blank"><span class="lang-fr">Telecharger</span><span class="lang-en">Download</span></a></p>
    </div>
  </div>
</div>

<hr/>

<p><em><span class="lang-fr">Cours suivi en 2023-2024 a l'INSA Toulouse, Departement Genie Electrique et Informatique.</span><span class="lang-en">Course taken in 2023-2024 at INSA Toulouse, Department of Electrical Engineering and Computer Science.</span></em></p>

</div>

<div class="lang-en">

<h1>Object-Oriented Design UML - Semester 7</h1>

<p><strong>Academic Year</strong>: 2023-2024<br/>
<strong>Semester</strong>: 7<br/>
<strong>Credits</strong>: 2.5 ECTS<br/>
<strong>Specialty</strong>: Software Engineering and Methodology</p>

<hr/>

<h2>PART A - General Module Overview</h2>

<h3 class="section-title">Overview</h3>

<p>This course teaches object-oriented design and the UML (Unified Modeling Language) language for analyzing, designing and documenting complex software systems. It provides a structured methodology for moving from requirements analysis to a robust software architecture before implementation.</p>

<p><strong>Learning objectives</strong>:</p>
<ul>
<li>Master structural and behavioral UML diagrams</li>
<li>Apply object-oriented design principles (SOLID)</li>
<li>Use classic design patterns (GoF)</li>
<li>Design maintainable software architectures</li>
<li>Effectively document a software project</li>
</ul>

<h3 class="section-title">Position in the Curriculum</h3>

<p>This module complements:</p>
<ul>
<li><strong>Object-Oriented Programming C++ (S7)</strong>: OOP concepts in practice</li>
<li><strong>Object-Oriented Programming Java (S7)</strong>: design implementation</li>
<li><strong>C Language (S5)</strong>: transition to OOP</li>
</ul>

<p>It prepares for:</p>
<ul>
<li><strong>Software engineering projects</strong>: complex architectures</li>
<li><strong>Teamwork</strong>: communication via UML</li>
<li><strong>Industrial software engineering</strong>: standardized documentation</li>
<li><strong>Maintenance and evolution</strong>: structured and extensible code</li>
</ul>

<hr/>

<h2>PART B - Personal Experience and Learning Context</h2>

<h3 class="section-title">Organization and Resources</h3>

<p>The module was structured in several components:</p>

<p><strong>Lectures (12h)</strong>:</p>
<ul>
<li>Introduction to UML and object-oriented design</li>
<li>Structural diagrams (classes, objects, components, deployment)</li>
<li>Behavioral diagrams (sequence, activity, states)</li>
<li>SOLID principles and best practices</li>
<li>Gang of Four design patterns</li>
</ul>

<p><strong>Tutorials (12h)</strong>:</p>
<ul>
<li>Modeling exercises on case studies</li>
<li>Correction and discussion of tutorials</li>
<li>Available resource: Correction_TD.txt with detailed Notion link</li>
<li>Analysis of real-world problems (library, e-commerce, embedded system)</li>
</ul>

<p><strong>Design project (16h)</strong>:</p>
<p>Complete implementation of a system with:</p>
<ul>
<li>Requirements analysis (use cases)</li>
<li>Structural modeling (class diagrams)</li>
<li>Behavioral modeling (sequence, states)</li>
<li>Prototyping in Java or C++</li>
<li>Complete UML documentation</li>
</ul>

<p><strong>Teaching resources</strong>:</p>
<ul>
<li>Cours_ConceptionArchitectures.pdf (course material)</li>
<li>Shared Notion notes (tutorial corrections)</li>
<li>Tools: Enterprise Architect, StarUML, PlantUML</li>
<li>Reference books: "Design Patterns" (GoF), "UML 2" (Pascal Roques)</li>
</ul>

<h3 class="section-title">Learning Methodology</h3>

<p><strong>Phase 1: Requirements Analysis</strong>:</p>
<p>Identify actors, define use cases, specify functional and non-functional requirements.</p>

<p><strong>Phase 2: Structural Modeling</strong>:</p>
<p>Create class diagrams (entities, relationships, multiplicities), define interfaces and layered architecture.</p>

<p><strong>Phase 3: Behavioral Modeling</strong>:</p>
<p>Describe interactions (sequence diagrams), workflows (activity diagrams), states (state machines).</p>

<p><strong>Phase 4: Applying Patterns</strong>:</p>
<p>Identify recurring problems and apply appropriate patterns (Factory, Observer, Strategy, etc.).</p>

<p><strong>Phase 5: Implementation</strong>:</p>
<p>Generate skeleton code from diagrams, implement business logic, maintain UML/code consistency.</p>

<h3 class="section-title">Difficulties Encountered</h3>

<p><strong>Level of abstraction</strong>:</p>
<p>Finding the right balance between detail and abstraction. Too detailed makes diagrams unreadable, too abstract makes them useless.</p>

<p><strong>Multiplicity of diagrams</strong>:</p>
<p>UML offers 14 types of diagrams. Knowing which to use depending on the context is not immediate.</p>

<p><strong>Maintaining consistency</strong>:</p>
<p>Keeping diagrams synchronized with the code during evolution requires rigor and time.</p>

<p><strong>Over-engineering</strong>:</p>
<p>Tendency to apply too many patterns or create overly complex architectures for the given problem.</p>

<hr/>

<h2>PART C - Detailed Technical Aspects</h2>

<h3 class="section-title">1. Introduction to UML</h3>

<p><strong>UML = Unified Modeling Language</strong></p>

<p>A standardized graphical modeling language (ISO/IEC 19505) for visualizing, specifying, constructing and documenting software systems.</p>

<p><strong>History</strong>:</p>
<ul>
<li>1990s: merger of Booch, OMT, OOSE methods</li>
<li>Version 1.0 in 1997</li>
<li>Current version 2.5 (2015)</li>
</ul>

<p><strong>The 14 UML diagrams</strong>:</p>

<table>
<tr><th>Category</th><th>Diagrams</th></tr>
<tr><td>Structural</td><td>Classes, Objects, Components, Deployment, Packages, Composite structure, Profile</td></tr>
<tr><td>Behavioral</td><td>Use case, Activity, State machine, Sequence, Communication, Timing, Interaction overview</td></tr>
</table>

<p><strong>In practice</strong>: Mainly 5-6 diagrams are used (classes, sequence, activity, states, use cases, components).</p>

<h3 class="section-title">2. Use Case Diagram</h3>

<p><strong>Objective</strong>: Describe system functionalities from the user's perspective.</p>

<p><strong>Elements</strong>:</p>
<ul>
<li><strong>Actor</strong>: User or external system</li>
<li><strong>Use case</strong>: Offered functionality</li>
<li><strong>Relationships</strong>: include (mandatory inclusion), extend (conditional extension), generalization</li>
</ul>

<p><strong>Example: Library System</strong></p>

<p>Actors:</p>
<ul>
<li>Reader (borrow book, browse catalog)</li>
<li>Librarian (register return, manage fines)</li>
<li>Administrator (add book, manage users)</li>
</ul>

<p>Relationships:</p>
<ul>
<li>"Borrow book" include "Check availability"</li>
<li>"Search book" extend "Filter by author"</li>
</ul>

<p><strong>Notation</strong>:</p>
<ul>
<li>Actor: stick figure</li>
<li>Use case: ellipse with name</li>
<li>Relationships: arrows with stereotypes</li>
</ul>

<h3 class="section-title">3. Class Diagram</h3>

<p><strong>Objective</strong>: Describe the static structure of the system (classes, attributes, methods, relationships).</p>

<p><strong>Class</strong>:</p>

<p>A class contains three compartments:</p>
<ul>
<li>Class name</li>
<li>Attributes (visibility name : type)</li>
<li>Methods (visibility name(parameters) : return_type)</li>
</ul>

<p><strong>Visibilities</strong>:</p>
<ul>
<li>+ public (accessible everywhere)</li>
<li>- private (accessible only within the class)</li>
<li># protected (accessible in the class and its subclasses)</li>
<li>~ package (accessible within the package)</li>
</ul>

<p><strong>Example</strong>:</p>
<pre><code>Book
--------------
- isbn : String
- title : String
- author : String
- available : Boolean
--------------
+ borrow() : Boolean
+ return() : void
+ isAvailable() : Boolean</code></pre>

<p><strong>Relationships between classes</strong>:</p>

<table>
<tr><th>Relationship</th><th>Symbol</th><th>Meaning</th><th>Example</th></tr>
<tr><td>Association</td><td>simple line</td><td>Classes know each other</td><td>Reader --- Book</td></tr>
<tr><td>Aggregation</td><td>empty diamond</td><td>"Has" (part can exist alone)</td><td>Library --- Book</td></tr>
<tr><td>Composition</td><td>filled diamond</td><td>"Composed of" (part tied to whole)</td><td>Car --- Engine</td></tr>
<tr><td>Inheritance</td><td>empty triangle arrow</td><td>"Is a"</td><td>DigitalBook ---|&gt; Book</td></tr>
<tr><td>Realization</td><td>dotted triangle arrow</td><td>Implements interface</td><td>ConcreteClass ..|&gt; Interface</td></tr>
<tr><td>Dependency</td><td>dotted arrow</td><td>Uses temporarily</td><td>Client ...&gt; Service</td></tr>
</table>

<p><strong>Multiplicities</strong>:</p>
<ul>
<li>1 : exactly one</li>
<li>0..1 : zero or one</li>
<li>* : zero or many</li>
<li>1..* : one or many</li>
<li>2..5 : between 2 and 5</li>
</ul>

<p><strong>Complete example</strong>:</p>
<p>Library (1) --- (0..*) Book<br/>
Reader (1) --- (0..5) Loan<br/>
Loan (*) --- (1) Book</p>
<p>A reader can have a maximum of 5 simultaneous loans.</p>

<h3 class="section-title">4. Object Diagram</h3>

<p><strong>Objective</strong>: Show concrete instances at a given point in time (snapshot).</p>

<p><strong>Difference from class diagram</strong>:</p>
<ul>
<li>Classes: general structure</li>
<li>Objects: particular instances with values</li>
</ul>

<p><strong>Example</strong>:</p>
<pre><code>book1 : Book
- isbn = "978-2-1234"
- title = "Design Patterns"
- available = false

reader1 : Reader
- name = "Dupont"
- cardNumber = "12345"

loan1 : Loan
- loanDate = "2024-11-15"
- expectedReturnDate = "2024-12-15"</code></pre>

<p><strong>Usefulness</strong>: Validate the class diagram with concrete examples, illustrate complex configurations.</p>

<h3 class="section-title">5. Sequence Diagram</h3>

<p><strong>Objective</strong>: Show interactions between objects over time (chronological order of messages).</p>

<p><strong>Elements</strong>:</p>
<ul>
<li><strong>Lifelines</strong>: vertical lines representing objects</li>
<li><strong>Messages</strong>: horizontal arrows between lifelines</li>
<li><strong>Activation</strong>: rectangle on lifeline (active object)</li>
<li><strong>Fragments</strong>: alt (alternative), loop (loop), opt (optional), par (parallel)</li>
</ul>

<p><strong>Message types</strong>:</p>
<ul>
<li>Synchronous: solid arrow (caller waits for response)</li>
<li>Asynchronous: open arrow (caller continues without waiting)</li>
<li>Return: dotted arrow</li>
</ul>

<p><strong>Example: Borrowing a book</strong></p>

<pre><code>Reader -> Library : borrowBook(isbn)
Library -> Catalog : searchBook(isbn)
Catalog -> Library : book
alt book available
    Library -> Loan : createLoan(reader, book)
    Loan -> Book : markBorrowed()
    Library -> Reader : borrowConfirmation
else book unavailable
    Library -> Reader : errorMessage
end</code></pre>

<p><strong>Useful fragments</strong>:</p>
<ul>
<li><strong>alt</strong>: if/else (alternative branches)</li>
<li><strong>loop</strong>: loop (condition and iteration)</li>
<li><strong>opt</strong>: optional (executed if condition is true)</li>
<li><strong>par</strong>: parallel (simultaneous execution)</li>
<li><strong>ref</strong>: reference to another diagram</li>
</ul>

<h3 class="section-title">6. Activity Diagram</h3>

<p><strong>Objective</strong>: Model workflows, business processes, algorithms (similar to an enhanced flowchart).</p>

<p><strong>Elements</strong>:</p>
<ul>
<li><strong>Initial node</strong>: filled black circle</li>
<li><strong>Final node</strong>: black circle with surrounding circle</li>
<li><strong>Activity</strong>: rounded rectangle</li>
<li><strong>Decision</strong>: diamond (condition)</li>
<li><strong>Fork/Join</strong>: horizontal bar (parallelism)</li>
<li><strong>Swimlanes</strong>: partitions by actor/system</li>
</ul>

<p><strong>Example: Borrowing process</strong></p>

<pre><code>[Start]
|
Reader presents card
|
&lt;Card valid?&gt;
  No -> Refuse loan -> [End]
  Yes |
Scan book barcode
|
&lt;Book available?&gt;
  No -> Offer reservation -> [End]
  Yes |
Register loan
|
Print receipt
|
[End]</code></pre>

<p><strong>Parallelism with fork/join</strong>:</p>
<p>Fork (horizontal bar):<br/>
-> Activity A<br/>
-> Activity B (in parallel)</p>
<p>Join: synchronization (wait for both A and B to complete)</p>

<h3 class="section-title">7. State Machine Diagram</h3>

<p><strong>Objective</strong>: Model the lifecycle of an object (possible states and transitions).</p>

<p><strong>Elements</strong>:</p>
<ul>
<li><strong>State</strong>: rounded rectangle</li>
<li><strong>Transition</strong>: arrow with triggering event</li>
<li><strong>Initial state</strong>: black circle</li>
<li><strong>Final state</strong>: black circle with surrounding circle</li>
<li><strong>Actions</strong>: entry/ (on entry), do/ (during), exit/ (on exit)</li>
</ul>

<p><strong>Example: States of a book</strong></p>

<pre><code>[Initial]
|
Available
  entry/ displayAvailable()

Available --[borrow]--> Borrowed
  entry/ registerLoan()
  do/ decrementAvailability()

Borrowed --[return]--> Available
  exit/ releaseItem()

Borrowed --[exceed deadline]--> Overdue
  entry/ calculateFine()

Overdue --[return + pay fine]--> Available

Available --[remove from catalog]--> [Final]</code></pre>

<p><strong>Composite states</strong>:</p>
<p>A state can contain sub-states (hierarchy).</p>

<p><strong>Concurrent states</strong>:</p>
<p>Multiple states active simultaneously (separated by dotted line).</p>

<h3 class="section-title">8. Component and Deployment Diagrams</h3>

<p><strong>Component diagram</strong>:</p>

<p>Shows the software organization in modules/libraries with their dependencies.</p>

<p>Typical components:</p>
<ul>
<li>User Interface (UI)</li>
<li>Business Logic</li>
<li>Data Access (DAO)</li>
<li>External libraries</li>
</ul>

<p>Relationships:</p>
<ul>
<li>Dependencies between components</li>
<li>Provided interfaces (circle) and required interfaces (half-circle)</li>
</ul>

<p><strong>Deployment diagram</strong>:</p>

<p>Shows the physical architecture (servers, networks, deployed artifacts).</p>

<p>Elements:</p>
<ul>
<li><strong>Nodes</strong>: hardware (server, PC, mobile)</li>
<li><strong>Artifacts</strong>: deployed files (JAR, EXE, WAR)</li>
<li><strong>Communications</strong>: protocols (HTTP, TCP, etc.)</li>
</ul>

<p>Example:</p>
<pre><code>Web Server
  - Apache Tomcat
  - Application.war

Database
  - MySQL Server
  - Library schema

Client Workstation
  - Web Browser
  - HTML/CSS/JS Interface</code></pre>

<h3 class="section-title">9. SOLID Design Principles</h3>

<p>A set of 5 principles for creating maintainable and extensible code.</p>

<p><strong>S - Single Responsibility Principle (SRP)</strong>:</p>
<p>A class should have only one reason to change (a single responsibility).</p>

<p>Bad:</p>
<pre><code>class Book
  + saveToDatabase()          // persistence responsibility
  + sendEmailNotification()   // notification responsibility</code></pre>

<p>Good:</p>
<pre><code>class Book
  // only book business logic

class BookRepository
  + save(book)

class NotificationService
  + sendEmail(recipient, message)</code></pre>

<p><strong>O - Open/Closed Principle (OCP)</strong>:</p>
<p>Classes should be open for extension, closed for modification.</p>
<p>Use inheritance, composition, or interfaces to extend without modifying existing code.</p>

<p><strong>L - Liskov Substitution Principle (LSP)</strong>:</p>
<p>Objects of a derived class should be able to replace objects of the base class without altering behavior.</p>

<p><strong>I - Interface Segregation Principle (ISP)</strong>:</p>
<p>Several specific interfaces are better than one general interface.</p>

<p>Bad:</p>
<pre><code>interface DocumentActions
  + print()
  + scan()
  + fax()</code></pre>

<p>A simple printer must implement scan() and fax() even if it doesn't support them.</p>

<p>Good:</p>
<pre><code>interface Printable
  + print()

interface Scannable
  + scan()

class SimplePrinter implements Printable
class MultifunctionPrinter implements Printable, Scannable</code></pre>

<p><strong>D - Dependency Inversion Principle (DIP)</strong>:</p>
<p>Depend on abstractions (interfaces), not on concrete implementations.</p>

<p>Bad:</p>
<pre><code>class Library
  private MySQLDatabase db  // concrete dependency</code></pre>

<p>Good:</p>
<pre><code>interface Database
  + save(data)
  + load(id)

class Library
  private Database db  // abstract dependency

class MySQLDatabase implements Database
class MongoDBDatabase implements Database</code></pre>

<p>Allows easily switching databases without modifying Library.</p>

<h3 class="section-title">10. Design Patterns</h3>

<p>Proven solutions to recurring design problems.</p>

<p><strong>Creational patterns</strong>: managing object creation</p>

<p><strong>Singleton</strong>:</p>
<p>Guarantee a single instance of a class.</p>

<pre><code>class ConfigurationManager
  private static instance : ConfigurationManager

  private ConfigurationManager()  // private constructor

  public static getInstance() : ConfigurationManager
    if instance == null
      instance = new ConfigurationManager()
    return instance</code></pre>

<p>Usage: unique managers (configuration, logging, connection pool).</p>

<p><strong>Factory Method</strong>:</p>
<p>Delegate object creation to subclasses.</p>

<pre><code>abstract class DocumentFactory
  abstract createDocument() : Document

class PDFFactory extends DocumentFactory
  createDocument() : Document
    return new PDFDocument()

class WordFactory extends DocumentFactory
  createDocument() : Document
    return new WordDocument()</code></pre>

<p><strong>Abstract Factory</strong>:</p>
<p>Create families of related objects without specifying their concrete classes.</p>

<p><strong>Structural patterns</strong>: organizing classes and objects</p>

<p><strong>Adapter</strong>:</p>
<p>Convert the interface of a class into another expected interface.</p>

<pre><code>interface MultimediaPlayer
  + play(file)

class MP3Player
  + playMP3(file)

class MP3Adapter implements MultimediaPlayer
  private mp3Player : MP3Player

  play(file)
    mp3Player.playMP3(file)</code></pre>

<p><strong>Decorator</strong>:</p>
<p>Dynamically add responsibilities to an object.</p>

<pre><code>interface Coffee
  + cost() : double

class SimpleCoffee implements Coffee
  cost() : double
    return 2.0

class WithMilk implements Coffee
  private coffee : Coffee

  cost() : double
    return coffee.cost() + 0.5

class WithSugar implements Coffee
  private coffee : Coffee

  cost() : double
    return coffee.cost() + 0.2</code></pre>

<p>Usage:</p>
<pre><code>Coffee myCoffee = new WithMilk(new WithSugar(new SimpleCoffee()))
// cost = 2.0 + 0.2 + 0.5 = 2.7</code></pre>

<p><strong>Composite</strong>:</p>
<p>Compose objects into tree structures (treat individual objects and compositions uniformly).</p>

<p><strong>Behavioral patterns</strong>: interactions between objects</p>

<p><strong>Observer</strong>:</p>
<p>Automatically notify objects when a state change occurs.</p>

<pre><code>interface Observer
  + update(subject)

class Subject
  private observers : List&lt;Observer&gt;

  + attach(observer)
    observers.add(observer)

  + notify()
    for each observer in observers
      observer.update(this)

class TemperatureDisplay implements Observer
  update(subject)
    temperature = subject.getTemperature()
    display(temperature)</code></pre>

<p>Usage: graphical interfaces (MVC), event-driven systems.</p>

<p><strong>Strategy</strong>:</p>
<p>Encapsulate interchangeable algorithms.</p>

<pre><code>interface FineCalculationStrategy
  + calculate(daysOverdue) : double

class StandardFine implements FineCalculationStrategy
  calculate(daysOverdue) : double
    return daysOverdue * 0.5

class StudentFine implements FineCalculationStrategy
  calculate(daysOverdue) : double
    return daysOverdue * 0.2

class LoanManager
  private strategy : FineCalculationStrategy

  setStrategy(strategy)
    this.strategy = strategy

  calculateFine(daysOverdue)
    return strategy.calculate(daysOverdue)</code></pre>

<p><strong>Command</strong>:</p>
<p>Encapsulate a request as an object.</p>
<p>Enables: undo, command queues, logging.</p>

<p><strong>State</strong>:</p>
<p>Modify an object's behavior according to its internal state.</p>

<p><strong>Template Method</strong>:</p>
<p>Define the skeleton of an algorithm; subclasses redefine certain steps.</p>

<h3 class="section-title">11. From UML to Code</h3>

<p><strong>Forward Engineering</strong>: generate code from UML diagrams.</p>

<p>Tools:</p>
<ul>
<li>Enterprise Architect (Java, C++, C#, Python generation)</li>
<li>StarUML (basic code generation)</li>
<li>PlantUML + custom scripts</li>
</ul>

<p>Example: class diagram -> Java classes with attributes and method signatures (skeletons).</p>

<p><strong>Reverse Engineering</strong>: generate UML diagrams from existing code.</p>

<p>Useful for:</p>
<ul>
<li>Documenting legacy code</li>
<li>Analyzing an unknown codebase</li>
<li>Maintaining code/documentation consistency</li>
</ul>

<p><strong>Round-trip Engineering</strong>: bidirectional code / UML synchronization.</p>

<p>Code modifications reflected in diagrams and vice versa.</p>

<p>In practice: difficult to maintain, requires discipline and appropriate tooling.</p>

<h3 class="section-title">12. Modeling Tools</h3>

<table>
<tr><th>Tool</th><th>Type</th><th>Advantages</th><th>Disadvantages</th></tr>
<tr><td>Enterprise Architect</td><td>Commercial</td><td>Complete, code generation, collaboration</td><td>Expensive, complex interface</td></tr>
<tr><td>StarUML</td><td>Open-source/Commercial</td><td>Intuitive interface, lightweight</td><td>Limited features in free version</td></tr>
<tr><td>PlantUML</td><td>Open-source</td><td>Text-based, CI/CD integration, versioning</td><td>Syntax learning curve</td></tr>
<tr><td>Lucidchart</td><td>Web</td><td>Collaborative, easy</td><td>Limited free version</td></tr>
<tr><td>draw.io</td><td>Web/Open</td><td>Free, simple</td><td>Not specialized for UML</td></tr>
<tr><td>Visual Paradigm</td><td>Commercial</td><td>Powerful, training included</td><td>Expensive</td></tr>
</table>

<p><strong>Personal recommendation</strong>:</p>
<ul>
<li>Personal projects: PlantUML (versionable with Git)</li>
<li>Enterprise: Enterprise Architect or Visual Paradigm</li>
<li>Quick collaboration: Lucidchart or Miro</li>
</ul>

<hr/>

<h2>PART D - Reflective Analysis and Perspectives</h2>

<h3 class="section-title">Skills Acquired</h3>

<p><strong>Modeling and abstraction</strong>:</p>
<p>Ability to analyze a complex problem and decompose it into modelable entities, relationships and behaviors.</p>

<p><strong>Technical communication</strong>:</p>
<p>UML provides a universal language for communicating architectures between developers, project managers, and clients.</p>

<p><strong>Anticipation and planning</strong>:</p>
<p>Designing before implementing allows identifying architecture problems early, reducing refactoring costs.</p>

<p><strong>Software quality</strong>:</p>
<p>Applying SOLID principles and patterns produces more maintainable, testable and extensible code.</p>

<h3 class="section-title">Completed Project: Library Management System</h3>

<p><strong>Context</strong>:</p>
<p>Complete design of a multimedia library system (books, DVDs, periodicals) with loan management, reservations, fines, and users.</p>

<p><strong>Deliverables</strong>:</p>
<ul>
<li>Use case diagram (12 cases, 4 actors)</li>
<li>Complete class diagram (35+ classes)</li>
<li>Sequence diagrams (borrow, return, reserve, pay fine)</li>
<li>State diagrams (book lifecycle, loan)</li>
<li>Activity diagram (complete borrowing process)</li>
<li>Java prototype with applied patterns</li>
</ul>

<p><strong>Patterns used</strong>:</p>
<ul>
<li><strong>Singleton</strong>: LibraryManager (single instance)</li>
<li><strong>Factory</strong>: DocumentFactory to create Book, DVD, Periodical</li>
<li><strong>Observer</strong>: availability notification for reservations</li>
<li><strong>Strategy</strong>: fine calculation by user type (standard, student, teacher)</li>
<li><strong>State</strong>: loan state management (in progress, overdue, completed)</li>
</ul>

<p><strong>Results</strong>:</p>
<p>Clear and extensible architecture. Adding new document types or new fine rules was easy thanks to patterns. Well-structured code with separation of responsibilities.</p>

<h3 class="section-title">Key Takeaways</h3>

<p><strong>1. UML = tool, not objective</strong>:</p>
<p>The goal is good design, not beautiful diagrams. Use UML pragmatically.</p>

<p><strong>2. Not all diagrams are necessary</strong>:</p>
<p>Identify those that add value depending on the context (class and sequence often suffice).</p>

<p><strong>3. SOLID before patterns</strong>:</p>
<p>Understanding and applying SOLID is more important than knowing all patterns.</p>

<p><strong>4. Patterns = solutions, not magic recipes</strong>:</p>
<p>Do not force the use of a pattern. Apply it only if the problem matches.</p>

<p><strong>5. Living documentation</strong>:</p>
<p>Documentation must evolve with the code, otherwise it becomes obsolete and misleading.</p>

<h3 class="section-title">Experience Feedback</h3>

<p><strong>Learning curve</strong>:</p>
<p>UML seemed complex initially (14 diagrams, specific notations). With practice, one quickly identifies the 5-6 essential diagrams.</p>

<p><strong>Link with OOP</strong>:</p>
<p>This course strengthened my understanding of OOP beyond syntax. Concepts like encapsulation, abstraction, and polymorphism became concrete.</p>

<p><strong>Application in projects</strong>:</p>
<p>Using UML on real projects (even simplified ones) proved its usefulness. Time savings and fewer bugs thanks to upfront thinking.</p>

<p><strong>Facilitated collaboration</strong>:</p>
<p>Working as a team with UML as a common language greatly improved communication and reduced misunderstandings.</p>

<h3 class="section-title">Practical Applications</h3>

<p><strong>Software development</strong>:</p>
<ul>
<li>Enterprise applications (ERP, CRM)</li>
<li>Embedded systems (modeling critical states and sequences)</li>
<li>Web applications (MVC/MVVM architecture)</li>
</ul>

<p><strong>Refactoring</strong>:</p>
<p>Reverse engineering of legacy code, identifying problems (tight coupling, mixed responsibilities), then SOLID-guided refactoring.</p>

<p><strong>Documentation</strong>:</p>
<p>Automatically generate technical documentation from UML diagrams. Integration into enterprise wikis.</p>

<p><strong>Client communication</strong>:</p>
<p>Use case and activity diagrams understandable by non-developers to validate requirements.</p>

<h3 class="section-title">Limitations and Criticisms</h3>

<p><strong>Heavy and verbose UML</strong>:</p>
<p>Creating and maintaining all diagrams takes time. Agile approach prefers "lightweight UML" (a few key diagrams).</p>

<p><strong>Documentation/code gap</strong>:</p>
<p>Without discipline or synchronization tools, diagrams quickly become obsolete.</p>

<p><strong>Over-engineering</strong>:</p>
<p>Risk of creating overly complex architectures, with too many patterns, for simple problems.</p>

<p><strong>Modern alternatives</strong>:</p>
<ul>
<li><strong>C4 Model</strong>: pragmatic architectural documentation (Context, Containers, Components, Code)</li>
<li><strong>Architecture Decision Records (ADR)</strong>: documenting decisions rather than diagrams</li>
<li><strong>Living Documentation</strong>: tests and code as documentation</li>
</ul>

<h3 class="section-title">Evolutions and Perspectives</h3>

<p><strong>Domain-Driven Design (DDD)</strong>:</p>
<p>Business domain-centered approach. Uses UML but adds concepts (Entities, Value Objects, Aggregates, Repositories).</p>

<p><strong>SysML</strong>:</p>
<p>UML extension for systems engineering (not just software). Used in aerospace, automotive, defense.</p>

<p><strong>Modern tools</strong>:</p>
<ul>
<li>Automatic diagram generation from code (Doxygen, Javadoc UML)</li>
<li>Documentation as Code (PlantUML in Markdown, Git versioning)</li>
<li>Real-time collaboration (Miro, Lucidchart, Figma for UML)</li>
</ul>

<p><strong>Artificial Intelligence</strong>:</p>
<p>AI generating UML diagrams from text descriptions, automatic detection of SOLID violations, pattern suggestions.</p>

<h3 class="section-title">Tips for Success</h3>

<p><strong>1. Practice on concrete projects</strong>:</p>
<p>Model real systems (e-commerce, social network, game) rather than abstract exercises.</p>

<p><strong>2. Start simple</strong>:</p>
<p>Begin with class and sequence diagrams. Add other types as needed.</p>

<p><strong>3. Validate with code</strong>:</p>
<p>Implement designs to verify their consistency and feasibility.</p>

<p><strong>4. Study open-source code</strong>:</p>
<p>Analyze the architecture of popular projects (Spring Framework, Apache Commons) to see SOLID and patterns in practice.</p>

<p><strong>5. Iterate</strong>:</p>
<p>Design is never perfect on the first try. Revise and improve as you go.</p>

<h3 class="section-title">Conclusion</h3>

<p>This module provides an essential methodology for designing robust and maintainable software systems. Beyond UML syntax, it is the object-oriented design principles (SOLID) and patterns that constitute the major contribution.</p>

<p><strong>Transferable skills</strong>:</p>
<ul>
<li>Architectural and abstract thinking</li>
<li>Design before implementation</li>
<li>Effective technical communication</li>
<li>Professional quality code</li>
</ul>

<p><strong>Professional relevance</strong>:</p>
<p>In the workplace, design and documentation are expected, especially for critical or regulated projects. Knowing how to model and justify architecture choices is a major asset.</p>

<p><strong>Key message</strong>:</p>
<p>UML is one tool among many. The essential thing is to develop a structured design approach, applicable regardless of the formalism. SOLID principles and patterns are universal and transcend languages and tools.</p>

<p><strong>Recommendations</strong>:</p>
<ul>
<li>Use UML pragmatically (avoid dogmatism)</li>
<li>Prioritize diagrams that add value</li>
<li>Keep documentation up to date (automate if possible)</li>
<li>Continue learning advanced patterns and architectures (microservices, event-driven)</li>
<li>Explore DDD to deepen business modeling</li>
</ul>

<p><strong>Links with other courses</strong>:</p>
<ul>
<li><a href="./poo-cpp.html">Object-Oriented Programming C++ - S7</a>: concept implementation</li>
<li><a href="./poo-java.html">Object-Oriented Programming Java - S7</a>: practical application</li>
<li><a href="./graphes-programmation-lineaire.html">Graphs and Linear Programming - S8</a>: problem modeling</li>
</ul>

<hr/>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Design and Architecture Course</h4>
      <p>Complete UML course: class diagrams, sequence diagrams, use cases, design patterns and SOLID principles.</p>
      <embed src="/cours-pdf/S7/Conception-UML/cours-conception.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Conception-UML/cours-conception.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Tutorial Subject</h4>
      <p>Tutorials on object-oriented design: modeling of embedded systems and software architectures.</p>
      <embed src="/cours-pdf/S7/Conception-UML/td-sujet.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S7/Conception-UML/td-sujet.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

<hr/>

<p><em>Course taken in 2023-2024 at INSA Toulouse, Department of Electrical Engineering and Computer Science.</em></p>

</div>

<div class="back-nav">
    <a href="./my-courses-2023-2024.html" data-i18n-html="back-courses-2023-2024">&larr; Retour aux Cours 2023-2024</a>
</div>
