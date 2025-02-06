import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 53)  # DNS server address

while True:
    hostname = input("Enter hostname/alias: ")
    client_socket.sendto(hostname.encode(), server_address)

    response, _ = client_socket.recvfrom(4096)
    info = response.decode()
    print(info)

    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != 'yes':
        break

client_socket.close()
