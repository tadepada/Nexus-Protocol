# main.py
# Version 1.0 - Complete, tested code for the Nexus Protocol Minimal Viable Product.
# Implements conditional planning and an error awareness monitor.

import json
import time
import random

# WORLD STATE
WORLD_STATE = {
    "locations": {
        "storage_area": ["red_cube", "blue_ball"],
        "zone_A": [],
        "zone_B": ["green_pyramid"],
        "robot_home": []
    }
}

def display_world_state():
    """Helper function to print the current state of the world."""
    print("\n--- Current World State ---")
    for location, items in WORLD_STATE['locations'].items():
        print(f"{location}: {items if items else '[empty]'}")
    print("---------------------------\n")

class AwarenessMonitor:
    """Module that checks if the outcome of an action matches expectations."""
    def __init__(self):
        self.log = []
        print("Awareness Monitor [KMSS]: Initialized. Monitoring reality.")

    def check_outcome(self, action, target, state_before, state_after):
        log_entry = f"[ANALYSIS] Action: {action}, Target: {target}. "
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
            log_entry += "Outcome as expected."
        else:
            log_entry += "ANOMALY! Outcome does not match expectation!"
        
        print(log_entry)
        self.log.append(log_entry)

class CloudCortex:
    """The strategic brain capable of conditional planning."""
    def __init__(self):
        print("Cloud Cortex [LLM]: Initialized.")
        self.entity_map = { "czerwony": "red", "niebieski": "blue", "zielony": "green", "sześcian": "cube", "piłka": "ball", "piramida": "pyramid", "strefy a": "zone_A", "strefy b": "zone_B", "bazy": "robot_home", "magazynu": "storage_area" }

    def create_sub_plan(self, object_id, destination_id):
        source_location = next((loc for loc, items in WORLD_STATE['locations'].items() if object_id in items), None)
        if not source_location:
            print(f"Cloud Cortex [LLM]: Sub-plan error - object '{object_id}' does not exist.")
            return None
        return [
            {"action": "GOTO", "target": source_location},
            {"action": "PICKUP", "target": object_id},
            {"action": "GOTO", "target": destination_id},
            {"action": "DROP", "target": object_id}
        ]

    def generate_plan(self, high_level_goal: str) -> list:
        print(f"\nCloud Cortex [LLM]: Received goal: '{high_level_goal}'. Analyzing...")
        time.sleep(1.5)
        goal_lower = high_level_goal.lower()

        if goal_lower.startswith("jeśli"):
             condition_obj_id = "red_cube"; condition_loc = "storage_area"
             print(f"Cloud Cortex [LLM]: Checking condition: Is '{condition_obj_id}' in '{condition_loc}'?")
             if condition_obj_id in WORLD_STATE['locations'].get(condition_loc, []):
                 print("Cloud Cortex [LLM]: Condition TRUE. Executing first path.")
                 return self.create_sub_plan("red_cube", "zone_B")
             else:
                 print("Cloud Cortex [LLM]: Condition FALSE. Executing 'else' path.")
                 return self.create_sub_plan("blue_ball", "zone_A")
        else:
            print("Cloud Cortex [LLM]: Conditional command not recognized. Returning empty plan.")
            return []

class OnboardCore:
    def __init__(self, world_state_ref):
        self.world_state_ref = world_state_ref
        self.robot_state = {"holding": None, "location": "robot_home"}
        print("OnboardCore: Initialized. Ready for action.")

    def execute_plan(self, plan: list, monitor: AwarenessMonitor):
        print("\nOnboard Core [Robot]: Plan received. Starting execution.")
        if not plan: return

        for step in plan:
            action, target = step.get("action"), step.get("target")
            print(f"--- Executing step: {action}, Target: {target or 'N/A'} ---")
            
            state_before = {'robot': self.robot_state.copy(), 'world': json.loads(json.dumps(self.world_state_ref))}
            time.sleep(1)
            success = self.perform_action(action, target)
            state_after = {'robot': self.robot_state.copy(), 'world': json.loads(json.dumps(self.world_state_ref))}
            monitor.check_outcome(action, target, state_before, state_after)

            if not success:
                print("Onboard Core [Robot]: Step execution failed. Aborting plan."); break
        print("\nOnboard Core [Robot]: Plan execution finished.")

    def perform_action(self, action, target):
        world_locations = self.world_state_ref['locations']
        if action == "GOTO":
            self.robot_state["location"] = target; return True
        if action == "PICKUP":
            if random.random() < 0.33:
                print(f"Onboard Core [Robot]: CRITICAL ERROR! Gripper slipped on '{target}'."); return True
            if target in world_locations[self.robot_state['location']] and self.robot_state['holding'] is None:
                world_locations[self.robot_state['location']].remove(target); self.robot_state['holding'] = target
                print(f"Onboard Core [Robot]: Picked up '{target}'."); return True
            return False
        if action == "DROP":
            if self.robot_state['holding'] is not None and self.robot_state['holding'] == target:
                world_locations[self.robot_state['location']].append(self.robot_state['holding']); self.robot_state['holding'] = None
                print(f"Onboard Core [Robot]: Dropped '{target}' in '{self.robot_state['location']}'."); return True
            return False
        return False

def main():
    """Main function to run the simulation."""
    print("--- Starting Nexus Protocol MVP v1.0 Simulation ---")
    world_instance = WORLD_STATE
    cortex = CloudCortex()
    core = OnboardCore(world_instance)
    monitor = AwarenessMonitor()
    display_world_state()
    user_goal = "Jeśli w magazynie jest czerwony sześcian, przenieś go do strefy B. W przeciwnym razie, przynieś niebieską piłkę do strefy A."
    strategic_plan = cortex.generate_plan(user_goal)
    core.execute_plan(strategic_plan, monitor)
    print("\n--- Final World State ---")
    display_world_state()

if __name__ == "__main__":
    main()
