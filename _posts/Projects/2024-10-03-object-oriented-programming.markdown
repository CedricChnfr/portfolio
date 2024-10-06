---
layout: default
title:  "Object Oriented Programming"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---
## **Introduction**
This project is a collection of C++ programs that illustrate various concepts of object-oriented programming, vector manipulation, and geometric figure management. It is structured into several steps and tutorials (TD), each focusing on specific aspects of C++ programming.

## **Steps**
The files Step_1.cpp, Step_2.cpp, Step_3.cpp, Step_4.cpp, and Step_5.cpp, Step_6.cpp illustrate the manipulation of points in 2D and 3D. 
All these steps were mainly to understand how C++ works.

<p align="center">
    <a href="/code/cpp/Etape_1.cpp" target="_blank">Step 1</a> -
    <a href="/code/cpp/Etape_2.cpp" target="_blank">Step 2</a> -
    <a href="/code/cpp/Etape_3.cpp" target="_blank">Step 3</a> -
    <a href="/code/cpp/Etape_4.cpp" target="_blank">Step 4</a> -
    <a href="/code/cpp/Etape_5.cpp" target="_blank">Step 5</a> - 
    <a href="/code/cpp/Etape_6.cpp" target="_blank">Step 6</a>
</p>

Features include:
- Input and Display: Points can be input and displayed.

- Mathematical Operations: Points can be added and multiplied by scalars.


## **TDs**
Vector Manipulation
The files TD1.cpp, TD2.cpp, TD4.cpp, and TD5.cpp contain implementations of the vector class. This class allows you to create and manipulate vectors of different dimensions. Here are some key features:

<p align="center">
    <a href="/code/cpp/TD1.cpp" target="_blank">TD1</a> -
    <a href="/code/cpp/TD2.cpp" target="_blank">TD2</a> -
    <a href="/code/cpp/TD4.cpp" target="_blank">TD4</a> -
    <a href="/code/cpp/TD5.cpp" target="_blank">TD5</a>
</p>


- Constructors and Destructors: The vector class has several constructors to initialize vectors with specific dimensions and values. The destructor ensures the freeing of dynamically allocated memory.

- Input and Display: The input and display methods allow you to input vector values ​​and display them respectively.

- Overloaded Operators: The class overloads several operators, including the indexing operator [], the assignment operator =, and the addition operator +.

## **TPs**

In this part, you will find two key C++ projects focused on geometric figure management and the use of the **Standard Template Library (STL)**.

<p align="center">
    <a href="/code/cpp/TP_figure.cpp" target="_blank">TP Figure</a> -
    <a href="/code/cpp/TP_stl.cpp" target="_blank">TP STL</a>
</p>

### TP 1: Geometric Figure Management

This project revolves around the management of **geometric figures** such as squares, circles, equilateral triangles, and rectangles using advanced object-oriented programming concepts like **abstract classes**, **inheritance**, and **polymorphism**.

- **Dynamic Creation and Display**: Figures are created dynamically using polymorphism. Each figure (square, circle, triangle, rectangle) has unique characteristics that are displayed using virtual functions.
  
- **Perimeter Calculation**: Each figure calculates and displays its perimeter, achieved by redefining the virtual function `perimetre()` in derived classes.
  
- **Polymorphism and Dynamic Binding**: The program leverages polymorphism by iterating through a list of figures and calling appropriate methods for each figure type dynamically.

- **List Management with Iterators**: Figures are stored in a list, and standard operations like insertion and deletion are performed using iterators.

- **Color Management (Multiple Inheritance)**: Circles also inherit from a `Coloriable` class, allowing them to store and display a color. This showcases **multiple inheritance** in C++.
  
- **Queue Operations**: Figures are stored in a queue, enabling insertion and deletion while preserving the order of entry. The project also demonstrates linked structures and queue management for figure manipulation.

### TP 2: Standard Template Library (STL) in C++

The **STL** is a powerful C++ library that provides pre-built data structures and algorithms. This project explores how to effectively use containers, iterators, and algorithms provided by the STL.

- **Containers**: The project introduces both **sequential containers** like `vector`, `list`, and `deque`, as well as **associative containers** such as `set` and `map`. These containers are used to store data and efficiently manage access to the elements.

- **Iterators**: Iterators allow for easy traversal of the containers, functioning similarly to pointers in arrays. The project highlights how to iterate through containers using **`begin()`** and **`end()`** methods and perform operations on each element.

- **STL Algorithms**: The project demonstrates the use of algorithms such as **`reverse()`**, **`sort()`**, and **`find()`**, which work on iterators to manipulate the contents of containers without altering the container structure itself.

- **Vector and List Operations**: Practical examples include creating vectors and lists, adding and removing elements dynamically, and performing operations such as sorting and searching.

- **Advanced Exercises**:
  - Creating a vector of 10 float values, modifying the second half of the vector.
  - Managing lists of alphabet characters and inserting or deleting elements efficiently.

- **Set and Map Operations**: The use of `set` ensures uniqueness of elements, while `map` provides a key-value store for efficient lookups. The project also demonstrates complex operations like finding and removing elements based on conditions.

By combining geometric figure management and the use of STL, these two projects illustrate the powerful capabilities of C++ in handling both **object-oriented design** and **template programming**.

## **Conclusion**
This project demonstrates a thorough understanding of basic and advanced C++ programming concepts. The various steps and tutorials demonstrate how to manipulate vectors, manage geometric figures, and perform operations on 2D and 3D points. This project is an excellent example of the practical application of object-oriented programming principles in C++.

<style>
p {
    text-align: justify;
}
</style>