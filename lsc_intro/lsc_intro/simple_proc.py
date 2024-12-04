import cv2
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class SimpleProc(Node):

    def __init__(self):
        super().__init__("simple_proc")
        self.subscription = self.create_subscription(
            Image,
            '/image_noise',
            self.image_callback,
            10
        )
        self.bridge = CvBridge()
        self.get_logger().info("Random Noise Image Subscriber Node has been started.")

    def image_callback(self, msg):
        try:
            # Convert ROS Image message to OpenCV image
            cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
            # Display the image
            cv2.imshow("Random Noise Image", cv_image)
            cv2.waitKey(1)  # Needed to refresh the OpenCV window
        except Exception as e:
            self.get_logger().error(f"Failed to process image: {e}")


def main(args=None):

    rclpy.init(args=args)

    simple_proc = SimpleProc()

    rclpy.spin(simple_proc)
    simple_proc.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
