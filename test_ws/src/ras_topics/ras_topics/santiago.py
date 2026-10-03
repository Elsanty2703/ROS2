import rclpy
import serial

from rclpy.node import Node
from example_interfaces.msg import UInt16

class santiago(Node):
    def init(self):
        super().__init__('Santiagox')

        self.serial = serial.Serial(
            port="/dev/ttyACM0",
            baudrate = 115200,
            timeout = 0
        )

        self.subscriber = self.create_subscription(
            UInt16,
            'manguera',
            self.subCallnack,
            10
        )

        self.publisher = self.create_publisher(
            UInt16,
            'tubo',
            10
        )

        self.timerpub = self.self.create_timer(
            0.02,
            self.timerCallback
        )

    def subCallback(self, msg):
        pwm = msg.data
        self.serial.write(pwm)

        self.get_logger().info(f"Mi bro, escucha > {pwm}")

    def timerCallback(self):
        self.serial.read()
