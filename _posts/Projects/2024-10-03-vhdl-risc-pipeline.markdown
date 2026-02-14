---
layout: default
title:  "Design of a RISC type microprocessor"
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
<h1><strong>Introduction</strong></h1>
<p>Notre projet consiste a concevoir un microprocesseur de type RISC, designe en VHDL sur l'outil de developpement, simulation et implementation Vivado. Cette architecture promet une execution plus rapide des programmes grace a ses 5 niveaux de pipeline. Ce rapport sera structure pour couvrir les differentes phases du projet.</p>
<p>Nous commencerons par presenter l'architecture du microprocesseur avec les differents composants cles tels que l'Unite Arithmetique et Logique (UAL), le Banc de Registres, la Memoire d'Instructions, la Memoire de Donnees, et d'autres elements essentiels qui guideront la conception de notre microprocesseur. Nous aborderons egalement la gestion des ALEAS, un aspect crucial de la conception.</p>
<p>Enfin, nous analyserons les resultats de synthese mettant en evidence les optimisations realisees pour augmenter la frequence de fonctionnement ainsi que la reduction de sa consommation energetique.</p>
</div>

<div class="lang-en">
<h1><strong>Introduction</strong></h1>
<p>Our project is to design a RISC type microprocessor, designated in VHDL on the Vivado development, simulation and implementation tool. This architecture promises faster program execution thanks to its 5 pipeline levels. This report will be structured to cover the different phases of the project.</p>
<p>We will start by presenting the microprocessor architecture with the different key components such as the Arithmetic Logic Unit (ALU), the Register Bank, the Instruction Memory, the Data Memory, and other essential elements that will guide the design of our microprocessor. We will also address ALEA management, a crucial aspect of the design.</p>
<p>Finally, we will analyze the synthesis results highlighting the optimizations made to increase the operating frequency as well as the reduction of its energy consumption.</p>
</div>

<div class="lang-fr">
<h1><strong>Architecture du microprocesseur RISC</strong></h1>
<h1>Composants du microprocesseur</h1>
<p>Dans cette partie nous allons nous interesser a l'architecture d'un microprocesseur RISC, cependant nous n'entrerons pas dans les details. En effet il existe beaucoup de documentation sur le sujet, qui est claire et synthetique. Nous presenterons donc de maniere fonctionnelle les 5 elements presents dans notre microprocesseur : l'UAL, la memoire de donnees, la memoire d'instructions et le banc de registres.</p>

<h2>Unite arithmetique et logique</h2>
<h3>Description fonctionnelle</h3>
<p>L'Unite Arithmetique et Logique (UAL) est le composant central qui permet l'execution des operations arithmetiques et logiques du microprocesseur. Le bus de controle (Ctrl_ALU) determine le type d'operation a effectuer. L'UAL prend deux entrees A et B de 8 bits, qui seront les operandes, et S le resultat de l'operation egalement sur 8 bits. Nous avons egalement 4 drapeaux en sortie : Negatif, Retenue, Zero et Debordement.</p>
</div>

<div class="lang-en">
<h1><strong>RISC Microprocessor Architecture</strong></h1>
<h1>Microprocessor Component</h1>
<p>In this part we will look at the architecture of a RISC microprocessor, however we will not go into details. Indeed there is a lot of documentation on this subject, which is clear and synthetic. We will therefore present in a functional way the 5 elements present in our microprocessor: the ALU, the data memory, the instruction memory and the register bank.</p>

<h2>Arithmetic and Logic Unit</h2>
<h3>Functional Description</h3>
<p>The Arithmetic Logic Unit (ALU) is the central component that allows the execution of arithmetic and logic operations of the microprocessor. The Control Bus (Ctrl_ALU) determines the type of operation to be performed. The ALU takes two inputs A and B of 8 bits, which will be the operands and S the result of the operation also on 8 bits. We also have 4 flags at the output, Negative, Carry, Zero and Overflow.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/ALU.png" style="width: 30%;"/>
</div>

<div class="lang-fr">
<h3>Simulation fonctionnelle</h3>
<p>Ci-dessous se trouve l'une des simulations fonctionnelles de notre UAL. Cette simulation ne depend pas du temps et de l'implementation et nous permet uniquement de verifier le fonctionnement logique du circuit.</p>
</div>

<div class="lang-en">
<h3>Functional Simulation</h3>
<p>Below is one of the functional simulations of our ALU. This simulation does not depend on time and implementation and only allows us to verify the logical operation of the circuit.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/ALU_simu.png" style="width: 90%;"/>
</div>
<div style="text-align: center;">
    <img src="/img/BE_Pipeline/ALU_tab.png" style="width: 90%;"/>
</div>

<div class="lang-fr">
<p>Le resultat de chaque operation est stocke dans la sortie S. De plus, le composant fournit des informations sur le resultat sous forme de drapeaux dans la sortie Flag, indiquant si une operation a genere une retenue, si le resultat est negatif, s'il est nul ou s'il y a eu un debordement.</p>

<h2>Banc de registres</h2>
<h3>Description fonctionnelle</h3>
<p>Le banc de registres, integre dans notre architecture, represente un element fondamental pour le stockage temporaire des donnees lors de l'execution des instructions. Il se compose de 16 registres de 8 bits, offrant une capacite de stockage significative pour les operations en cours. Cette configuration permet des operations d'acces en lecture simultanees via les ports QA et QB, ainsi que des operations d'ecriture via le port W_in.</p>
</div>

<div class="lang-en">
<p>The result of each operation is stored in the S output. Additionally, the component outputs information about the result in the form of flags in the Flag output, indicating whether an operation generated a carry, whether the result is negative, whether it is zero, or whether there was an overflow.</p>

<h2>Register Bench</h2>
<h3>Functional Description</h3>
<p>The Register Bank, integrated in our architecture, represents a fundamental element for temporary data storage during instruction execution. It consists of 16 8-bit registers, providing significant storage capacity for ongoing operations. This configuration allows simultaneous read access operations via ports QA and QB, as well as write operations via port W_in.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/Register_bench.png" style="width: 30%;"/>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/Register_bench_simu.png" style="width: 90%;"/>
    <img src="/img/BE_Pipeline/Register_bench_tab.png" style="width: 90%;"/>
</div>

<div class="lang-fr">
<h2>Memoire de donnees</h2>
<h3>Description fonctionnelle</h3>
<p>La memoire de donnees est utilisee pour stocker les informations temporaires necessaires au fonctionnement d'un programme. Les operations sur la memoire de donnees incluent la lecture de valeurs stockees a des adresses specifiques et l'ecriture de nouvelles valeurs a ces adresses.</p>
</div>

<div class="lang-en">
<h2>Data Memory</h2>
<h3>Functional Description</h3>
<p>Data memory is used to store temporary information needed for a program to operate. Operations on data memory include reading values stored at specific addresses and writing new values to those addresses.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/Data_Memory.png" style="width: 30%;"/>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/Data_Memory_simu.png" style="width: 90%;"/>
    <img src="/img/BE_Pipeline/Data_Memory_tab.png" style="width: 90%;"/>
</div>

<div class="lang-fr">
<h2>Memoire d'instructions</h2>
<h3>Description fonctionnelle</h3>
<p>La memoire d'instructions stocke la liste des instructions machine qui composent le programme execute par le processeur. Chaque instruction est associee a une adresse memoire specifique. Chaque instruction est representee sur 32 bits et est accessible a une adresse specifique en memoire.</p>
</div>

<div class="lang-en">
<h2>Instruction Memory</h2>
<h3>Functional Description</h3>
<p>Instruction memory stores the list of machine instructions that make up the program executed by the processor. Each instruction is associated with a specific memory address. Each instruction is represented on 32 bits and is accessible at a specific address in memory.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/Instruction_Memory.png" style="width: 30%;"/>
    <img src="/img/BE_Pipeline/Instruction_Memory_simu.png" style="width: 30%;"/>
    <img src="/img/BE_Pipeline/Instruction_Memory_tab.png" style="width: 30%;"/>
</div>

<div class="lang-fr">
<h1>Gestion des ALEAS</h1>
<h3>Description fonctionnelle</h3>
<p>Nous distinguons les ALEAS de donnees et les ALEAS de branchement. Nous nous concentrerons sur les ALEAS de donnees. Un ALEA de donnees est un evenement declenche par au moins deux instructions s'executant consecutivement et de maniere incompatible. Une premiere instruction modifie la valeur d'une donnee dans une zone memoire, la seconde utilise cette zone memoire alors que la valeur n'a pas ete mise a jour. Pour resoudre ce probleme, nous avons cree un nouveau composant dans notre chemin de donnees.</p>
</div>

<div class="lang-en">
<h1>ALEA Management</h1>
<h3>Functional Description</h3>
<p>We distinguish between data ALEA events and branch ALEA events. We will focus on data ALEA events. A data ALEA event is an event triggered by at least two instructions executing consecutively and in an incompatible manner. A first instruction modifies the value of a data item in a memory area, the second uses this memory area while the value has not been updated. To address this issue we have created a new component in our data path.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/ALEA.png" style="width: 100%;"/>
</div>

<div class="lang-fr">
<h3>Condition de detection</h3>
<p>Nous voulons avoir les conditions les plus generales possibles pour detecter nos ALEAS. Ci-dessous les conditions de detection pour les instructions MUL, SOU et ADD, puis pour COP et STORE.</p>
</div>

<div class="lang-en">
<h3>Detection Condition</h3>
<p>We want to have the most general conditions possible to detect our ALEA events. Below are the detection conditions for MUL, SOU, and ADD instructions, then for COP and STORE.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/ALEA_tab.png" style="width: 60%;"/>
    <img src="/img/BE_Pipeline/ALEA_tab2.png" style="width: 60%;"/>
</div>

<div class="lang-fr">
<h3>Simulation fonctionnelle</h3>
<p><strong>ALEA simple :</strong></p>
<p>Un premier ALEA simple a percevoir est une succession de deux AFC suivis d'une addition des deux registres.</p>
</div>

<div class="lang-en">
<h3>Functional Simulation</h3>
<p><strong>Simple ALEA:</strong></p>
<p>A first simple ALEA to perceive is a succession of two AFCs followed by an addition of the two registers.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/ALEA_simu_simple.png" style="width: 100%;"/>
</div>

<div class="lang-fr">
<p><strong>ALEA complexe :</strong></p>
<p>Un deuxieme exemple d'ALEA est un ALEA cause par deux instructions non successives.</p>
</div>

<div class="lang-en">
<p><strong>Complex ALEA:</strong></p>
<p>A second example of ALEA is ALEA caused by two non-successive instructions.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/ALEA_simu_complex.png" style="width: 100%;"/>
</div>

<div class="lang-fr">
<p><strong>ALEA complementaire :</strong></p>
<p>Enfin, un dernier exemple d'ALEA cause par deux instructions non successives.</p>
</div>

<div class="lang-en">
<p><strong>Complementary ALEA:</strong></p>
<p>Finally, a last example of ALEA caused by two non-successive instructions.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/ALEA_simu_complem.png" style="width: 100%;"/>
</div>

<div class="lang-fr">
<h1>Implementation du microprocesseur RISC</h1>
<h2>Choix d'implementation</h2>
<p>Nous avons decide d'implementer les 4 MUX delimitant les etages du pipeline sous forme de composants. Les composants LC discrets et MUX simples ont ete implementes de maniere concurrente directement dans le chemin de donnees.</p>

<h2>Analyse frequentielle et chemin critique</h2>
<p>Notre premier rapport de timing indique une frequence MAX de 65MHz. Le chemin critique nous indique de regarder nos memoires. Apres optimisation, notre frequence n'a pas augmente malgre nos efforts.</p>
</div>

<div class="lang-en">
<h1>RISC Microprocessor Implementation</h1>
<h2>Implementation Choices</h2>
<p>We decided to implement the 4 MUX delimiting the pipeline stages in the form of components. The discrete LC and simple MUX components were implemented concurrently directly in the data path.</p>

<h2>Frequency Analysis and Critical Path</h2>
<p>Our first Timing report indicates a MAX frequency of 65MHz. The critical path tells us that we should look at our memories. After optimization, our frequency did not increase despite our efforts.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/Pipeline_data.png" style="width: 80%;"/>
    <img src="/img/BE_Pipeline/Pipeline_path.png" style="width: 100%;"/>
    <img src="/img/BE_Pipeline/Pipeline_data2.png" style="width: 100%;"/>
</div>

<div class="lang-fr">
<h2>Performance</h2>
<h3>Consommation energetique</h3>
<p>Bien que nos modifications n'aient pas augmente la frequence, la consommation energetique a diminue de maniere significative, de l'ordre de 175%.</p>
</div>

<div class="lang-en">
<h2>Performance</h2>
<h3>Energy Consumption</h3>
<p>Although our modifications did not increase the frequency, the energy consumption has decreased significantly, by approximately 175%.</p>
</div>

<div style="text-align: center;">
    <img src="/img/BE_Pipeline/Energy.png" style="width: 80%;"/>
    <img src="/img/BE_Pipeline/Consumption.png" style="width: 80%;"/>
</div>

<div class="lang-fr">
<h1><strong>Conclusion</strong></h1>
<p>Le projet a ete tres interessant a realiser, la decouverte du logiciel Vivado a ete instructive pour nous qui n'avions travaille que sur Quartus. Ce projet nous a egalement permis d'appliquer de maniere concrete les differentes notions vues lors de la modelisation de composants et architectures numeriques.</p>
<p>Nous avons rencontre de nombreuses difficultes, notamment en essayant d'optimiser les chemins critiques, et nous n'avons finalement pas atteint nos objectifs. Malgre cet echec, nous sommes satisfaits de notre gestion des aleas. De plus, la demarche nous a permis d'aller plus loin dans l'utilisation des differents outils offerts par Vivado, et sur la conception VHDL en general.</p>
<p>La connaissance et la comprehension de l'architecture d'un microprocesseur nous sont egalement utiles, nous pouvons decrire ces connaissances comme des competences transversales.</p>
</div>

<div class="lang-en">
<h1><strong>Conclusion</strong></h1>
<p>The project was very interesting to carry out, the discovery of the Vivado software was instructive for us who had only worked on Quartus. This project also allowed us to apply in a concrete way the different notions seen during the modeling of digital components and architectures.</p>
<p>We encountered many difficulties, particularly when trying to optimize critical paths, and we ultimately did not achieve our goals. Despite this failure, we are satisfied with our management of hazards. In addition, the approach allowed us to go further in the use of the different tools offered by Vivado, and on VHDL design in general.</p>
<p>Knowledge and understanding of the architecture of a microprocessor are also useful to us, we can describe this knowledge as transversal skills.</p>
</div>
