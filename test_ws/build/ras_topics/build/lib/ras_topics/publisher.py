import rclpy
from std_msgs.msg import String


def main():
    #Inicializar ROS 2
    rclpy.init()
    
    #Crear Nodo
    node = rclpy.create_node('publisher_node')

    #Crear Publicador
    pub = node.create_publisher(String, 'ras_publicador', 10)

    #Crear Mensage
    msg = String() #Twist, Float32 Int32 
    i = 0

    #While
    while rclpy.ok():
        print('Publicando mensaje...')

        #Crando el mansaje
        msg_python = f'Hola desde RAS {i}'
        i += 1

        #Llenar compos del mensaje
        msg.data = msg_python

        #Publicar mensaje
        pub.publish(msg)
    
    #Destruir nodo
    node.destroy_node()

    #FInalizar ROS2
    rclpy.shutdown()



if __name__ == '__main__':
    main()