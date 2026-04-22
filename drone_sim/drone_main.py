import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from .modules.motion_controller import MotionController
from .modules.safety_monitor import SafetyMonitor
from .modules.vision_processor import VisionProcessor

class DroneMain(Node):
    def __init__(self):
        super().__init__('drone_main')
        self.publisher = self.create_publisher(Twist, '/model/x3/cmd_vel', 10)
        self.motion = MotionController()
        self.safety = SafetyMonitor()
        self.vision = VisionProcessor(self)
        self.speed = 1.0
        self.run_loop()

    def run_loop(self):
        # ADD THIS PRINT SO YOU KNOW IT STARTED
        print("\n" + "="*30)
        print("DRONE MISSION CONTROL ACTIVE")
        print("Use WSAD to fly, U/J for Alt, K for KILL")
        print("="*30 + "\n")

        while rclpy.ok():
            key = self.motion.get_key()
            is_killed = self.safety.check_kill_switch(key)
            
            # This will print in your terminal every time you press a key
            self.vision.log_status(self.speed, is_killed)

            msg = Twist()
            if not is_killed:
                if key in self.motion.key_map:
                    move = self.motion.key_map[key]
                    msg.linear.x = float(move[0] * self.speed)
                    msg.linear.y = float(move[1] * self.speed)
                    msg.linear.z = float(move[2] * self.speed)
                elif key == '+': self.speed += 0.5
                elif key == '-': self.speed = max(0.5, self.speed - 0.5)
            
            self.publisher.publish(msg)
            if key == '\x03': break

def main():
    rclpy.init()
    rclpy.spin(DroneMain())
    rclpy.shutdown()
