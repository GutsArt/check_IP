import requests
import ipaddress

def get_external_ip():
    try:
        response = requests.get('https://ifconfig.me')
        external_ip = response.text.strip()
        return external_ip
    except requests.RequestException:
        return None

def is_private_ip(ip):
    return ipaddress.ip_address(ip).is_private

external_ip = get_external_ip()
if external_ip:
    if is_private_ip(external_ip):
        print(f"Ваш IP-адрес {external_ip} является серым (частным).")
    else:
        print(f"Ваш IP-адрес {external_ip} является белым (публичным).")
else:
    print("Не удалось определить внешний IP-адрес.")
