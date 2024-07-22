import subprocess
import string
import random
import re
import platform

def RANDOM_MAC(): 
    uppercased_hexdigits = ''.join(set(string.hexdigits.upper())) + '13579BDF' # neue Symbole hinzufügen
    mac = ""
    for i in range(6):
        for j in range(2):
            if i == 0:
                mac += random.choice("02468ACE")
            else:
                mac += random.choice(uppercased_hexdigits)
        mac += ":"
    return mac.strip(":")

def GET_PERMANENT_MAC(iface):
    # OS Spezifische Kommando zur Abfrage der MAC-Adresse
    if platform.system() == "Windows":
        output = subprocess.check_output(f"getmac /v /fo list", shell=True).decode()
        mac_addresses = re.findall(r"Physical Address:\s*([A-F0-9:-]+)", output)
        if mac_addresses:
            return mac_addresses[0]
        else:
            return "MAC address not found"
    elif platform.system() == "Linux":
        output = subprocess.check_output(f"ip link show {iface}", shell=True).decode()
        return re.search(r"ether\s([A-Fa-f0-9:]+)", output).group(1).strip()

def CHANGE_MAC_ADRESS(iface, NEW_MAC_ADRESS):
    # Plattform-spezifische Kommandos zur Deaktivierung und Aktivierung des Netzwerkinterfaces
    if platform.system() == "Windows":
        subprocess.check_output(f"netsh interface set interface \"{iface}\" admin=disable", shell=True)
        subprocess.check_output(f"reg add HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Class\\{{4D36E972-E325-11CE-BFC1-08002BE10318}}\\0001 /v NetworkAddress /t REG_SZ /d {NEW_MAC_ADRESS} /f", shell=True)
        subprocess.check_output(f"netsh interface set interface \"{iface}\" admin=enable", shell=True)
    elif platform.system() == "Linux":
        subprocess.check_output(f"sudo ip link set dev {iface} down", shell=True)
        subprocess.check_output(f"sudo ip link set dev {iface} address {NEW_MAC_ADRESS}", shell=True)
        subprocess.check_output(f"sudo ip link set dev {iface} up", shell=True)

if __name__ == "__main__":
    import argparse 
    PARSER = argparse.ArgumentParser(description="Python Macspoofer Coded by Yqno")
    PARSER.add_argument("interface", help="The network interface name")
    PARSER.add_argument("-r", "--random", action="store_true", help="Generate a random MAC address")
    PARSER.add_argument("-m", "--mac", help="The new MAC address you want to change to")
    args = PARSER.parse_args()
    iface = args.interface
    if args.random:
        # Wenn der Random-Parameter gesetzt ist, generiere eine zufällige MAC-Adresse
        NEW_MAC_ADRESS = RANDOM_MAC()
    elif args.mac:
        # Wenn die MAC-Adresse gesetzt ist, benutze sie stattdessen
        NEW_MAC_ADRESS = args.mac
    else:
        print("Error: You must specify either --random or --mac")
        exit(1)
        
    # Abfrage der permanenten MAC-Adresse
    PERMANENT_MAC_ADRESS = GET_PERMANENT_MAC(iface)
    print("[*] Permanent MAC address:", PERMANENT_MAC_ADRESS)   
    # Ändern der MAC-Adresse
    CHANGE_MAC_ADRESS(iface, NEW_MAC_ADRESS)
    print("[*] New MAC address:", NEW_MAC_ADRESS)
