import socket

def serverSocketMode(application):
    ip = '192.168.100.10'
    port = 65002
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind( (ip, port) )
    server.listen(1)
    while True:
        connection, client = server.accept()
        msg = connection.recv(1024)
        application.setMessage(msg.decode("utf-8"))

def sendMessageSocket(message):
    ip = '192.168.100.10'
    port = 65002
    socketobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socketobj.connect((ip, port))
    socketobj.send(message.encode('UTF-8'))

# Funcao que converte strings para uma string de numeros binarios.
def toBin(st, withSpace):
    string = ''
    #Coloca um espaco no final de cada conjunto de bits que correponde a uma letra
    if withSpace == True:
        for x in st:
            string += format(ord(x), 'b') + " "
    #Sem espaco no final, usado para gerar o gráfico
    elif withSpace == False:
        for x in st:
            string += format(ord(x), 'b')

    return string

def binToString(bits, encoding='ISO-8859-1', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def encodeMesage(binary_message, encode_type):
    if encode_type == 'NRZ Unipolar Encoded':
        return binary_message
    elif encode_type == 'NRZ-Invert Encoded':
        return encodeNRZInvert(binary_message)
    elif encode_type == 'NRZ-Level Encoded':
        return encodeNRZLevel(binary_message)
    elif encode_type == 'RZ Encoded':
        return encodeRZ(binary_message)   
    else:
        return None

def signalStringToList(signal_string):
    binary_list = []
    past_bin = None
    for bin in signal_string:
        if bin == '1' and past_bin == '-':
            binary_list.append('-1')
        elif bin == '1' and (past_bin == '1' or past_bin == '0' or past_bin == None):
            binary_list.append('1')
        elif bin == '0':
            binary_list.append('0')
        past_bin = bin

    return binary_list

def decodeMesage(signal_message, decode_type):
    signal_message = signalStringToList(signal_message)
    if decode_type == 'NRZ Unipolar Encoded':
        return signal_message
    elif decode_type == 'NRZ-Invert Encoded':
        return decodeNRZInvert(signal_message)
    elif decode_type == 'NRZ-Level Encoded':
        return decodeNRZLevel(signal_message)
    elif decode_type == 'RZ Encoded':
        return decodeRZ(signal_message)   
    else:
        return None

def encodeNRZLevel(message):
    encoded_signal = []
    for bit in message:
        if bit == '1':
            encoded_signal.append('-1')
        else:
            encoded_signal.append('1')
    
    return encoded_signal

def decodeNRZLevel(signal):
    decoded_message = []
    for sig in signal:
        if sig == '-1':
            decoded_message.append('1')
        else:
            decoded_message.append('0')

    return decoded_message


def encodeNRZInvert(message):
    encoded_signal = []
    first_bit = False
    for bit in message:
        if first_bit == False:
            first_bit = True
            if bit == '1':
                signal = -1
            else:
                signal = 1
        else:
            if bit == '1':
                signal = signal*(-1)

        encoded_signal.append(signal)

    encoded_signal = [str(e) for e in encoded_signal]
    return encoded_signal

def decodeNRZInvert(signal):
    decoded_message = []
    first_sig = False
    past_sig = None
    for sig in signal:
        if first_sig == False:
            first_sig = True
            if sig == '1':
                bit = '0'
            else:
                bit = '1'
        else:
            if sig == past_sig:
                bit = '0'
            else:
                bit = '1'
        
        decoded_message.append(bit)
        past_sig = sig

    return decoded_message

def encodeRZ(message):
    encoded_signal = []
    for bit in message:
        if bit == '1':
            encoded_signal.append('1')
            encoded_signal.append('0')
        else:
            encoded_signal.append('-1')
            encoded_signal.append('0')

    return encoded_signal

def decodeRZ(signal):
    decoded_message = []
    for i in range(0, len(signal), 2):
        if signal[i] == '1' and  signal[i+1] == '0':
            decoded_message .append('1')
        else:
            decoded_message.append('0')

    return decoded_message

