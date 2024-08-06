def is_valid_ip(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    return True

# Example usage
ip_addresses = ["192.168.1.1", "256.100.50.0", "192.168.1", "192.168.1.256", "192.168.1.a"]

for ip in ip_addresses:
    if is_valid_ip(ip):
        print(f"{ip} is a valid IP address.")
    else:
        print(f"{ip} is not a valid IP address.")


