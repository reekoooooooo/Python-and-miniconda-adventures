def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

def ip_to_binary(ip):
    if not is_valid_ip(ip):
        return None
    return ''.join(f'{int(part):08b}' for part in ip.split('.'))

def is_ip_in_subnet(ip, subnet, mask):
    if not is_valid_ip(ip) or not is_valid_ip(subnet) or not 0 <= mask <= 32:
        return False
    ip_bin = ip_to_binary(ip)
    subnet_bin = ip_to_binary(subnet)
    return ip_bin[:mask] == subnet_bin[:mask]

# Example usage
ip = "192.168.3.100"
subnet = "192.168.3.0"
mask = 28

if is_ip_in_subnet(ip, subnet, mask):
    print(f"{ip} is in the subnet {subnet}/{mask}.")
else:
    print(f"{ip} is not in the subnet {subnet}/{mask}.")



