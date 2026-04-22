class SafetyMonitor:
    def __init__(self):
        self.emergency_lock = False

    def check_kill_switch(self, key):
        # Press 'k' for Emergency Kill
        if key == 'k':
            print("\n!!! EMERGENCY KILL SWITCH ACTIVATED !!!")
            self.emergency_lock = True
            return True
        # Press 'r' to Reset after kill
        if key == 'r' and self.emergency_lock:
            print("\nSafety Reset. Drone Re-armed.")
            self.emergency_lock = False
        return self.emergency_lock
