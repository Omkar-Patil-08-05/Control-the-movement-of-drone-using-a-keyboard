import sys
import termios
import tty

class KeyboardHandler:
    def __init__(self):
        self.settings = termios.tcgetattr(sys.stdin)
        
        # Mapping: (Linear X, Linear Y, Linear Z)
        self.key_map = {
            'w': (1.0, 0.0, 0.0),   # Forward
            's': (-1.0, 0.0, 0.0),  # Backward
            'a': (0.0, 1.0, 0.0),   # Left
            'd': (0.0, -1.0, 0.0),  # Right
            'u': (0.0, 0.0, 1.0),   # Up
            'j': (0.0, 0.0, -1.0),  # Down
            'x': (0.0, 0.0, 0.0),   # Stop
        }

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key
