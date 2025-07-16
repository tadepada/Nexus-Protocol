# Nexus Protocol - Quick Start Guide

This guide will help you run the MVP simulation of the Nexus Protocol on your local machine in just a few minutes.

## Prerequisites

* **Python 3.8+** installed on your system.
* **Git** installed on your system.

## 1. Clone the Repository

First, open your terminal or command prompt and clone the project repository from GitHub.

```bash
git clone [https://github.com/tadepada/Nexus-Protocol.git](https://github.com/tadepada/Nexus-Protocol.git)
2. Navigate to the Project Directory
Move into the newly created project folder.

Bash

cd Nexus-Protocol
3. Run the MVP Simulation
You are now ready to run the simulation.

Bash

python main.py
4. Expected Output
If everything is set up correctly, you should see a simulation running in your terminal, showing how the Cloud Cortex generates a plan and the Onboard Core executes it by moving objects between locations.

--- Start Symulacji Nexus Protocol MVP v0.8 ---
Cloud Cortex [LLM]: Inicjalizacja.
Onboard Core [Robot]: Inicjalizacja. Stan: {'holding': None, 'location': 'robot_home'}
Awareness Monitor [KMŚS]: Inicjalizacja. Monitoruję rzeczywistość.

--- Aktualny Stan Świata ---
storage_area: ['red_cube', 'blue_ball']
zone_A: [pusto]
zone_B: ['green_pyramid']
robot_home: [pusto]
---------------------------


Cloud Cortex [LLM]: Otrzymano cel warunkowy: 'Jeśli w magazynie jest czerwony sześcian, przenieś go do strefy B. W przeciwnym razie, przynieś niebieską piłkę do strefy A.'. Analiza warunków...
Cloud Cortex [LLM]: Sprawdzam warunek: Czy 'red_cube' jest w 'storage_area'?
Cloud Cortex [LLM]: Warunek PRAWDZIWY. Wykonuję pierwszą ścieżkę.

Onboard Core [Robot]: Otrzymano plan. Rozpoczynam wykonanie.
--- Wykonuję krok: GOTO, Cel: storage_area ---
[ANALIZA] Akcja: GOTO, Cel: storage_area. Wynik zgodny z oczekiwaniami.
--- Wykonuję krok: PICKUP, Cel: red_cube ---
Onboard Core [Robot]: Obiekt 'red_cube' podniesiony.
[ANALIZA] Akcja: PICKUP, Cel: red_cube. Wynik zgodny z oczekiwaniami.
--- Wykonuję krok: GOTO, Cel: zone_B ---
[ANALIZA] Akcja: GOTO, Cel: zone_B. Wynik zgodny z oczekiwaniami.
--- Wykonuję krok: DROP, Cel: red_cube ---
Onboard Core [Robot]: Obiekt 'red_cube' upuszczony w 'zone_B'.
[ANALIZA] Akcja: DROP, Cel: red_cube. Wynik zgodny z oczekiwaniami.

Onboard Core [Robot]: Zakończono wykonywanie planu.

--- Końcowy Stan Świata ---

--- Aktualny Stan Świata ---
storage_area: ['blue_ball']
zone_A: [pusto]
zone_B: ['green_pyramid', 'red_cube']
robot_home: [pusto]
---------------------------

=== Kod został wykonany ===
