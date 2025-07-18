# main.py
# Version 1.1 - MVP refactored for clarity and professionalism. All comments and prints are in English.
# Added a placeholder for a real LLM API call in CloudCortex.

import json
import time
import random

# --- WORLD STATE ---
# Defines the virtual world in which the robot operates.
# This is our "single source of truth" for the location of objects.
WORLD_STATE = {
    "locations": {
        "storage_area": ["red_cube", "blue_ball"],
        "zone_A": [],
        "zone_B": ["green_pyramid"],
        "robot_home": []
    }
}

def display_world_state():
    """Helper function to print the current state of the world nicely."""
    print("\n--- Current World State ---")
    for location, items in WORLD_STATE['locations'].items():
        print(f"{location}: {items if items else '[empty]'}")
    print("---------------------------\n")

class AwarenessMonitor:
    """
    This module checks if the outcome of an action matches expectations.
    It's the core of the system's "operational awareness".
    """
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
    """
    The strategic brain of the operation. In a real system, this would make a call
    to a powerful LLM (like Gemini API) to generate a plan.
    """
    def __init__(self):
        print("Cloud Cortex [LLM]: Initialized. Ready for strategic planning.")

    def generate_plan(self, high_level_goal: str) -> list:
        """
        Takes a natural language goal and returns a structured plan.
        *** THIS IS THE FUNCTION TO BE REPLACED WITH A REAL LLM API CALL ***
        """
        print(f"\nCloud Cortex [LLM]: Received goal: '{high_level_goal}'. Generating plan...")
        time.sleep(1.5)

        # For MVP purposes, we simulate the LLM's output with simple logic.
        # A real implementation would send the goal and world state to an LLM
        # and parse the JSON response.
        if "red cube" in high_level_goal and "storage" in high_level_goal and "zone B" in high_level_goal:
            source_location = "storage_area"
            destination = "zone_B"
            obj = "red_cube"
            
            print(f"Cloud Cortex [LLM]: Plan generated successfully.")
            return [
                {"action": "GOTO", "target": source_location},
                {"action": "PICKUP", "target": obj},
                {"action": "GOTO", "target": destination},
                {"action": "DROP", "target": obj}
            ]
        else:
            print(f"Cloud Cortex [LLM]: Could not generate a plan for this goal.")
            return []

class OnboardCore:
    """
    The "body" or "executor" of the operation. It executes the plan step-by-step.
    """
    def __init__(self, world_state_ref):
        self.world_state_ref = world_state_ref
        self.robot_state = {"holding": None, "location": "robot_home"}
        print("OnboardCore [Robot]: Initialized. Ready for action.")

    def execute_plan(self, plan: list, monitor: AwarenessMonitor):
        print("\nOnboard Core [Robot]: Plan received. Starting execution.")
        if not plan: 
            print("Onboard Core [Robot]: Plan is empty. No actions to perform.")
            return

        for step in plan:
            action, target = step.get("action"), step.get("target")
            print(f"--- Executing step: {action}, Target: {target or 'N/A'} ---")
            
            state_before = {'robot': self.robot_state.copy(), 'world': json.loads(json.dumps(self.world_state_ref))}
            time.sleep(1)
            success = self.perform_action(action, target)
            state_after = {'robot': self.robot_state.copy(), 'world': json.loads(json.dumps(self.world_state_ref))}

            monitor.check_outcome(action, target, state_before, state_after)

            if not success:
                print("Onboard Core [Robot]: Step execution failed. Aborting plan.")
                break
        print("\nOnboard Core [Robot]: Plan execution finished.")

    def perform_action(self, action, target):
        """Simulates the physical execution of a single action."""
        world_locations = self.world_state_ref['locations']
        if action == "GOTO":
            self.robot_state["location"] = target
            print(f"Onboard Core [Robot]: Moved to '{target}'.")
            return True
        if action == "PICKUP":
            # Simulating a physical failure
            if random.random() < 0.33:
                print(f"Onboard Core [Robot]: CRITICAL ERROR! Gripper slipped while trying to pick up '{target}'.")
                return True # The action was attempted, but the outcome was a failure
            if target in world_locations[self.robot_state['location']] and self.robot_state['holding'] is None:
                world_locations[self.robot_state['location']].remove(target)
                self.robot_state['holding'] = target
                print(f"Onboard Core [Robot]: Picked up '{target}'.")
                return True
            return False
        if action == "DROP":
            if self.robot_state['holding'] is not None and self.robot_state['holding'] == target:
                world_locations[self.robot_state['location']].append(self.robot_state['holding'])
                self.robot_state['holding'] = None
                print(f"Onboard Core [Robot]: Dropped '{target}' in '{self.robot_state['location']}'.")
                return True
            return False
        return False

def main():
    """Main function to run the simulation."""
    print("--- Starting Nexus Protocol MVP v1.1 Simulation ---")
    
    world_instance = WORLD_STATE
    cortex = CloudCortex()
    core = OnboardCore(world_instance)
    monitor = AwarenessMonitor()

    display_world_state()

    user_goal = "Bring the red cube from the storage area to zone B"
    strategic_plan = cortex.generate_plan(user_goal)
    core.execute_plan(strategic_plan, monitor)

    print("\n--- Final World State ---")
    display_world_state()

if __name__ == "__main__":
    main()
