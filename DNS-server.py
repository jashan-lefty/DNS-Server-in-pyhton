import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 53)  # DNS uses port 53

# Bind the socket to the server address
server_socket.bind(server_address)
adr_a_dict = {
    "www.Localhost.com": ["127.0.0.1", "vhost.localhost.au.com"],
    "google.com": ["192.168.128.103", "www.google.access.au"],
    "www.deakin.edu.au": ["10.10.46.15","server.deakin.access.au"],
    "www.realwebpage": ["255.255.255.255", "www.realwebpage.address.au"],
    "www.hitsongs.org": ["198.168.48.157", "vchost.hitsong.atp.au"]
}

print("DNS Server is running...")

while True:
    data, client_address = server_socket.recvfrom(4096)  # Receive data from client
    hostname = (data.decode())

    # Simulate DNS response based on hostname
    for key in adr_a_dict:
        if hostname == key:
            response = ("IP address: " + adr_a_dict[key][0] + ", CNAME: " + adr_a_dict[key][1])
            break
        else:
            response = "Host not found"

    # Send response back to client
    response = response.encode()
    server_socket.sendto(response, client_address)
