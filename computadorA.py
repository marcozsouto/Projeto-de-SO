import socket
import numpy as np

mutex = 0
mutex1 = 0


def processo(cliente):
    print('computadorA - processo')
    mutex = 1
    mensagem = cliente.recv(2048)
    mensagem = np.frombuffer(mensagem, dtype=int)
    a, b = np.split(mensagem,2)
    a = a.reshape(10,10)
    b = b.reshape(10,10)
    m = a.dot(b)
    cliente.send(m.tostring())
    mutex = 0

def processo1(cliente):
    print('computadorA - processo 1')
    mutex1 = 1
    mensagem = cliente.recv(2048)
    mensagem = np.frombuffer(mensagem, dtype=int)
    a, b = np.split(mensagem,2)
    a = a.reshape(10,10)
    b = b.reshape(10,10)
    m = a.dot(b)
    cliente.send(m.tostring())
    mutex1 = 0