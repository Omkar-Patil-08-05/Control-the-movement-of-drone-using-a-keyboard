import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from .modules.keyboard_handler import KeyboardHandler

class DroneController(Node):
    def __init__(self):
        super().__init__('drone_controller')
        self.publisher_ = self.create_publisher(Twist, '/model/x3/cmd_vel', 10)
        self.kh = KeyboardHandler()
        self.speed = 5.0
        self.run_loop()

    def run_loop(self):
        print("\n--- Drone 6-DOF Controller ---")
        print("W/S: Front/Back | A/D: Left/Right")
        print("U/J: Up/Down    | X: Stop")
        print("+/-: Change Speed")
        
        while rclpy.ok():
            key = self.kh.get_key()
            msg = Twist()
            
            if key in self.kh.key_map:
                move = self.kh.key_map[key]
                msg.linear.x = move[0] * self.speed
                msg.linear.y = move[1] * self.speed
                msg.linear.z = move[2] * self.speed
                self.publisher_.publish(msg)
            elif key == '+' or key == '=':
                self.speed += 0.1
                print(f"Speed: {self.speed:.1f}")
            elif key == '-' or key == '_':
                self.speed = max(0.1, self.speed - 0.1)
                print(f"Speed: {self.speed:.1f}")
            elif key == '\x03': # Ctrl+C
                break

def main():
    rclpy.init()
    node = DroneController()
    rclpy.spin(node)
    rclpy.shutdown()
