---
layout: default
title:  "Service Oriented Architecture"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
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
  <a href="./my-courses-2024-2025.html">← Retour a Mes Cours 2024-2025</a>
</div>

# Service Oriented Architecture

**Annee Academique**: 2024-2025
**Semestre**: 9 (S9)
**Enseignant**: N. Guermouche
**Categorie**: Architectures Logicielles / Services Web

---

## PART A: PRESENTATION GENERALE
{: .section-title}

### Presentation

Le cours d'Architecture Orientee Services (SOA) a constitue une immersion approfondie dans les principes et les pratiques de conception et d'implementation de systemes orientes services. Enseigne par N. Guermouche, ce cours a couvert les architectures de services traditionnelles et modernes, en se concentrant sur la creation de systemes scalables, maintenables et performants.

Le programme s'articulait autour de trois grands axes :
- **Les services web traditionnels (SOAP/WSDL)** : comprendre les fondements historiques de la SOA, les protocoles d'echange standardises et la description formelle des services.
- **Les services RESTful** : maitriser l'approche moderne basee sur les ressources HTTP, les formats de donnees legers (JSON, XML, YAML) et le modele de maturite de Richardson (RMM).
- **Les microservices** : apprehender la decomposition d'applications monolithiques en services autonomes, independamment deployables et scalables, avec Spring Boot comme framework de reference.

### Competences visees

- Comprendre les principes fondamentaux des architectures orientees services
- Concevoir et implementer des services web SOAP et REST
- Maitriser la description de services avec WSDL
- Developper des API RESTful conformes aux bonnes pratiques
- Architecturer des applications en microservices
- Utiliser Maven pour la gestion de projets Java
- Appliquer les tests unitaires avec JUnit
- Collaborer avec Git dans un workflow de developpement

---

## PART B: EXPERIENCE ET CONTEXTE
{: .section-title}

### Details de l'experience

#### Environnement et Contexte

Ce cours s'est revele particulierement utile dans un contexte ou la demande industrielle pour des systemes distribues et des architectures de services ne cesse de croitre. L'industrie du logiciel migre massivement des architectures monolithiques vers des architectures en microservices, rendant ces competences essentielles pour tout ingenieur en informatique.

Les seances de travaux pratiques m'ont permis d'appliquer les concepts appris en cours a des scenarios concrets, ce qui a ete benefique pour comprendre les differentes methodologies architecturales. Le cours etait structure en progression : des fondamentaux SOA/SOAP vers REST, puis vers les microservices, chaque etape construisant sur la precedente.

#### Ma Fonction

Dans le cadre de ce cours, j'ai ete responsable de :
- Comprendre les principes des architectures orientees services (couplage lache, contrats de service, abstraction)
- Concevoir et implementer des systemes orientes services avec SOAP et REST
- Developper un projet complet en microservices avec Spring Boot
- Rediger un rapport WSDL et des exercices de modelisation de services
- Mener des experimentations pour tester l'efficacite et la scalabilite des differentes architectures
- Collaborer en binome (avec T. Bigot) sur le projet final de microservices

---

## PART C: ASPECTS TECHNIQUES
{: .section-title}

Cette section explore en detail les aspects techniques du cours d'Architecture Orientee Services, acquis principalement lors des travaux pratiques portant sur SOAP, REST et les microservices.

### Concepts Techniques

#### 1. Principes fondamentaux de la SOA

L'Architecture Orientee Services repose sur plusieurs principes fondamentaux :

**Couplage lache (Loose Coupling)** :
Les services sont conçus pour minimiser les dependances entre eux. Chaque service peut evoluer independamment sans impacter les autres. Cela favorise la maintenabilite et la flexibilite du systeme global.

**Contrats de service** :
Chaque service expose un contrat formel (WSDL pour SOAP, OpenAPI/Swagger pour REST) decrivant ses operations, ses types de donnees et ses protocoles de communication. Ce contrat sert d'interface entre le fournisseur et le consommateur du service.

**Abstraction** :
Les details d'implementation sont caches derriere l'interface du service. Le consommateur n'a pas besoin de connaitre la logique interne, la base de donnees ou le langage de programmation utilise.

**Reutilisabilite** :
Les services sont conçus pour etre reutilises dans differents contextes et applications. Un service de gestion d'utilisateurs peut etre utilise par plusieurs applications differentes.

**Decouverte de services** :
Les services peuvent etre decouverts dynamiquement via un registre (UDDI pour SOAP, service registry pour microservices), permettant une composition flexible.

#### 2. WSDL - Web Services Description Language

Le WSDL est un langage XML utilise pour decrire les services web SOAP. Il definit quatre elements principaux :

- **Types** : les types de donnees utilises par le service (schemas XSD)
- **Messages** : les messages echanges (entree/sortie)
- **PortType** : les operations disponibles (l'interface du service)
- **Binding** : le protocole de transport et le format d'encodage

Voici un exemple de fichier WSDL que j'ai etudie et produit en TP, decrivant un service de recherche de livres :

```xml
<wsdl:definitions xmlns:tns="http://www.example.org/BookService/"
                  xmlns:wsdl="http://schemas.xmlsoap.org/wsdl/"
                  xmlns:xsd="http://www.w3.org/2001/XMLSchema"
                  xmlns:soap="http://schemas.xmlsoap.org/wsdl/soap/"
                  name="BookService"
                  targetNamespace="http://www.example.org/BookService/">

    <wsdl:types>
        <xsd:schema targetNamespace="http://www.example.org/BookService/">
            <xsd:complexType name="BookType">
                <xsd:sequence>
                    <xsd:element name="title" type="xsd:string"/>
                    <xsd:element name="author" type="xsd:int"/>
                    <xsd:element name="isbn" type="xsd:string"/>
                </xsd:sequence>
            </xsd:complexType>
            <xsd:element name="book" type="tns:BookType"/>
        </xsd:schema>
    </wsdl:types>

    <wsdl:message name="searchbookIn">
        <wsdl:part name="title" type="xsd:string"/>
    </wsdl:message>
    <wsdl:message name="searchbookOut">
        <wsdl:part name="book" element="tns:book"/>
    </wsdl:message>

    <wsdl:portType name="Port1">
        <wsdl:operation name="searchBook">
            <wsdl:input message="tns:searchbookIn"/>
            <wsdl:output message="tns:searchbookOut"/>
        </wsdl:operation>
    </wsdl:portType>

    <wsdl:binding name="BookWSPortBinding" type="tns:Port1">
        <soap:binding style="document"
                      transport="http://schemas.xmlsoap.org/soap/http"/>
        <wsdl:operation name="searchBook">
            <wsdl:input><soap:body use="literal"/></wsdl:input>
            <wsdl:output><soap:body use="literal"/></wsdl:output>
        </wsdl:operation>
    </wsdl:binding>

    <wsdl:service name="UnivWS">
        <wsdl:port name="UnivWSPort" binding="tns:BookWSPortBinding">
            <soap:address location="http://localhost:8080/UnivWSApplication/UnivWS"/>
        </wsdl:port>
    </wsdl:service>
</wsdl:definitions>
```

J'ai egalement developpe des classes Java correspondant aux types WSDL, comme la modelisation d'un systeme de gestion de cours :

```java
public class CoursType {
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
```

#### 3. Protocole SOAP

Le protocole SOAP (Simple Object Access Protocol) est un protocole d'echange de messages structures pour les services web. Il utilise XML pour le formatage des messages et s'appuie sur des protocoles de la couche application tels que HTTP ou SMTP pour la transmission.

La structure d'un message SOAP comprend trois parties :
- **Envelope** : l'element racine qui encapsule l'ensemble du message
- **Header** (optionnel) : contient des metadonnees (authentification, routage, etc.)
- **Body** : contient le contenu du message (requete ou reponse)

**Requete SOAP** : L'enveloppe de requete contient le message SOAP envoye au service web. Par exemple, si la chaine recherchee est "cedric", l'enveloppe SOAP ressemble a ceci :

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:web="http://example.com/webservice">
    <soapenv:Header/>
    <soapenv:Body>
        <web:MyRequest>
            <web:chain>cedric</web:chain>
        </web:MyRequest>
    </soapenv:Body>
</soapenv:Envelope>
```

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_MOOC/SOAP_send.png" alt="Envoi d'une requete SOAP" style="width: 70%; border: 1px solid #ddd; border-radius: 5px; padding: 5px;"/>
</div>
<p style="text-align: center; font-style: italic;">Envoi d'une requete SOAP depuis un client</p>
<br>

**Reponse SOAP** : La reponse est retournee par le service web apres traitement de la requete. Par exemple, si la reponse retourne 6 (longueur de la chaine) :

```xml
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/"
                  xmlns:tns="http://www.example.org/BookService/">
    <soapenv:Header/>
    <soapenv:Body>
        <tns:searchBookResponse>
            <tns:book>
                <tns:title>Les Miserables</tns:title>
                <tns:author>123</tns:author>
                <tns:isbn>13.978-2211215350</tns:isbn>
            </tns:book>
        </tns:searchBookResponse>
    </soapenv:Body>
</soapenv:Envelope>
```

<div style="display: flex; justify-content: center;">
    <img src="/img/BE_MOOC/SOAP_receive.png" alt="Reception d'une reponse SOAP" style="width: 70%; border: 1px solid #ddd; border-radius: 5px; padding: 5px;"/>
</div>
<p style="text-align: center; font-style: italic;">Reception d'une reponse SOAP</p>
<br>

Les tutoriels SOA nous ont permis de pratiquer deux approches :
- **Bottom-Up (Code First)** : on ecrit d'abord le code Java, puis on genere le WSDL automatiquement avec Apache CXF
- **Top-Down (Contract First)** : on ecrit d'abord le WSDL, puis on genere les stubs Java avec le plugin cxf-codegen

#### 4. Services RESTful

REST (Representational State Transfer) est un style architectural qui utilise les methodes HTTP standard pour interagir avec des ressources. Contrairement a SOAP, REST est sans etat (stateless), plus leger et s'appuie sur les standards du Web.

**Methodes HTTP** :

| Methode | Action | Exemple | Description |
|---------|--------|---------|-------------|
| **GET** | Lecture | `GET /users/1` | Recupere l'utilisateur avec l'ID 1 |
| **POST** | Creation | `POST /users` | Cree un nouvel utilisateur |
| **PUT** | Mise a jour complete | `PUT /users/1` | Remplace l'utilisateur 1 |
| **PATCH** | Mise a jour partielle | `PATCH /users/1` | Modifie partiellement l'utilisateur 1 |
| **DELETE** | Suppression | `DELETE /users/1` | Supprime l'utilisateur 1 |

**Codes de statut HTTP** :

| Code | Signification |
|------|---------------|
| 200 | OK - Requete reussie |
| 201 | Created - Ressource creee |
| 204 | No Content - Succes sans contenu de retour |
| 400 | Bad Request - Requete invalide |
| 401 | Unauthorized - Authentification requise |
| 403 | Forbidden - Acces refuse |
| 404 | Not Found - Ressource non trouvee |
| 500 | Internal Server Error - Erreur serveur |

**HATEOAS (Hypermedia As The Engine Of Application State)** :
HATEOAS est un principe REST ou les reponses contiennent des liens hypertextes vers les actions disponibles. Cela permet au client de naviguer dynamiquement dans l'API sans connaitre a l'avance les URLs. Par exemple, une reponse pour un utilisateur pourrait inclure des liens vers ses commandes, son profil, etc.

**Modele de Maturite de Richardson (RMM)** :
Le RMM definit quatre niveaux de maturite pour les API REST :

- **Niveau 0** : Un seul point d'entree (type RPC sur HTTP). Toutes les requetes passent par une seule URL.
- **Niveau 1** : Introduction des ressources. Chaque ressource a sa propre URI (par exemple `/users`, `/orders`).
- **Niveau 2** : Utilisation correcte des verbes HTTP (GET, POST, PUT, DELETE) et des codes de statut.
- **Niveau 3** : HATEOAS. Les reponses contiennent des liens hypertextes pour guider le client. C'est le niveau le plus mature.

J'ai developpe des services RESTful pour la gestion de commandes en utilisant JAX-RS et JSON pour l'echange de donnees :

```java
public class OrderService {
    private static List<Order> orders = new ArrayList<>();
    private static int idCounter = 1;

    @GET
    @Produces(MediaType.APPLICATION_JSON)
    public List<Order> getAllOrders() {
        return orders;
    }

    @GET
    @Path("/{id}")
    @Produces(MediaType.APPLICATION_JSON)
    public Order getOrder(@PathParam("id") int id) {
        return orders.stream()
            .filter(order -> order.getId() == id)
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
        orders.removeIf(order -> order.getId() == id);
    }
}
```

J'ai egalement developpe un controleur REST avec Spring Boot pour la gestion d'utilisateurs :

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

    @Autowired
    private UserService userService;

    @GetMapping
    public List<User> getAllUsers() {
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
```

Les outils de test comme Postman ont ete utilises pour valider les endpoints, verifier les codes de statut HTTP et inspecter les corps de requete/reponse en JSON.

#### 5. Formats de donnees : JSON, XML et YAML

Les services web utilisent differents formats de serialisation pour l'echange de donnees :

**JSON (JavaScript Object Notation)** : format leger, lisible et largement adopte pour les API REST.
```json
{
    "id": 1,
    "product": "Laptop",
    "quantity": 3
}
```

**XML (eXtensible Markup Language)** : format historique utilise par SOAP, plus verbeux mais avec un schema de validation fort (XSD).
```xml
<order>
    <id>1</id>
    <product>Laptop</product>
    <quantity>3</quantity>
</order>
```

**YAML (YAML Ain't Markup Language)** : format lisible souvent utilise pour la configuration (fichiers Spring Boot `application.yml`, Docker Compose, etc.).
```yaml
order:
  id: 1
  product: Laptop
  quantity: 3
```

#### 6. Architecture Microservices

Les microservices representent un style architectural qui structure une application comme un ensemble de services faiblement couples, chacun deployable et scalable de maniere independante.

**Patterns de decomposition** :
- **Decomposition par domaine metier** : chaque microservice correspond a un domaine fonctionnel (utilisateurs, commandes, feedback, etc.)
- **Decomposition par sous-domaine** : approche DDD (Domain-Driven Design) pour delimiter les contextes bornes (bounded contexts)

**Decouverte de services (Service Discovery)** :
Dans une architecture microservices, les services doivent pouvoir se trouver mutuellement. Des outils comme Eureka (Netflix) ou Consul (HashiCorp) permettent l'enregistrement et la decouverte dynamique des services.

**API Gateway** :
Un point d'entree unique qui route les requetes vers les microservices appropries. L'API Gateway gere egalement des preoccupations transversales comme l'authentification, le rate limiting et le load balancing.

Dans le cadre du projet, j'ai utilise Spring Boot pour creer plusieurs microservices independants :
- **userManagement** : gestion des utilisateurs (CRUD, profils)
- **volunteerManagement** : gestion des benevoles
- **volunteerService** : logique metier des benevoles
- **userRequestService** : gestion des demandes utilisateurs
- **feedbackService** : gestion des retours et evaluations
- **AnalyseProject** : service d'analyse globale

Chaque microservice possede son propre fichier `pom.xml`, sa propre base de donnees et peut etre deploye independamment. La communication entre les services se fait via des appels REST HTTP.

#### 7. Gestion de projet avec Maven

Maven est l'outil de gestion de projet et de build utilise tout au long du cours. Le fichier `pom.xml` centralise :
- Les dependances du projet (Spring Boot, CXF, JAX-RS, etc.)
- Les plugins de build (compilation, tests, packaging)
- La configuration du projet (version Java, encoding, etc.)

Exemple de configuration Maven pour un microservice Spring Boot :
```xml
<dependencies>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-web</artifactId>
    </dependency>
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-test</artifactId>
        <scope>test</scope>
    </dependency>
</dependencies>
```

#### 8. Workflow Git

Le projet de microservices a ete gere avec Git pour le controle de version. Le workflow collaboratif incluait :
- **Branching** : une branche par fonctionnalite ou microservice
- **Commits** : des commits atomiques et messages descriptifs
- **Merge** : integration des branches dans la branche principale
- **Remote** : synchronisation avec un depot distant (GitLab INSA)

#### 9. Tests unitaires avec JUnit

Les tests unitaires avec JUnit ont permis de valider le bon fonctionnement de chaque composant individuellement. Les tests couvrent les services, les controleurs et la logique metier :

```java
@Test
public void testCreateUser() {
    User user = new User("Cedric", "cedric@insa.fr");
    User created = userService.createUser(user);
    assertNotNull(created.getId());
    assertEquals("Cedric", created.getName());
}

@Test
public void testGetAllOrders() {
    List<Order> orders = orderService.getAllOrders();
    assertNotNull(orders);
}
```

#### 10. Framework Spring Boot

Spring Boot a ete le framework principal pour le developpement des microservices. Ses avantages cles :
- **Auto-configuration** : configuration automatique basee sur les dependances presentes
- **Serveur embarque** : Tomcat integre, pas besoin de deploiement externe
- **Starters** : des packages de dependances pre-configures (spring-boot-starter-web, etc.)
- **Actuator** : monitoring et metriques de l'application
- **Profils** : gestion de configurations multiples (dev, test, prod)

---

## PART D: ANALYSE ET REFLEXION
{: .section-title}

### Connaissances et Competences Mobilisees

- Comprehension des concepts et caracteristiques des architectures orientees services
- Developpement d'architectures distribuees utilisant les services web
- Deploiement et configuration de SOA avec SOAP et REST
- Conception, developpement et deploiement d'architectures en microservices
- Maitrise du langage Java et du framework Spring Boot
- Gestion de projet avec Maven et Git
- Tests unitaires avec JUnit
- Comprehension des formats de donnees (JSON, XML, YAML)
- Connaissance des niveaux de maturite REST (RMM) et de HATEOAS

### Auto-evaluation

L'utilisation de tous les nouveaux concepts appris pendant le cours etait au debut un peu complexe, mais heureusement les tutoriels etaient bien structures, me permettant d'apprendre etape par etape. De plus, il y avait un grand nombre de seances pratiques pour s'exercer et comprendre tous les concepts. N'etant pas habitue a Java, j'ai du reapprendre les bases de ce langage, ce qui a represente un defi supplementaire.

Je n'ai pas beaucoup participe aux TP SOAP car je souhaitais me concentrer davantage sur REST et les microservices en raison de contraintes de temps. Neanmoins, les exercices de modelisation WSDL ont ete tres formateurs pour comprendre la structure formelle des contrats de service.

Le projet de microservices a ete l'element le plus enrichissant du cours. Concevoir une architecture complete avec plusieurs services independants, gerer les communications inter-services et deployer le tout m'a donne une vision concrete de ce qu'implique le developpement d'applications distribuees en production.

La progression pedagogique du cours -- des fondamentaux SOA vers SOAP, puis REST, puis les microservices -- etait logique et bien construite. Chaque technologie introduisait des concepts qui preparaient a la suivante.

### Mon Avis

Avant de suivre ce cours, je n'avais entendu parler que de certains concepts lies a l'architecture orientee services. Grace aux seances de travaux pratiques, j'ai maintenant une bien meilleure comprehension de l'architecture des applications web et de la maniere d'interagir avec elles. Par exemple, simplement en observant le reseau d'un site web et en comprenant toutes les requetes en arriere-plan.

De plus, developper en Java pendant le cours m'a rappele comment coder dans ce langage, ce qui est important car il est tres utilise dans l'industrie. Meme si je prefererais coder en C pour mon avenir professionnel, je peux desormais postuler a des postes Java si necessaire.

La comparaison entre SOAP et REST m'a permis de comprendre pourquoi l'industrie migre vers REST : simplicite, performance et meilleure integration avec les architectures modernes. Cependant, SOAP reste pertinent dans des contextes ou la securite et la fiabilite transactionnelle sont critiques (secteur bancaire, sante).

L'apprentissage des microservices a ete une ouverture vers les pratiques DevOps modernes. La decomposition en services independants facilite le deploiement continu, le scaling horizontal et la resilience des systemes. Ce sont des competences tres recherchees sur le marche du travail.

---

## Documents de Cours
{: .section-title}

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
      <embed src="/cours-pdf/S9/SOA/2-2-Standards-WSDL-1 .pdf" type="application/pdf" width="100%" height="800px" />
      <p><a href="/cours-pdf/S9/SOA/2-2-Standards-WSDL-1 .pdf" target="_blank">Telecharger</a></p>
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

---

## Rapports et Projets
{: .section-title}

### Rapport de Projet - Architecture de Services

<div style="display: flex; justify-content: center;">
    <iframe src="/file/reports/S9/Bigot_Chanfreau_Service_Architecture_Rapport.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/file/reports/S9/Bigot_Chanfreau_Service_Architecture_Rapport.pdf" target="_blank">Ouvrir le Rapport Complet</a>
</p>

### Rapport de Projet BE

<div style="display: flex; justify-content: center;">
    <iframe src="/img/BE_Service_Archi/BE_service_architecture.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_Service_Archi/BE_service_architecture.pdf" target="_blank">Ouvrir le Rapport de BE</a>
</p>

### Rapport de TP

<div style="display: flex; justify-content: center;">
    <iframe src="/img/BE_Service_Archi/Bigot_Chanfreau_Service_Architecture_Rapport_TP.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_Service_Archi/Bigot_Chanfreau_Service_Architecture_Rapport_TP.pdf" target="_blank">Ouvrir le Rapport de TP</a>
</p>

### Sujet de TP

<p style="text-align: center;">
    <a href="/img/BE_Service_Archi/Lab_Subject_service.pdf" target="_blank">Ouvrir le Sujet de TP</a>
</p>
