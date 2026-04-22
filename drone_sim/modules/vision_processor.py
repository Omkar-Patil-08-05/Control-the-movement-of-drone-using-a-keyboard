class VisionProcessor:
    def __init__(self, node):
        self.node = node

    def log_status(self, speed, locked):
        status = "LOCKED (Kill Switch)" if locked else "ACTIVE"
        self.node.get_logger().info(f"Status: {status} | Current Speed: {speed:.1f}")
