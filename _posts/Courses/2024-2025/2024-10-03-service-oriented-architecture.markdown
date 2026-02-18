---
layout: default
title:  "Service Oriented Architecture"
date:   2024-10-02 10:56:03 +0200
---

<style>
.back-nav {
  margin-bottom: 20px;
}
.back-nav a {
  text-decoration: none;
  color: #2a7ae2;
  font-weight: 600;
}
.back-nav a:hover {
  text-decoration: underline;
}
.section-title {
  color: #2a7ae2;
  border-bottom: 2px solid #2a7ae2;
  padding-bottom: 10px;
  margin-top: 30px;
  margin-bottom: 20px;
}
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
  <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour a Mes Cours 2024-2025</a>
</div>

<div class="lang-fr">

<h1>Service Oriented Architecture - Semestre 9</h1>

<p><strong>Annee Academique</strong> : 2024-2025<br>
<strong>Semestre</strong> : 9 (S9)<br>
<strong>Enseignant</strong> : N. Guermouche<br>
<strong>Categorie</strong> : Architectures Logicielles / Services Web</p>

<hr>

<h2>PART A : PRESENTATION GENERALE</h2>

<h3 class="section-title">Presentation</h3>

<p>Le cours d'Architecture Orientee Services (SOA) a constitue une immersion approfondie dans les principes et les pratiques de conception et d'implementation de systemes orientes services. Enseigne par N. Guermouche, ce cours a couvert les architectures de services traditionnelles et modernes, en se concentrant sur la creation de systemes scalables, maintenables et performants.</p>

<p>Le programme s'articulait autour de trois grands axes :</p>
<ul>
<li><strong>Les services web traditionnels (SOAP/WSDL)</strong> : comprendre les fondements historiques de la SOA, les protocoles d'echange standardises et la description formelle des services.</li>
<li><strong>Les services RESTful</strong> : maitriser l'approche moderne basee sur les ressources HTTP, les formats de donnees legers (JSON, XML, YAML) et le modele de maturite de Richardson (RMM).</li>
<li><strong>Les microservices</strong> : apprehender la decomposition d'applications monolithiques en services autonomes, independamment deployables et scalables, avec Spring Boot comme framework de reference.</li>
</ul>

<h3 class="section-title">Competences visees</h3>

<ul>
<li>Comprendre les principes fondamentaux des architectures orientees services</li>
<li>Concevoir et implementer des services web SOAP et REST</li>
<li>Maitriser la description de services avec WSDL</li>
<li>Developper des API RESTful conformes aux bonnes pratiques</li>
<li>Architecturer des applications en microservices</li>
<li>Utiliser Maven pour la gestion de projets Java</li>
<li>Appliquer les tests unitaires avec JUnit</li>
<li>Collaborer avec Git dans un workflow de developpement</li>
</ul>

<hr>

<h2>PART B : EXPERIENCE ET CONTEXTE</h2>

<h3 class="section-title">Details de l'experience</h3>

<h4>Environnement et Contexte</h4>

<p>Ce cours s'est revele particulierement utile dans un contexte ou la demande industrielle pour des systemes distribues et des architectures de services ne cesse de croitre. L'industrie du logiciel migre massivement des architectures monolithiques vers des architectures en microservices, rendant ces competences essentielles pour tout ingenieur en informatique.</p>

<p>Les seances de travaux pratiques m'ont permis d'appliquer les concepts appris en cours a des scenarios concrets, ce qui a ete benefique pour comprendre les differentes methodologies architecturales. Le cours etait structure en progression : des fondamentaux SOA/SOAP vers REST, puis vers les microservices, chaque etape construisant sur la precedente.</p>

<h4>Ma Fonction</h4>

<p>Dans le cadre de ce cours, j'ai ete responsable de :</p>
<ul>
<li>Comprendre les principes des architectures orientees services (couplage lache, contrats de service, abstraction)</li>
<li>Concevoir et implementer des systemes orientes services avec SOAP et REST</li>
<li>Developper un projet complet en microservices avec Spring Boot</li>
<li>Rediger un rapport WSDL et des exercices de modelisation de services</li>
<li>Mener des experimentations pour tester l'efficacite et la scalabilite des differentes architectures</li>
<li>Collaborer en binome (avec T. Bigot) sur le projet final de microservices</li>
</ul>

<hr>

<h2>PART C : ASPECTS TECHNIQUES</h2>

<p>Cette section explore en detail les aspects techniques du cours d'Architecture Orientee Services, acquis principalement lors des travaux pratiques portant sur SOAP, REST et les microservices.</p>

<h3 class="section-title">Concepts Techniques</h3>

<h4>1. Principes fondamentaux de la SOA</h4>

<p>L'Architecture Orientee Services repose sur plusieurs principes fondamentaux :</p>

<p><strong>Couplage lache (Loose Coupling)</strong> :
Les services sont conçus pour minimiser les dependances entre eux. Chaque service peut evoluer independamment sans impacter les autres. Cela favorise la maintenabilite et la flexibilite du systeme global.</p>

<p><strong>Contrats de service</strong> :
Chaque service expose un contrat formel (WSDL pour SOAP, OpenAPI/Swagger pour REST) decrivant ses operations, ses types de donnees et ses protocoles de communication. Ce contrat sert d'interface entre le fournisseur et le consommateur du service.</p>

<p><strong>Abstraction</strong> :
Les details d'implementation sont caches derriere l'interface du service. Le consommateur n'a pas besoin de connaitre la logique interne, la base de donnees ou le langage de programmation utilise.</p>

<p><strong>Reutilisabilite</strong> :
Les services sont conçus pour etre reutilises dans differents contextes et applications. Un service de gestion d'utilisateurs peut etre utilise par plusieurs applications differentes.</p>

<p><strong>Decouverte de services</strong> :
Les services peuvent etre decouverts dynamiquement via un registre (UDDI pour SOAP, service registry pour microservices), permettant une composition flexible.</p>

<h4>2. WSDL - Web Services Description Language</h4>

<p>Le WSDL est un langage XML utilise pour decrire les services web SOAP. Il definit quatre elements principaux :</p>

<ul>
<li><strong>Types</strong> : les types de donnees utilises par le service (schemas XSD)</li>
<li><strong>Messages</strong> : les messages echanges (entree/sortie)</li>
<li><strong>PortType</strong> : les operations disponibles (l'interface du service)</li>
<li><strong>Binding</strong> : le protocole de transport et le format d'encodage</li>
</ul>

<p>Voici un exemple de fichier WSDL que j'ai etudie et produit en TP, decrivant un service de recherche de livres :</p>

<pre><code class="language-xml">&lt;wsdl:definitions xmlns:tns="http://www.example.org/BookService/"
                  xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
                  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                  xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
                  name="BookService"
                  targetNamespace="http://www.example.org/BookService/"&gt;

    &lt;wsdl:types&gt;
        &lt;xsd:schema targetNamespace="http://www.example.org/BookService/"&gt;
            &lt;xsd:complexType name="BookType"&gt;
                &lt;xsd:sequence&gt;
                    &lt;xsd:element name="title" type="xsd:string"/&gt;
                    &lt;xsd:element name="author" type="xsd:int"/&gt;
                    &lt;xsd:element name="isbn" type="xsd:string"/&gt;
                &lt;/xsd:sequence&gt;
            &lt;/xsd:complexType&gt;
            &lt;xsd:element name="book" type="tns:BookType"/&gt;
        &lt;/xsd:schema&gt;
    &lt;/wsdl:types&gt;

    &lt;wsdl:message name="searchbookIn"&gt;
        &lt;wsdl:part name="title" type="xsd:string"/&gt;
    &lt;/wsdl:message&gt;
    &lt;wsdl:message name="searchbookOut"&gt;
        &lt;wsdl:part name="book" element="tns:book"/&gt;
    &lt;/wsdl:message&gt;

    &lt;wsdl:portType name="Port1"&gt;
        &lt;wsdl:operation name="searchBook"&gt;
            &lt;wsdl:input message="tns:searchbookIn"/&gt;
            &lt;wsdl:output message="tns:searchbookOut"/&gt;
        &lt;/wsdl:operation&gt;
    &lt;/wsdl:portType&gt;

    &lt;wsdl:binding name="BookWSPortBinding" type="tns:Port1"&gt;
        &lt;soap:binding style="document"
                      transport="http://schemas.xmlsoap.org/soap/http"/&gt;
        &lt;wsdl:operation name="searchBook"&gt;
            &lt;wsdl:input&gt;&lt;soap:body use="literal"/&gt;&lt;/wsdl:input&gt;
            &lt;wsdl:output&gt;&lt;soap:body use="literal"/&gt;&lt;/wsdl:output&gt;
        &lt;/wsdl:operation&gt;
    &lt;/wsdl:binding&gt;

    &lt;wsdl:service name="UnivWS"&gt;
        &lt;wsdl:port name="UnivWSPort" binding="tns:BookWSPortBinding"&gt;
            &lt;soap:address location="http://localhost:8080/UnivWSApplication/UnivWS"/&gt;
        &lt;/wsdl:port&gt;
    &lt;/wsdl:service&gt;
&lt;/wsdl:definitions&gt;
</code></pre>

<p>J'ai egalement developpe des classes Java correspondant aux types WSDL, comme la modelisation d'un systeme de gestion de cours :</p>

<pre><code class="language-java">public class CoursType {
    private String intitule;
    private int ects;
    private String nomResponsable;

    public CoursType(String intitule, int ects, String nomResponsable) {
        this.intitule = intitule;
        this.ects = ects;
        this.nomResponsable = nomResponsable;
    }
    // getters et setters
}
</code></pre>

<h4>3. Protocole SOAP</h4>

<p>Le protocole SOAP (Simple Object Access Protocol) est un protocole d'echange de messages structures pour les services web. Il utilise XML pour le formatage des messages et s'appuie sur des protocoles de la couche application tels que HTTP ou SMTP pour la transmission.</p>

<p>La structure d'un message SOAP comprend trois parties :</p>
<ul>
<li><strong>Envelope</strong> : l'element racine qui encapsule l'ensemble du message</li>
<li><strong>Header</strong> (optionnel) : contient des metadonnees (authentification, routage, etc.)</li>
<li><strong>Body</strong> : contient le contenu du message (requete ou reponse)</li>
</ul>

<p><strong>Requete SOAP</strong> : L'enveloppe de requete contient le message SOAP envoye au service web. Par exemple, si la chaine recherchee est "cedric", l'enveloppe SOAP ressemble a ceci :</p>

<pre><code class="language-xml">&lt;soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:web="http://example.com/webservice"&gt;
    &lt;soapenv:Header/&gt;
    &lt;soapenv:Body&gt;
        &lt;web:MyRequest&gt;
            &lt;web:chain&gt;cedric&lt;/web:chain&gt;
        &lt;/web:MyRequest&gt;
    &lt;/soapenv:Body&gt;
&lt;/soapenv:Envelope&gt;
</code></pre>

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_MOOC/SOAP_send.png" alt="Envoi d'une requete SOAP" style="width: 70%; border: 1px solid #ddd; border-radius: 5px; padding: 5px;"/>
</div>
<p style="text-align: center; font-style: italic;">Envoi d'une requete SOAP depuis un client</p>
<br>

<p><strong>Reponse SOAP</strong> : La reponse est retournee par le service web apres traitement de la requete. Par exemple, si la reponse retourne 6 (longueur de la chaine) :</p>

<pre><code class="language-xml">&lt;soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:tns="http://www.example.org/BookService/"&gt;
    &lt;soapenv:Header/&gt;
    &lt;soapenv:Body&gt;
        &lt;tns:searchBookResponse&gt;
            &lt;tns:book&gt;
                &lt;tns:title&gt;Les Miserables&lt;/tns:title&gt;
                &lt;tns:author&gt;123&lt;/tns:author&gt;
                &lt;tns:isbn&gt;13.978-2211215350&lt;/tns:isbn&gt;
            &lt;/tns:book&gt;
        &lt;/tns:searchBookResponse&gt;
    &lt;/soapenv:Body&gt;
&lt;/soapenv:Envelope&gt;
</code></pre>

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_MOOC/SOAP_receive.png" alt="Reception d'une reponse SOAP" style="width: 70%; border: 1px solid #ddd; border-radius: 5px; padding: 5px;"/>
</div>
<p style="text-align: center; font-style: italic;">Reception d'une reponse SOAP</p>
<br>

<p>Les tutoriels SOA nous ont permis de pratiquer deux approches :</p>
<ul>
<li><strong>Bottom-Up (Code First)</strong> : on ecrit d'abord le code Java, puis on genere le WSDL automatiquement avec Apache CXF</li>
<li><strong>Top-Down (Contract First)</strong> : on ecrit d'abord le WSDL, puis on genere les stubs Java avec le plugin cxf-codegen</li>
</ul>

<h4>4. Services RESTful</h4>

<p>REST (Representational State Transfer) est un style architectural qui utilise les methodes HTTP standard pour interagir avec des ressources. Contrairement a SOAP, REST est sans etat (stateless), plus leger et s'appuie sur les standards du Web.</p>

<p><strong>Methodes HTTP</strong> :</p>

<table>
<tr><th>Methode</th><th>Action</th><th>Exemple</th><th>Description</th></tr>
<tr><td><strong>GET</strong></td><td>Lecture</td><td><code>GET /users/1</code></td><td>Recupere l'utilisateur avec l'ID 1</td></tr>
<tr><td><strong>POST</strong></td><td>Creation</td><td><code>POST /users</code></td><td>Cree un nouvel utilisateur</td></tr>
<tr><td><strong>PUT</strong></td><td>Mise a jour complete</td><td><code>PUT /users/1</code></td><td>Remplace l'utilisateur 1</td></tr>
<tr><td><strong>PATCH</strong></td><td>Mise a jour partielle</td><td><code>PATCH /users/1</code></td><td>Modifie partiellement l'utilisateur 1</td></tr>
<tr><td><strong>DELETE</strong></td><td>Suppression</td><td><code>DELETE /users/1</code></td><td>Supprime l'utilisateur 1</td></tr>
</table>

<p><strong>Codes de statut HTTP</strong> :</p>

<table>
<tr><th>Code</th><th>Signification</th></tr>
<tr><td>200</td><td>OK - Requete reussie</td></tr>
<tr><td>201</td><td>Created - Ressource creee</td></tr>
<tr><td>204</td><td>No Content - Succes sans contenu de retour</td></tr>
<tr><td>400</td><td>Bad Request - Requete invalide</td></tr>
<tr><td>401</td><td>Unauthorized - Authentification requise</td></tr>
<tr><td>403</td><td>Forbidden - Acces refuse</td></tr>
<tr><td>404</td><td>Not Found - Ressource non trouvee</td></tr>
<tr><td>500</td><td>Internal Server Error - Erreur serveur</td></tr>
</table>

<p><strong>HATEOAS (Hypermedia As The Engine Of Application State)</strong> :
HATEOAS est un principe REST ou les reponses contiennent des liens hypertextes vers les actions disponibles. Cela permet au client de naviguer dynamiquement dans l'API sans connaitre a l'avance les URLs. Par exemple, une reponse pour un utilisateur pourrait inclure des liens vers ses commandes, son profil, etc.</p>

<p><strong>Modele de Maturite de Richardson (RMM)</strong> :
Le RMM definit quatre niveaux de maturite pour les API REST :</p>

<ul>
<li><strong>Niveau 0</strong> : Un seul point d'entree (type RPC sur HTTP). Toutes les requetes passent par une seule URL.</li>
<li><strong>Niveau 1</strong> : Introduction des ressources. Chaque ressource a sa propre URI (par exemple <code>/users</code>, <code>/orders</code>).</li>
<li><strong>Niveau 2</strong> : Utilisation correcte des verbes HTTP (GET, POST, PUT, DELETE) et des codes de statut.</li>
<li><strong>Niveau 3</strong> : HATEOAS. Les reponses contiennent des liens hypertextes pour guider le client. C'est le niveau le plus mature.</li>
</ul>

<p>J'ai developpe des services RESTful pour la gestion de commandes en utilisant JAX-RS et JSON pour l'echange de donnees :</p>

<pre><code class="language-java">public class OrderService {
    private static List&lt;Order&gt; orders = new ArrayList&lt;&gt;();
    private static int idCounter = 1;

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public List&lt;Order&gt; getAllOrders() {
        return orders;
    }

    @GET
    @Path("/{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public Order getOrder(@PathParam("id") int id) {
        return orders.stream()
            .filter(order -&gt; order.getId() == id)
            .findFirst().orElse(null);
    }

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Order createOrder(Order order) {
        order.setId(idCounter++);
        orders.add(order);
        return order;
    }

    @PUT
    @Path("/{id}")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Order updateOrder(@PathParam("id") int id, Order updatedOrder) {
        for (Order order : orders) {
            if (order.getId() == id) {
                order.setProduct(updatedOrder.getProduct());
                order.setQuantity(updatedOrder.getQuantity());
                return order;
            }
        }
        return null;
    }

    @DELETE
    @Path("/{id}")
    public void deleteOrder(@PathParam("id") int id) {
        orders.removeIf(order -&gt; order.getId() == id);
    }
}
</code></pre>

<p>J'ai egalement developpe un controleur REST avec Spring Boot pour la gestion d'utilisateurs :</p>

<pre><code class="language-java">@RestController
@RequestMapping("/api/users")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping
    public List&lt;User&gt; getAllUsers() {
        return userService.getAllUsers();
    }

    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        return userService.getUserById(id);
    }

    @PostMapping
    public User createUser(@RequestBody User user) {
        return userService.createUser(user);
    }

    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User userDetails) {
        return userService.updateUser(id, userDetails);
    }

    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
    }
}
</code></pre>

<p>Les outils de test comme Postman ont ete utilises pour valider les endpoints, verifier les codes de statut HTTP et inspecter les corps de requete/reponse en JSON.</p>

<h4>5. Formats de donnees : JSON, XML et YAML</h4>

<p>Les services web utilisent differents formats de serialisation pour l'echange de donnees :</p>

<p><strong>JSON (JavaScript Object Notation)</strong> : format leger, lisible et largement adopte pour les API REST.</p>

<pre><code class="language-json">{
    "id": 1,
    "product": "Laptop",
    "quantity": 3
}
</code></pre>

<p><strong>XML (eXtensible Markup Language)</strong> : format historique utilise par SOAP, plus verbeux mais avec un schema de validation fort (XSD).</p>

<pre><code class="language-xml">&lt;order&gt;
    &lt;id&gt;1&lt;/id&gt;
    &lt;product&gt;Laptop&lt;/product&gt;
    &lt;quantity&gt;3&lt;/quantity&gt;
&lt;/order&gt;
</code></pre>

<p><strong>YAML (YAML Ain't Markup Language)</strong> : format lisible souvent utilise pour la configuration (fichiers Spring Boot <code>application.yml</code>, Docker Compose, etc.).</p>

<pre><code class="language-yaml">order:
  id: 1
  product: Laptop
  quantity: 3
</code></pre>

<h4>6. Architecture Microservices</h4>

<p>Les microservices representent un style architectural qui structure une application comme un ensemble de services faiblement couples, chacun deployable et scalable de maniere independante.</p>

<p><strong>Patterns de decomposition</strong> :</p>
<ul>
<li><strong>Decomposition par domaine metier</strong> : chaque microservice correspond a un domaine fonctionnel (utilisateurs, commandes, feedback, etc.)</li>
<li><strong>Decomposition par sous-domaine</strong> : approche DDD (Domain-Driven Design) pour delimiter les contextes bornes (bounded contexts)</li>
</ul>

<p><strong>Decouverte de services (Service Discovery)</strong> :
Dans une architecture microservices, les services doivent pouvoir se trouver mutuellement. Des outils comme Eureka (Netflix) ou Consul (HashiCorp) permettent l'enregistrement et la decouverte dynamique des services.</p>

<p><strong>API Gateway</strong> :
Un point d'entree unique qui route les requetes vers les microservices appropries. L'API Gateway gere egalement des preoccupations transversales comme l'authentification, le rate limiting et le load balancing.</p>

<p>Dans le cadre du projet, j'ai utilise Spring Boot pour creer plusieurs microservices independants :</p>
<ul>
<li><strong>userManagement</strong> : gestion des utilisateurs (CRUD, profils)</li>
<li><strong>volunteerManagement</strong> : gestion des benevoles</li>
<li><strong>volunteerService</strong> : logique metier des benevoles</li>
<li><strong>userRequestService</strong> : gestion des demandes utilisateurs</li>
<li><strong>feedbackService</strong> : gestion des retours et evaluations</li>
<li><strong>AnalyseProject</strong> : service d'analyse globale</li>
</ul>

<p>Chaque microservice possede son propre fichier <code>pom.xml</code>, sa propre base de donnees et peut etre deploye independamment. La communication entre les services se fait via des appels REST HTTP.</p>

<h4>7. Gestion de projet avec Maven</h4>

<p>Maven est l'outil de gestion de projet et de build utilise tout au long du cours. Le fichier <code>pom.xml</code> centralise :</p>
<ul>
<li>Les dependances du projet (Spring Boot, CXF, JAX-RS, etc.)</li>
<li>Les plugins de build (compilation, tests, packaging)</li>
<li>La configuration du projet (version Java, encoding, etc.)</li>
</ul>

<p>Exemple de configuration Maven pour un microservice Spring Boot :</p>

<pre><code class="language-xml">&lt;dependencies&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
    &lt;/dependency&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
        &lt;scope&gt;test&lt;/scope&gt;
    &lt;/dependency&gt;
&lt;/dependencies&gt;
</code></pre>

<h4>8. Workflow Git</h4>

<p>Le projet de microservices a ete gere avec Git pour le controle de version. Le workflow collaboratif incluait :</p>
<ul>
<li><strong>Branching</strong> : une branche par fonctionnalite ou microservice</li>
<li><strong>Commits</strong> : des commits atomiques et messages descriptifs</li>
<li><strong>Merge</strong> : integration des branches dans la branche principale</li>
<li><strong>Remote</strong> : synchronisation avec un depot distant (GitLab INSA)</li>
</ul>

<h4>9. Tests unitaires avec JUnit</h4>

<p>Les tests unitaires avec JUnit ont permis de valider le bon fonctionnement de chaque composant individuellement. Les tests couvrent les services, les controleurs et la logique metier :</p>

<pre><code class="language-java">@Test
public void testCreateUser() {
    User user = new User("Cedric", "cedric@insa.fr");
    User created = userService.createUser(user);
    assertNotNull(created.getId());
    assertEquals("Cedric", created.getName());
}

@Test
public void testGetAllOrders() {
    List&lt;Order&gt; orders = orderService.getAllOrders();
    assertNotNull(orders);
}
</code></pre>

<h4>10. Framework Spring Boot</h4>

<p>Spring Boot a ete le framework principal pour le developpement des microservices. Ses avantages cles :</p>
<ul>
<li><strong>Auto-configuration</strong> : configuration automatique basee sur les dependances presentes</li>
<li><strong>Serveur embarque</strong> : Tomcat integre, pas besoin de deploiement externe</li>
<li><strong>Starters</strong> : des packages de dependances pre-configures (spring-boot-starter-web, etc.)</li>
<li><strong>Actuator</strong> : monitoring et metriques de l'application</li>
<li><strong>Profils</strong> : gestion de configurations multiples (dev, test, prod)</li>
</ul>

<hr>

<h2>PART D : ANALYSE ET REFLEXION</h2>

<h3 class="section-title">Connaissances et Competences Mobilisees</h3>

<ul>
<li>Comprehension des concepts et caracteristiques des architectures orientees services</li>
<li>Developpement d'architectures distribuees utilisant les services web</li>
<li>Deploiement et configuration de SOA avec SOAP et REST</li>
<li>Conception, developpement et deploiement d'architectures en microservices</li>
<li>Maitrise du langage Java et du framework Spring Boot</li>
<li>Gestion de projet avec Maven et Git</li>
<li>Tests unitaires avec JUnit</li>
<li>Comprehension des formats de donnees (JSON, XML, YAML)</li>
<li>Connaissance des niveaux de maturite REST (RMM) et de HATEOAS</li>
</ul>

<h3 class="section-title">Auto-evaluation</h3>

<p>L'utilisation de tous les nouveaux concepts appris pendant le cours etait au debut un peu complexe, mais heureusement les tutoriels etaient bien structures, me permettant d'apprendre etape par etape. De plus, il y avait un grand nombre de seances pratiques pour s'exercer et comprendre tous les concepts. N'etant pas habitue a Java, j'ai du reapprendre les bases de ce langage, ce qui a represente un defi supplementaire.</p>

<p>Je n'ai pas beaucoup participe aux TP SOAP car je souhaitais me concentrer davantage sur REST et les microservices en raison de contraintes de temps. Neanmoins, les exercices de modelisation WSDL ont ete tres formateurs pour comprendre la structure formelle des contrats de service.</p>

<p>Le projet de microservices a ete l'element le plus enrichissant du cours. Concevoir une architecture complete avec plusieurs services independants, gerer les communications inter-services et deployer le tout m'a donne une vision concrete de ce qu'implique le developpement d'applications distribuees en production.</p>

<p>La progression pedagogique du cours -- des fondamentaux SOA vers SOAP, puis REST, puis les microservices -- etait logique et bien construite. Chaque technologie introduisait des concepts qui preparaient a la suivante.</p>

<h3 class="section-title">Mon Avis</h3>

<p>Avant de suivre ce cours, je n'avais entendu parler que de certains concepts lies a l'architecture orientee services. Grace aux seances de travaux pratiques, j'ai maintenant une bien meilleure comprehension de l'architecture des applications web et de la maniere d'interagir avec elles. Par exemple, simplement en observant le reseau d'un site web et en comprenant toutes les requetes en arriere-plan.</p>

<p>De plus, developper en Java pendant le cours m'a rappele comment coder dans ce langage, ce qui est important car il est tres utilise dans l'industrie. Meme si je prefererais coder en C pour mon avenir professionnel, je peux desormais postuler a des postes Java si necessaire.</p>

<p>La comparaison entre SOAP et REST m'a permis de comprendre pourquoi l'industrie migre vers REST : simplicite, performance et meilleure integration avec les architectures modernes. Cependant, SOAP reste pertinent dans des contextes ou la securite et la fiabilite transactionnelle sont critiques (secteur bancaire, sante).</p>

<p>L'apprentissage des microservices a ete une ouverture vers les pratiques DevOps modernes. La decomposition en services independants facilite le deploiement continu, le scaling horizontal et la resilience des systemes. Ce sont des competences tres recherchees sur le marche du travail.</p>

<hr>

<h2>Documents de Cours</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Introduction a la SOA</h4>
      <p>Cours d'introduction aux principes fondamentaux de l'Architecture Orientee Services : couplage lache, contrats de service, abstraction et reutilisabilite.</p>
      <embed src="/cours-pdf/S9/SOA/2-1-Intro-SOA.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-1-Intro-SOA.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Standards WSDL (Partie 1)</h4>
      <p>Web Services Description Language : structure du WSDL, types, messages, portType et binding.</p>
      <embed src="/cours-pdf/S9/SOA/2-2-Standards-WSDL-1_.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-2-Standards-WSDL-1_.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Standards WSDL (Partie 2)</h4>
      <p>Approfondissement du WSDL : binding SOAP, exemples avancees et generation de code.</p>
      <embed src="/cours-pdf/S9/SOA/2-2-Standards-WSDL-2BIS.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-2-Standards-WSDL-2BIS.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Standards SOAP</h4>
      <p>Protocole SOAP : structure des messages (Envelope, Header, Body), encodage et transport HTTP.</p>
      <embed src="/cours-pdf/S9/SOA/2-3-StandardsSOAP.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-3-StandardsSOAP.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Introduction a REST</h4>
      <p>Architecture RESTful : principes, methodes HTTP, ressources et representations.</p>
      <embed src="/cours-pdf/S9/SOA/2-1-Intro-Rest.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-1-Intro-Rest.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>REST - Formats de Donnees</h4>
      <p>Formats de serialisation pour les API REST : JSON, XML, YAML et leurs cas d'usage.</p>
      <embed src="/cours-pdf/S9/SOA/2-2-Rest-Data-Format.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-2-Rest-Data-Format.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>REST - Richardson Maturity Model</h4>
      <p>Modele de maturite de Richardson : les 4 niveaux de maturite REST, de RPC sur HTTP a HATEOAS.</p>
      <embed src="/cours-pdf/S9/SOA/2-3-Rest-RMM.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-3-Rest-RMM.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Microservices - Introduction</h4>
      <p>Introduction aux microservices : definition, comparaison avec monolithique, avantages et defis.</p>
      <embed src="/cours-pdf/S9/SOA/4-1-Microservices.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/4-1-Microservices.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Microservices - Proprietes</h4>
      <p>Proprietes des microservices : independance, scalabilite, resilience et deploiement continu.</p>
      <embed src="/cours-pdf/S9/SOA/4-2-Microservices-Properties.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/4-2-Microservices-Properties.pdf" target="_blank">Telecharger</a></p>
    </div>
    <div class="pdf-item">
      <h4>Microservices - Architecture</h4>
      <p>Patterns architecturaux des microservices : API Gateway, service discovery, decomposition et communication.</p>
      <embed src="/cours-pdf/S9/SOA/4-3-Microservices-Archi.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/4-3-Microservices-Archi.pdf" target="_blank">Telecharger</a></p>
    </div>
  </div>
</div>

<hr>

<h2>Rapports et Projets</h2>

<div style="text-align: center;">
    <h3>Rapport de Projet - Architecture de Services</h3>
</div>

<div style="display: flex; justify-content: center;">
    <iframe src="/file/reports/S9/Bigot_Chanfreau_Service_Architecture_Rapport.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Bigot_Chanfreau_Service_Architecture_Rapport.pdf" target="_blank">Ouvrir le Rapport Complet</a>
</p>

<div style="text-align: center;">
    <h3>Rapport de TP</h3>
</div>

<div style="display: flex; justify-content: center;">
    <iframe src="/img/BE_Service_Archi/Bigot_Chanfreau_Service_Architecture_Rapport_TP.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_Service_Archi/Bigot_Chanfreau_Service_Architecture_Rapport_TP.pdf" target="_blank">Ouvrir le Rapport de TP</a>
</p>

<p style="text-align: center;">
    <a href="/img/BE_Service_Archi/Lab_Subject_service.pdf" target="_blank">Ouvrir le Sujet de TP</a>
</p>

<hr>
<p><em>Cours suivi en 2024-2025 a l'INSA Toulouse, Departement Genie Electrique et Informatique, specialite ISS.</em></p>

</div>

<div class="lang-en">

<h1>Service Oriented Architecture - Semester 9</h1>

<p><strong>Academic Year</strong>: 2024-2025<br>
<strong>Semester</strong>: 9 (S9)<br>
<strong>Instructor</strong>: N. Guermouche<br>
<strong>Category</strong>: Software Architectures / Web Services</p>

<hr>

<h2>PART A: GENERAL PRESENTATION</h2>

<h3 class="section-title">Presentation</h3>

<p>The Service Oriented Architecture (SOA) course provided an in-depth immersion into the principles and practices of designing and implementing service-oriented systems. Taught by N. Guermouche, this course covered both traditional and modern service architectures, focusing on building scalable, maintainable and high-performance systems.</p>

<p>The curriculum was organized around three main areas:</p>
<ul>
<li><strong>Traditional web services (SOAP/WSDL)</strong>: understanding the historical foundations of SOA, standardized exchange protocols and formal service description.</li>
<li><strong>RESTful services</strong>: mastering the modern approach based on HTTP resources, lightweight data formats (JSON, XML, YAML) and the Richardson Maturity Model (RMM).</li>
<li><strong>Microservices</strong>: understanding the decomposition of monolithic applications into autonomous services, independently deployable and scalable, with Spring Boot as the reference framework.</li>
</ul>

<h3 class="section-title">Target skills</h3>

<ul>
<li>Understand the fundamental principles of service-oriented architectures</li>
<li>Design and implement SOAP and REST web services</li>
<li>Master service description with WSDL</li>
<li>Develop RESTful APIs following best practices</li>
<li>Architect applications as microservices</li>
<li>Use Maven for Java project management</li>
<li>Apply unit testing with JUnit</li>
<li>Collaborate with Git in a development workflow</li>
</ul>

<hr>

<h2>PART B: EXPERIENCE AND CONTEXT</h2>

<h3 class="section-title">Experience details</h3>

<h4>Environment and Context</h4>

<p>This course proved particularly useful in a context where industrial demand for distributed systems and service architectures continues to grow. The software industry is massively migrating from monolithic architectures to microservices architectures, making these skills essential for any computer engineering professional.</p>

<p>The lab sessions allowed me to apply the concepts learned in lectures to concrete scenarios, which was beneficial for understanding the different architectural methodologies. The course was structured progressively: from SOA/SOAP fundamentals to REST, then to microservices, with each step building on the previous one.</p>

<h4>My Role</h4>

<p>As part of this course, I was responsible for:</p>
<ul>
<li>Understanding the principles of service-oriented architectures (loose coupling, service contracts, abstraction)</li>
<li>Designing and implementing service-oriented systems with SOAP and REST</li>
<li>Developing a complete microservices project with Spring Boot</li>
<li>Writing a WSDL report and service modeling exercises</li>
<li>Conducting experiments to test the efficiency and scalability of different architectures</li>
<li>Collaborating in a pair (with T. Bigot) on the final microservices project</li>
</ul>

<hr>

<h2>PART C: TECHNICAL ASPECTS</h2>

<p>This section explores in detail the technical aspects of the Service Oriented Architecture course, acquired mainly during lab sessions covering SOAP, REST and microservices.</p>

<h3 class="section-title">Technical Concepts</h3>

<h4>1. Fundamental principles of SOA</h4>

<p>Service Oriented Architecture is based on several fundamental principles:</p>

<p><strong>Loose Coupling</strong>:
Services are designed to minimize dependencies between them. Each service can evolve independently without impacting the others. This promotes maintainability and flexibility of the overall system.</p>

<p><strong>Service contracts</strong>:
Each service exposes a formal contract (WSDL for SOAP, OpenAPI/Swagger for REST) describing its operations, data types and communication protocols. This contract serves as an interface between the service provider and consumer.</p>

<p><strong>Abstraction</strong>:
Implementation details are hidden behind the service interface. The consumer does not need to know the internal logic, the database or the programming language used.</p>

<p><strong>Reusability</strong>:
Services are designed to be reused in different contexts and applications. A user management service can be used by several different applications.</p>

<p><strong>Service discovery</strong>:
Services can be discovered dynamically via a registry (UDDI for SOAP, service registry for microservices), enabling flexible composition.</p>

<h4>2. WSDL - Web Services Description Language</h4>

<p>WSDL is an XML language used to describe SOAP web services. It defines four main elements:</p>

<ul>
<li><strong>Types</strong>: the data types used by the service (XSD schemas)</li>
<li><strong>Messages</strong>: the messages exchanged (input/output)</li>
<li><strong>PortType</strong>: the available operations (the service interface)</li>
<li><strong>Binding</strong>: the transport protocol and encoding format</li>
</ul>

<p>Here is an example of a WSDL file that I studied and produced in lab sessions, describing a book search service:</p>

<pre><code class="language-xml">&lt;wsdl:definitions xmlns:tns="http://www.example.org/BookService/"
                  xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
                  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                  xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
                  name="BookService"
                  targetNamespace="http://www.example.org/BookService/"&gt;

    &lt;wsdl:types&gt;
        &lt;xsd:schema targetNamespace="http://www.example.org/BookService/"&gt;
            &lt;xsd:complexType name="BookType"&gt;
                &lt;xsd:sequence&gt;
                    &lt;xsd:element name="title" type="xsd:string"/&gt;
                    &lt;xsd:element name="author" type="xsd:int"/&gt;
                    &lt;xsd:element name="isbn" type="xsd:string"/&gt;
                &lt;/xsd:sequence&gt;
            &lt;/xsd:complexType&gt;
            &lt;xsd:element name="book" type="tns:BookType"/&gt;
        &lt;/xsd:schema&gt;
    &lt;/wsdl:types&gt;

    &lt;wsdl:message name="searchbookIn"&gt;
        &lt;wsdl:part name="title" type="xsd:string"/&gt;
    &lt;/wsdl:message&gt;
    &lt;wsdl:message name="searchbookOut"&gt;
        &lt;wsdl:part name="book" element="tns:book"/&gt;
    &lt;/wsdl:message&gt;

    &lt;wsdl:portType name="Port1"&gt;
        &lt;wsdl:operation name="searchBook"&gt;
            &lt;wsdl:input message="tns:searchbookIn"/&gt;
            &lt;wsdl:output message="tns:searchbookOut"/&gt;
        &lt;/wsdl:operation&gt;
    &lt;/wsdl:portType&gt;

    &lt;wsdl:binding name="BookWSPortBinding" type="tns:Port1"&gt;
        &lt;soap:binding style="document"
                      transport="http://schemas.xmlsoap.org/soap/http"/&gt;
        &lt;wsdl:operation name="searchBook"&gt;
            &lt;wsdl:input&gt;&lt;soap:body use="literal"/&gt;&lt;/wsdl:input&gt;
            &lt;wsdl:output&gt;&lt;soap:body use="literal"/&gt;&lt;/wsdl:output&gt;
        &lt;/wsdl:operation&gt;
    &lt;/wsdl:binding&gt;

    &lt;wsdl:service name="UnivWS"&gt;
        &lt;wsdl:port name="UnivWSPort" binding="tns:BookWSPortBinding"&gt;
            &lt;soap:address location="http://localhost:8080/UnivWSApplication/UnivWS"/&gt;
        &lt;/wsdl:port&gt;
    &lt;/wsdl:service&gt;
&lt;/wsdl:definitions&gt;
</code></pre>

<p>I also developed Java classes corresponding to the WSDL types, such as modeling a course management system:</p>

<pre><code class="language-java">public class CoursType {
    private String intitule;
    private int ects;
    private String nomResponsable;

    public CoursType(String intitule, int ects, String nomResponsable) {
        this.intitule = intitule;
        this.ects = ects;
        this.nomResponsable = nomResponsable;
    }
    // getters et setters
}
</code></pre>

<h4>3. SOAP Protocol</h4>

<p>The SOAP (Simple Object Access Protocol) protocol is a structured message exchange protocol for web services. It uses XML for message formatting and relies on application layer protocols such as HTTP or SMTP for transmission.</p>

<p>The structure of a SOAP message comprises three parts:</p>
<ul>
<li><strong>Envelope</strong>: the root element that encapsulates the entire message</li>
<li><strong>Header</strong> (optional): contains metadata (authentication, routing, etc.)</li>
<li><strong>Body</strong>: contains the message content (request or response)</li>
</ul>

<p><strong>SOAP Request</strong>: The request envelope contains the SOAP message sent to the web service. For example, if the searched string is "cedric", the SOAP envelope looks like this:</p>

<pre><code class="language-xml">&lt;soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:web="http://example.com/webservice"&gt;
    &lt;soapenv:Header/&gt;
    &lt;soapenv:Body&gt;
        &lt;web:MyRequest&gt;
            &lt;web:chain&gt;cedric&lt;/web:chain&gt;
        &lt;/web:MyRequest&gt;
    &lt;/soapenv:Body&gt;
&lt;/soapenv:Envelope&gt;
</code></pre>

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_MOOC/SOAP_send.png" alt="Sending a SOAP request" style="width: 70%; border: 1px solid #ddd; border-radius: 5px; padding: 5px;"/>
</div>
<p style="text-align: center; font-style: italic;">Sending a SOAP request from a client</p>
<br>

<p><strong>SOAP Response</strong>: The response is returned by the web service after processing the request. For example, if the response returns 6 (string length):</p>

<pre><code class="language-xml">&lt;soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:tns="http://www.example.org/BookService/"&gt;
    &lt;soapenv:Header/&gt;
    &lt;soapenv:Body&gt;
        &lt;tns:searchBookResponse&gt;
            &lt;tns:book&gt;
                &lt;tns:title&gt;Les Miserables&lt;/tns:title&gt;
                &lt;tns:author&gt;123&lt;/tns:author&gt;
                &lt;tns:isbn&gt;13.978-2211215350&lt;/tns:isbn&gt;
            &lt;/tns:book&gt;
        &lt;/tns:searchBookResponse&gt;
    &lt;/soapenv:Body&gt;
&lt;/soapenv:Envelope&gt;
</code></pre>

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_MOOC/SOAP_receive.png" alt="Receiving a SOAP response" style="width: 70%; border: 1px solid #ddd; border-radius: 5px; padding: 5px;"/>
</div>
<p style="text-align: center; font-style: italic;">Receiving a SOAP response</p>
<br>

<p>The SOA tutorials allowed us to practice two approaches:</p>
<ul>
<li><strong>Bottom-Up (Code First)</strong>: the Java code is written first, then the WSDL is generated automatically with Apache CXF</li>
<li><strong>Top-Down (Contract First)</strong>: the WSDL is written first, then the Java stubs are generated with the cxf-codegen plugin</li>
</ul>

<h4>4. RESTful Services</h4>

<p>REST (Representational State Transfer) is an architectural style that uses standard HTTP methods to interact with resources. Unlike SOAP, REST is stateless, lighter and relies on Web standards.</p>

<p><strong>HTTP Methods</strong>:</p>

<table>
<tr><th>Method</th><th>Action</th><th>Example</th><th>Description</th></tr>
<tr><td><strong>GET</strong></td><td>Read</td><td><code>GET /users/1</code></td><td>Retrieves the user with ID 1</td></tr>
<tr><td><strong>POST</strong></td><td>Create</td><td><code>POST /users</code></td><td>Creates a new user</td></tr>
<tr><td><strong>PUT</strong></td><td>Full update</td><td><code>PUT /users/1</code></td><td>Replaces user 1</td></tr>
<tr><td><strong>PATCH</strong></td><td>Partial update</td><td><code>PATCH /users/1</code></td><td>Partially modifies user 1</td></tr>
<tr><td><strong>DELETE</strong></td><td>Delete</td><td><code>DELETE /users/1</code></td><td>Deletes user 1</td></tr>
</table>

<p><strong>HTTP Status Codes</strong>:</p>

<table>
<tr><th>Code</th><th>Meaning</th></tr>
<tr><td>200</td><td>OK - Successful request</td></tr>
<tr><td>201</td><td>Created - Resource created</td></tr>
<tr><td>204</td><td>No Content - Success with no return content</td></tr>
<tr><td>400</td><td>Bad Request - Invalid request</td></tr>
<tr><td>401</td><td>Unauthorized - Authentication required</td></tr>
<tr><td>403</td><td>Forbidden - Access denied</td></tr>
<tr><td>404</td><td>Not Found - Resource not found</td></tr>
<tr><td>500</td><td>Internal Server Error - Server error</td></tr>
</table>

<p><strong>HATEOAS (Hypermedia As The Engine Of Application State)</strong>:
HATEOAS is a REST principle where responses contain hypertext links to available actions. This allows the client to dynamically navigate the API without knowing the URLs in advance. For example, a response for a user could include links to their orders, profile, etc.</p>

<p><strong>Richardson Maturity Model (RMM)</strong>:
The RMM defines four maturity levels for REST APIs:</p>

<ul>
<li><strong>Level 0</strong>: A single entry point (RPC-style over HTTP). All requests go through a single URL.</li>
<li><strong>Level 1</strong>: Introduction of resources. Each resource has its own URI (e.g., <code>/users</code>, <code>/orders</code>).</li>
<li><strong>Level 2</strong>: Correct use of HTTP verbs (GET, POST, PUT, DELETE) and status codes.</li>
<li><strong>Level 3</strong>: HATEOAS. Responses contain hypertext links to guide the client. This is the most mature level.</li>
</ul>

<p>I developed RESTful services for order management using JAX-RS and JSON for data exchange:</p>

<pre><code class="language-java">public class OrderService {
    private static List&lt;Order&gt; orders = new ArrayList&lt;&gt;();
    private static int idCounter = 1;

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public List&lt;Order&gt; getAllOrders() {
        return orders;
    }

    @GET
    @Path("/{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public Order getOrder(@PathParam("id") int id) {
        return orders.stream()
            .filter(order -&gt; order.getId() == id)
            .findFirst().orElse(null);
    }

    @POST
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Order createOrder(Order order) {
        order.setId(idCounter++);
        orders.add(order);
        return order;
    }

    @PUT
    @Path("/{id}")
    @Consumes(MediaType.APPLICATION_JSON)
    @Produces(MediaType.APPLICATION_JSON)
    public Order updateOrder(@PathParam("id") int id, Order updatedOrder) {
        for (Order order : orders) {
            if (order.getId() == id) {
                order.setProduct(updatedOrder.getProduct());
                order.setQuantity(updatedOrder.getQuantity());
                return order;
            }
        }
        return null;
    }

    @DELETE
    @Path("/{id}")
    public void deleteOrder(@PathParam("id") int id) {
        orders.removeIf(order -&gt; order.getId() == id);
    }
}
</code></pre>

<p>I also developed a REST controller with Spring Boot for user management:</p>

<pre><code class="language-java">@RestController
@RequestMapping("/api/users")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping
    public List&lt;User&gt; getAllUsers() {
        return userService.getAllUsers();
    }

    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        return userService.getUserById(id);
    }

    @PostMapping
    public User createUser(@RequestBody User user) {
        return userService.createUser(user);
    }

    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User userDetails) {
        return userService.updateUser(id, userDetails);
    }

    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
    }
}
</code></pre>

<p>Testing tools such as Postman were used to validate endpoints, verify HTTP status codes and inspect JSON request/response bodies.</p>

<h4>5. Data formats: JSON, XML and YAML</h4>

<p>Web services use different serialization formats for data exchange:</p>

<p><strong>JSON (JavaScript Object Notation)</strong>: lightweight, readable format widely adopted for REST APIs.</p>

<pre><code class="language-json">{
    "id": 1,
    "product": "Laptop",
    "quantity": 3
}
</code></pre>

<p><strong>XML (eXtensible Markup Language)</strong>: historical format used by SOAP, more verbose but with a strong validation schema (XSD).</p>

<pre><code class="language-xml">&lt;order&gt;
    &lt;id&gt;1&lt;/id&gt;
    &lt;product&gt;Laptop&lt;/product&gt;
    &lt;quantity&gt;3&lt;/quantity&gt;
&lt;/order&gt;
</code></pre>

<p><strong>YAML (YAML Ain't Markup Language)</strong>: readable format often used for configuration (Spring Boot <code>application.yml</code> files, Docker Compose, etc.).</p>

<pre><code class="language-yaml">order:
  id: 1
  product: Laptop
  quantity: 3
</code></pre>

<h4>6. Microservices Architecture</h4>

<p>Microservices represent an architectural style that structures an application as a set of loosely coupled services, each independently deployable and scalable.</p>

<p><strong>Decomposition patterns</strong>:</p>
<ul>
<li><strong>Decomposition by business domain</strong>: each microservice corresponds to a functional domain (users, orders, feedback, etc.)</li>
<li><strong>Decomposition by subdomain</strong>: DDD (Domain-Driven Design) approach to delineate bounded contexts</li>
</ul>

<p><strong>Service Discovery</strong>:
In a microservices architecture, services must be able to find each other. Tools like Eureka (Netflix) or Consul (HashiCorp) enable dynamic service registration and discovery.</p>

<p><strong>API Gateway</strong>:
A single entry point that routes requests to the appropriate microservices. The API Gateway also handles cross-cutting concerns such as authentication, rate limiting and load balancing.</p>

<p>As part of the project, I used Spring Boot to create several independent microservices:</p>
<ul>
<li><strong>userManagement</strong>: user management (CRUD, profiles)</li>
<li><strong>volunteerManagement</strong>: volunteer management</li>
<li><strong>volunteerService</strong>: volunteer business logic</li>
<li><strong>userRequestService</strong>: user request management</li>
<li><strong>feedbackService</strong>: feedback and evaluation management</li>
<li><strong>AnalyseProject</strong>: global analysis service</li>
</ul>

<p>Each microservice has its own <code>pom.xml</code> file, its own database and can be deployed independently. Communication between services is done via REST HTTP calls.</p>

<h4>7. Project management with Maven</h4>

<p>Maven is the project management and build tool used throughout the course. The <code>pom.xml</code> file centralizes:</p>
<ul>
<li>Project dependencies (Spring Boot, CXF, JAX-RS, etc.)</li>
<li>Build plugins (compilation, testing, packaging)</li>
<li>Project configuration (Java version, encoding, etc.)</li>
</ul>

<p>Example of Maven configuration for a Spring Boot microservice:</p>

<pre><code class="language-xml">&lt;dependencies&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-web&lt;/artifactId&gt;
    &lt;/dependency&gt;
    &lt;dependency&gt;
        &lt;groupId&gt;org.springframework.boot&lt;/groupId&gt;
        &lt;artifactId&gt;spring-boot-starter-test&lt;/artifactId&gt;
        &lt;scope&gt;test&lt;/scope&gt;
    &lt;/dependency&gt;
&lt;/dependencies&gt;
</code></pre>

<h4>8. Git Workflow</h4>

<p>The microservices project was managed with Git for version control. The collaborative workflow included:</p>
<ul>
<li><strong>Branching</strong>: one branch per feature or microservice</li>
<li><strong>Commits</strong>: atomic commits with descriptive messages</li>
<li><strong>Merge</strong>: integration of branches into the main branch</li>
<li><strong>Remote</strong>: synchronization with a remote repository (GitLab INSA)</li>
</ul>

<h4>9. Unit testing with JUnit</h4>

<p>Unit tests with JUnit were used to validate the correct functioning of each component individually. Tests cover services, controllers and business logic:</p>

<pre><code class="language-java">@Test
public void testCreateUser() {
    User user = new User("Cedric", "cedric@insa.fr");
    User created = userService.createUser(user);
    assertNotNull(created.getId());
    assertEquals("Cedric", created.getName());
}

@Test
public void testGetAllOrders() {
    List&lt;Order&gt; orders = orderService.getAllOrders();
    assertNotNull(orders);
}
</code></pre>

<h4>10. Spring Boot Framework</h4>

<p>Spring Boot was the main framework for microservices development. Its key advantages:</p>
<ul>
<li><strong>Auto-configuration</strong>: automatic configuration based on present dependencies</li>
<li><strong>Embedded server</strong>: built-in Tomcat, no need for external deployment</li>
<li><strong>Starters</strong>: pre-configured dependency packages (spring-boot-starter-web, etc.)</li>
<li><strong>Actuator</strong>: application monitoring and metrics</li>
<li><strong>Profiles</strong>: management of multiple configurations (dev, test, prod)</li>
</ul>

<hr>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3 class="section-title">Knowledge and Skills Mobilized</h3>

<ul>
<li>Understanding of concepts and characteristics of service-oriented architectures</li>
<li>Development of distributed architectures using web services</li>
<li>Deployment and configuration of SOA with SOAP and REST</li>
<li>Design, development and deployment of microservices architectures</li>
<li>Mastery of the Java language and the Spring Boot framework</li>
<li>Project management with Maven and Git</li>
<li>Unit testing with JUnit</li>
<li>Understanding of data formats (JSON, XML, YAML)</li>
<li>Knowledge of REST maturity levels (RMM) and HATEOAS</li>
</ul>

<h3 class="section-title">Self-assessment</h3>

<p>Using all the new concepts learned during the course was a bit complex at first, but fortunately the tutorials were well structured, allowing me to learn step by step. Moreover, there were a large number of practical sessions to practice and understand all the concepts. Not being accustomed to Java, I had to relearn the basics of this language, which represented an additional challenge.</p>

<p>I did not participate much in the SOAP lab sessions as I wanted to focus more on REST and microservices due to time constraints. Nevertheless, the WSDL modeling exercises were very instructive for understanding the formal structure of service contracts.</p>

<p>The microservices project was the most enriching element of the course. Designing a complete architecture with several independent services, managing inter-service communications and deploying everything gave me a concrete vision of what developing distributed applications in production entails.</p>

<p>The pedagogical progression of the course -- from SOA fundamentals to SOAP, then REST, then microservices -- was logical and well constructed. Each technology introduced concepts that prepared for the next one.</p>

<h3 class="section-title">My Opinion</h3>

<p>Before taking this course, I had only heard of certain concepts related to service-oriented architecture. Thanks to the lab sessions, I now have a much better understanding of web application architecture and how to interact with them. For example, simply by observing a website's network traffic and understanding all the requests in the background.</p>

<p>Furthermore, developing in Java during the course reminded me how to code in this language, which is important as it is widely used in the industry. Even though I would prefer to code in C for my professional future, I can now apply for Java positions if needed.</p>

<p>The comparison between SOAP and REST allowed me to understand why the industry is migrating toward REST: simplicity, performance and better integration with modern architectures. However, SOAP remains relevant in contexts where security and transactional reliability are critical (banking sector, healthcare).</p>

<p>Learning microservices was an opening to modern DevOps practices. Decomposition into independent services facilitates continuous deployment, horizontal scaling and system resilience. These are highly sought-after skills in the job market.</p>

<hr>

<h2>Course Documents</h2>

<div class="pdf-container">
  <div class="pdf-viewer">
    <div class="pdf-item">
      <h4>Introduction to SOA</h4>
      <p>Introductory course on the fundamental principles of Service Oriented Architecture: loose coupling, service contracts, abstraction and reusability.</p>
      <embed src="/cours-pdf/S9/SOA/2-1-Intro-SOA.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-1-Intro-SOA.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>WSDL Standards (Part 1)</h4>
      <p>Web Services Description Language: WSDL structure, types, messages, portType and binding.</p>
      <embed src="/cours-pdf/S9/SOA/2-2-Standards-WSDL-1_.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-2-Standards-WSDL-1_.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>WSDL Standards (Part 2)</h4>
      <p>Advanced WSDL: SOAP binding, advanced examples and code generation.</p>
      <embed src="/cours-pdf/S9/SOA/2-2-Standards-WSDL-2BIS.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-2-Standards-WSDL-2BIS.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>SOAP Standards</h4>
      <p>SOAP protocol: message structure (Envelope, Header, Body), encoding and HTTP transport.</p>
      <embed src="/cours-pdf/S9/SOA/2-3-StandardsSOAP.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-3-StandardsSOAP.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Introduction to REST</h4>
      <p>RESTful architecture: principles, HTTP methods, resources and representations.</p>
      <embed src="/cours-pdf/S9/SOA/2-1-Intro-Rest.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-1-Intro-Rest.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>REST - Data Formats</h4>
      <p>Serialization formats for REST APIs: JSON, XML, YAML and their use cases.</p>
      <embed src="/cours-pdf/S9/SOA/2-2-Rest-Data-Format.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-2-Rest-Data-Format.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>REST - Richardson Maturity Model</h4>
      <p>Richardson Maturity Model: the 4 REST maturity levels, from RPC over HTTP to HATEOAS.</p>
      <embed src="/cours-pdf/S9/SOA/2-3-Rest-RMM.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-3-Rest-RMM.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Microservices - Introduction</h4>
      <p>Introduction to microservices: definition, comparison with monolithic, advantages and challenges.</p>
      <embed src="/cours-pdf/S9/SOA/4-1-Microservices.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/4-1-Microservices.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Microservices - Properties</h4>
      <p>Microservices properties: independence, scalability, resilience and continuous deployment.</p>
      <embed src="/cours-pdf/S9/SOA/4-2-Microservices-Properties.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/4-2-Microservices-Properties.pdf" target="_blank">Download</a></p>
    </div>
    <div class="pdf-item">
      <h4>Microservices - Architecture</h4>
      <p>Microservices architectural patterns: API Gateway, service discovery, decomposition and communication.</p>
      <embed src="/cours-pdf/S9/SOA/4-3-Microservices-Archi.pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/4-3-Microservices-Archi.pdf" target="_blank">Download</a></p>
    </div>
  </div>
</div>

<hr>

<h2>Reports and Projects</h2>

<div style="text-align: center;">
    <h3>Project Report - Service Architecture</h3>
</div>

<div style="display: flex; justify-content: center;">
    <iframe src="/file/reports/S9/Bigot_Chanfreau_Service_Architecture_Rapport.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Bigot_Chanfreau_Service_Architecture_Rapport.pdf" target="_blank">Open the Full Report</a>
</p>

<div style="text-align: center;">
    <h3>Lab Report</h3>
</div>

<div style="display: flex; justify-content: center;">
    <iframe src="/img/BE_Service_Archi/Bigot_Chanfreau_Service_Architecture_Rapport_TP.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_Service_Archi/Bigot_Chanfreau_Service_Architecture_Rapport_TP.pdf" target="_blank">Open the Lab Report</a>
</p>

<p style="text-align: center;">
    <a href="/img/BE_Service_Archi/Lab_Subject_service.pdf" target="_blank">Open the Lab Subject</a>
</p>

<hr>

<p><em>Course taken in 2024-2025 at INSA Toulouse, Department of Electrical and Computer Engineering, ISS specialization.</em></p>

</div>

<div class="back-nav">
  <a href="./my-courses-2024-2025.html" data-i18n-html="back-courses-2024-2025">&larr; Retour a Mes Cours 2024-2025</a>
</div>
