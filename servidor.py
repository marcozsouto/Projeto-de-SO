import socket
import threading
import numpy as np
import computadorA

host = 'localhost'
porta = 50000
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((host, porta))
servidor.listen()
print ('aguardando resposta')


while True:
    cliente, endereço = servidor.accept()
    print('conectado em ', endereço)
    
    # mapeamento das Threads
    requisicao = threading.Thread(target=computadorA.processo, args=(cliente,))
    requisicao1 = threading.Thread(target=computadorA.processo1, args=(cliente,))

    if computadorA.mutex == 0:
        requisicao.run()
    elif computadorA.mutex1 == 0:
        requisicao1.run()
