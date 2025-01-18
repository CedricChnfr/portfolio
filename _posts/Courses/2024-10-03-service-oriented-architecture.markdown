---
layout: default
title:  "Service Oriented Architecture"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Service Oriented Architecture

## PART A: GENERALITIES

### Presentation
The Service Oriented Architecture (SOA) course was a deep dive into the principles and practices of designing and implementing service-oriented systems. Taught by N. Guermouche, the course covered legacy and modern service architectures focusing on how to create scalable, maintainable, and efficient systems.

## PART B: DESCRIPTIVE PART

### Experience Details

#### Environment and Context

This course was really useful as the increasing demand for scalable and maintainable systems in the industry that highlights the relevance of this subject. The labs sessions allowed me to apply the concepts learned in class to real-world scenarios which was beneficial to understand different architecture methodologies.

#### My Function

In this course, I was responsible for:
- Understanding the principles of service-oriented architectures.
- Designing and implementing service-oriented systems.
- Conducting experiments to test the efficiency and scalability of various service architectures.

## PART C: TECHNICAL PART

This section explores the technical aspects of the Service Architecture course mainly learnt during technical labs focusing on SOAP, REST and microservices.

### Technical Concepts Learned

#### 1. SOAP Architecture
I learned about the SOAP (Simple Object Access Protocol) architecture which is a protocol for exchanging structured information in web services. SOAP uses XML for message formatting and relies on other application layer protocols, such as HTTP or SMTP, for message negotiation and transmission. 

1. **SOAP Request Envelope**: The request envelope contains the SOAP message that is sent to the web service. For example, if the chain is "cedric", the SOAP request envelope would look like this:
    ```xml
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://example.com/webservice">
        <soapenv:Header/>
        <soapenv:Body>
            <web:MyRequest>
                <web:chain>cedric</web:chain>
            </web:MyRequest>
        </soapenv:Body>
    </soapenv:Envelope>
    ```

2. **SOAP Response**: The response is returned by the web service after processing the request. For example, if the response returns 6, the SOAP response would look like this:
    ```xml
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:web="http://example.com/webservice">
        <soapenv:Header/>
        <soapenv:Body>
            <web:MyResponse>
                <web:result>6</web:result>
            </web:MyResponse>
        </soapenv:Body>
    </soapenv:Envelope>
    ```

#### 2. REST Architecture
I also learned about REST (Representational State Transfer), an architectural style that uses standard HTTP methods (POST, GET, PUT, DELETE) to interact with resources.


- **POST**: Creates a new resource, e.g., `POST /users` creates a new user.
- **GET**: Retrieves a resource, e.g., `GET /users/1` retrieves user with ID 1.
- **PUT**: Updates a resource, e.g., `PUT /users/1` updates user with ID 1.
- **DELETE**: Deletes a resource, e.g., `DELETE /users/1` deletes user with ID 1.

I developed RESTful services for managing user requests using JSON for data interchange and tools like Postman for testing.

```java
@RestController
@RequestMapping("/api/users")
public class UserController {

    @Autowired
    private UserService userService;

    // Get all users
    @GetMapping
    public List<User> getAllUsers() {
        return userService.getAllUsers();
    }

    // Get a user by ID
    @GetMapping("/{id}")
    public User getUserById(@PathVariable Long id) {
        return userService.getUserById(id);
    }

    // Create a new user
    @PostMapping
    public User createUser(@RequestBody User user) {
        return userService.createUser(user);
    }

    // Update an existing user
    @PutMapping("/{id}")
    public User updateUser(@PathVariable Long id, @RequestBody User userDetails) {
        return userService.updateUser(id, userDetails);
    }

    // Delete a user by ID
    @DeleteMapping("/{id}")
    public void deleteUser(@PathVariable Long id) {
        userService.deleteUser(id);
    }
}
```

#### 3. Microservices Development
Microservices are an architectural style that structures an application as a collection of coupled services. Each service is independently deployable and scalable. I used Spring Boot to create microservices for user management, volunteer management, request management, and feedback management (refer to [Project Report](#project-report)) . 

## PART D: ANALYTICAL PART

### Knowledge and Skills Mobilized
- Understanding of service-oriented architecture concepts and features.
- Development of distributed architectures using web services.
- Deployment and configuration of SOA using SOAP and REST.
- Design, development, and deployment of microservice architectures.
- Mastering the architecture of energy management systems, simple storage, energy recovery, and sizing storage elements according to specifications.


### Self Evaluation
Using all the new concepts learned during the course was at first a bit complicated but fortunately the tutorials were well-structured allowing me to learn step by step. Also, there was a large number of practical sessions to practice and understand all the concepts. As I am not used to Java, I had to relearn the basics of this language which was a bit challenging.

I didn't participate much in the SOAP concept labs because I wanted to focus more on REST and microservices due to time constraints.

### My Opinion
Before taking this course, I had only heard about some of the concepts related to service-oriented architecture. Thanks to the lab sessions, I now have a much better understanding of the architecture of web applications and how to interact with them. 

Additionally, developing in Java during the course reminded me of how to code in this language which is important as it is use in lot of companies industry. Even if I'd prefer to code in C for my professional future, I can now apply for Java positions if needed.

<div style="text-align: center;">
    <h1>Project Report</h1>
</div>

<div style="display: flex; justify-content: center;">
    <iframe src="/img/BE_service_architecture.pdf" width="100%" height="800px" style="overflow: auto;" frameborder="0"></iframe>
</div>

<p style="text-align: center;">
    <a href="/img/BE_service_architecture.pdf" target="_blank">Download Complete Report</a>
</p>

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