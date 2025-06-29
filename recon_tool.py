import socket
import sys
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def clear_screen():
    os.system("clear")

def banner():
    print(Fore.CYAN + Style.BRIGHT + r"""
                                                                                       

  _ \  __|   __|   _ \   \ |    __ __| _ \   _ \  |    
    /  _|   (     (   | .  | ____| |  (   | (   | |    
 _|_\ ___| \___| \___/ _|\_|      _| \___/ \___/ ____| 
 
                              GitHub => Stanley-blik    
    """)
    print(Fore.GREEN + "          CyberSec Tool 1 - SimpleReconScanner\n")
    print(Fore.YELLOW + "        [+] Author: Stanley (The Cyber Security Bro)\n")

def scan_port(target_ip, port):
    s = socket.socket()
    s.settimeout(1)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(Fore.GREEN + f"[+] Port {port} is OPEN")
        try:
            s.send(b'Hello\r\n')
            banner = s.recv(1024)
            print(Fore.MAGENTA + f"    Banner: {banner.decode().strip()}")
        except:
            print(Fore.RED + "    No banner received.")
    s.close()

def main():
    clear_screen()
    banner()

    target_ip = input(Fore.CYAN + "[?] Enter target IP address: ")

    ports = [
        21,   # FTP
        22,   # SSH
        23,   # Telnet
        25,   # SMTP
        53,   # DNS
        80,   # HTTP
        110,  # POP3
        143,  # IMAP
        443,  # HTTPS
        3306, # MySQL
        8080  # HTTP-alt
    ]

    print(Fore.YELLOW + f"\n[*] Starting scan on {target_ip}\n")

    try:
        for port in ports:
            scan_port(target_ip, port)
    except KeyboardInterrupt:
        print(Fore.RED + "\n[!] Scan interrupted by user.")
        sys.exit()

    print(Fore.GREEN + "\n[*] Scan complete.")

if __name__ == "__main__":
    main()