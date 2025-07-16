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
3. (Recommended) Create a Virtual Environment
It's good practice to use a virtual environment to keep project dependencies isolated.

On macOS / Linux:

Bash

python3 -m venv venv
source venv/bin/activate
On Windows:

Bash

python -m venv venv
.\venv\Scripts\activate
(Note: In the future, if we add any dependencies, we will install them here using pip install -r requirements.txt)

4. Run the MVP Simulation
You are now ready to run the simulation.

Bash

python main.py
5. Expected Output
If everything is set up correctly, you should see the following output in your terminal, demonstrating the interaction between the Cloud Cortex and the Onboard Core:

--- Start Symulacji Nexus Protocol MVP v0.1 ---
Cloud Cortex [LLM]: Inicjalizacja. Gotowy do planowania.
Onboard Core [Robot]: Inicjalizacja. Stan: {'hand_empty': True, 'location': 'start_point'}

Cloud Cortex [LLM]: Otrzymano cel: 'Przynieś czerwony sześcian do zielonej strefy'. Generowanie planu...
Cloud Cortex [LLM]: Plan wygenerowany pomyślnie.

Onboard Core [Robot]: Otrzymano plan. Rozpoczynam wykonanie.
--- Wykonuję krok: GOTO, Cel: red_cube_location ---
Onboard Core [Robot]: Przeniesiono do 'red_cube_location'.
Onboard Core [Robot]: Aktualny stan: {'hand_empty': True, 'location': 'red_cube_location'}
--- Wykonuję krok: VERIFY_OBJECT, Cel: red_cube ---
Onboard Core [Robot]: Weryfikacja obiektu 'red_cube'. Obiekt zgodny.
Onboard Core [Robot]: Aktualny stan: {'hand_empty': True, 'location': 'red_cube_location'}
--- Wykonuję krok: PICKUP, Cel: N/A ---
Onboard Core [Robot]: Obiekt podniesiony.
Onboard Core [Robot]: Aktualny stan: {'hand_empty': False, 'location': 'red_cube_location'}
--- Wykonuję krok: GOTO, Cel: green_zone ---
Onboard Core [Robot]: Przeniesiono do 'green_zone'.
Onboard Core [Robot]: Aktualny stan: {'hand_empty': False, 'location': 'green_zone'}
--- Wykonuję krok: DROP, Cel: N/A ---
Onboard Core [Robot]: Obiekt upuszczony.
Onboard Core [Robot]: Aktualny stan: {'hand_empty': True, 'location': 'green_zone'}

Onboard Core [Robot]: Wszystkie kroki planu zostały wykonane.

--- Koniec Symulacji ---
And that's it! You have successfully run the Nexus Protocol MVP.


---

Gdy dodasz ten plik oraz zaktualizowane wersje `README.md` i `ROADMAP.md` do repozytorium, nasz fundament będzie kompletny i znacznie bardziej profesjonalny.

Będziemy gotowi, aby w pełni skupić się na implementacji logiki w pliku `main.py`.
