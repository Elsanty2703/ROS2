import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/elsanty2703r/Descargas/RAS_Javeriana/test_ws/install/ras_topics'
