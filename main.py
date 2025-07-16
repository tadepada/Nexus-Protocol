# main.py
# Wersja 0.4 - Poprawka mapowania języka na encje i drobne ulepszenia

import json
import time

# STAN ŚWIATA (bez zmian)
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

class CloudCortex:
    """
    Ulepszona Kora w Chmurze z mapowaniem encji.
    """
    def __init__(self):
        print("Cloud Cortex [LLM]: Inicjalizacja. Gotowy do planowania strategicznego.")
        self.actions = ['przynieś', 'zabierz', 'połóż', 'odłóż']
        # Słownik encji: mapuje polskie słowa na ustandaryzowane ID
        self.entity_map = {
            "czerwony": "red", "niebieski": "blue", "zielony": "green",
            "sześcian": "cube", "piłka": "ball", "piramida": "pyramid",
            "strefy a": "zone_A", "strefy b": "zone_B", "bazy": "robot_home", "magazynu": "storage_area"
        }

    def get_entity_from_token(self, token: str) -> str:
        """Zwraca ID encji na podstawie tokenu (słowa)."""
        return self.entity_map.get(token)

    def generate_plan(self, high_level_goal: str) -> list:
        print(f"\nCloud Cortex [LLM]: Otrzymano cel: '{high_level_goal}'. Parsowanie polecenia...")
        time.sleep(1.5)
        words = high_level_goal.lower().split()

        # Ulepszone parsowanie z użyciem mapy encji
        parsed_action = next((word for word in words if word in self.actions), None)
        parsed_color = next((self.get_entity_from_token(word) for word in words if self.get_entity_from_token(word) in ["red", "green", "blue"]), None)
        parsed_type = next((self.get_entity_from_token(word) for word in words if self.get_entity_from_token(word) in ["cube", "ball", "pyramid"]), None)
        
        # Znajdźmy lokalizacje, obsługując jedno- i dwu-wyrazowe nazwy
        parsed_destination = None
        for i, word in enumerate(words):
            # Sprawdź dwuwyrazowe lokalizacje
            if i + 1 < len(words):
                two_word_loc = f"{word} {words[i+1]}"
                if self.entity_map.get(two_word_loc):
                    parsed_destination = self.entity_map.get(two_word_loc)
                    break
            # Sprawdź jednowyrazowe lokalizacje
            if self.entity_map.get(word) and self.entity_map.get(word).startswith("zone"):
                parsed_destination = self.entity_map.get(word)
                break

        if not (parsed_action and parsed_color and parsed_type and parsed_destination):
            print("Cloud Cortex [LLM]: Nie udało się zrozumieć polecenia. Brak kluczowych informacji.")
            return []

        # Tworzenie ustandaryzowanego ID obiektu
        canonical_object_id = f"{parsed_color}_{parsed_type}"
        
        source_location = None
        for loc, items in WORLD_STATE['locations'].items():
            if canonical_object_id in items:
                source_location = loc
                break
        
        if not source_location:
            print(f"Cloud Cortex [LLM]: Błąd planowania - obiekt '{canonical_object_id}' nie został znaleziony w świecie.")
            return []

        plan = [
            {"action": "GOTO", "target": source_location},
            {"action": "VERIFY_OBJECT", "target": canonical_object_id},
            {"action": "PICKUP", "target": canonical_object_id},
            {"action": "GOTO", "target": parsed_destination},
            {"action": "DROP"}
        ]
        
        print(f"Cloud Cortex [LLM]: Polecenie zrozumiane. Plan dla '{canonical_object_id}' wygenerowany pomyślnie.")
        return plan

class OnboardCore:
    # Ta klasa pozostaje bez zmian
    def __init__(self):
        self.robot_state = {"holding": None, "location": "robot_home"}
        print(f"Onboard Core [Robot]: Inicjalizacja. Stan: {self.robot_state}")

    def execute_plan(self, plan: list):
        print("\nOnboard Core [Robot]: Otrzymano plan. Rozpoczynam wykonanie.")
        if not plan:
            print("Onboard Core [Robot]: Plan jest pusty. Brak akcji do wykonania.")
            return

        for step in plan:
            action = step.get("action")
            target = step.get("target")
            print(f"--- Wykonuję krok: {action}, Cel: {target if target else 'N/A'} ---")
            time.sleep(1)
            
            success = False
            # ... logika wykonywania kroków pozostaje bez zmian ...
            if action == "GOTO":
                self.robot_state["location"] = target
                success = True
                print(f"Onboard Core [Robot]: Przeniesiono do '{target}'.")
            elif action == "VERIFY_OBJECT":
                if target in WORLD_STATE['locations'][self.robot_state['location']]:
                    success = True
                    print(f"Onboard Core [Robot]: Weryfikacja obiektu '{target}' udana.")
                else:
                    print(f"Onboard Core [Robot]: BŁĄD! Nie znaleziono '{target}' w '{self.robot_state['location']}'.")
            elif action == "PICKUP":
                if target in WORLD_STATE['locations'][self.robot_state['location']] and self.robot_state['holding'] is None:
                    WORLD_STATE['locations'][self.robot_state['location']].remove(target)
                    self.robot_state['holding'] = target
                    success = True
                    print(f"Onboard Core [Robot]: Obiekt '{target}' podniesiony.")
                else:
                    print(f"Onboard Core [Robot]: BŁĄD! Nie można podnieść '{target}'.")
            elif action == "DROP":
                if self.robot_state['holding'] is not None:
                    WORLD_STATE['locations'][self.robot_state['location']].append(self.robot_state['holding'])
                    self.robot_state['holding'] = None
                    success = True
                    print(f"Onboard Core [Robot]: Obiekt upuszczony w '{self.robot_state['location']}'.")
                else:
                    print("Onboard Core [Robot]: BŁĄD! Nie trzymam żadnego obiektu.")

            if not success:
                print("Onboard Core [Robot]: Wykonanie kroku nie powiodło się. Przerywam plan.")
                break
        
        print("\nOnboard Core [Robot]: Zakończono wykonywanie planu.")


def main():
    print("--- Start Symulacji Nexus Protocol MVP v0.4 ---")
    display_world_state()
    
    cortex = CloudCortex()
    core = OnboardCore()

    user_goal = "Przynieś czerwony sześcian z magazynu do strefy A"

    strategic_plan = cortex.generate_plan(user_goal)
    core.execute_plan(strategic_plan)

    print("\n--- Końcowy Stan Świata ---")
    display_world_state()


if __name__ == "__main__":
    main()
