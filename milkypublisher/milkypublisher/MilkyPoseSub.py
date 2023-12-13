import rclpy
from rclpy.node import Node
from milkypublisher_msgs.msg import MilkyPPose

class MilkyPoseSub(Node):
    
        def __init__(self):
            super().__init__('milkyPoseSub')
            self.subscription = self.create_subscription(
                MilkyPPose,
                'milkypublisher/pose',
                self.listener_callback,
                10)
            self.subscription  # prevent unused variable warning
    
        def listener_callback(self, msg):
            self.get_logger().info('I heard: "%s"' % msg.left_ankle)

def main(args=None):
    rclpy.init(args=args)

    milkyPoseSub = MilkyPoseSub()

    rclpy.spin(milkyPoseSub)

    milkyPoseSub.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()