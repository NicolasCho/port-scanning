import socket

def check_ip():
    while True:
        try:
            ip = socket.gethostbyname(input('=> '))
            break
        except socket.gaierror:
            print("Host inválido!")
    return ip

def check_input(n_options, include_zero = False, exclude_limit = False):
    floor = 0
    ceiling = n_options
    if include_zero:
        floor = -1
    if exclude_limit:
        ceiling = n_options - 1 

    servico = floor 
    while servico == floor:
        user_input = input("=> ")
        try:
            servico = int(user_input)
            if servico <= floor or servico > ceiling:
                servico = floor
                print("Entrada inválida")

        except:
            print("Entrada inválida")

    
    
    return servico

def check_range(start, end):
    valor = -1
    while valor < 0:
        valor = input("=> ")
        try:
            valor = int(valor)
            if valor < start  or valor > end:
                valor = -1
                print("Entrada inválida")

        except:
            valor = -1
            print("Entrada inválida")
    
    return valor