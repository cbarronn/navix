import socket

class Config:
    DEBUG = True
    
    # Obtener un puerto disponible dinámicamente
    s = socket.socket()
    s.bind(('localhost', 0))
    PORT = s.getsockname()[1]
    s.close()
    
    HOST = '0.0.0.0'  # Accesible por IP
