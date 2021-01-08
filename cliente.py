import socket
import numpy as np

host = 'localhost'
porta = 50000

a = np.arange(100).reshape(10,10)
b = np.arange(100).reshape(10,10)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((host, porta))
cliente.send(a.tobytes())
cliente.send(b.tobytes())
resposta = cliente.recv(2048)
resposta = np.frombuffer(resposta, dtype=int).reshape(10,10)
print('devolvido: ', resposta)
