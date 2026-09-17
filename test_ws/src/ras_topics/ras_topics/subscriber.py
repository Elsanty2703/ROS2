import rclpy
from std_msgs.msg import String


def callback_string(msg):
    print(f'Mensaje recibido: {msg.data}')


def main():
    #Iniciar ROS 2
    rclpy.init()

    #Crear Nodo
    node = rclpy.create_node('subscriber_node')

    #Crear Subscriptor
    sub = node.create_subscription(
        String,
        'ras_publicador',
        callback_string,
        10
    )

    #While (SPIN, mantiene el nodo activo escuchando)
    rclpy.spin(node)

    #Destruir nodo
    node.destroy_node()

    #Finalizar ROS 2
    rclpy.shutdown()


if __name__ == '__main__':
    main()