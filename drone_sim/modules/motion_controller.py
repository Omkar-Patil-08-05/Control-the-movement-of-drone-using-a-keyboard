import sys, termios, tty

class MotionController:
    def __init__(self):
        self.settings = termios.tcgetattr(sys.stdin)
        self.key_map = {
            'w': (1.0, 0.0, 0.0), 's': (-1.0, 0.0, 0.0),
            'a': (0.0, 1.0, 0.0), 'd': (0.0, -1.0, 0.0),
            'u': (0.0, 0.0, 1.0), 'j': (0.0, 0.0, -1.0),
            'x': (0.0, 0.0, 0.0) # Stop
        }

    def get_key(self):
        tty.setraw(sys.stdin.fileno())
        key = sys.stdin.read(1)
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self.settings)
        return key
