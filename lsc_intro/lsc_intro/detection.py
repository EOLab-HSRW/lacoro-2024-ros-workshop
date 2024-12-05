import rclpy
from rclpy.node import Node
from ultralytics import YOLO

class Detection(Node):

    def __init__(self):
        super().__init__("detection_node")

def main(args=None):

    rclpy.init(args=args)

    detection_node = Detection()

    rclpy.spin(detection_node)
    detection_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
