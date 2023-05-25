import socket

def get_ip_address(domain_name):
    try:
        ip_address = socket.gethostbyname(domain_name)
        return ip_address
    except socket.gaierror:
        return None

# Example usage
domain_name = input("Enter the domain name: ")
ip_address = get_ip_address(domain_name)

if ip_address:
    print(f"The IP address of {domain_name} is: {ip_address}")
else:
    print(f"Failed to retrieve the IP address for {domain_name}")
