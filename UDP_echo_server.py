# Description: This is a simple UDP echo server that listens on port 10000 and echos back the received message.
# I can run this server on my local machine and run in a separate terminal window the UDP echo client to send messages to the server like a microservice.
# python socket module is used to create the server.
import socket

# my local IP address
IP_ADDRESS = "127.0.0.1"     # Localhost
PORT = 10100


def udp_echo_server():
    # Create a datagram UDP socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        # Bind the socket to the address and port
        sock.bind((IP_ADDRESS, PORT))
        print("UDP Echo Server started on port ", PORT)
        # Listen for incoming messages

        try:
            while True:
                data, addr = sock.recvfrom(1024)
                print(f"Received message: {data.decode()} from {addr}")
                if data.decode() == "Goodbye":
                    print("UDP Echo Server stopped")
                    sock.close()
                    break

                # Echo back the received message
                sock.sendto(data, addr)
                print(f"Sent message: {data.decode()} to {addr}")

        except KeyboardInterrupt:
            print("UDP Echo Server stopped")
            sock.close()


if __name__ == "__main__":
    udp_echo_server()
