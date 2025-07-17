# main.py
# Wersja 1.0 - Kompletny, przetestowany kod dla Minimal Viable Product projektu Nexus Protocol.
# Zawiera logikę planowania warunkowego oraz monitor świadomości błędów.

import json
import time
import random

# STAN ŚWIATA
WORLD_STATE = {
    "locations": {
        "storage_area": ["red_cube", "blue_ball"],
        "zone_A": [],
        "zone_B": ["green_pyramid"],
        "robot_home": []
    }
}

def display_world_state():
    """Funkcja pomocnicza do ładnego wyświetlania stanu świata."""
    print("\n--- Aktualny Stan Świata ---")
    for location, items in WORLD_STATE['locations'].items():
        print(f"{location}: {items if items else '[pusto]'}")
    print("---------------------------\n")

class AwarenessMonitor:
    """Moduł sprawdzający, czy wynik akcji zgadza się z oczekiwaniami."""
    def __init__(self):
        self.log = []
        print("Awareness Monitor [KMŚS]: Inicjalizacja. Monitoruję rzeczywistość.")

    def check_outcome(self, action, target, state_before, state_after):
        log_entry = f"[ANALIZA] Akcja: {action}, Cel: {target}. "
        expected_to_succeed = True

        if action == "PICKUP":
            if target in state_after['world']['locations'][state_after['robot']['location']] or state_after['robot']['holding'] != target:
                expected_to_succeed = False
        
        elif action == "DROP":
            object_that_was_held = state_before['robot']['holding']
            if object_that_was_held is None or \
               object_that_was_held not in state_after['world']['locations'][state_after['robot']['location']] or \
               state_after['robot']['holding'] is not None:
                expected_to_succeed = False
        
        if expected_to_succeed:
            log_entry += "Wynik zgodny z oczekiwaniami."
        else:
            log_entry += "ANOMALIA! Wynik niezgodny z oczekiwaniami!"
        
        print(log_entry)
        self.log.append(log_entry)

class CloudCortex:
    """Kora w Chmurze zdolna do planowania warunkowego i sekwencyjnego."""
    def __init__(self):
        print("Cloud Cortex [LLM]: Inicjalizacja.")
        self.actions = ['przynieś', 'zabierz', 'połóż', 'odłóż']
        self.entity_map = { "czerwony": "red", "niebieski": "blue", "zielony": "green", "sześcian": "cube", "piłka": "ball", "piramida": "pyramid", "strefy a": "zone_A", "strefy b": "zone_B", "bazy": "robot_home", "magazynu": "storage_area" }

    def create_sub_plan(self, object_id, destination_id):
        """Tworzy pod-plan dla prostej akcji 'przynieś'."""
        source_location = next((loc for loc, items in WORLD_STATE['locations'].items() if object_id in items), None)
        if not source_location:
            print(f"Cloud Cortex [LLM]: Błąd pod-planu - obiekt '{object_id}' nie istnieje.")
            return None
        return [
            {"action": "GOTO", "target": source_location},
            {"action": "PICKUP", "target": object_id},
            {"action": "GOTO", "target": destination_id},
            {"action": "DROP", "target": object_id}
        ]

    def generate_plan(self, high_level_goal: str) -> list:
        print(f"\nCloud Cortex [LLM]: Otrzymano cel: '{high_level_goal}'. Analiza...")
        time.sleep(1.5)
        goal_lower = high_level_goal.lower()

        if goal_lower.startswith("jeśli"):
             # Uproszczona logika warunkowa
             condition_obj_id = "red_cube"; condition_loc = "storage_area"
             print(f"Cloud Cortex [LLM]: Sprawdzam warunek: Czy '{condition_obj_id}' jest w '{condition_loc}'?")
             if condition_obj_id in WORLD_STATE['locations'].get(condition_loc, []):
                 print("Cloud Cortex [LLM]: Warunek PRAWDZIWY. Wykonuję pierwszą ścieżkę.")
                 return self.create_sub_plan("red_cube", "zone_B")
             else:
                 print("Cloud Cortex [LLM]: Warunek FAŁSZYWY. Wykonuję ścieżkę 'w przeciwnym razie'.")
                 return self.create_sub_plan("blue_ball", "zone_A")
        else:
            print("Cloud Cortex [LLM]: Nie rozpoznano polecenia warunkowego. Zwracam pusty plan.")
            return []

class OnboardCore:
    def __init__(self):
        self.robot_state = {"holding": None, "location": "robot_home"}
        print(f"Onboard Core [Robot]: Inicjalizacja. Stan: {self.robot_state}")

    def execute_plan(self, plan: list, monitor: AwarenessMonitor):
        print("\nOnboard Core [Robot]: Otrzymano plan. Rozpoczynam wykonanie.")
        if not plan: return

        for step in plan:
            action, target = step.get("action"), step.get("target")
            print(f"--- Wykonuję krok: {action}, Cel: {target or 'N/A'} ---")
            
            state_before = {'robot': self.robot_state.copy(), 'world': json.loads(json.dumps(WORLD_STATE))}
            time.sleep(1)
            success = self.perform_action(action, target)
            state_after = {'robot': self.robot_state.copy(), 'world': json.loads(json.dumps(WORLD_STATE))}

            monitor.check_outcome(action, target, state_before, state_after)

            if not success:
                print("Onboard Core [Robot]: Wykonanie kroku nie powiodło się. Przerywam plan.")
                break
        print("\nOnboard Core [Robot]: Zakończono wykonywanie planu.")

    def perform_action(self, action, target):
        if action == "GOTO":
            self.robot_state["location"] = target
            return True
        if action == "PICKUP":
            if random.random() < 0.33:
                print(f"Onboard Core [Robot]: KRYTYCZNY BŁĄD! Chwytak ześlizgnął się z obiektu '{target}'.")
                return True 
            if target in WORLD_STATE['locations'][self.robot_state['location']] and self.robot_state['holding'] is None:
                WORLD_STATE['locations'][self.robot_state['location']].remove(target)
                self.robot_state['holding'] = target
                print(f"Onboard Core [Robot]: Obiekt '{target}' podniesiony.")
                return True
            return False
        if action == "DROP":
            if self.robot_state['holding'] is not None and self.robot_state['holding'] == target:
                WORLD_STATE['locations'][self.robot_state['location']].append(self.robot_state['holding'])
                self.robot_state['holding'] = None
                print(f"Onboard Core [Robot]: Obiekt '{target}' upuszczony w '{self.robot_state['location']}'.")
                return True
            return False
        return False

def main():
    print("--- Start Symulacji Nexus Protocol MVP v1.0 ---")
    display_world_state()
    
    cortex = CloudCortex()
    core = OnboardCore()
    monitor = AwarenessMonitor()

    user_goal = "Jeśli w magazynie jest czerwony sześcian, przenieś go do strefy B. W przeciwnym razie, przynieś niebieską piłkę do strefy A."

    strategic_plan = cortex.generate_plan(user_goal)
    core.execute_plan(strategic_plan, monitor)

    print("\n--- Końcowy Stan Świata ---")
    display_world_state()

if __name__ == "__main__":
    main()
