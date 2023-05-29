import socket

def get_ip_address(domain):
    try:
        ip_address = socket.gethostbyname(domain)
        return ip_address
    except socket.gaierror:
        return None

# Пример использования:
domain = "tatyanabushkova.taplink.ws"  # Замените на свой домен или сайт
ip = get_ip_address(domain)
if ip:
    print(f"IP-адрес для {domain}: {ip}")
else:
    print(f"Не удалось получить IP-адрес для {domain}")