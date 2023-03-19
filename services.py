from input_validators import *
import os


def host_scan():
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
    print("  PORTA    SERVIÇO ")
    try:
        for port in range(port_init, port_end):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.5)

            if(s.connect_ex((host_ip, port)) == 0):
                if port <= 1023: # Well known ports
                    print("   {}   |   {}   \n".format(port, socket.getservbyport(port)))
                else:
                    print("{}\n".format(port))
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