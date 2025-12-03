---
layout: default
title: "Informatique Embarquée (IE) - S2"
date: 2024-10-02 10:56:03 +0200
categories: jekyll update
---

# Informatique Embarquée (IE) - Semestre 2

## 📋 Description du cours

Introduction à la programmation de microcontrôleurs et aux systèmes embarqués. Ce cours couvre la programmation bas niveau, la gestion des périphériques et les concepts de systèmes temps réel.

## 🎯 Objectifs pédagogiques

- Comprendre l'architecture des microcontrôleurs
- Programmer des microcontrôleurs en C embarqué
- Gérer les périphériques (GPIO, timers, ADC, UART, etc.)
- Appréhender les contraintes des systèmes embarqués
- Développer des applications temps réel simples

## 📚 Contenu du cours

### Architecture des microcontrôleurs
- Architecture Harvard vs Von Neumann
- CPU, mémoires (Flash, RAM, EEPROM)
- Bus et périphériques
- Registres et espace mémoire
- Modes de fonctionnement et économie d'énergie

### Programmation C embarqué
- Différences avec le C standard
- Types de données et optimisation
- Accès aux registres matériels
- Pointeurs et adressage direct
- Volatilité et optimisation du compilateur
- Gestion de la mémoire limitée

### Périphériques de base
#### GPIO (General Purpose Input/Output)
- Configuration des broches
- Lecture d'entrées (boutons, capteurs TOR)
- Commande de sorties (LED, relais)
- Interruptions externes

#### Timers/Compteurs
- Timers de base
- PWM (Modulation de Largeur d'Impulsion)
- Génération de bases de temps
- Capture et comparaison

#### Convertisseurs ADC
- Principe de conversion analogique-numérique
- Configuration et utilisation
- Résolution et échantillonnage
- Lecture de capteurs analogiques

#### Communications série
- UART/USART (RS232)
- Configuration et utilisation
- Communication avec PC
- Protocoles simples

### Systèmes temps réel
- Contraintes temporelles
- Ordonnancement de tâches
- Interruptions et priorités
- Introduction aux RTOS (Real-Time Operating System)
- Gestion de l'énergie

## 🛠️ Plateformes utilisées

### Microcontrôleurs
- **Arduino** (ATmega328P) : Plateforme d'apprentissage
- **STM32** : Microcontrôleurs ARM professionnels
- **PIC** : Microchip (selon disponibilité)

### Environnements de développement
- **Arduino IDE** : Développement rapide
- **STM32CubeIDE** : Développement professionnel STM32
- **MPLAB X** : Pour microcontrôleurs PIC
- **Keil µVision** : IDE professionnel ARM

## 🎯 Projets pratiques

### Mini-projets guidés
- Clignotement de LED et gestion de boutons
- Génération de PWM pour variation de luminosité
- Lecture de capteurs analogiques (température, lumière)
- Communication série et affichage sur PC
- Gestion d'afficheur LCD

### Projet intégratif
Réalisation d'un système embarqué complet intégrant :
- Acquisition de données (capteurs)
- Traitement et décision
- Actionnement (moteurs, relais)
- Interface utilisateur (boutons, écran)
- Communication (série, sans fil)

## 🔧 Outils de développement

### Logiciels
- Compilateurs C (GCC, Keil, XC)
- Debuggers (GDB, JTAG, SWD)
- Outils de programmation
- Moniteurs série (PuTTY, Tera Term)

### Matériel
- Cartes de développement
- Programmateurs/Debuggers (ST-Link, JTAG)
- Oscilloscope logique
- Multimètre

## 📊 Évaluation

- Travaux pratiques (40%)
- Projet embarqué (30%)
- Examen théorique (20%)
- Examen pratique (10%)

## 🔗 Liens avec d'autres cours

- **Programmation S1** : Bases du C
- **SIN** : Logique numérique et architecture
- **SE** : Concepts de systèmes d'exploitation
- **ER** : Interface électronique/informatique

## 💡 Compétences développées

- Programmation bas niveau
- Débogage de systèmes embarqués
- Lecture de documentation technique (datasheets)
- Gestion des contraintes matérielles
- Optimisation de code
- Tests et validation de systèmes embarqués

## 📖 Ressources

- Datasheets des microcontrôleurs
- Manuels de référence (Reference Manual, Programming Manual)
- Forums et communautés (Arduino, STM32, etc.)
- Exemples de code et bibliothèques

## ⚠️ Bonnes pratiques

- Toujours consulter la datasheet
- Initialiser correctement les périphériques
- Gérer les cas d'erreur
- Déboguer méthodiquement
- Commenter le code matériel
- Vérifier les contraintes de timing
