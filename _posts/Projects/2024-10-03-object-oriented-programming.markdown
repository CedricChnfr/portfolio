---
layout: default
title:  "Object Oriented Programming"
date:   2024-10-02 10:56:03 +0200
categories: jekyll update
---

<style>
p {
    text-align: justify;
}
</style>

<div class="back-nav">
    <a href="./my-projects.html" data-i18n-html="back-projects">&larr; Retour aux Projets</a>
</div>

<div class="lang-fr">
<h2><strong>Introduction</strong></h2>
<p>Ce projet est une collection de programmes C++ qui illustrent divers concepts de la programmation orientee objet, de la manipulation de vecteurs et de la gestion de figures geometriques. Il est structure en plusieurs etapes et travaux diriges (TD), chacun se concentrant sur des aspects specifiques de la programmation C++.</p>

<h2><strong>Etapes</strong></h2>
<p>Les fichiers Etape_1.cpp a Etape_6.cpp illustrent la manipulation de points en 2D et 3D. Toutes ces etapes avaient principalement pour but de comprendre le fonctionnement du C++.</p>
</div>

<div class="lang-en">
<h2><strong>Introduction</strong></h2>
<p>This project is a collection of C++ programs that illustrate various concepts of object-oriented programming, vector manipulation, and geometric figure management. It is structured into several steps and tutorials (TD), each focusing on specific aspects of C++ programming.</p>

<h2><strong>Steps</strong></h2>
<p>The files Step_1.cpp, Step_2.cpp, Step_3.cpp, Step_4.cpp, Step_5.cpp, and Step_6.cpp illustrate the manipulation of points in 2D and 3D. All these steps were mainly to understand how C++ works.</p>
</div>

<p align="center">
    <a href="/code/cpp/Etape_1.cpp" target="_blank">Step 1</a> -
    <a href="/code/cpp/Etape_2.cpp" target="_blank">Step 2</a> -
    <a href="/code/cpp/Etape_3.cpp" target="_blank">Step 3</a> -
    <a href="/code/cpp/Etape_4.cpp" target="_blank">Step 4</a> -
    <a href="/code/cpp/Etape_5.cpp" target="_blank">Step 5</a> -
    <a href="/code/cpp/Etape_6.cpp" target="_blank">Step 6</a>
</p>

<div class="lang-fr">
<p>Les fonctionnalites comprennent :</p>
<ul>
<li>Saisie et affichage : Les points peuvent etre saisis et affiches.</li>
<li>Operations mathematiques : Les points peuvent etre additionnes et multiplies par des scalaires.</li>
</ul>

<h2><strong>TDs</strong></h2>
<p><strong>Manipulation de vecteurs</strong></p>
<p>Les fichiers TD1.cpp, TD2.cpp, TD4.cpp et TD5.cpp contiennent des implementations de la classe vecteur. Cette classe permet de creer et de manipuler des vecteurs de differentes dimensions. Voici quelques fonctionnalites cles :</p>
</div>

<div class="lang-en">
<p>Features include:</p>
<ul>
<li>Input and Display: Points can be input and displayed.</li>
<li>Mathematical Operations: Points can be added and multiplied by scalars.</li>
</ul>

<h2><strong>TDs</strong></h2>
<p><strong>Vector Manipulation</strong></p>
<p>The files TD1.cpp, TD2.cpp, TD4.cpp, and TD5.cpp contain implementations of the vector class. This class allows you to create and manipulate vectors of different dimensions. Here are some key features:</p>
</div>

<p align="center">
    <a href="/code/cpp/TD1.cpp" target="_blank">TD1</a> -
    <a href="/code/cpp/TD2.cpp" target="_blank">TD2</a> -
    <a href="/code/cpp/TD4.cpp" target="_blank">TD4</a> -
    <a href="/code/cpp/TD5.cpp" target="_blank">TD5</a>
</p>

<div class="lang-fr">
<ul>
<li>Constructeurs et destructeurs : La classe vecteur possede plusieurs constructeurs pour initialiser les vecteurs avec des dimensions et des valeurs specifiques. Le destructeur assure la liberation de la memoire allouee dynamiquement.</li>
<li>Saisie et affichage : Les methodes de saisie et d'affichage permettent respectivement de saisir et d'afficher les valeurs des vecteurs.</li>
<li>Operateurs surcharges : La classe surcharge plusieurs operateurs, dont l'operateur d'indexation [], l'operateur d'affectation = et l'operateur d'addition +.</li>
</ul>

<h2><strong>TPs</strong></h2>
<p>Dans cette partie, vous trouverez deux projets C++ cles axes sur la gestion de figures geometriques et l'utilisation de la <strong>Standard Template Library (STL)</strong>.</p>
</div>

<div class="lang-en">
<ul>
<li>Constructors and Destructors: The vector class has several constructors to initialize vectors with specific dimensions and values. The destructor ensures the freeing of dynamically allocated memory.</li>
<li>Input and Display: The input and display methods allow you to input vector values and display them respectively.</li>
<li>Overloaded Operators: The class overloads several operators, including the indexing operator [], the assignment operator =, and the addition operator +.</li>
</ul>

<h2><strong>TPs</strong></h2>
<p>In this part, you will find two key C++ projects focused on geometric figure management and the use of the <strong>Standard Template Library (STL)</strong>.</p>
</div>

<p align="center">
    <a href="/code/cpp/TP_figure.cpp" target="_blank">TP Figure</a> -
    <a href="/code/cpp/TP_stl.cpp" target="_blank">TP STL</a>
</p>

<div class="lang-fr">
<h3>TP 1 : Gestion de figures geometriques</h3>
<p>Ce projet tourne autour de la gestion de <strong>figures geometriques</strong> telles que les carres, cercles, triangles equilateraux et rectangles en utilisant des concepts avances de programmation orientee objet comme les <strong>classes abstraites</strong>, l'<strong>heritage</strong> et le <strong>polymorphisme</strong>.</p>
<ul>
<li><strong>Creation et affichage dynamiques</strong> : Les figures sont creees dynamiquement en utilisant le polymorphisme.</li>
<li><strong>Calcul du perimetre</strong> : Chaque figure calcule et affiche son perimetre via la redefinition de la fonction virtuelle <code>perimetre()</code>.</li>
<li><strong>Polymorphisme et liaison dynamique</strong> : Le programme exploite le polymorphisme en iterant sur une liste de figures et en appelant dynamiquement les methodes appropriees.</li>
<li><strong>Gestion de listes avec iterateurs</strong> : Les figures sont stockees dans une liste et les operations standard sont realisees avec des iterateurs.</li>
<li><strong>Gestion des couleurs (heritage multiple)</strong> : Les cercles heritent egalement d'une classe <code>Coloriable</code>, illustrant l'<strong>heritage multiple</strong> en C++.</li>
<li><strong>Operations de file</strong> : Les figures sont stockees dans une file, permettant l'insertion et la suppression tout en preservant l'ordre d'entree.</li>
</ul>

<h3>TP 2 : Standard Template Library (STL) en C++</h3>
<p>La <strong>STL</strong> est une puissante bibliotheque C++ fournissant des structures de donnees et des algorithmes pre-construits. Ce projet explore l'utilisation efficace des conteneurs, iterateurs et algorithmes fournis par la STL.</p>
<ul>
<li><strong>Conteneurs</strong> : Le projet introduit des conteneurs <strong>sequentiels</strong> comme <code>vector</code>, <code>list</code> et <code>deque</code>, ainsi que des conteneurs <strong>associatifs</strong> tels que <code>set</code> et <code>map</code>.</li>
<li><strong>Iterateurs</strong> : Les iterateurs permettent le parcours facile des conteneurs.</li>
<li><strong>Algorithmes STL</strong> : Le projet demontre l'utilisation d'algorithmes tels que <code>reverse()</code>, <code>sort()</code> et <code>find()</code>.</li>
<li><strong>Operations sur set et map</strong> : L'utilisation de <code>set</code> garantit l'unicite des elements, tandis que <code>map</code> fournit un stockage cle-valeur pour des recherches efficaces.</li>
</ul>

<p>En combinant la gestion de figures geometriques et l'utilisation de la STL, ces deux projets illustrent les puissantes capacites du C++ en matiere de <strong>conception orientee objet</strong> et de <strong>programmation generique</strong>.</p>

<h2><strong>Conclusion</strong></h2>
<p>Ce projet demontre une comprehension approfondie des concepts de base et avances de la programmation C++. Les differentes etapes et travaux diriges montrent comment manipuler des vecteurs, gerer des figures geometriques et effectuer des operations sur des points 2D et 3D. Ce projet est un excellent exemple d'application pratique des principes de la programmation orientee objet en C++.</p>
</div>

<div class="lang-en">
<h3>TP 1: Geometric Figure Management</h3>
<p>This project revolves around the management of <strong>geometric figures</strong> such as squares, circles, equilateral triangles, and rectangles using advanced object-oriented programming concepts like <strong>abstract classes</strong>, <strong>inheritance</strong>, and <strong>polymorphism</strong>.</p>
<ul>
<li><strong>Dynamic Creation and Display</strong>: Figures are created dynamically using polymorphism.</li>
<li><strong>Perimeter Calculation</strong>: Each figure calculates and displays its perimeter by redefining the virtual function <code>perimetre()</code>.</li>
<li><strong>Polymorphism and Dynamic Binding</strong>: The program leverages polymorphism by iterating through a list of figures and calling appropriate methods dynamically.</li>
<li><strong>List Management with Iterators</strong>: Figures are stored in a list and standard operations are performed using iterators.</li>
<li><strong>Color Management (Multiple Inheritance)</strong>: Circles also inherit from a <code>Coloriable</code> class, showcasing <strong>multiple inheritance</strong> in C++.</li>
<li><strong>Queue Operations</strong>: Figures are stored in a queue, enabling insertion and deletion while preserving the order of entry.</li>
</ul>

<h3>TP 2: Standard Template Library (STL) in C++</h3>
<p>The <strong>STL</strong> is a powerful C++ library that provides pre-built data structures and algorithms. This project explores how to effectively use containers, iterators, and algorithms provided by the STL.</p>
<ul>
<li><strong>Containers</strong>: The project introduces both <strong>sequential containers</strong> like <code>vector</code>, <code>list</code>, and <code>deque</code>, as well as <strong>associative containers</strong> such as <code>set</code> and <code>map</code>.</li>
<li><strong>Iterators</strong>: Iterators allow for easy traversal of the containers.</li>
<li><strong>STL Algorithms</strong>: The project demonstrates the use of algorithms such as <code>reverse()</code>, <code>sort()</code>, and <code>find()</code>.</li>
<li><strong>Set and Map Operations</strong>: The use of <code>set</code> ensures uniqueness of elements, while <code>map</code> provides a key-value store for efficient lookups.</li>
</ul>

<p>By combining geometric figure management and the use of STL, these two projects illustrate the powerful capabilities of C++ in handling both <strong>object-oriented design</strong> and <strong>template programming</strong>.</p>

<h2><strong>Conclusion</strong></h2>
<p>This project demonstrates a thorough understanding of basic and advanced C++ programming concepts. The various steps and tutorials demonstrate how to manipulate vectors, manage geometric figures, and perform operations on 2D and 3D points. This project is an excellent example of the practical application of object-oriented programming principles in C++.</p>
</div>
