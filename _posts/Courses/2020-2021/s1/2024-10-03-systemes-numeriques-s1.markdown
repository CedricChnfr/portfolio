---
layout: default
title: "Systèmes Numériques (SIN) - S1"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

<div class="lang-fr">

<h1>Systemes Numeriques (SIN) - Semestre 1</h1>

<h2>PART A - Presentation Generale du Cours</h2>

<h3>Contexte de la formation</h3>
<p>Les systemes numeriques sont au coeur de tous les equipements electroniques modernes : ordinateurs, smartphones, systemes embarques, automatismes industriels. Ce module introduit les fondements de la logique digitale et de la conception de circuits numeriques, competences indispensables pour tout technicien ou ingenieur en GEII. La maitrise du VHDL (langage de description materiel) permet de concevoir des systemes numeriques complexes sur FPGA.</p>

<h3>Positionnement dans le cursus</h3>
<ul>
  <li><strong>Semestre</strong> : S1 (1ere annee DUT GEII)</li>
  <li><strong>Volume horaire</strong> : 65h (25h CM + 20h TD + 20h TP)</li>
  <li><strong>Credits ECTS</strong> : 6</li>
  <li><strong>Prerequis</strong> : Connaissances de base en mathematiques (binaire, booleen)</li>
  <li><strong>Continuite</strong> : Logique Sequentielle (S2), Architectures Numeriques Avancees (S3-S4)</li>
</ul>

<h3>Public vise</h3>
<p>Etudiants de premiere annee DUT GEII decouvrant la conception de circuits numeriques depuis les bases (portes logiques) jusqu'a la programmation FPGA en VHDL.</p>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXTE ET FONCTION</h2>

<h3>Objectifs pedagogiques</h3>

<p><strong>Competences en logique numerique :</strong></p>
<ul>
  <li>Maitriser les systemes de numeration et les conversions</li>
  <li>Comprendre et appliquer l'algebre de Boole</li>
  <li>Concevoir des circuits combinatoires et sequentiels</li>
  <li>Simplifier des fonctions logiques</li>
</ul>

<p><strong>Competences en VHDL et FPGA :</strong></p>
<ul>
  <li>Ecrire du code VHDL pour decrire des circuits</li>
  <li>Simuler et valider des designs numeriques</li>
  <li>Synthetiser et programmer des FPGA</li>
  <li>Utiliser l'environnement Quartus Prime (Intel/Altera)</li>
</ul>

<p><strong>Competences transversales :</strong></p>
<ul>
  <li>Analyser un probleme et le traduire en circuit logique</li>
  <li>Tester et deboguer des systemes numeriques</li>
  <li>Documenter ses conceptions</li>
</ul>

<h3>Programme detaille</h3>

<h4>1. Systemes de numeration (8h)</h4>

<p><strong>Bases numeriques :</strong></p>

<p><strong>Binaire (base 2) :</strong></p>
<ul>
  <li>Chiffres : 0, 1</li>
  <li>Exemple : 1011&#x2082; = 1x2&#xB3; + 0x2&#xB2; + 1x2&#xB9; + 1x2&#x2070; = 11&#x2081;&#x2080;</li>
</ul>

<p><strong>Octal (base 8) :</strong></p>
<ul>
  <li>Chiffres : 0-7</li>
  <li>Utilise historiquement, moins courant aujourd'hui</li>
  <li>Conversion facile : 3 bits binaires = 1 chiffre octal</li>
</ul>

<p><strong>Hexadecimal (base 16) :</strong></p>
<ul>
  <li>Chiffres : 0-9, A-F (A=10, B=11, ..., F=15)</li>
  <li>Tres utilise en informatique (adresses memoire, couleurs RGB)</li>
  <li>Conversion : 4 bits binaires = 1 chiffre hexadecimal</li>
  <li>Exemple : 0xA3 = 10100011&#x2082; = 163&#x2081;&#x2080;</li>
</ul>

<p><strong>Conversions entre bases :</strong></p>

<p><em>Decimal &rarr; Binaire (divisions successives) :</em></p>
<pre><code>45&#x2081;&#x2080; &rarr; Binaire ?
45 / 2 = 22 reste 1  (bit de poids faible)
22 / 2 = 11 reste 0
11 / 2 = 5 reste 1
5 / 2 = 2 reste 1
2 / 2 = 1 reste 0
1 / 2 = 0 reste 1  (bit de poids fort)
Resultat : 101101&#x2082;</code></pre>

<p><em>Binaire &rarr; Hexadecimal (groupes de 4 bits) :</em></p>
<pre><code>11010110&#x2082; = 1101 0110 = D6&#x2081;&#x2086;</code></pre>

<p><strong>Codes numeriques :</strong></p>

<p><strong>BCD (Binary Coded Decimal) :</strong></p>
<ul>
  <li>Chaque chiffre decimal code sur 4 bits</li>
  <li>Exemple : 95&#x2081;&#x2080; = 1001 0101 (BCD) &ne; 1011111&#x2082; (binaire pur)</li>
  <li>Utilise dans les afficheurs 7 segments</li>
</ul>

<p><strong>Code Gray :</strong></p>
<ul>
  <li>Un seul bit change entre deux valeurs consecutives</li>
  <li>Reduit les erreurs lors de transitions</li>
  <li>Utilise dans les encodeurs rotatifs</li>
</ul>

<table>
  <thead><tr><th>Decimal</th><th>Binaire</th><th>Gray</th></tr></thead>
  <tbody>
    <tr><td>0</td><td>000</td><td>000</td></tr>
    <tr><td>1</td><td>001</td><td>001</td></tr>
    <tr><td>2</td><td>010</td><td>011</td></tr>
    <tr><td>3</td><td>011</td><td>010</td></tr>
    <tr><td>4</td><td>100</td><td>110</td></tr>
  </tbody>
</table>

<p><strong>Code ASCII :</strong></p>
<ul>
  <li>7 bits pour coder les caracteres (lettres, chiffres, symboles)</li>
  <li>Exemple : 'A' = 65&#x2081;&#x2080; = 01000001&#x2082;</li>
</ul>

<p><strong>Arithmetique binaire :</strong></p>

<p><strong>Addition binaire :</strong></p>
<pre><code>  1011  (11)
+ 0110  (6)
-------
 10001  (17)

Regles : 0+0=0, 0+1=1, 1+1=10 (retenue)</code></pre>

<p><strong>Soustraction binaire (complement a 2) :</strong></p>
<pre><code>A - B = A + (-B)
-B = complement a 1 de B + 1

Exemple : 7 - 3
7 = 0111
3 = 0011 &rarr; Complement a 1 : 1100 &rarr; +1 : 1101 (-3)
0111 + 1101 = 10100 &rarr; on garde les 4 bits de poids faible : 0100 = 4</code></pre>

<p><strong>Representation des nombres signes :</strong></p>
<ul>
  <li><strong>Signe + valeur absolue</strong> : 1 bit de signe + valeur</li>
  <li><strong>Complement a 1</strong> : inverser tous les bits</li>
  <li><strong>Complement a 2</strong> (le plus utilise) : complement a 1 + 1</li>
</ul>
<p>Sur n bits, plage : -2^(n-1) a 2^(n-1)-1<br/>
Exemple sur 8 bits : -128 a +127</p>

<h4>2. Algebre de Boole et logique combinatoire (15h)</h4>

<p><strong>Portes logiques fondamentales :</strong></p>

<table>
  <thead><tr><th>Porte</th><th>Symbole</th><th>Equation</th><th>Table de verite (A, B &rarr; S)</th></tr></thead>
  <tbody>
    <tr><td><strong>NOT</strong> (inverseur)</td><td>&not;A ou A'</td><td>S = NOT A</td><td>0&rarr;1, 1&rarr;0</td></tr>
    <tr><td><strong>AND</strong> (ET)</td><td>A &and; B</td><td>S = A AND B</td><td>00&rarr;0, 01&rarr;0, 10&rarr;0, 11&rarr;1</td></tr>
    <tr><td><strong>OR</strong> (OU)</td><td>A &or; B</td><td>S = A OR B</td><td>00&rarr;0, 01&rarr;1, 10&rarr;1, 11&rarr;1</td></tr>
    <tr><td><strong>NAND</strong> (NON-ET)</td><td>A &uarr; B</td><td>S = NOT (A AND B)</td><td>00&rarr;1, 01&rarr;1, 10&rarr;1, 11&rarr;0</td></tr>
    <tr><td><strong>NOR</strong> (NON-OU)</td><td>A &darr; B</td><td>S = NOT (A OR B)</td><td>00&rarr;1, 01&rarr;0, 10&rarr;0, 11&rarr;0</td></tr>
    <tr><td><strong>XOR</strong> (OU exclusif)</td><td>A &oplus; B</td><td>S = A XOR B</td><td>00&rarr;0, 01&rarr;1, 10&rarr;1, 11&rarr;0</td></tr>
    <tr><td><strong>XNOR</strong></td><td>A &#x2299; B</td><td>S = NOT (A XOR B)</td><td>00&rarr;1, 01&rarr;0, 10&rarr;0, 11&rarr;1</td></tr>
  </tbody>
</table>

<p><strong>Proprietes de l'algebre de Boole :</strong></p>
<ul>
  <li><strong>Commutativite</strong> : A AND B = B AND A</li>
  <li><strong>Associativite</strong> : (A AND B) AND C = A AND (B AND C)</li>
  <li><strong>Distributivite</strong> : A AND (B OR C) = (A AND B) OR (A AND C)</li>
  <li><strong>Element neutre</strong> : A AND 1 = A ; A OR 0 = A</li>
  <li><strong>Element absorbant</strong> : A AND 0 = 0 ; A OR 1 = 1</li>
  <li><strong>Idempotence</strong> : A AND A = A ; A OR A = A</li>
  <li><strong>Lois de Morgan</strong> :
    <ul>
      <li>NOT (A AND B) = (NOT A) OR (NOT B)</li>
      <li>NOT (A OR B) = (NOT A) AND (NOT B)</li>
    </ul>
  </li>
</ul>

<p><strong>Fonctions logiques et tables de verite :</strong></p>
<p>Exemple : Fonction S = (A AND B) OR (NOT C)</p>

<table>
  <thead><tr><th>A</th><th>B</th><th>C</th><th>NOT C</th><th>A AND B</th><th>S</th></tr></thead>
  <tbody>
    <tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr>
    <tr><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr>
    <tr><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr>
    <tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>
    <tr><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>
  </tbody>
</table>

<p><strong>Formes canoniques :</strong></p>
<ul>
  <li><strong>Somme de produits (SOP / minterms)</strong> : S = ABC' + A'B'C + ...</li>
  <li><strong>Produit de sommes (POS / maxterms)</strong> : S = (A+B+C')(A'+B'+C)...</li>
</ul>

<p><strong>Simplification par tableaux de Karnaugh :</strong></p>
<p>Tableau de Karnaugh pour 3 variables (A, B, C) :</p>
<pre><code>      C'  C
   +----+----+
AB' | 0  | 1  |
   +----+----+
A'B'| 2  | 3  |
   +----+----+
A'B | 6  | 7  |
   +----+----+
AB  | 4  | 5  |
   +----+----+</code></pre>

<p><em>Methode :</em></p>
<ol>
  <li>Remplir le tableau avec les valeurs de sortie</li>
  <li>Regrouper les '1' adjacents par puissances de 2 (1, 2, 4, 8...)</li>
  <li>Extraire les termes simplifies</li>
</ol>

<p><strong>Circuits combinatoires usuels :</strong></p>

<p><strong>Demi-additionneur (Half Adder) :</strong></p>
<ul>
  <li>Entrees : A, B</li>
  <li>Sorties : Somme = A XOR B ; Retenue = A AND B</li>
</ul>

<p><strong>Additionneur complet (Full Adder) :</strong></p>
<ul>
  <li>Entrees : A, B, Cin (retenue entrante)</li>
  <li>Sorties : Somme = A XOR B XOR Cin ; Cout = (A AND B) OR (Cin AND (A XOR B))</li>
</ul>

<p><strong>Multiplexeur (MUX) :</strong></p>
<ul>
  <li>Selectionne une entree parmi plusieurs selon des signaux de selection</li>
  <li>MUX 4:1 &rarr; 4 entrees, 2 bits de selection, 1 sortie</li>
</ul>

<p><strong>Demultiplexeur (DEMUX) :</strong></p>
<ul>
  <li>Inverse du MUX : 1 entree vers n sorties</li>
</ul>

<p><strong>Decodeur :</strong></p>
<ul>
  <li>Convertit un code binaire en activation d'une sortie</li>
  <li>Decodeur 3:8 &rarr; 3 entrees, 8 sorties (une seule active a la fois)</li>
</ul>

<p><strong>Encodeur :</strong></p>
<ul>
  <li>Inverse du decodeur : plusieurs entrees &rarr; code binaire</li>
</ul>

<p><strong>Comparateur :</strong></p>
<ul>
  <li>Compare deux nombres binaires</li>
  <li>Sorties : A&gt;B, A=B, A&lt;B</li>
</ul>

<h4>3. Logique sequentielle (12h)</h4>

<p><strong>Difference combinatoire/sequentiel :</strong></p>
<ul>
  <li><strong>Combinatoire</strong> : Sortie = f(Entrees actuelles)</li>
  <li><strong>Sequentiel</strong> : Sortie = f(Entrees + Etat precedent)
    <ul>
      <li>Notion de memoire</li>
      <li>Depend du temps (horloge)</li>
    </ul>
  </li>
</ul>

<p><strong>Bascules (Flip-Flops) :</strong></p>

<p><strong>Bascule RS (Reset-Set) :</strong></p>
<ul>
  <li>2 entrees : R (Reset), S (Set)</li>
  <li>2 sorties : Q, Q'</li>
  <li>Etats : Set (Q=1), Reset (Q=0), Memoire, <strong>Interdit</strong> (R=S=1)</li>
</ul>

<p><strong>Bascule D (Data) :</strong></p>
<ul>
  <li>1 entree : D</li>
  <li>Sur front d'horloge : Q &larr; D</li>
  <li>La plus utilisee (memorisation simple)</li>
</ul>

<p><strong>Bascule JK :</strong></p>
<ul>
  <li>2 entrees : J, K</li>
  <li>J=K=0 : Memoire</li>
  <li>J=1, K=0 : Set</li>
  <li>J=0, K=1 : Reset</li>
  <li>J=K=1 : Toggle (Q &larr; NOT Q)</li>
</ul>

<p><strong>Bascule T (Toggle) :</strong></p>
<ul>
  <li>1 entree : T</li>
  <li>Si T=1 : toggle a chaque front d'horloge</li>
</ul>

<p><strong>Registres :</strong></p>
<ul>
  <li><strong>Registre parallele</strong> : n bascules D pour stocker n bits simultanement</li>
  <li><strong>Registre a decalage</strong> : Les bits se decalent a chaque coup d'horloge
    <ul>
      <li>SISO (Serial In Serial Out)</li>
      <li>SIPO (Serial In Parallel Out)</li>
      <li>PISO (Parallel In Serial Out)</li>
      <li>PIPO (Parallel In Parallel Out)</li>
    </ul>
  </li>
</ul>

<p><strong>Compteurs :</strong></p>

<p><strong>Compteur asynchrone :</strong></p>
<ul>
  <li>Les bascules ne partagent pas la meme horloge</li>
  <li>Temps de propagation cumulatif</li>
  <li>Simple mais lent</li>
</ul>

<p><strong>Compteur synchrone :</strong></p>
<ul>
  <li>Toutes les bascules sur la meme horloge</li>
  <li>Plus rapide, prefere en pratique</li>
  <li>Compteur binaire, BCD, modulo-N</li>
</ul>

<p><strong>Machines a etats finis (FSM) :</strong></p>

<p><strong>Types :</strong></p>
<ul>
  <li><strong>Moore</strong> : Sorties dependent uniquement de l'etat</li>
  <li><strong>Mealy</strong> : Sorties dependent de l'etat ET des entrees</li>
</ul>

<p><strong>Diagramme d'etats :</strong></p>
<pre><code>     +------+  E=1  +------+
     |  S0  |------&gt;|  S1  |
     +------+       +------+
        ^              |
        +--------------+
           E=0</code></pre>

<p><strong>Etapes de conception :</strong></p>
<ol>
  <li>Diagramme d'etats</li>
  <li>Table de transition</li>
  <li>Codage des etats (binaire)</li>
  <li>Equations des bascules et sorties</li>
  <li>Implementation (schema ou VHDL)</li>
</ol>

<h4>4. Introduction au VHDL (20h)</h4>

<p><strong>VHDL = VHSIC Hardware Description Language</strong></p>
<ul>
  <li>Langage de description materiel (pas de programmation sequentielle classique)</li>
  <li>Decrit la structure et le comportement de circuits numeriques</li>
  <li>Synthetisable sur FPGA ou ASIC</li>
</ul>

<p><strong>Structure d'un code VHDL :</strong></p>
<pre><code>-- Bibliotheques
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Entite (interface externe)
entity PorteAND is
    Port (
        A : in STD_LOGIC;
        B : in STD_LOGIC;
        S : out STD_LOGIC
    );
end PorteAND;

-- Architecture (comportement interne)
architecture Behavioral of PorteAND is
begin
    S &lt;= A AND B;
end Behavioral;</code></pre>

<p><strong>Types de donnees :</strong></p>
<ul>
  <li><strong>STD_LOGIC</strong> : '0', '1', 'Z' (haute impedance), 'X' (inconnu)</li>
  <li><strong>STD_LOGIC_VECTOR</strong> : Bus de plusieurs bits
    <ul><li>Exemple : <code>signal bus : STD_LOGIC_VECTOR(7 downto 0);</code></li></ul>
  </li>
  <li><strong>INTEGER</strong> : Nombres entiers</li>
  <li><strong>BOOLEAN</strong> : TRUE, FALSE</li>
</ul>

<p><strong>Operateurs :</strong></p>
<ul>
  <li>Logiques : AND, OR, NOT, NAND, NOR, XOR, XNOR</li>
  <li>Arithmetiques : +, -, *, / (necessite <code>use IEEE.NUMERIC_STD.ALL;</code>)</li>
  <li>Comparaison : =, /=, &lt;, &gt;, &lt;=, &gt;=</li>
  <li>Concatenation : &amp;</li>
</ul>

<p><strong>Affectations :</strong></p>
<ul>
  <li><strong>Signal</strong> : <code>&lt;=</code> (affectation concurrente, hors process)</li>
  <li><strong>Variable</strong> : <code>:=</code> (affectation sequentielle, dans process)</li>
</ul>

<p><strong>Processus (PROCESS) :</strong></p>
<pre><code>process(clk, reset)  -- Liste de sensibilite
begin
    if reset = '1' then
        compteur &lt;= 0;
    elsif rising_edge(clk) then  -- Front montant d'horloge
        compteur &lt;= compteur + 1;
    end if;
end process;</code></pre>

<p><strong>Structures de controle :</strong></p>

<p><strong>IF-THEN-ELSE :</strong></p>
<pre><code>if (condition) then
    -- instructions
elsif (autre_condition) then
    -- instructions
else
    -- instructions
end if;</code></pre>

<p><strong>CASE :</strong></p>
<pre><code>case sel is
    when "00" =&gt; sortie &lt;= entree0;
    when "01" =&gt; sortie &lt;= entree1;
    when "10" =&gt; sortie &lt;= entree2;
    when others =&gt; sortie &lt;= entree3;
end case;</code></pre>

<p><strong>FOR LOOP :</strong></p>
<pre><code>for i in 0 to 7 loop
    sortie(i) &lt;= entree(7-i);  -- Inversion de bus
end loop;</code></pre>

<p><strong>Exemple complet : Compteur 8 bits</strong></p>
<pre><code>library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity Compteur8bits is
    Port (
        clk : in STD_LOGIC;
        reset : in STD_LOGIC;
        enable : in STD_LOGIC;
        count : out STD_LOGIC_VECTOR(7 downto 0)
    );
end Compteur8bits;

architecture Behavioral of Compteur8bits is
    signal compteur : unsigned(7 downto 0) := (others =&gt; '0');
begin
    process(clk, reset)
    begin
        if reset = '1' then
            compteur &lt;= (others =&gt; '0');
        elsif rising_edge(clk) then
            if enable = '1' then
                compteur &lt;= compteur + 1;
            end if;
        end if;
    end process;

    count &lt;= std_logic_vector(compteur);
end Behavioral;</code></pre>

<h3>Travaux pratiques</h3>

<h4>TP1 : Prise en main de Quartus Prime</h4>
<ul>
  <li>Installation et configuration</li>
  <li>Creation d'un projet</li>
  <li>Saisie schematique (portes logiques)</li>
  <li>Compilation et analyse</li>
  <li>Assignement des pins (carte FPGA)</li>
  <li>Programmation du FPGA</li>
</ul>

<h4>TP2 : Circuits combinatoires</h4>
<ul>
  <li>Decodeur BCD vers 7 segments</li>
  <li>Multiplexeur 4:1</li>
  <li>Additionneur 4 bits</li>
  <li>Tests et validation</li>
</ul>

<h4>TP3 : Introduction VHDL</h4>
<ul>
  <li>Portes logiques en VHDL</li>
  <li>Multiplexeur en VHDL</li>
  <li>Simulation avec ModelSim</li>
  <li>Synthese et programmation</li>
</ul>

<h4>TP4 : Logique sequentielle</h4>
<ul>
  <li>Bascules D et JK</li>
  <li>Registres a decalage</li>
  <li>Compteurs (up, down, modulo)</li>
  <li>Diviseur de frequence</li>
</ul>

<h4>TP5 : Machine a etats finis</h4>
<ul>
  <li>Conception d'une FSM (feu tricolore, distributeur, etc.)</li>
  <li>Implementation en VHDL</li>
  <li>Tests sur FPGA</li>
  <li>Validation fonctionnelle</li>
</ul>

<hr/>

<h2>PART C: ASPECTS TECHNIQUES</h2>

<h3>Outils de conception</h3>

<h4>Intel Quartus Prime</h4>

<p><strong>Installation :</strong></p>
<ul>
  <li>Version Lite (gratuite) : Jusqu'a 32k elements logiques</li>
  <li>Compatible Windows/Linux</li>
  <li>Telechargement : ~5-6 GB</li>
</ul>

<p><strong>Workflow de conception :</strong></p>
<ol>
  <li><strong>Creation projet</strong> : File &rarr; New Project Wizard</li>
  <li><strong>Ajout fichiers</strong> : .vhd, .v, ou schema</li>
  <li><strong>Compilation</strong> : Processing &rarr; Start Compilation (Ctrl+L)</li>
  <li><strong>Analyse</strong> : Compilation Report (ressources, timing, etc.)</li>
  <li><strong>Assignement pins</strong> : Assignments &rarr; Pin Planner</li>
  <li><strong>Programmation</strong> : Tools &rarr; Programmer</li>
</ol>

<p><strong>Analyses disponibles :</strong></p>
<ul>
  <li><strong>RTL Viewer</strong> : Visualisation schema synthetise</li>
  <li><strong>Technology Map Viewer</strong> : Mapping sur elements FPGA</li>
  <li><strong>Timing Analyzer</strong> : Analyse des chemins critiques</li>
  <li><strong>Resource Usage</strong> : LUTs, registres, memoire utilises</li>
</ul>

<h4>ModelSim (Simulation)</h4>

<p><strong>Fonctionnalites :</strong></p>
<ul>
  <li>Simulation comportementale (avant synthese)</li>
  <li>Simulation post-synthese (avec delais reels)</li>
  <li>Waveform viewer (chronogrammes)</li>
  <li>Testbenches VHDL</li>
</ul>

<p><strong>Exemple de testbench :</strong></p>
<pre><code>library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Compteur_TB is
end Compteur_TB;

architecture Behavioral of Compteur_TB is
    component Compteur8bits
        Port (clk, reset, enable : in STD_LOGIC;
              count : out STD_LOGIC_VECTOR(7 downto 0));
    end component;

    signal clk_tb, reset_tb, enable_tb : STD_LOGIC := '0';
    signal count_tb : STD_LOGIC_VECTOR(7 downto 0);
    constant clk_period : time := 10 ns;

begin
    UUT: Compteur8bits port map(clk_tb, reset_tb, enable_tb, count_tb);

    -- Generation horloge
    clk_process : process
    begin
        clk_tb &lt;= '0';
        wait for clk_period/2;
        clk_tb &lt;= '1';
        wait for clk_period/2;
    end process;

    -- Stimulus
    stim_proc: process
    begin
        reset_tb &lt;= '1';
        wait for 20 ns;
        reset_tb &lt;= '0';
        enable_tb &lt;= '1';
        wait for 1000 ns;
        enable_tb &lt;= '0';
        wait;
    end process;
end Behavioral;</code></pre>

<h3>Cartes FPGA utilisees</h3>

<h4>Altera/Intel Cyclone IV/V</h4>

<p><strong>Caracteristiques :</strong></p>
<ul>
  <li>6K - 115K elements logiques</li>
  <li>Memoire embarquee (M9K blocks)</li>
  <li>PLL (Phase-Locked Loops) pour gestion horloges</li>
  <li>DSP blocks (multiplieurs materiels)</li>
  <li>GPIO configurable (LVTTL, LVCMOS, LVDS)</li>
</ul>

<p><strong>Cartes de developpement :</strong></p>
<ul>
  <li><strong>DE0-Nano</strong> : Cyclone IV, compacte, ~80&euro;</li>
  <li><strong>DE1-SoC</strong> : Cyclone V + ARM Cortex-A9, ~200&euro;</li>
  <li><strong>DE2-115</strong> : Cyclone IV, nombreux peripheriques, ~300&euro;</li>
</ul>

<p><strong>Peripheriques typiques :</strong></p>
<ul>
  <li>LEDs, boutons poussoirs, switches</li>
  <li>Afficheurs 7 segments</li>
  <li>VGA/HDMI</li>
  <li>GPIO (connecteurs d'extension)</li>
  <li>USB, Ethernet (selon modele)</li>
</ul>

<h3>Methodologie de conception</h3>

<h4>Bonnes pratiques VHDL</h4>

<p><strong>Nommage :</strong></p>
<ul>
  <li>Signaux/variables : lowercase_avec_underscores</li>
  <li>Constantes : UPPERCASE</li>
  <li>Entites/architectures : CamelCase</li>
</ul>

<p><strong>Commentaires :</strong></p>
<pre><code>-- Commentaire ligne simple

--======================
-- Bloc de commentaire
--======================</code></pre>

<p><strong>Conception synchrone :</strong></p>
<ul>
  <li>Toujours utiliser une horloge unique si possible</li>
  <li>Eviter les logiques asynchrones complexes</li>
  <li>Reinitialiser les signaux (reset)</li>
</ul>

<p><strong>Testabilite :</strong></p>
<ul>
  <li>Creer des testbenches systematiquement</li>
  <li>Tester les cas limites</li>
  <li>Verifier le timing (setup/hold)</li>
</ul>

<h4>Debogage</h4>

<p><strong>Erreurs de compilation courantes :</strong></p>
<ul>
  <li><code>Signal not declared</code> &rarr; Oublie de declarer le signal</li>
  <li><code>Multiple drivers</code> &rarr; Signal assigne a plusieurs endroits</li>
  <li><code>Type mismatch</code> &rarr; Conversion de type necessaire (std_logic_vector &harr; unsigned)</li>
</ul>

<p><strong>Outils de debogage :</strong></p>
<ul>
  <li><strong>SignalTap II</strong> (Quartus) : Analyseur logique interne au FPGA</li>
  <li><strong>Simulation</strong> : Toujours simuler avant de synthetiser</li>
  <li><strong>LEDs de debug</strong> : Afficher des etats internes</li>
</ul>

<hr/>

<h2>PART D: ANALYSE ET REFLEXION</h2>

<h3>Evaluation des competences</h3>

<h4>Modalites d'evaluation</h4>

<p><strong>Controle continu (40%) :</strong></p>
<ul>
  <li>QCM theoriques (2x1h) : Algebre de Boole, logique sequentielle - 20%</li>
  <li>Tests pratiques Quartus (2x1h30) - 20%</li>
</ul>

<p><strong>Travaux pratiques (35%) :</strong></p>
<ul>
  <li>5 TP notes avec rapports</li>
  <li>Evaluation : montage fonctionnel, code VHDL, tests, documentation</li>
</ul>

<p><strong>Projet (15%) :</strong></p>
<ul>
  <li>Mini-projet VHDL (machine a etats + compteur + affichage)</li>
  <li>Demo sur carte FPGA</li>
  <li>Code source commente</li>
  <li>Rapport technique</li>
</ul>

<p><strong>Examen terminal (10%) :</strong></p>
<ul>
  <li>Epreuve theorique (1h30)</li>
  <li>Tableaux de Karnaugh, chronogrammes, VHDL</li>
</ul>

<h4>Grille d'evaluation TP</h4>

<table>
  <thead><tr><th>Critere</th><th>Points</th></tr></thead>
  <tbody>
    <tr><td><strong>Fonctionnalite</strong> : Circuit fonctionne sur FPGA</td><td>/6</td></tr>
    <tr><td><strong>Code VHDL</strong> : Qualite, clarte, commentaires</td><td>/5</td></tr>
    <tr><td><strong>Simulation</strong> : Testbench et chronogrammes</td><td>/4</td></tr>
    <tr><td><strong>Tests</strong> : Validation complete</td><td>/3</td></tr>
    <tr><td><strong>Rapport</strong> : Clarte, schemas, analyses</td><td>/2</td></tr>
    <tr><td><strong>Total</strong></td><td><strong>/20</strong></td></tr>
  </tbody>
</table>

<h3>Competences acquises</h3>

<h4>Savoirs theoriques</h4>
<ul>
  <li>Maitriser l'algebre de Boole et les systemes de numeration</li>
  <li>Comprendre la logique combinatoire et sequentielle</li>
  <li>Connaitre les circuits numeriques fondamentaux</li>
  <li>Comprendre les principes des FPGA</li>
</ul>

<h4>Savoir-faire techniques</h4>
<ul>
  <li>Concevoir des circuits numeriques (combinatoires et sequentiels)</li>
  <li>Simplifier des fonctions logiques (Karnaugh)</li>
  <li>Programmer en VHDL</li>
  <li>Simuler et valider des designs numeriques</li>
  <li>Synthetiser et programmer des FPGA avec Quartus</li>
  <li>Deboguer des circuits numeriques</li>
</ul>

<h4>Savoir-etre</h4>
<ul>
  <li>Rigueur dans la conception (chronogrammes, timing)</li>
  <li>Methodologie de test et validation</li>
  <li>Documentation technique claire</li>
  <li>Travail en equipe sur projets</li>
</ul>

<h3>Progression et liens avec le cursus</h3>

<h4>Suite du parcours Systemes Numeriques</h4>

<table>
  <thead><tr><th>Semestre</th><th>Module</th><th>Contenu</th></tr></thead>
  <tbody>
    <tr><td><strong>S1</strong></td><td>SIN 1</td><td>Logique combinatoire, sequentielle, VHDL de base</td></tr>
    <tr><td><strong>S2</strong></td><td>Logique Sequentielle</td><td>FSM avancees, FIFO, memoires, bus</td></tr>
    <tr><td><strong>S3</strong></td><td>Architectures Numeriques Avancees</td><td>Processeurs, pipelines, VHDL avance</td></tr>
    <tr><td><strong>S4</strong></td><td>Projet FPGA</td><td>Conception systeme complet (SoC)</td></tr>
  </tbody>
</table>

<h4>Liens avec les autres matieres</h4>

<table>
  <thead><tr><th>Matiere</th><th>Utilisation des systemes numeriques</th></tr></thead>
  <tbody>
    <tr><td><strong>Programmation</strong></td><td>Similarites algorithmes/FSM</td></tr>
    <tr><td><strong>Informatique Embarquee</strong></td><td>Microcontroleurs (logique interne)</td></tr>
    <tr><td><strong>Electronique</strong></td><td>Interface analogique/numerique (ADC, DAC)</td></tr>
    <tr><td><strong>Automatique</strong></td><td>Controleurs numeriques, regulateurs discrets</td></tr>
    <tr><td><strong>Telecommunications</strong></td><td>Modulation/demodulation numerique</td></tr>
  </tbody>
</table>

<h3>Indicateurs de reussite</h3>

<h4>Statistiques</h4>
<p><strong>Taux de reussite :</strong> 88%<br/>
<strong>Moyenne generale :</strong> 12.8/20</p>

<p><strong>Difficultes frequentes :</strong></p>
<ul>
  <li>Confusion entre logique combinatoire et sequentielle</li>
  <li>Oubli de la liste de sensibilite dans les process</li>
  <li>Conversions de types en VHDL</li>
  <li>Timing (setup/hold violations)</li>
  <li>Simplification par Karnaugh (regroupements)</li>
</ul>

<p><strong>Cles de reussite :</strong></p>
<ul>
  <li>Dessiner les chronogrammes avant de coder</li>
  <li>Toujours simuler avant de synthetiser</li>
  <li>Commencer simple, complexifier progressivement</li>
  <li>Utiliser les exemples de code fournis</li>
  <li>Tester sur carte FPGA regulierement</li>
</ul>

<h3>Debouches et applications</h3>

<h4>Applications professionnelles</h4>

<p><strong>Metiers utilisant les FPGA/VHDL :</strong></p>
<ul>
  <li>Ingenieur FPGA (aeronautique, spatial, defense)</li>
  <li>Concepteur de circuits ASIC</li>
  <li>Ingenieur en traitement du signal numerique</li>
  <li>Developpeur systemes embarques critiques</li>
  <li>Architecte materiel (hardware architect)</li>
</ul>

<p><strong>Industries :</strong></p>
<ul>
  <li><strong>Aeronautique/Spatial</strong> : Systemes critiques, resistance radiations</li>
  <li><strong>Telecommunications</strong> : Modems, routeurs, 5G</li>
  <li><strong>Automobile</strong> : ADAS, controle moteur</li>
  <li><strong>Medical</strong> : Imagerie (echographie, IRM), appareils de diagnostic</li>
  <li><strong>Finance</strong> : Trading haute frequence (FPGA pour latence ultra-faible)</li>
  <li><strong>IA</strong> : Accelerateurs materiels (inference neuronale)</li>
</ul>

<hr/>

<h2>Ressources complementaires</h2>

<h3>Ouvrages de reference</h3>

<p><strong>Logique numerique :</strong></p>
<ol>
  <li><em>Systemes logiques - Tome 1 et 2</em> - A. Vachoux (PPUR) - Reference francophone</li>
  <li><em>Digital Design</em> - M. Morris Mano (Pearson) - Classique mondial</li>
  <li><em>Circuits numeriques et synthese logique</em> - Jacques Weber (Eyrolles)</li>
</ol>

<p><strong>VHDL :</strong></p>
<ul>
  <li><em>VHDL - Du langage a la modelisation</em> - Jacques Weber (Dunod)</li>
  <li><em>Free Range VHDL</em> - Bryan Mealy (gratuit en ligne)</li>
  <li><em>VHDL for Engineers</em> - Kenneth L. Short (Pearson)</li>
</ul>

<h3>Sites web et tutoriels</h3>

<p><strong>Cours en ligne :</strong></p>
<ul>
  <li><strong>VHDL Whiz</strong> (vhdlwhiz.com) - Tutoriels video gratuits</li>
  <li><strong>Nandland</strong> (nandland.com) - Projets FPGA pour debutants</li>
  <li><strong>FPGA4Fun</strong> (fpga4fun.com) - Nombreux exemples VHDL</li>
</ul>

<p><strong>Forums et communautes :</strong></p>
<ul>
  <li><strong>Reddit</strong> : r/FPGA</li>
  <li><strong>EDAboard</strong> : Forum specialise FPGA/VHDL</li>
  <li><strong>Stack Overflow</strong> : Tag [vhdl]</li>
</ul>

<p><strong>Simulateurs en ligne :</strong></p>
<ul>
  <li><strong>CircuitVerse</strong> (circuitverse.org) - Logique digitale interactive</li>
  <li><strong>EDA Playground</strong> (edaplayground.com) - Simulation VHDL en ligne</li>
</ul>

<h3>Logiciels libres alternatifs</h3>
<ul>
  <li><strong>GHDL</strong> : Simulateur VHDL open source</li>
  <li><strong>GTKWave</strong> : Visualisateur de formes d'ondes</li>
  <li><strong>Icarus Verilog</strong> : Si vous voulez apprendre Verilog aussi</li>
</ul>

<hr/>

<h2>Conseils methodologiques</h2>

<h3>Pour reussir en systemes numeriques</h3>

<p><strong>Pendant les cours/TD :</strong></p>
<ul>
  <li>Dessiner les circuits au fur et a mesure</li>
  <li>Refaire les simplifications de Karnaugh chez soi</li>
  <li>Comprendre les chronogrammes (temps = horizontal)</li>
</ul>

<p><strong>En TP :</strong></p>
<ul>
  <li>Lire le sujet entierement avant de commencer</li>
  <li>Concevoir sur papier avant de coder</li>
  <li>Simuler systematiquement avant de programmer le FPGA</li>
  <li>Sauvegarder frequemment son projet</li>
  <li>Tester progressivement (fonction par fonction)</li>
</ul>

<p><strong>Travail personnel (2-3h/semaine) :</strong></p>
<ul>
  <li>Refaire les exercices de simplification</li>
  <li>Creer ses propres petits circuits en VHDL</li>
  <li>Regarder des tutoriels video (Nandland, VHDL Whiz)</li>
  <li>Pratiquer les conversions de bases</li>
</ul>

<h3>Erreurs a eviter</h3>
<ul>
  <li>Oublier <code>rising_edge(clk)</code> dans les process synchrones</li>
  <li>Melanger affectations <code>&lt;=</code> et <code>:=</code></li>
  <li>Negliger les types (STD_LOGIC vs INTEGER vs UNSIGNED)</li>
  <li>Creer des boucles combinatoires (A depend de A)</li>
  <li>Ne pas tester les cas limites (reset, overflow, etc.)</li>
</ul>

<p><strong>Bonnes pratiques :</strong></p>
<ul>
  <li>Toujours declarer un signal de reset</li>
  <li>Utiliser des noms de signaux explicites</li>
  <li>Commenter son code VHDL</li>
  <li>Verifier le Resource Usage apres compilation</li>
  <li>Documenter ses montages avec schemas</li>
</ul>

<hr/>

<p><strong>Bon courage dans la decouverte passionnante des systemes numeriques !</strong></p>

<blockquote><p>"In theory, theory and practice are the same. In practice, they are not." - Yogi Berra</p></blockquote>

<p>En systemes numeriques, la simulation et les tests sur materiel reel sont essentiels. N'hesitez pas a experimenter sur les cartes FPGA !</p>

<ul>
  <li><strong>Programmation</strong> : Structures de controle et algorithmique</li>
  <li><strong>ER (Electronique et Realisation)</strong> : Interface analogique/numerique</li>
  <li><strong>Mathematiques</strong> : Algebre de Boole</li>
</ul>

<h2>Ressources complementaires</h2>
<ul>
  <li>Documentation Intel Quartus</li>
  <li>Tutoriels VHDL</li>
  <li>Datasheets des composants FPGA</li>
</ul>

</div>

<div class="lang-en">

<h1>Digital Systems (SIN) - Semester 1</h1>

<h2>PART A - General Course Overview</h2>

<h3>Training Context</h3>
<p>Digital systems are at the heart of all modern electronic equipment: computers, smartphones, embedded systems, and industrial automation. This module introduces the foundations of digital logic and digital circuit design, essential skills for any GEII technician or engineer. Mastering VHDL (hardware description language) enables the design of complex digital systems on FPGAs.</p>

<h3>Position in the Curriculum</h3>
<ul>
  <li><strong>Semester</strong>: S1 (1st year DUT GEII)</li>
  <li><strong>Course hours</strong>: 65h (25h lectures + 20h tutorials + 20h lab sessions)</li>
  <li><strong>ECTS credits</strong>: 6</li>
  <li><strong>Prerequisites</strong>: Basic mathematics knowledge (binary, Boolean)</li>
  <li><strong>Continuation</strong>: Sequential Logic (S2), Advanced Digital Architectures (S3-S4)</li>
</ul>

<h3>Target Audience</h3>
<p>First-year DUT GEII students discovering digital circuit design from the basics (logic gates) to FPGA programming in VHDL.</p>

<hr/>

<h2>PART B: EXPERIENCE, CONTEXT AND FUNCTION</h2>

<h3>Learning Objectives</h3>

<p><strong>Digital logic skills:</strong></p>
<ul>
  <li>Master number systems and conversions</li>
  <li>Understand and apply Boolean algebra</li>
  <li>Design combinational and sequential circuits</li>
  <li>Simplify logic functions</li>
</ul>

<p><strong>VHDL and FPGA skills:</strong></p>
<ul>
  <li>Write VHDL code to describe circuits</li>
  <li>Simulate and validate digital designs</li>
  <li>Synthesize and program FPGAs</li>
  <li>Use the Quartus Prime environment (Intel/Altera)</li>
</ul>

<p><strong>Cross-cutting skills:</strong></p>
<ul>
  <li>Analyze a problem and translate it into a logic circuit</li>
  <li>Test and debug digital systems</li>
  <li>Document designs</li>
</ul>

<h3>Detailed Syllabus</h3>

<h4>1. Number Systems (8h)</h4>

<p><strong>Number bases:</strong></p>

<p><strong>Binary (base 2):</strong></p>
<ul>
  <li>Digits: 0, 1</li>
  <li>Example: 1011&#x2082; = 1x2&#xB3; + 0x2&#xB2; + 1x2&#xB9; + 1x2&#x2070; = 11&#x2081;&#x2080;</li>
</ul>

<p><strong>Octal (base 8):</strong></p>
<ul>
  <li>Digits: 0-7</li>
  <li>Historically used, less common today</li>
  <li>Easy conversion: 3 binary bits = 1 octal digit</li>
</ul>

<p><strong>Hexadecimal (base 16):</strong></p>
<ul>
  <li>Digits: 0-9, A-F (A=10, B=11, ..., F=15)</li>
  <li>Widely used in computing (memory addresses, RGB colors)</li>
  <li>Conversion: 4 binary bits = 1 hexadecimal digit</li>
  <li>Example: 0xA3 = 10100011&#x2082; = 163&#x2081;&#x2080;</li>
</ul>

<p><strong>Base conversions:</strong></p>

<p><em>Decimal &rarr; Binary (successive divisions):</em></p>
<pre><code>45&#x2081;&#x2080; &rarr; Binary?
45 / 2 = 22 remainder 1  (least significant bit)
22 / 2 = 11 remainder 0
11 / 2 = 5 remainder 1
5 / 2 = 2 remainder 1
2 / 2 = 1 remainder 0
1 / 2 = 0 remainder 1  (most significant bit)
Result: 101101&#x2082;</code></pre>

<p><em>Binary &rarr; Hexadecimal (groups of 4 bits):</em></p>
<pre><code>11010110&#x2082; = 1101 0110 = D6&#x2081;&#x2086;</code></pre>

<p><strong>Digital codes:</strong></p>

<p><strong>BCD (Binary Coded Decimal):</strong></p>
<ul>
  <li>Each decimal digit encoded on 4 bits</li>
  <li>Example: 95&#x2081;&#x2080; = 1001 0101 (BCD) &ne; 1011111&#x2082; (pure binary)</li>
  <li>Used in 7-segment displays</li>
</ul>

<p><strong>Gray Code:</strong></p>
<ul>
  <li>Only one bit changes between two consecutive values</li>
  <li>Reduces errors during transitions</li>
  <li>Used in rotary encoders</li>
</ul>

<table>
  <thead><tr><th>Decimal</th><th>Binary</th><th>Gray</th></tr></thead>
  <tbody>
    <tr><td>0</td><td>000</td><td>000</td></tr>
    <tr><td>1</td><td>001</td><td>001</td></tr>
    <tr><td>2</td><td>010</td><td>011</td></tr>
    <tr><td>3</td><td>011</td><td>010</td></tr>
    <tr><td>4</td><td>100</td><td>110</td></tr>
  </tbody>
</table>

<p><strong>ASCII Code:</strong></p>
<ul>
  <li>7 bits to encode characters (letters, digits, symbols)</li>
  <li>Example: 'A' = 65&#x2081;&#x2080; = 01000001&#x2082;</li>
</ul>

<p><strong>Binary arithmetic:</strong></p>

<p><strong>Binary addition:</strong></p>
<pre><code>  1011  (11)
+ 0110  (6)
-------
 10001  (17)

Rules: 0+0=0, 0+1=1, 1+1=10 (carry)</code></pre>

<p><strong>Binary subtraction (two's complement):</strong></p>
<pre><code>A - B = A + (-B)
-B = one's complement of B + 1

Example: 7 - 3
7 = 0111
3 = 0011 &rarr; One's complement: 1100 &rarr; +1: 1101 (-3)
0111 + 1101 = 10100 &rarr; keep the 4 least significant bits: 0100 = 4</code></pre>

<p><strong>Signed number representation:</strong></p>
<ul>
  <li><strong>Sign + absolute value</strong>: 1 sign bit + value</li>
  <li><strong>One's complement</strong>: invert all bits</li>
  <li><strong>Two's complement</strong> (most commonly used): one's complement + 1</li>
</ul>
<p>On n bits, range: -2^(n-1) to 2^(n-1)-1<br/>
Example on 8 bits: -128 to +127</p>

<h4>2. Boolean Algebra and Combinational Logic (15h)</h4>

<p><strong>Fundamental logic gates:</strong></p>

<table>
  <thead><tr><th>Gate</th><th>Symbol</th><th>Equation</th><th>Truth Table (A, B &rarr; S)</th></tr></thead>
  <tbody>
    <tr><td><strong>NOT</strong> (inverter)</td><td>&not;A or A'</td><td>S = NOT A</td><td>0&rarr;1, 1&rarr;0</td></tr>
    <tr><td><strong>AND</strong></td><td>A &and; B</td><td>S = A AND B</td><td>00&rarr;0, 01&rarr;0, 10&rarr;0, 11&rarr;1</td></tr>
    <tr><td><strong>OR</strong></td><td>A &or; B</td><td>S = A OR B</td><td>00&rarr;0, 01&rarr;1, 10&rarr;1, 11&rarr;1</td></tr>
    <tr><td><strong>NAND</strong></td><td>A &uarr; B</td><td>S = NOT (A AND B)</td><td>00&rarr;1, 01&rarr;1, 10&rarr;1, 11&rarr;0</td></tr>
    <tr><td><strong>NOR</strong></td><td>A &darr; B</td><td>S = NOT (A OR B)</td><td>00&rarr;1, 01&rarr;0, 10&rarr;0, 11&rarr;0</td></tr>
    <tr><td><strong>XOR</strong> (exclusive OR)</td><td>A &oplus; B</td><td>S = A XOR B</td><td>00&rarr;0, 01&rarr;1, 10&rarr;1, 11&rarr;0</td></tr>
    <tr><td><strong>XNOR</strong></td><td>A &#x2299; B</td><td>S = NOT (A XOR B)</td><td>00&rarr;1, 01&rarr;0, 10&rarr;0, 11&rarr;1</td></tr>
  </tbody>
</table>

<p><strong>Boolean algebra properties:</strong></p>
<ul>
  <li><strong>Commutativity</strong>: A AND B = B AND A</li>
  <li><strong>Associativity</strong>: (A AND B) AND C = A AND (B AND C)</li>
  <li><strong>Distributivity</strong>: A AND (B OR C) = (A AND B) OR (A AND C)</li>
  <li><strong>Identity element</strong>: A AND 1 = A ; A OR 0 = A</li>
  <li><strong>Annihilator</strong>: A AND 0 = 0 ; A OR 1 = 1</li>
  <li><strong>Idempotence</strong>: A AND A = A ; A OR A = A</li>
  <li><strong>De Morgan's laws</strong>:
    <ul>
      <li>NOT (A AND B) = (NOT A) OR (NOT B)</li>
      <li>NOT (A OR B) = (NOT A) AND (NOT B)</li>
    </ul>
  </li>
</ul>

<p><strong>Logic functions and truth tables:</strong></p>
<p>Example: Function S = (A AND B) OR (NOT C)</p>

<table>
  <thead><tr><th>A</th><th>B</th><th>C</th><th>NOT C</th><th>A AND B</th><th>S</th></tr></thead>
  <tbody>
    <tr><td>0</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr>
    <tr><td>0</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td><td>1</td></tr>
    <tr><td>0</td><td>1</td><td>1</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>1</td><td>0</td><td>0</td><td>1</td><td>0</td><td>1</td></tr>
    <tr><td>1</td><td>0</td><td>1</td><td>0</td><td>0</td><td>0</td></tr>
    <tr><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td><td>1</td></tr>
    <tr><td>1</td><td>1</td><td>1</td><td>0</td><td>1</td><td>1</td></tr>
  </tbody>
</table>

<p><strong>Canonical forms:</strong></p>
<ul>
  <li><strong>Sum of Products (SOP / minterms)</strong>: S = ABC' + A'B'C + ...</li>
  <li><strong>Product of Sums (POS / maxterms)</strong>: S = (A+B+C')(A'+B'+C)...</li>
</ul>

<p><strong>Simplification using Karnaugh maps:</strong></p>
<p>Karnaugh map for 3 variables (A, B, C):</p>
<pre><code>      C'  C
   +----+----+
AB' | 0  | 1  |
   +----+----+
A'B'| 2  | 3  |
   +----+----+
A'B | 6  | 7  |
   +----+----+
AB  | 4  | 5  |
   +----+----+</code></pre>

<p><em>Method:</em></p>
<ol>
  <li>Fill the table with output values</li>
  <li>Group adjacent '1's by powers of 2 (1, 2, 4, 8...)</li>
  <li>Extract the simplified terms</li>
</ol>

<p><strong>Common combinational circuits:</strong></p>

<p><strong>Half Adder:</strong></p>
<ul>
  <li>Inputs: A, B</li>
  <li>Outputs: Sum = A XOR B ; Carry = A AND B</li>
</ul>

<p><strong>Full Adder:</strong></p>
<ul>
  <li>Inputs: A, B, Cin (carry in)</li>
  <li>Outputs: Sum = A XOR B XOR Cin ; Cout = (A AND B) OR (Cin AND (A XOR B))</li>
</ul>

<p><strong>Multiplexer (MUX):</strong></p>
<ul>
  <li>Selects one input among several according to selection signals</li>
  <li>MUX 4:1 &rarr; 4 inputs, 2 selection bits, 1 output</li>
</ul>

<p><strong>Demultiplexer (DEMUX):</strong></p>
<ul>
  <li>Inverse of MUX: 1 input to n outputs</li>
</ul>

<p><strong>Decoder:</strong></p>
<ul>
  <li>Converts a binary code to activation of one output</li>
  <li>Decoder 3:8 &rarr; 3 inputs, 8 outputs (only one active at a time)</li>
</ul>

<p><strong>Encoder:</strong></p>
<ul>
  <li>Inverse of decoder: multiple inputs &rarr; binary code</li>
</ul>

<p><strong>Comparator:</strong></p>
<ul>
  <li>Compares two binary numbers</li>
  <li>Outputs: A&gt;B, A=B, A&lt;B</li>
</ul>

<h4>3. Sequential Logic (12h)</h4>

<p><strong>Combinational vs. sequential difference:</strong></p>
<ul>
  <li><strong>Combinational</strong>: Output = f(Current inputs)</li>
  <li><strong>Sequential</strong>: Output = f(Inputs + Previous state)
    <ul>
      <li>Memory concept</li>
      <li>Depends on time (clock)</li>
    </ul>
  </li>
</ul>

<p><strong>Flip-Flops:</strong></p>

<p><strong>RS Flip-Flop (Reset-Set):</strong></p>
<ul>
  <li>2 inputs: R (Reset), S (Set)</li>
  <li>2 outputs: Q, Q'</li>
  <li>States: Set (Q=1), Reset (Q=0), Memory, <strong>Forbidden</strong> (R=S=1)</li>
</ul>

<p><strong>D Flip-Flop (Data):</strong></p>
<ul>
  <li>1 input: D</li>
  <li>On clock edge: Q &larr; D</li>
  <li>The most commonly used (simple storage)</li>
</ul>

<p><strong>JK Flip-Flop:</strong></p>
<ul>
  <li>2 inputs: J, K</li>
  <li>J=K=0: Memory</li>
  <li>J=1, K=0: Set</li>
  <li>J=0, K=1: Reset</li>
  <li>J=K=1: Toggle (Q &larr; NOT Q)</li>
</ul>

<p><strong>T Flip-Flop (Toggle):</strong></p>
<ul>
  <li>1 input: T</li>
  <li>If T=1: toggles on each clock edge</li>
</ul>

<p><strong>Registers:</strong></p>
<ul>
  <li><strong>Parallel register</strong>: n D flip-flops to store n bits simultaneously</li>
  <li><strong>Shift register</strong>: Bits shift on each clock cycle
    <ul>
      <li>SISO (Serial In Serial Out)</li>
      <li>SIPO (Serial In Parallel Out)</li>
      <li>PISO (Parallel In Serial Out)</li>
      <li>PIPO (Parallel In Parallel Out)</li>
    </ul>
  </li>
</ul>

<p><strong>Counters:</strong></p>

<p><strong>Asynchronous counter:</strong></p>
<ul>
  <li>Flip-flops do not share the same clock</li>
  <li>Cumulative propagation delay</li>
  <li>Simple but slow</li>
</ul>

<p><strong>Synchronous counter:</strong></p>
<ul>
  <li>All flip-flops on the same clock</li>
  <li>Faster, preferred in practice</li>
  <li>Binary counter, BCD, modulo-N</li>
</ul>

<p><strong>Finite State Machines (FSM):</strong></p>

<p><strong>Types:</strong></p>
<ul>
  <li><strong>Moore</strong>: Outputs depend only on the state</li>
  <li><strong>Mealy</strong>: Outputs depend on the state AND the inputs</li>
</ul>

<p><strong>State diagram:</strong></p>
<pre><code>     +------+  E=1  +------+
     |  S0  |------&gt;|  S1  |
     +------+       +------+
        ^              |
        +--------------+
           E=0</code></pre>

<p><strong>Design steps:</strong></p>
<ol>
  <li>State diagram</li>
  <li>Transition table</li>
  <li>State encoding (binary)</li>
  <li>Flip-flop and output equations</li>
  <li>Implementation (schematic or VHDL)</li>
</ol>

<h4>4. Introduction to VHDL (20h)</h4>

<p><strong>VHDL = VHSIC Hardware Description Language</strong></p>
<ul>
  <li>Hardware description language (not classical sequential programming)</li>
  <li>Describes the structure and behavior of digital circuits</li>
  <li>Synthesizable on FPGA or ASIC</li>
</ul>

<p><strong>VHDL code structure:</strong></p>
<pre><code>-- Libraries
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Entity (external interface)
entity PorteAND is
    Port (
        A : in STD_LOGIC;
        B : in STD_LOGIC;
        S : out STD_LOGIC
    );
end PorteAND;

-- Architecture (internal behavior)
architecture Behavioral of PorteAND is
begin
    S &lt;= A AND B;
end Behavioral;</code></pre>

<p><strong>Data types:</strong></p>
<ul>
  <li><strong>STD_LOGIC</strong>: '0', '1', 'Z' (high impedance), 'X' (unknown)</li>
  <li><strong>STD_LOGIC_VECTOR</strong>: Multi-bit bus
    <ul><li>Example: <code>signal bus : STD_LOGIC_VECTOR(7 downto 0);</code></li></ul>
  </li>
  <li><strong>INTEGER</strong>: Integer numbers</li>
  <li><strong>BOOLEAN</strong>: TRUE, FALSE</li>
</ul>

<p><strong>Operators:</strong></p>
<ul>
  <li>Logic: AND, OR, NOT, NAND, NOR, XOR, XNOR</li>
  <li>Arithmetic: +, -, *, / (requires <code>use IEEE.NUMERIC_STD.ALL;</code>)</li>
  <li>Comparison: =, /=, &lt;, &gt;, &lt;=, &gt;=</li>
  <li>Concatenation: &amp;</li>
</ul>

<p><strong>Assignments:</strong></p>
<ul>
  <li><strong>Signal</strong>: <code>&lt;=</code> (concurrent assignment, outside process)</li>
  <li><strong>Variable</strong>: <code>:=</code> (sequential assignment, inside process)</li>
</ul>

<p><strong>Process (PROCESS):</strong></p>
<pre><code>process(clk, reset)  -- Sensitivity list
begin
    if reset = '1' then
        counter &lt;= 0;
    elsif rising_edge(clk) then  -- Rising clock edge
        counter &lt;= counter + 1;
    end if;
end process;</code></pre>

<p><strong>Control structures:</strong></p>

<p><strong>IF-THEN-ELSE:</strong></p>
<pre><code>if (condition) then
    -- instructions
elsif (other_condition) then
    -- instructions
else
    -- instructions
end if;</code></pre>

<p><strong>CASE:</strong></p>
<pre><code>case sel is
    when "00" =&gt; output &lt;= input0;
    when "01" =&gt; output &lt;= input1;
    when "10" =&gt; output &lt;= input2;
    when others =&gt; output &lt;= input3;
end case;</code></pre>

<p><strong>FOR LOOP:</strong></p>
<pre><code>for i in 0 to 7 loop
    output(i) &lt;= input(7-i);  -- Bus inversion
end loop;</code></pre>

<p><strong>Complete example: 8-bit Counter</strong></p>
<pre><code>library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity Counter8bits is
    Port (
        clk : in STD_LOGIC;
        reset : in STD_LOGIC;
        enable : in STD_LOGIC;
        count : out STD_LOGIC_VECTOR(7 downto 0)
    );
end Counter8bits;

architecture Behavioral of Counter8bits is
    signal counter : unsigned(7 downto 0) := (others =&gt; '0');
begin
    process(clk, reset)
    begin
        if reset = '1' then
            counter &lt;= (others =&gt; '0');
        elsif rising_edge(clk) then
            if enable = '1' then
                counter &lt;= counter + 1;
            end if;
        end if;
    end process;

    count &lt;= std_logic_vector(counter);
end Behavioral;</code></pre>

<h3>Lab Sessions</h3>

<h4>Lab 1: Getting Started with Quartus Prime</h4>
<ul>
  <li>Installation and configuration</li>
  <li>Creating a project</li>
  <li>Schematic entry (logic gates)</li>
  <li>Compilation and analysis</li>
  <li>Pin assignment (FPGA board)</li>
  <li>FPGA programming</li>
</ul>

<h4>Lab 2: Combinational Circuits</h4>
<ul>
  <li>BCD to 7-segment decoder</li>
  <li>4:1 Multiplexer</li>
  <li>4-bit adder</li>
  <li>Testing and validation</li>
</ul>

<h4>Lab 3: Introduction to VHDL</h4>
<ul>
  <li>Logic gates in VHDL</li>
  <li>Multiplexer in VHDL</li>
  <li>Simulation with ModelSim</li>
  <li>Synthesis and programming</li>
</ul>

<h4>Lab 4: Sequential Logic</h4>
<ul>
  <li>D and JK flip-flops</li>
  <li>Shift registers</li>
  <li>Counters (up, down, modulo)</li>
  <li>Frequency divider</li>
</ul>

<h4>Lab 5: Finite State Machine</h4>
<ul>
  <li>FSM design (traffic light, vending machine, etc.)</li>
  <li>VHDL implementation</li>
  <li>FPGA testing</li>
  <li>Functional validation</li>
</ul>

<hr/>

<h2>PART C: TECHNICAL ASPECTS</h2>

<h3>Design Tools</h3>

<h4>Intel Quartus Prime</h4>

<p><strong>Installation:</strong></p>
<ul>
  <li>Lite version (free): Up to 32k logic elements</li>
  <li>Windows/Linux compatible</li>
  <li>Download: ~5-6 GB</li>
</ul>

<p><strong>Design workflow:</strong></p>
<ol>
  <li><strong>Project creation</strong>: File &rarr; New Project Wizard</li>
  <li><strong>Add files</strong>: .vhd, .v, or schematic</li>
  <li><strong>Compilation</strong>: Processing &rarr; Start Compilation (Ctrl+L)</li>
  <li><strong>Analysis</strong>: Compilation Report (resources, timing, etc.)</li>
  <li><strong>Pin assignment</strong>: Assignments &rarr; Pin Planner</li>
  <li><strong>Programming</strong>: Tools &rarr; Programmer</li>
</ol>

<p><strong>Available analyses:</strong></p>
<ul>
  <li><strong>RTL Viewer</strong>: Synthesized schematic visualization</li>
  <li><strong>Technology Map Viewer</strong>: Mapping onto FPGA elements</li>
  <li><strong>Timing Analyzer</strong>: Critical path analysis</li>
  <li><strong>Resource Usage</strong>: LUTs, registers, memory used</li>
</ul>

<h4>ModelSim (Simulation)</h4>

<p><strong>Features:</strong></p>
<ul>
  <li>Behavioral simulation (before synthesis)</li>
  <li>Post-synthesis simulation (with real delays)</li>
  <li>Waveform viewer (timing diagrams)</li>
  <li>VHDL testbenches</li>
</ul>

<p><strong>Testbench example:</strong></p>
<pre><code>library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity Counter_TB is
end Counter_TB;

architecture Behavioral of Counter_TB is
    component Counter8bits
        Port (clk, reset, enable : in STD_LOGIC;
              count : out STD_LOGIC_VECTOR(7 downto 0));
    end component;

    signal clk_tb, reset_tb, enable_tb : STD_LOGIC := '0';
    signal count_tb : STD_LOGIC_VECTOR(7 downto 0);
    constant clk_period : time := 10 ns;

begin
    UUT: Counter8bits port map(clk_tb, reset_tb, enable_tb, count_tb);

    -- Clock generation
    clk_process : process
    begin
        clk_tb &lt;= '0';
        wait for clk_period/2;
        clk_tb &lt;= '1';
        wait for clk_period/2;
    end process;

    -- Stimulus
    stim_proc: process
    begin
        reset_tb &lt;= '1';
        wait for 20 ns;
        reset_tb &lt;= '0';
        enable_tb &lt;= '1';
        wait for 1000 ns;
        enable_tb &lt;= '0';
        wait;
    end process;
end Behavioral;</code></pre>

<h3>FPGA Boards Used</h3>

<h4>Altera/Intel Cyclone IV/V</h4>

<p><strong>Characteristics:</strong></p>
<ul>
  <li>6K - 115K logic elements</li>
  <li>Embedded memory (M9K blocks)</li>
  <li>PLL (Phase-Locked Loops) for clock management</li>
  <li>DSP blocks (hardware multipliers)</li>
  <li>Configurable GPIO (LVTTL, LVCMOS, LVDS)</li>
</ul>

<p><strong>Development boards:</strong></p>
<ul>
  <li><strong>DE0-Nano</strong>: Cyclone IV, compact, ~80&euro;</li>
  <li><strong>DE1-SoC</strong>: Cyclone V + ARM Cortex-A9, ~200&euro;</li>
  <li><strong>DE2-115</strong>: Cyclone IV, numerous peripherals, ~300&euro;</li>
</ul>

<p><strong>Typical peripherals:</strong></p>
<ul>
  <li>LEDs, push buttons, switches</li>
  <li>7-segment displays</li>
  <li>VGA/HDMI</li>
  <li>GPIO (expansion connectors)</li>
  <li>USB, Ethernet (depending on model)</li>
</ul>

<h3>Design Methodology</h3>

<h4>VHDL Best Practices</h4>

<p><strong>Naming:</strong></p>
<ul>
  <li>Signals/variables: lowercase_with_underscores</li>
  <li>Constants: UPPERCASE</li>
  <li>Entities/architectures: CamelCase</li>
</ul>

<p><strong>Comments:</strong></p>
<pre><code>-- Single line comment

--======================
-- Comment block
--======================</code></pre>

<p><strong>Synchronous design:</strong></p>
<ul>
  <li>Always use a single clock if possible</li>
  <li>Avoid complex asynchronous logic</li>
  <li>Reset signals properly</li>
</ul>

<p><strong>Testability:</strong></p>
<ul>
  <li>Systematically create testbenches</li>
  <li>Test edge cases</li>
  <li>Verify timing (setup/hold)</li>
</ul>

<h4>Debugging</h4>

<p><strong>Common compilation errors:</strong></p>
<ul>
  <li><code>Signal not declared</code> &rarr; Forgot to declare the signal</li>
  <li><code>Multiple drivers</code> &rarr; Signal assigned in multiple places</li>
  <li><code>Type mismatch</code> &rarr; Type conversion needed (std_logic_vector &harr; unsigned)</li>
</ul>

<p><strong>Debugging tools:</strong></p>
<ul>
  <li><strong>SignalTap II</strong> (Quartus): Internal FPGA logic analyzer</li>
  <li><strong>Simulation</strong>: Always simulate before synthesizing</li>
  <li><strong>Debug LEDs</strong>: Display internal states</li>
</ul>

<hr/>

<h2>PART D: ANALYSIS AND REFLECTION</h2>

<h3>Skills Assessment</h3>

<h4>Assessment Methods</h4>

<p><strong>Continuous assessment (40%):</strong></p>
<ul>
  <li>Theoretical quizzes (2x1h): Boolean algebra, sequential logic - 20%</li>
  <li>Practical Quartus tests (2x1h30) - 20%</li>
</ul>

<p><strong>Lab work (35%):</strong></p>
<ul>
  <li>5 graded labs with reports</li>
  <li>Assessment: working circuit, VHDL code, tests, documentation</li>
</ul>

<p><strong>Project (15%):</strong></p>
<ul>
  <li>VHDL mini-project (state machine + counter + display)</li>
  <li>Demo on FPGA board</li>
  <li>Commented source code</li>
  <li>Technical report</li>
</ul>

<p><strong>Final exam (10%):</strong></p>
<ul>
  <li>Theoretical exam (1h30)</li>
  <li>Karnaugh maps, timing diagrams, VHDL</li>
</ul>

<h4>Lab Grading Rubric</h4>

<table>
  <thead><tr><th>Criterion</th><th>Points</th></tr></thead>
  <tbody>
    <tr><td><strong>Functionality</strong>: Circuit works on FPGA</td><td>/6</td></tr>
    <tr><td><strong>VHDL Code</strong>: Quality, clarity, comments</td><td>/5</td></tr>
    <tr><td><strong>Simulation</strong>: Testbench and timing diagrams</td><td>/4</td></tr>
    <tr><td><strong>Tests</strong>: Complete validation</td><td>/3</td></tr>
    <tr><td><strong>Report</strong>: Clarity, diagrams, analysis</td><td>/2</td></tr>
    <tr><td><strong>Total</strong></td><td><strong>/20</strong></td></tr>
  </tbody>
</table>

<h3>Skills Acquired</h3>

<h4>Theoretical Knowledge</h4>
<ul>
  <li>Master Boolean algebra and number systems</li>
  <li>Understand combinational and sequential logic</li>
  <li>Know fundamental digital circuits</li>
  <li>Understand FPGA principles</li>
</ul>

<h4>Technical Know-How</h4>
<ul>
  <li>Design digital circuits (combinational and sequential)</li>
  <li>Simplify logic functions (Karnaugh)</li>
  <li>Program in VHDL</li>
  <li>Simulate and validate digital designs</li>
  <li>Synthesize and program FPGAs with Quartus</li>
  <li>Debug digital circuits</li>
</ul>

<h4>Soft Skills</h4>
<ul>
  <li>Rigor in design (timing diagrams, timing)</li>
  <li>Test and validation methodology</li>
  <li>Clear technical documentation</li>
  <li>Teamwork on projects</li>
</ul>

<h3>Progression and Curriculum Links</h3>

<h4>Digital Systems Curriculum Path</h4>

<table>
  <thead><tr><th>Semester</th><th>Module</th><th>Content</th></tr></thead>
  <tbody>
    <tr><td><strong>S1</strong></td><td>SIN 1</td><td>Combinational logic, sequential logic, basic VHDL</td></tr>
    <tr><td><strong>S2</strong></td><td>Sequential Logic</td><td>Advanced FSMs, FIFO, memories, buses</td></tr>
    <tr><td><strong>S3</strong></td><td>Advanced Digital Architectures</td><td>Processors, pipelines, advanced VHDL</td></tr>
    <tr><td><strong>S4</strong></td><td>FPGA Project</td><td>Complete system design (SoC)</td></tr>
  </tbody>
</table>

<h4>Links with Other Subjects</h4>

<table>
  <thead><tr><th>Subject</th><th>Use of Digital Systems</th></tr></thead>
  <tbody>
    <tr><td><strong>Programming</strong></td><td>Algorithm/FSM similarities</td></tr>
    <tr><td><strong>Embedded Computing</strong></td><td>Microcontrollers (internal logic)</td></tr>
    <tr><td><strong>Electronics</strong></td><td>Analog/digital interface (ADC, DAC)</td></tr>
    <tr><td><strong>Control Systems</strong></td><td>Digital controllers, discrete regulators</td></tr>
    <tr><td><strong>Telecommunications</strong></td><td>Digital modulation/demodulation</td></tr>
  </tbody>
</table>

<h3>Success Indicators</h3>

<h4>Statistics</h4>
<p><strong>Pass rate:</strong> 88%<br/>
<strong>Overall average:</strong> 12.8/20</p>

<p><strong>Common difficulties:</strong></p>
<ul>
  <li>Confusion between combinational and sequential logic</li>
  <li>Forgetting the sensitivity list in processes</li>
  <li>Type conversions in VHDL</li>
  <li>Timing (setup/hold violations)</li>
  <li>Karnaugh simplification (groupings)</li>
</ul>

<p><strong>Keys to success:</strong></p>
<ul>
  <li>Draw timing diagrams before coding</li>
  <li>Always simulate before synthesizing</li>
  <li>Start simple, increase complexity gradually</li>
  <li>Use the provided code examples</li>
  <li>Test on FPGA board regularly</li>
</ul>

<h3>Career Opportunities and Applications</h3>

<h4>Professional Applications</h4>

<p><strong>Careers using FPGA/VHDL:</strong></p>
<ul>
  <li>FPGA engineer (aerospace, space, defense)</li>
  <li>ASIC circuit designer</li>
  <li>Digital signal processing engineer</li>
  <li>Critical embedded systems developer</li>
  <li>Hardware architect</li>
</ul>

<p><strong>Industries:</strong></p>
<ul>
  <li><strong>Aerospace/Space</strong>: Critical systems, radiation resistance</li>
  <li><strong>Telecommunications</strong>: Modems, routers, 5G</li>
  <li><strong>Automotive</strong>: ADAS, engine control</li>
  <li><strong>Medical</strong>: Imaging (ultrasound, MRI), diagnostic devices</li>
  <li><strong>Finance</strong>: High-frequency trading (FPGA for ultra-low latency)</li>
  <li><strong>AI</strong>: Hardware accelerators (neural inference)</li>
</ul>

<hr/>

<h2>Additional Resources</h2>

<h3>Reference Books</h3>

<p><strong>Digital logic:</strong></p>
<ol>
  <li><em>Systemes logiques - Tome 1 et 2</em> - A. Vachoux (PPUR) - French-language reference</li>
  <li><em>Digital Design</em> - M. Morris Mano (Pearson) - World classic</li>
  <li><em>Circuits numeriques et synthese logique</em> - Jacques Weber (Eyrolles)</li>
</ol>

<p><strong>VHDL:</strong></p>
<ul>
  <li><em>VHDL - Du langage a la modelisation</em> - Jacques Weber (Dunod)</li>
  <li><em>Free Range VHDL</em> - Bryan Mealy (free online)</li>
  <li><em>VHDL for Engineers</em> - Kenneth L. Short (Pearson)</li>
</ul>

<h3>Websites and Tutorials</h3>

<p><strong>Online courses:</strong></p>
<ul>
  <li><strong>VHDL Whiz</strong> (vhdlwhiz.com) - Free video tutorials</li>
  <li><strong>Nandland</strong> (nandland.com) - FPGA projects for beginners</li>
  <li><strong>FPGA4Fun</strong> (fpga4fun.com) - Numerous VHDL examples</li>
</ul>

<p><strong>Forums and communities:</strong></p>
<ul>
  <li><strong>Reddit</strong>: r/FPGA</li>
  <li><strong>EDAboard</strong>: Specialized FPGA/VHDL forum</li>
  <li><strong>Stack Overflow</strong>: Tag [vhdl]</li>
</ul>

<p><strong>Online simulators:</strong></p>
<ul>
  <li><strong>CircuitVerse</strong> (circuitverse.org) - Interactive digital logic</li>
  <li><strong>EDA Playground</strong> (edaplayground.com) - Online VHDL simulation</li>
</ul>

<h3>Alternative Open Source Software</h3>
<ul>
  <li><strong>GHDL</strong>: Open source VHDL simulator</li>
  <li><strong>GTKWave</strong>: Waveform viewer</li>
  <li><strong>Icarus Verilog</strong>: If you also want to learn Verilog</li>
</ul>

<hr/>

<h2>Methodological Advice</h2>

<h3>How to Succeed in Digital Systems</h3>

<p><strong>During lectures/tutorials:</strong></p>
<ul>
  <li>Draw circuits as you go</li>
  <li>Redo Karnaugh simplifications at home</li>
  <li>Understand timing diagrams (time = horizontal)</li>
</ul>

<p><strong>In lab sessions:</strong></p>
<ul>
  <li>Read the entire assignment before starting</li>
  <li>Design on paper before coding</li>
  <li>Systematically simulate before programming the FPGA</li>
  <li>Save your project frequently</li>
  <li>Test progressively (function by function)</li>
</ul>

<p><strong>Personal work (2-3h/week):</strong></p>
<ul>
  <li>Redo simplification exercises</li>
  <li>Create your own small VHDL circuits</li>
  <li>Watch video tutorials (Nandland, VHDL Whiz)</li>
  <li>Practice base conversions</li>
</ul>

<h3>Mistakes to Avoid</h3>
<ul>
  <li>Forgetting <code>rising_edge(clk)</code> in synchronous processes</li>
  <li>Mixing <code>&lt;=</code> and <code>:=</code> assignments</li>
  <li>Neglecting types (STD_LOGIC vs INTEGER vs UNSIGNED)</li>
  <li>Creating combinational loops (A depends on A)</li>
  <li>Not testing edge cases (reset, overflow, etc.)</li>
</ul>

<p><strong>Best practices:</strong></p>
<ul>
  <li>Always declare a reset signal</li>
  <li>Use explicit signal names</li>
  <li>Comment your VHDL code</li>
  <li>Check Resource Usage after compilation</li>
  <li>Document your circuits with diagrams</li>
</ul>

<hr/>

<p><strong>Good luck discovering the fascinating world of digital systems!</strong></p>

<blockquote><p>"In theory, theory and practice are the same. In practice, they are not." - Yogi Berra</p></blockquote>

<p>In digital systems, simulation and real hardware testing are essential. Don't hesitate to experiment on FPGA boards!</p>

<ul>
  <li><strong>Programming</strong>: Control structures and algorithms</li>
  <li><strong>ER (Electronics and Implementation)</strong>: Analog/digital interface</li>
  <li><strong>Mathematics</strong>: Boolean algebra</li>
</ul>

<h2>Additional Resources</h2>
<ul>
  <li>Intel Quartus documentation</li>
  <li>VHDL tutorials</li>
  <li>FPGA component datasheets</li>
</ul>

</div>
