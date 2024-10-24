---
layout: default
title:  "Service Oriented Architecture Course"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# **Service Architecture/Software Engineering**

# Service-Oriented Architecture

Service-Oriented Architecture (SOA) is a design model that allows structuring software applications as a collection of independent and interconnected services. Each service is encapsulated, meaning it exposes functionalities through a well-defined interface, enabling smooth integration and efficient reuse of services in different applications.

## SOA Objectives

The objectives of Service-Oriented Architecture are:

- **Encapsulation of business applications into services**: A service exposes a specific functionality in a standardized manner.

- **Interoperability**: Services are independent of programming languages and platforms, allowing for inter-system integration.

- **Application evolution**: SOA enables systems to evolve while reusing existing services.

- **Service reuse**: A service can be used by multiple applications.

<div style="text-align: center;">
    <img src="/img/Cours_SOA/Distr_App.png" style="width: 60%;"/>
</div>

## Example of Applications with and without SOA

- **Without SOA**: Applications are often monolithic, difficult to maintain, and evolve.

- **With SOA**: Applications are composed of reusable services. For example, an ApplicationA offers functionalities via services (Service1, Service2...), and an ApplicationB can reuse these same services without code duplication.

<div style="text-align: center;">
    <img src="/img/Cours_SOA/Service_reuse.png" style="width: 70%;"/>
</div>


# Web Services

Web services are software accessible via standard web protocols and provide an interface that offers data and services. They enable decoupling of platforms and programming languages.

<div style="text-align: center;">
    <img src="/img/Cours_SOA/Web_service.png" style="width: 80%;"/>
</div>

Service-Oriented Architecture (SOA) relies on XML standards to facilitate integration, interoperability, and communication between services. The main standards are:

## Web Services Description Language (WSDL)

WSDL is an XML language that allows describing web services in a standardized manner. It provides crucial information about the services, such as:

- **Offered operations**: Actions that the service can perform (e.g., data transmission, computation).

- **Data types**: Definitions of the data structures exchanged (e.g., XML Schema).

- **Transport protocols**: Protocols used for exchanges (HTTP, SOAP, etc.).

- **Service location**: The URL where the service is accessible.

**Structure of a WSDL Document**

A WSDL document is structured into several elements:

`<definitions>`: Root element listing namespaces and organizing the document.

`<types>`: Defines the data types exchanged between the client and the service.

`<message>`: Describes the input and output messages used by the service.

`<portType>`: Defines the operations offered by the service.

`<binding>`: Specifies the transport protocol (e.g., SOAP over HTTP).

`<service>`: Defines the service entry points via network addresses (ports).

<div style="text-align: center;">
    <img src="/img/Cours_SOA/wsdl.png" style="width: 30%;"/>
</div>

## Universal Descrition Discovery and Integration (UDDI)

UDDI (Universal Description, Discovery, and Integration) is a directory that allows discovering and integrating web services. It enables businesses to publish their services in a registry, facilitating their discovery by other entities.

The integration process with UDDI involves several steps:

1. **Publication**: The service is described in WSDL and published in the UDDI directory.

2. **Discovery**: Clients search for services that meet their needs in the directory.

3. **Invocation**: Once the service is found, it is invoked via a transport protocol like SOAP.

## Simple Object Access Protocol (SOAP)

SOAP is an XML-based protocol that allows exchanging structured messages between a client and a web service. It is designed to be extensible and works over different transport protocols like HTTP, SMTP, or even network-specific protocols.

## Structure of a SOAP Message
A SOAP message consists of three parts:

1. Envelope: Root element that contains the entire message.

2. Header (optional): Adds additional information such as security or routing.

3. Body: Contains the exchanged data (e.g., invoked method and its parameters).

<div style="text-align: center;">
    <img src="/img/Cours_SOA/soap.png" style="width: 80%;"/>
</div>

## Examples of SOAP Operations

- One-way: The service receives a request without sending a response.

- Request/Response: The service receives a request and sends back a response.

- Notification: The service sends a notification to the client without waiting for a response.

- Solicit-Response: The service solicits a response from the client after sending a message.


## Web Service Interactions Example

The complete interaction process between a client and a web service via SOA and SOAP can be summarized in these steps:

1. The client sends a SOAP request to the address defined in the service's WSDL.
2. The web service receives and processes the request, then returns a SOAP response.
3. The client receives the SOAP response with the requested results or data.


<style>
p {
    text-align: justify;
}
</style>