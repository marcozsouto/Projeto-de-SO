import socket
import threading
import numpy as np
import computadorA
import computadorB
import time

lista = []
host = 'localhost'
porta = 50000
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, porta))
servidor.listen()
print ('aguardando resposta')

def requisicao(target, cliente):    
    
    #target mutex
    if target == computadorA.processo:
        mutex =  computadorA.mutex
    elif target == computadorA.processo1:
        mutex =  computadorA.mutex1
    elif target == computadorB.processo:
        mutex =  computadorB.mutex
    elif target == computadorB.processo1:
        mutex =  computadorB.mutex1
    elif target == computadorB.processo2:
        mutex =  computadorB.mutex2

    #tenta usar a thread desejada 
    if mutex == 0:
        requisicao = threading.Thread(target=target, args=(cliente,))
        requisicao.start()
        return True

    #testa as outras
    elif computadorA.mutex == 0:  
        requisicao = threading.Thread(target=computadorA.processo, args=(cliente,))
        requisicao.start()
        return True

    elif computadorA.mutex1 == 0:
        requisicao = threading.Thread(target=computadorA.processo1, args=(cliente,))
        requisicao.start()
        return True

    return False

while True:
    cliente, endereço = servidor.accept()
    print('conectado em ', endereço)
    #chamada de novo processo 
    requisicao(computadorA.processo, cliente)
    