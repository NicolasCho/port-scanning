from input_validators import *
import os
import socket


def host_scan():
    port_dict = {}
    with open("ports.txt") as f:
        for line in f:
            (key,val) = line.split(":")
            port_dict[int(key)] = val

    os.system("cls")
    print("HOST SCAN\n")   
    print("---------------------------------------\n")

    print("Insira IP do host alvo:")
    host_ip = check_ip()

    print("\nDefina o intervalo de portas\n")

    print("RANGE DE PORTAS")
    print("Well Known Ports  => 0 - 1023")
    print("Registered Ports  => 1024 - 49151")
    print("Other Ports       => 49152 - 64738\n")

    print("Porta de início do intervalo: ")     
    port_init = check_range(0, 64738)

    print("\nPorta final do intervalo: ")   
    port_end = check_range(port_init, 64738)

    print("\nIniciando escaneamento...\n")
    print("PORTAS ABERTAS\n")
    print(" PROTOCOLO     PORTA      SERVIÇO ")
    try:
        for port in range(port_init, port_end):
            found = False
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.4)
            if(s.connect_ex((host_ip, port)) == 0):
                try:
                    print("    TCP  |     {}     |   {}   \n".format(port, socket.getservbyport(port, "tcp")))
                    found = True
                except:
                    pass
                try:
                    print("    UDP  |     {}     |   {}   \n".format(port, socket.getservbyport(port, "udp")))
                    found = True
                except:
                    pass
                if not found:
                    print("         |     {}     |   {}   \n".format(port, port_dict[port]))
                print("-----------------------------------")
                    
    except KeyboardInterrupt:
        print("Escaneamento encerrado\n")
    except socket.error:
        print("ERRO")
        print("Sem resposta\n")

    print("(pressione ENTER para voltar..)")
    voltar = input("=> ")

def net_scan():
    os.system("cls")
    print("LOCALNET SCAN\n")   
    print("---------------------------------------\n")

    os.system("arp -a")

    print("(pressione ENTER para voltar..)")
    voltar = input("=> ")