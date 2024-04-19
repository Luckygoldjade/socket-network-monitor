# Description: This is a simple UDP echo server that listens on port 10000 and echos back the received message.
# I can run this server on my local machine and run in a separate terminal window the UDP echo client to send messages to the server like a microservice.
# python socket module is used to create the server.
import socket

# my local IP address
IP_Address = "test"
Port = 10000

def udp_echo_server():
    # Create a datagram UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Bind the socket to the address and port
        sock.bind(("IP_Address", Port))
        print("UDP Echo Server started on port 10000")
        # Listen for incoming messages
        while True:
            data, addr = sock.recvfrom(1024)
            print(f"Received message: {data.decode()} from {addr}")
            # Echo back the received message
            sock.sendto(data, addr)
            print(f"Sent message: {data.decode()} to {addr}")

if __name__ == "__main__":
    udp_echo_server()
# Path: udp_echo_server.py








