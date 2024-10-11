---
layout: default
title:  "Service Oriented Architecture Course"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Service-Oriented Architecture 

Service-Oriented Architecture (SOA) is a design model that allows structuring software applications as a collection of independent and interconnected services. Each service is encapsulated, meaning it exposes functionalities through a well-defined interface, enabling smooth integration and efficient reuse of services in different applications.



## Application Evolution

Applications evolve in response to growing customer needs. Initially, an application may satisfy a basic need, but over time it must integrate new features to meet complex requirements.

- Example of evolution:
    - Application1 starts with functionalities A and B. 

    - Then, it evolves to include C and D, allowing reuse of existing components. 
    
<div style="text-align: center;">
    <img src="/img/Cours_SOA/App_evolution.png" style="width: 60%;"/>
</div>

This ability to evolve and reuse applications is essential in modern development.

## Distributed Applications

Client needs often become complex, requiring inter-organizational collaboration. This leads to the integration of distributed applications.

- Application Integration: Applications can be heterogeneous, written in different programming languages, and running on various platforms. This diversity poses integration challenges that SOA aims to solve.

<div style="text-align: center;">
    <img src="/img/Cours_SOA/Distr_App.png" style="width: 60%;"/>
</div>

## SOA Principles

- Encapsulation of business applications: SOA allows encapsulating business applications as services, thus providing functionalities accessible by other applications.

<div style="text-align: center;">
    <img src="/img/Cours_SOA/SOA.png" style="width: 60%;"/>
</div>

- Service reuse: Services can be reused in different applications, facilitating the evolution and integration of systems.

    - Without SOA: Applications are often monolithic and difficult to maintain.

    - With SOA: Applications are made up of individual services, as illustrated below:

<div style="text-align: center;">
    <img src="/img/Cours_SOA/Service_reuse.png" style="width: 70%;"/>
</div>
    
- Decoupling of platforms and languages: Web services allow the separation of services from the platform and the underlying programming language, facilitating integration.

<div style="text-align: center;">
    <img src="/img/Cours_SOA/Web.png" style="width: 20%;"/>
</div>

# Web Services

Web services are software accessible via standard web protocols and provide an interface that offers data and services. They enable decoupling of platforms and programming languages.

<div style="text-align: center;">
    <img src="/img/Cours_SOA/Web_service.png" style="width: 80%;"/>
</div>

## Web Services Properties

- Web Services Discovery: Clients can discover and use available Web services, which improves the flexibility and maintainability of applications.

<div style="text-align: center;">
    <img src="/img/Cours_SOA/Web_dec.png" style="width: 50%;"/>
</div>

- Web Services Composition: Composition allows the creation of new value-added services by combining several existing Web services, thus facilitating the creation of complex applications from simple components.

<div style="text-align: center;">
    <img src="/img/Cours_SOA/Web_comp.png" style="width: 60%;"/>
</div>



<style>
p {
    text-align: justify;
}
</style>