import rclpy
from rclpy.node import Node
from socket import socket, AF_INET, SOCK_DGRAM

from std_msgs.msg import String
from milkypublisher_msgs.msg import MilkyPPose

import time



class MilkyPublisher(Node):

    def __init__(self) -> None:
        super().__init__("Milkypublisher")
        self.logger = self.get_logger()
        HOST = '127.0.0.1'
        PORT = 4001
        self.s = socket(AF_INET,SOCK_DGRAM)
        self.s.bind((HOST,PORT))
        self.main()
    
    def main(self):
        while True:
            try :
                # ③Clientからのmessageの受付開始
                print('Waiting message')
                message, cli_addr = self.s.recvfrom(8192)
                message = message.decode(encoding='utf-8')
                print(f'Received message is [{message}]')
                ipaddress = message.split("%")[0]
                portaddress = message.split("%")[1]
                
                # Clientが受信待ちになるまで待つため
                time.sleep(0.05)
                
                
                # TODO: ROS2はライブラリ上ネットワークの制約を書けているかもしれない。要検討

            except KeyboardInterrupt:
                print ('\n . . .\n')
                self.s.close()
                break   


def main(args=None):
    rclpy.init(args=args)
    milkyplubsher = MilkyPublisher()
    rclpy.spin(milkyplubsher)
    milkyplubsher.destroy_node()
    rclpy.shutdown()
    
    


if __name__ == '__main__':
    main()
