import sys
import socket
import os
import ipaddress
from port_scanner import *
from services import *

def main():
    while True:
        os.system("cls")
        print("The Unnamed Port Scanning Project\n")

        print("---------------------------------------\n")
        print("Escolha o serviço:\n")

        print("    1 - Escaneamento de host\n    2 - Escaneamento de rede\n    3 - Sair\n")
        servico = check_input(3)

        if servico == 1:
            host_scan()
        elif servico == 2:
            net_scan()
        else:
            return

if __name__ == "__main__":
    main()