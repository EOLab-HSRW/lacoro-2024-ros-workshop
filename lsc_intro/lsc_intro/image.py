import numpy as np
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class ImageNode(Node):

    def __init__(self):
        super().__init__("image")

        self.__pub = self.create_publisher(Image, "/image_noise", 10)

        self.__timer = self.create_timer(1/30, self.pub_image)

        height, width = 480, 640
        img = np.random.randint(0, 256, (height, width, 3), dtype=np.uint8)

        bridge = CvBridge()
        self.__img_msg = bridge.cv2_to_imgmsg(img, encoding="bgr8")

    def pub_image(self):

        self.__pub.publish(self.__img_msg)


def main(args=None) -> None:

    rclpy.init(args=args)

    image_node = ImageNode()

    rclpy.spin(image_node)
    image_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
