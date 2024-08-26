# -- coding: utf-8 --

import time # Lib para o time
from netmiko import ConnectHandler    #lib netmiko
import pyfiglet #lib para o Banner do App

# Banner do aplicativo
banner = pyfiglet.figlet_format("Python + Automacao de Redes")
print(banner)


def print_menu(): # menu com a opção dos Device
    print('Qual Equipamento iremos acessar?')
    print('-=-' * 5, 'Escolha uma das opções', '-=-' * 5)
    print('1. Acessando o Switch Huawei S6730')
    print('2. Acessando o Switch Cisco Core')
    print('3. Acessando o Switch Mikrotik CRS')
    print('4. Acessando o Servidor Debian')
    print('5. Encerrar o programa')
    print('-=-' * 18)


def huawei_menu(connect): # opções para o Device Huawei
    while True:
        print('\n---- Comandos Disponíveis para Huawei S6730 ----')
        print('1. Mostrar diagnósticos de transceptores')
        print('2. Mostrar informações do sistema')
        print('3. Mostrar interfaces')
        print('4. Inserir um comando personalizado')
        print('5. Voltar ao Menu Anterior')
        print('6. Dicionário de Comandos da Huawei')
        comando = input('Escolha um comando [1-6]: ')

        output = ""  # Valor padrão para output

        try:
            if comando == '1':
                output = connect.send_command('display transceiver diagnostics interface')
            elif comando == '2':
                output = connect.send_command('display version')
            elif comando == '3':
                output = connect.send_command('display interface brief')
            elif comando == '4':
                comando_customizado = input('Digite o comando que deseja executar: ')
                output = connect.send_command(comando_customizado)
            elif comando == '5':
                break
            elif comando == '6':
                print("\nDicionário de Comandos Huawei:")
                print("1. display transceiver diagnostics interface")
                print("2. display interface brief")
                print("3. display cpu-usage")
                print("4. display version")
                print("5. display ip routing-table")
                print("6. display vlan")
                print("7. display arp")
                print("8. display logbuffer")
                print("9. display firewall policy")
                print("10. display interface description")
                print("11. display port-info")
                print("12. display dhcp snooping binding")
                print("13. display interface status")
                print("14. display route")
                print("15. display ssh server status")
                print("16. display system")
                print("17. display bgp peer")
                print("18. display ospf peer")
                print("19. display ntp status")
                print("20. display user-interface")
            else:
                print('Opção inválida. Tente novamente.')
                continue

            if output:
                print(output)
        except Exception as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")


def cisco_menu(connect): # Opções para o Device Cisco
    while True:
        print('\n---- Comandos Disponíveis para Cisco Core ----')
        print('1. Mostrar versão do sistema')
        print('2. Mostrar interfaces')
        print('3. Mostrar status da VLAN')
        print('4. Inserir um comando personalizado')
        print('5. Voltar ao Menu Anterior')
        print('6. Dicionário de Comandos Cisco')
        comando = input('Escolha um comando [1-6]: ')

        output = ""  # Valor padrão para output

        try:
            if comando == '1':
                output = connect.send_command('show version')
            elif comando == '2':
                output = connect.send_command('show ip interface brief')
            elif comando == '3':
                output = connect.send_command('show vlan brief')
            elif comando == '4':
                comando_customizado = input('Digite o comando que deseja executar: ')
                output = connect.send_command(comando_customizado)
            elif comando == '5':
                break
            elif comando == '6':
                print("\nDicionário de Comandos Cisco:")
                print("1. show ip interface brief")
                print("2. show mac address-table")
                print("3. show version")
                print("4. show running-config")
                print("5. show interfaces status")
                print("6. show ip route")
                print("7. show vlan brief")
                print("8. show arp")
                print("9. show logging")
                print("10. show processes cpu")
                print("11. show memory statistics")
                print("12. show ntp status")
                print("13. show cdp neighbors")
                print("14. show ip bgp summary")
                print("15. show ip ospf neighbor")
                print("16. show interfaces description")
                print("17. show startup-config")
                print("18. show ip protocols")
                print("19. show policy-map")
                print("20. show access-lists")
            else:
                print('Opção inválida. Tente novamente.')
                continue

            if output:
                print(output)
        except Exception as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")


def mikrotik_menu(connect): # Opções para o Device Mikrotik
    while True:
        print('\n---- Comandos Disponíveis para Mikrotik CRS ----')
        print('1. Mostrar informações do sistema')
        print('2. Mostrar interfaces')
        print('3. Mostrar configuração de IPs')
        print('4. Inserir um comando personalizado')
        print('5. Voltar ao Menu Anterior')
        print('6. Dicionário de Comandos Mikrotik')
        comando = input('Escolha um comando [1-6]: ')

        output = ""  # Valor padrão para output

        try:
            if comando == '1':
                output = connect.send_command('/system resource print')
            elif comando == '2':
                output = connect.send_command('/interface print')
            elif comando == '3':
                output = connect.send_command('/ip address print')
            elif comando == '4':
                comando_customizado = input('Digite o comando que deseja executar: ')
                output = connect.send_command(comando_customizado)
            elif comando == '5':
                break
            elif comando == '6':
                print("\nDicionário de Comandos Mikrotik:")
                print("1. /interface print")
                print("2. /ip address print")
                print("3. /ip route print")
                print("4. /system resource print")
                print("5. /ip arp print")
                print("6. /ip firewall filter print")
                print("7. /interface vlan print")
                print("8. /interface wireless print")
                print("9. /interface ethernet print")
                print("10. /system logging print")
                print("11. /system scheduler print")
                print("12. /interface bridge print")
                print("13. /system routerboard print")
                print("14. /ip dhcp-server lease print")
                print("15. /interface bridge port print")
                print("16. /ip firewall nat print")
                print("17. /interface wireless registration-table print")
                print("18. /interface ethernet switch print")
                print("19. /interface wireless access-list print")
                print("20. /interface ethernet switch port print")
            else:
                print('Opção inválida. Tente novamente.')
                continue

            if output:
                print(output)
        except Exception as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")


def debian_menu(connect): # Opções para o Host do Servidor Debian
    while True:
        print('\n---- Comandos Disponíveis para Servidor Debian ----')
        print('1. Mostrar informações do sistema')
        print('2. Mostrar interfaces de rede')
        print('3. Mostrar uso do disco')
        print('4. Inserir um comando personalizado')
        print('5. Voltar ao Menu Anterior')
        print('6. Dicionário de Comandos Debian')
        comando = input('Escolha um comando [1-6]: ')

        output = ""  # Valor padrão para output

        try:
            if comando == '1':
                output = connect.send_command('uname -a')
            elif comando == '2':
                output = connect.send_command('ip a')
            elif comando == '3':
                output = connect.send_command('df -h')
            elif comando == '4':
                comando_customizado = input('Digite o comando que deseja executar: ')
                output = connect.send_command(comando_customizado)
            elif comando == '5':
                break
            elif comando == '6':
                print("\nDicionário de Comandos Debian:")
                print("1. df -h")
                print("2. ps aux")
                print("3. ip a")
                print("4. free -h")
                print("5. uname -a")
                print("6. route -n")
                print("7. lsblk")
                print("8. netstat -tuln")
                print("9. top")
                print("10. uptime")
                print("11. dmesg")
                print("12. journalctl -xe")
                print("13. ls /var/log/")
                print("14. lsof -i")
                print("15. sudo lshw -short")
                print("16. cat /etc/network/interfaces")
                print("17. ifconfig")
                print("18. ip link show")
                print("19. cat /proc/cpuinfo")
                print("20. cat /proc/meminfo")
            else:
                print('Opção inválida. Tente novamente.')
                continue

            if output:
                print(output)
        except Exception as e:
            print(f"Ocorreu um erro ao executar o comando: {e}")


def connect_device(device_type, host):
    try:
        device = {
            'device_type': device_type,
            'host': host,
            'username': 'superadm',
            'password': 'SENHA-FORTE',
            'timeout': 60,   #Aumenta o timeout
            'fast_cli': False,  #Desativa o modo rápido, pode ajudar na detecção do prompt
            'session_log': 'session.log',  # Log para depuração
        }
        return ConnectHandler(**device)
    except Exception as e:
        print(f"Erro ao conectar ao dispositivo: {e}")
        return None


loop = True

while loop:
    time.sleep(1)
    print_menu()
    opcao = input('Selecione uma das Opções [1-5]: ')

    if opcao == '1':
        connect = connect_device('huawei', '10.0.250.1')
        if connect:
            print('Acessando o Switch Huawei S6730...')
            print(connect.find_prompt())
            huawei_menu(connect)

    elif opcao == '2':
        connect = connect_device('cisco_ios', '10.0.250.2')
        if connect:
            print('Acessando o Switch Cisco Core...')
            print(connect.find_prompt())
            cisco_menu(connect)

    elif opcao == '3':
        connect = connect_device('mikrotik_routeros', '10.0.250.3')
        if connect:
            print('Acessando o Switch Mikrotik CRS...')
            print(connect.find_prompt())
            mikrotik_menu(connect)

    elif opcao == '4':
        connect = connect_device('linux', '10.0.250.4')
        if connect:
            print('Acessando o Servidor Debian...')
            print(connect.find_prompt())
            debian_menu(connect)

    elif opcao == '5':
        print('Encerrando o programa.')
        loop = False

    else:
        print('Opção inválida. Tente novamente.')

    if 'connect' in locals() and connect:
        connect.disconnect() 