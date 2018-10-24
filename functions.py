import socket

def serverSocketMode(application):
    ip = 'localhost'
    port = 65001
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind( (ip, port) )
    server.listen(1)
    while True:
        connection, client = server.accept()
        msg = connection.recv(1024)
        application.setMessage(msg.decode("utf-8"))

def sendMessageSocket(message):
    ip = 'localhost'
    port = 65001
    socketobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketobj.connect((ip, port))
    socketobj.send(message.encode('UTF-8'))

# Funcao que converte strings para uma string de numeros binarios.
def toBin(st, withSpace):
    string = ''
    #Coloca um espaco no final de cada conjunto de bits que correponde a uma letra
    if withSpace == 1:
        for x in st:
            string += format(ord(x), 'b') + " "
    #Sem espaco no final, usado para gerar o gráfico
    elif withSpace == 0:
        for x in st:
            string += format(ord(x), 'b')

    return string

def encodeNRZLevel(message):
    encoded_message = []
    for character in message:
        if character == '1':
            encoded_message.append('-1')
        elif character == '0':
            encoded_message.append('1')
        else:
            encoded_message.append(character)
    
    return ''.join(encoded_message)

def decodeNRZLevel(message):
    decoded_message = []
    past_character = None
    for character in message:
        if past_character == '-': # If is -1 then the past character have to be '-'
            decoded_message.append('1')
        elif character == '1':
            decoded_message.append('0')
        past_character = character

    return ''.join(decoded_message)


def encodeNRZInvert(message):
    encoded_message = []
    first_character = False
    for character in message:
        if first_character == False:
            first_character = True
            signal = 1
        else:
            if character == '1':
                signal = signal*(-1)

        encoded_message.append(signal)

    return ''.join(str(e) for e in encoded_message)

def decodeNRZInvert(signals):
    decoded_message = []
    first_character = False
    past_character = None
    for signal in signals:
        if first_character == False:
            first_character = True
            signal = character
        else:
            if character == '1':
                signal = signal*(-1)

        decoded_message.append(bit)
        past_character = character

    return encoded_message